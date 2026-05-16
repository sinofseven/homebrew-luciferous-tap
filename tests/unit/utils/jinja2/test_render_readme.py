import pytest

from utils.jinja2.render_readme import render_readme
from utils.models import TapInfo, TapPackage


class TestRenderReadme:
    @pytest.mark.parametrize(
        "option,load_text",
        [
            pytest.param(
                {
                    "tap_name": "user/homebrew-tools",
                    "tap_info": TapInfo(mapping_casks={}, mapping_formulas={}),
                },
                "readme/only_tap_name.txt",
                id="only_tap_name",
            ),
            pytest.param(
                {
                    "tap_name": "alice/utilities",
                    "tap_info": TapInfo(
                        mapping_casks={
                            "tool-a": TapPackage(
                                name="tool-a",
                                description="Tool A description",
                            ),
                            "tool-b": TapPackage(
                                name="tool-b",
                                description="Tool B description",
                            ),
                        },
                        mapping_formulas={},
                    ),
                },
                "readme/multiple_casks_no_formulas.txt",
                id="multiple_casks_no_formulas",
            ),
            pytest.param(
                {
                    "tap_name": "bob/dev-tools",
                    "tap_info": TapInfo(
                        mapping_casks={},
                        mapping_formulas={
                            "linter": TapPackage(
                                name="linter",
                                description="Code linter tool",
                            ),
                            "formatter": TapPackage(
                                name="formatter",
                                description="Code formatter tool",
                            ),
                        },
                    ),
                },
                "readme/multiple_formulas_no_casks.txt",
                id="multiple_formulas_no_casks",
            ),
            pytest.param(
                {
                    "tap_name": "charlie/all-tools",
                    "tap_info": TapInfo(
                        mapping_casks={
                            "gui-app": TapPackage(
                                name="gui-app",
                                description="GUI application",
                            ),
                        },
                        mapping_formulas={
                            "cli-tool": TapPackage(
                                name="cli-tool",
                                description="CLI tool",
                            ),
                        },
                    ),
                },
                "readme/mixed_casks_and_formulas.txt",
                id="mixed_casks_and_formulas",
            ),
            pytest.param(
                {
                    "tap_name": "dave/branded-tools",
                    "tap_info": TapInfo(
                        mapping_casks={
                            "my-cask": TapPackage(
                                name="my-cask",
                                description="My branded cask",
                                display_name="My Branded Cask",
                            ),
                        },
                        mapping_formulas={
                            "my-formula": TapPackage(
                                name="my-formula",
                                description="My formula",
                                display_name="My CLI Tool",
                            ),
                        },
                    ),
                },
                "readme/display_name_override.txt",
                id="display_name_override",
            ),
            pytest.param(
                {
                    "tap_name": "eve/comprehensive",
                    "tap_info": TapInfo(
                        mapping_casks={
                            "complex-app": TapPackage(
                                name="complex-app",
                                description="This is a comprehensive application that provides many features including documentation generation, code analysis, and automated testing with support for multiple programming languages.",
                                display_name="Complex Application",
                            ),
                        },
                        mapping_formulas={},
                    ),
                },
                "readme/long_descriptions.txt",
                id="long_descriptions",
            ),
            pytest.param(
                {
                    "tap_name": "user-name/homebrew-special-tap-name",
                    "tap_info": TapInfo(
                        mapping_casks={
                            "my-special-tool": TapPackage(
                                name="my-special-tool",
                                description="A special tool",
                            ),
                        },
                        mapping_formulas={},
                    ),
                },
                "readme/special_chars_in_tap_name.txt",
                id="special_chars_in_tap_name",
            ),
        ],
        indirect=["load_text"],
    )
    def test_render_readme(self, option, load_text):
        result = render_readme(**option)
        assert result == load_text
