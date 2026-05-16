import json
from os.path import basename

from utils.logger import create_logger, logging_function
from utils.models import DecodedJwtInfo

logger = create_logger(__name__)


@logging_function(logger)
def parse_decoded_jwt_info(*, decoded_jwt_filename: str) -> DecodedJwtInfo:
    with open(decoded_jwt_filename) as f:
        data = json.load(f)
    return DecodedJwtInfo(
        version=basename(data["payload"]["ref"]),
        repository=data["payload"]["repository"],
    )
