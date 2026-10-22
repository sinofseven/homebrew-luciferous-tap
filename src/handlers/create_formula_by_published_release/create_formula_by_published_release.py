from pydantic_settings import BaseSettings, SettingsConfigDict

from utils.jinja2 import render_formula, render_readme
from utils.logger import create_logger, logging_function
from utils.models import FormulaInfoV2, TapInfo
from utils.usecases import parse_decoded_jwt_info, resolve_assets


class EnvironmentVariables(BaseSettings):
    model_config = SettingsConfigDict(env_ignore_empty=True)

    formula_name: str
    display_name: str | None = None
    file_name: str
    class_name: str
    description: str
    license: str
    bin_name: str
    command_test: str
    tap_name: str
    decoded_jwt_filename: str


logger = create_logger(__name__)


@logging_function(logger)
def main():
    # データの取得
    # noinspection argument-list
    env = EnvironmentVariables()
    jwt_info = parse_decoded_jwt_info(decoded_jwt_filename=env.decoded_jwt_filename)
    asset_info = resolve_assets(jwt_info=jwt_info)
    formula = FormulaInfoV2(
        name=env.formula_name,
        file_name=env.file_name,
        class_name=env.class_name,
        description=env.description,
        homepage=f"https://github.com/{jwt_info.repository}",
        version=jwt_info.version,
        license=env.license,
        assets=asset_info,
        bin_name=env.bin_name,
        command_test=env.command_test,
    )

    # データの更新
    tap_info = TapInfo.load()
    tap_info.update_formula(
        name=formula.name,
        description=formula.description,
        display_name=env.display_name,
    )
    tap_info.save()

    # レンダーファイル
    text_formula = render_formula(formula_info=formula)
    with open(f"Formula/{formula.file_name}.rb", "w") as f:
        f.write(text_formula)

    text_readme = render_readme(
        tap_name=env.tap_name.replace("homebrew-", ""), tap_info=tap_info
    )
    with open("README.md", "w") as f:
        f.write(text_readme)
