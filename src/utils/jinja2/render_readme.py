from pathlib import Path

from jinja2 import Template

from utils.logger import create_logger, logging_function
from utils.models import TapInfo

PATH_TEMPLATE = Path(__file__).parent.joinpath("templates/README.md.j2").resolve()

logger = create_logger(__name__)


@logging_function(logger)
def render_readme(*, tap_name: str, tap_info: TapInfo) -> str:
    with open(PATH_TEMPLATE) as f:
        raw_template = f.read()

    template = Template(raw_template)
    return template.render(
        tap_name=tap_name,
        all_casks=tap_info.mapping_casks.values(),
        all_formulas=tap_info.mapping_formulas.values(),
    )
