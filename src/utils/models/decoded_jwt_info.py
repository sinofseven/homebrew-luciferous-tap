from dataclasses import dataclass


@dataclass(frozen=True)
class DecodedJwtInfo:
    version: str
    repository: str
