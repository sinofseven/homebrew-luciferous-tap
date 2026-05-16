import pytest

from utils.jinja2.render_formula import render_formula
from utils.models import AssetInfo, AssetPackage, FormulaInfo


class TestRenderFormula:
    @pytest.mark.parametrize(
        "option, load_text",
        [
            # full_formula
            pytest.param(
                {
                    "formula_info": FormulaInfo(
                        name="oidc-jwks-converter",
                        class_name="OidcJwksConverter",
                        file_name="oidc_jwks_converter",
                        description="Convert OIDC JWKS public keys to PEM format",
                        homepage="https://github.com/sinofseven/oidc-jwks-converter",
                        version="0.1.0",
                        license="MIT",
                        command_test="--version",
                        assets=AssetInfo(
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
                        ),
                    )
                },
                "formula/full_formula.rb",
                id="full_formula",
            ),
            # only_macos_formula
            pytest.param(
                {
                    "formula_info": FormulaInfo(
                        name="oidc-jwks-converter",
                        class_name="OidcJwksConverter",
                        file_name="oidc_jwks_converter",
                        description="Convert OIDC JWKS public keys to PEM format",
                        homepage="https://github.com/sinofseven/oidc-jwks-converter",
                        version="0.1.0",
                        license="MIT",
                        command_test="--version",
                        assets=AssetInfo(
                            asset_macos=AssetPackage(
                                url="https://github.com/sinofseven/oidc-jwks-converter/releases/download/v0.1.0/oidc-jwks-converter_v0.1.0_aarch64-apple-darwin.zip",
                                sha256="c3c38539a5e5cd41f84e39d65b20c7b17a1e39df940185cf4a42978d5fb364fc",
                            ),
                        ),
                    )
                },
                "formula/only_macos_formula.rb",
                id="only_macos_formula",
            ),
            # only_linux_arm64_formula
            pytest.param(
                {
                    "formula_info": FormulaInfo(
                        name="oidc-jwks-converter",
                        class_name="OidcJwksConverter",
                        file_name="oidc_jwks_converter",
                        description="Convert OIDC JWKS public keys to PEM format",
                        homepage="https://github.com/sinofseven/oidc-jwks-converter",
                        version="0.1.0",
                        license="MIT",
                        command_test="--version",
                        assets=AssetInfo(
                            asset_linux_arm64=AssetPackage(
                                url="https://github.com/sinofseven/oidc-jwks-converter/releases/download/v0.1.0/oidc-jwks-converter_v0.1.0_aarch64-unknown-linux-musl.zip",
                                sha256="92c1bb7eec43082aa45ebc3a776347cbabe692d13fb01c2798ce9de263a70bf7",
                            ),
                        ),
                    )
                },
                "formula/only_linux_arm64_formula.rb",
                id="only_linux_arm64_formula",
            ),
            # only_linux_amd64_formula
            pytest.param(
                {
                    "formula_info": FormulaInfo(
                        name="oidc-jwks-converter",
                        class_name="OidcJwksConverter",
                        file_name="oidc_jwks_converter",
                        description="Convert OIDC JWKS public keys to PEM format",
                        homepage="https://github.com/sinofseven/oidc-jwks-converter",
                        version="0.1.0",
                        license="MIT",
                        command_test="--version",
                        assets=AssetInfo(
                            asset_linux_amd64=AssetPackage(
                                url="https://github.com/sinofseven/oidc-jwks-converter/releases/download/v0.1.0/oidc-jwks-converter_v0.1.0_x86_64-unknown-linux-musl.zip",
                                sha256="45742af8a6628205348de0217953179a5f1580619e028e43d5ca154c13110588",
                            ),
                        ),
                    )
                },
                "formula/only_linux_amd64_formula.rb",
                id="only_linux_amd64_formula",
            ),
            # macos_and_linux_arm64_formula
            pytest.param(
                {
                    "formula_info": FormulaInfo(
                        name="oidc-jwks-converter",
                        class_name="OidcJwksConverter",
                        file_name="oidc_jwks_converter",
                        description="Convert OIDC JWKS public keys to PEM format",
                        homepage="https://github.com/sinofseven/oidc-jwks-converter",
                        version="0.1.0",
                        license="MIT",
                        command_test="--version",
                        assets=AssetInfo(
                            asset_macos=AssetPackage(
                                url="https://github.com/sinofseven/oidc-jwks-converter/releases/download/v0.1.0/oidc-jwks-converter_v0.1.0_aarch64-apple-darwin.zip",
                                sha256="c3c38539a5e5cd41f84e39d65b20c7b17a1e39df940185cf4a42978d5fb364fc",
                            ),
                            asset_linux_arm64=AssetPackage(
                                url="https://github.com/sinofseven/oidc-jwks-converter/releases/download/v0.1.0/oidc-jwks-converter_v0.1.0_aarch64-unknown-linux-musl.zip",
                                sha256="92c1bb7eec43082aa45ebc3a776347cbabe692d13fb01c2798ce9de263a70bf7",
                            ),
                        ),
                    )
                },
                "formula/2_of_macos_and_linux_arm64_formula.rb",
                id="2_of_macos_and_linux_arm64_formula",
            ),
            # 2_of_macos_and_linux_amd64_formula
            pytest.param(
                {
                    "formula_info": FormulaInfo(
                        name="oidc-jwks-converter",
                        class_name="OidcJwksConverter",
                        file_name="oidc_jwks_converter",
                        description="Convert OIDC JWKS public keys to PEM format",
                        homepage="https://github.com/sinofseven/oidc-jwks-converter",
                        version="0.1.0",
                        license="MIT",
                        command_test="--version",
                        assets=AssetInfo(
                            asset_macos=AssetPackage(
                                url="https://github.com/sinofseven/oidc-jwks-converter/releases/download/v0.1.0/oidc-jwks-converter_v0.1.0_aarch64-apple-darwin.zip",
                                sha256="c3c38539a5e5cd41f84e39d65b20c7b17a1e39df940185cf4a42978d5fb364fc",
                            ),
                            asset_linux_amd64=AssetPackage(
                                url="https://github.com/sinofseven/oidc-jwks-converter/releases/download/v0.1.0/oidc-jwks-converter_v0.1.0_x86_64-unknown-linux-musl.zip",
                                sha256="45742af8a6628205348de0217953179a5f1580619e028e43d5ca154c13110588",
                            ),
                        ),
                    )
                },
                "formula/2_of_macos_and_linux_amd64_formula.rb",
                id="2_of_macos_and_linux_amd64_formula",
            ),
            # 2_of_linux_arm64_and_linux_amd64_formula
            pytest.param(
                {
                    "formula_info": FormulaInfo(
                        name="oidc-jwks-converter",
                        class_name="OidcJwksConverter",
                        file_name="oidc_jwks_converter",
                        description="Convert OIDC JWKS public keys to PEM format",
                        homepage="https://github.com/sinofseven/oidc-jwks-converter",
                        version="0.1.0",
                        license="MIT",
                        command_test="--version",
                        assets=AssetInfo(
                            asset_linux_arm64=AssetPackage(
                                url="https://github.com/sinofseven/oidc-jwks-converter/releases/download/v0.1.0/oidc-jwks-converter_v0.1.0_aarch64-unknown-linux-musl.zip",
                                sha256="92c1bb7eec43082aa45ebc3a776347cbabe692d13fb01c2798ce9de263a70bf7",
                            ),
                            asset_linux_amd64=AssetPackage(
                                url="https://github.com/sinofseven/oidc-jwks-converter/releases/download/v0.1.0/oidc-jwks-converter_v0.1.0_x86_64-unknown-linux-musl.zip",
                                sha256="45742af8a6628205348de0217953179a5f1580619e028e43d5ca154c13110588",
                            ),
                        ),
                    )
                },
                "formula/2_of_linux_arm64_and_linux_amd64_formula.rb",
                id="2_of_linux_arm64_and_linux_amd64_formula",
            ),
        ],
        indirect=["load_text"],
    )
    def test_normal(self, option, load_text):
        actual = render_formula(**option)
        assert actual == load_text
