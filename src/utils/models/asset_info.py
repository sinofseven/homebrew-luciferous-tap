from dataclasses import dataclass, field


@dataclass(frozen=True)
class AssetPackage:
    url: str
    sha256: str


@dataclass(frozen=True)
class AssetInfo:
    asset_macos: AssetPackage | None = field(default=None)
    asset_linux_arm64: AssetPackage | None = field(default=None)
    asset_linux_amd64: AssetPackage | None = field(default=None)
