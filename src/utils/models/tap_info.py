import json

from pydantic import BaseModel, Field

from .formula_info import FormulaInfo

FILENAME_TAP_INFO = "tap_info.json"


class TapPackage(BaseModel):
    name: str
    description: str
    display_name: str | None = None


class TapInfo(BaseModel):
    mapping_casks: dict[str, TapPackage] = Field(default_factory=dict)
    mapping_formulas: dict[str, TapPackage] = Field(default_factory=dict)

    @staticmethod
    def load() -> TapInfo:
        with open(FILENAME_TAP_INFO) as f:
            raw = f.read()
            return TapInfo.model_validate_json(raw)

    def save(self):
        data = self.model_dump()
        with open(FILENAME_TAP_INFO, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def update_formula(self, *, name: str, description: str, display_name: str | None):
        self.mapping_formulas[name] = TapPackage(
            name=name, description=description, display_name=display_name
        )
