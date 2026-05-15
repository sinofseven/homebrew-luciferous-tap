import json

from pydantic import BaseModel, Field

FILENAME_TAP_INFO = "tap_info.json"


class Package(BaseModel):
    name: str
    description: str
    display_name: str | None = None


class TapInfo(BaseModel):
    mapping_casks: dict[str, Package] = Field(default_factory=dict)
    mapping_formulas: dict[str, Package] = Field(default_factory=dict)

    @staticmethod
    def load() -> TapInfo:
        with open(FILENAME_TAP_INFO) as f:
            raw = f.read()
            return TapInfo.model_validate_json(raw)

    def save(self):
        data = self.model_dump()
        with open(FILENAME_TAP_INFO, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
