import pytest

from utils.models import AssetInfo, AssetPackage, DecodedJwtInfo
from utils.usecases.resolve_assets import (
    TARGETS_LINUX_AMD64,
    TARGETS_LINUX_ARM64,
    TARGETS_MACOS,
    parse_asset,
    resolve_assets,
)


def test_resolve_assets():
    jwt_info = DecodedJwtInfo(
        repository="sinofseven/oidc-jwks-converter",
        version="v0.1.0",
    )
    result = resolve_assets(jwt_info=jwt_info)
    assert result == AssetInfo(
        asset_macos=AssetPackage(
            url="https://github.com/sinofseven/oidc-jwks-converter/releases/download/v0.1.0/oidc-jwks-converter_v0.1.0_aarch64-apple-darwin.zip",
            sha256="c3c38539a5e5cd41f84e39d65b20c7b17a1e39df940185cf4a42978d5fb364fc",
        ),
        asset_linux_arm64=AssetPackage(
            url="https://github.com/sinofseven/oidc-jwks-converter/releases/download/v0.1.0/oidc-jwks-converter_v0.1.0_aarch64-unknown-linux-musl.zip",
            sha256="92c1bb7eec43082aa45ebc3a776347cbabe692d13fb01c2798ce9de263a70bf7",
        ),
        asset_linux_amd64=AssetPackage(
            url="https://github.com/sinofseven/oidc-jwks-converter/releases/download/v0.1.0/oidc-jwks-converter_v0.1.0_x86_64-unknown-linux-musl.zip",
            sha256="45742af8a6628205348de0217953179a5f1580619e028e43d5ca154c13110588",
        ),
    )


class TestParseAsset:
    @pytest.mark.parametrize(
        "all_assets, all_targets, expected",
        [
            pytest.param(
                [
                    {
                        "name": "binary_aarch64-apple-darwin.zip",
                        "browser_download_url": "https://example.com/binary_aarch64-apple-darwin.zip",
                        "digest": "sha256:abc1234567890def",
                    }
                ],
                TARGETS_MACOS,
                AssetPackage(
                    url="https://example.com/binary_aarch64-apple-darwin.zip",
                    sha256="abc1234567890def",
                ),
                id="single_target_single_match_macos",
            ),
            pytest.param(
                [
                    {
                        "name": "binary_aarch64-unknown-linux-musl.zip",
                        "browser_download_url": "https://example.com/binary_aarch64-unknown-linux-musl.zip",
                        "digest": "sha256:def4567890123abc",
                    }
                ],
                TARGETS_LINUX_ARM64,
                AssetPackage(
                    url="https://example.com/binary_aarch64-unknown-linux-musl.zip",
                    sha256="def4567890123abc",
                ),
                id="multiple_targets_first_match",
            ),
            pytest.param(
                [
                    {
                        "name": "binary_aarch64-unknown-linux-gnu.zip",
                        "browser_download_url": "https://example.com/binary_aarch64-unknown-linux-gnu.zip",
                        "digest": "sha256:ghi7890123456def",
                    }
                ],
                TARGETS_LINUX_ARM64,
                AssetPackage(
                    url="https://example.com/binary_aarch64-unknown-linux-gnu.zip",
                    sha256="ghi7890123456def",
                ),
                id="multiple_targets_second_match",
            ),
            pytest.param(
                [
                    {
                        "name": "binary_aarch64-apple-darwin.zip",
                        "browser_download_url": "https://example.com/binary_aarch64-apple-darwin.zip",
                        "digest": "sha256:jkl0123456789ghi",
                    }
                ],
                ["non-existent-target"],
                None,
                id="no_match",
            ),
            pytest.param(
                [],
                TARGETS_MACOS,
                None,
                id="empty_assets_list",
            ),
            pytest.param(
                [
                    {
                        "name": "binary_x86_64-unknown-linux-musl.zip",
                        "browser_download_url": "https://example.com/binary_x86_64-unknown-linux-musl.zip",
                        "digest": "sha256:mno4567890123jkl",
                    },
                    {
                        "name": "binary_x86_64-unknown-linux-gnu.zip",
                        "browser_download_url": "https://example.com/binary_x86_64-unknown-linux-gnu.zip",
                        "digest": "sha256:pqr7890123456mno",
                    },
                ],
                TARGETS_LINUX_AMD64,
                AssetPackage(
                    url="https://example.com/binary_x86_64-unknown-linux-musl.zip",
                    sha256="mno4567890123jkl",
                ),
                id="multiple_assets_first_match_returned",
            ),
        ],
    )
    def test_parse_asset(self, all_assets, all_targets, expected):
        result = parse_asset(all_assets=all_assets, all_targets=all_targets)
        assert result == expected
