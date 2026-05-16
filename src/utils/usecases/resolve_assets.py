import json
from http.client import HTTPResponse
from urllib.request import urlopen

from utils.logger import create_logger, logging_function
from utils.models import AssetInfo, AssetPackage, DecodedJwtInfo

logger = create_logger(__name__)

TARGETS_MACOS = ["aarch64-apple-darwin"]
TARGETS_LINUX_ARM64 = ["aarch64-unknown-linux-musl", "aarch64-unknown-linux-gnu"]
TARGETS_LINUX_AMD64 = ["x86_64-unknown-linux-musl", "x86_64-unknown-linux-gnu"]


@logging_function(logger)
def resolve_assets(*, jwt_info: DecodedJwtInfo) -> AssetInfo:
    url = f"https://api.github.com/repos/{jwt_info.repository}/releases/tags/{jwt_info.version}"

    with urlopen(url) as resp:
        resp: HTTPResponse
        data = json.load(resp)

    all_assets = data["assets"]
    asset_macos = parse_asset(all_assets=all_assets, all_targets=TARGETS_MACOS)
    asset_linux_arm64 = parse_asset(
        all_assets=all_assets, all_targets=TARGETS_LINUX_ARM64
    )
    asset_linux_amd64 = parse_asset(
        all_assets=all_assets, all_targets=TARGETS_LINUX_AMD64
    )

    return AssetInfo(
        asset_macos=asset_macos,
        asset_linux_arm64=asset_linux_arm64,
        asset_linux_amd64=asset_linux_amd64,
    )


@logging_function(logger)
def parse_asset(
    *, all_assets: list[dict], all_targets: list[str]
) -> AssetPackage | None:
    for asset in all_assets:
        name: str = asset["name"]
        for target in all_targets:
            if target in name:
                return AssetPackage(
                    url=asset["browser_download_url"],
                    sha256=asset["digest"].split(":")[1],
                )

    return None
