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


@dataclass(frozen=True)
class FormulaInfoV2:
    name: str  # inputs
    file_name: str  # inputs
    class_name: str  # inputs
    description: str  # inputs
    homepage: str  # from jwt
    version: str  # from jwt
    license: str  # inputs
    assets: AssetInfo  # auto calculate from jwt
    bin_name: str  # inputs
    command_test: str  # inputs
