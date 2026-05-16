from dataclasses import dataclass, field

from .asset_info import AssetInfo


@dataclass(frozen=True)
class FormulaInfo:
    name: str
    class_name: str
    file_name: str
    description: str
    homepage: str
    version: str
    license: str
    command_test: str
    assets: AssetInfo
