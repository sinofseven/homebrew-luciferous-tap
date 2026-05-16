import casefy

from utils.logger import create_logger, logging_function
from utils.models import AssetInfo, DecodedJwtInfo, FormulaInfo

logger = create_logger(__name__)


@logging_function(logger)
def create_formula_info(
    *,
    name: str,
    description: str,
    license_name: str,
    command_test: str,
    jwt_info: DecodedJwtInfo,
    asset_info: AssetInfo,
) -> FormulaInfo:
    pascal_name = casefy.pascalcase(name)
    kebab_name = casefy.kebabcase(pascal_name)
    return FormulaInfo(
        name=name,
        class_name=pascal_name,  # nameをPascalCaseに
        file_name=kebab_name,  # class_nameをkebab-caseに
        description=description,
        homepage=f"https://github.com/{jwt_info.repository}",
        version=jwt_info.version,
        license=license_name,
        command_test=command_test,
        assets=asset_info,
    )
