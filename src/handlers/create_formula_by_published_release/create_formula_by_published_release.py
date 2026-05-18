from pydantic_settings import BaseSettings, SettingsConfigDict

from utils.jinja2 import render_formula, render_readme
from utils.logger import create_logger, logging_function
from utils.models import TapInfo
from utils.usecases import create_formula_info, parse_decoded_jwt_info, resolve_assets


class EnvironmentVariables(BaseSettings):
    model_config = SettingsConfigDict(env_ignore_empty=True)

    filename: str
    display_name: str | None = None
    description: str
    license_name: str
    command_test: str
    decoded_jwt_filename: str
    tap_name: str


logger = create_logger(__name__)


@logging_function(logger)
def main():
    # データの取得
    env = EnvironmentVariables()
    jwt_info = parse_decoded_jwt_info(decoded_jwt_filename=env.decoded_jwt_filename)
    asset_info = resolve_assets(jwt_info=jwt_info)
    formula_info = create_formula_info(
        name=env.filename,
        description=env.description,
        license_name=env.license_name,
        command_test=env.command_test,
        jwt_info=jwt_info,
        asset_info=asset_info,
    )

    # データの更新
    tap_info = TapInfo.load()
    tap_info.update_formula(
        name=formula_info.name,
        description=formula_info.description,
        display_name=env.display_name,
    )
    tap_info.save()

    # レンダーファイル
    text_formula = render_formula(formula_info=formula_info)
    with open(f"Formula/{formula_info.file_name}.rb", "w") as f:
        f.write(text_formula)

    text_readme = render_readme(tap_name=env.tap_name, tap_info=tap_info)
    with open("README.md", "w") as f:
        f.write(text_readme)
