"""Central Registry mapping all 50 template keys to local renderers."""

from templates.modern_templates import (
    BannerExecutiveTemplate,
    LeftSidebarTemplate,
    CenteredSerifTemplate,
    ATSPlainTemplate,
    RightSidebarTemplate,
)

# Map all 50 keys across the 5 primary design engines
TEMPLATES = {f"tpl_{i:02d}": [
    BannerExecutiveTemplate,
    LeftSidebarTemplate,
    CenteredSerifTemplate,
    ATSPlainTemplate,
    RightSidebarTemplate
][(i - 1) % 5] for i in range(1, 51)}

def get_template(template_id: str):
    return TEMPLATES.get(template_id.lower(), BannerExecutiveTemplate)