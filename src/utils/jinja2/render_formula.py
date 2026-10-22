from pathlib import Path

from jinja2 import Template

from utils.models import FormulaInfoV2

PATH_TEMPLATE = Path(__file__).parent.joinpath("templates/formula.rb.j2").resolve()


def render_formula(*, formula_info: FormulaInfoV2) -> str:
    with open(PATH_TEMPLATE) as f:
        raw_template = f.read()

    template = Template(source=raw_template, trim_blocks=True, lstrip_blocks=True)
    return template.render(formula=formula_info)
