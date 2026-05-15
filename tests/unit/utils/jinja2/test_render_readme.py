import pytest

from utils.jinja2.render_readme import render_readme
from utils.models import Package, TapInfo


class TestRenderReadme:
    @pytest.mark.parametrize(
        "option,load_text",
        [
            (
                {
                    "tap_name": "user/homebrew-tools",
                    "tap_info": TapInfo(mapping_casks={}, mapping_formulas={}),
                },
                "only_tap_name.txt",
            ),
            (
                {
                    "tap_name": "alice/utilities",
                    "tap_info": TapInfo(
                        mapping_casks={
                            "tool-a": Package(
                                name="tool-a",
                                description="Tool A description",
                            ),
                            "tool-b": Package(
                                name="tool-b",
                                description="Tool B description",
                            ),
                        },
                        mapping_formulas={},
                    ),
                },
                "multiple_casks_no_formulas.txt",
            ),
            (
                {
                    "tap_name": "bob/dev-tools",
                    "tap_info": TapInfo(
                        mapping_casks={},
                        mapping_formulas={
                            "linter": Package(
                                name="linter",
                                description="Code linter tool",
                            ),
                            "formatter": Package(
                                name="formatter",
                                description="Code formatter tool",
                            ),
                        },
                    ),
                },
                "multiple_formulas_no_casks.txt",
            ),
            (
                {
                    "tap_name": "charlie/all-tools",
                    "tap_info": TapInfo(
                        mapping_casks={
                            "gui-app": Package(
                                name="gui-app",
                                description="GUI application",
                            ),
                        },
                        mapping_formulas={
                            "cli-tool": Package(
                                name="cli-tool",
                                description="CLI tool",
                            ),
                        },
                    ),
                },
                "mixed_casks_and_formulas.txt",
            ),
            (
                {
                    "tap_name": "dave/branded-tools",
                    "tap_info": TapInfo(
                        mapping_casks={
                            "my-cask": Package(
                                name="my-cask",
                                description="My branded cask",
                                display_name="My Branded Cask",
                            ),
                        },
                        mapping_formulas={
                            "my-formula": Package(
                                name="my-formula",
                                description="My formula",
                                display_name="My CLI Tool",
                            ),
                        },
                    ),
                },
                "display_name_override.txt",
            ),
            (
                {
                    "tap_name": "eve/comprehensive",
                    "tap_info": TapInfo(
                        mapping_casks={
                            "complex-app": Package(
                                name="complex-app",
                                description="This is a comprehensive application that provides many features including documentation generation, code analysis, and automated testing with support for multiple programming languages.",
                                display_name="Complex Application",
                            ),
                        },
                        mapping_formulas={},
                    ),
                },
                "long_descriptions.txt",
            ),
            (
                {
                    "tap_name": "user-name/homebrew-special-tap-name",
                    "tap_info": TapInfo(
                        mapping_casks={
                            "my-special-tool": Package(
                                name="my-special-tool",
                                description="A special tool",
                            ),
                        },
                        mapping_formulas={},
                    ),
                },
                "special_chars_in_tap_name.txt",
            ),
        ],
        ids=[
            "only_tap_name",
            "multiple_casks_no_formulas",
            "multiple_formulas_no_casks",
            "mixed_casks_and_formulas",
            "display_name_override",
            "long_descriptions",
            "special_chars_in_tap_name",
        ],
        indirect=["load_text"],
    )
    def test_render_readme(self, option, load_text):
        result = render_readme(**option)
        assert result == load_text
