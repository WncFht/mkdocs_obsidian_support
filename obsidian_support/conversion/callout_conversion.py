import re
from mkdocs.structure.pages import Page
from overrides import override

from obsidian_support.conversion.abstract_conversion import AbstractConversion, SyntaxGroup

class CalloutConversion(AbstractConversion):
    @property
    @override
    def obsidian_regex_pattern(self):
        return re.compile(r"^\[!(\w+)\]([^\n]*(?:\n(?!\[!(?:\w+)\]).*)*)", re.MULTILINE)

    @override
    def convert(self, syntax_groups: SyntaxGroup, page: Page, depth: int) -> str:
        callout_type, content = syntax_groups
        admonition_type = self._map_callout_type(callout_type)
        
        # 移除内容开头的换行符并缩进其余行
        content = content.strip()
        content = "\n    ".join(content.split("\n"))
        
        return f"""!!! {admonition_type}
    {content}
"""

    def _map_callout_type(self, callout_type: str) -> str:
        # 将 Obsidian callout 类型映射到 MkDocs admonition 类型
        mapping = {
            "note": "note",
            "abstract": "abstract",
            "info": "info",
            "tip": "tip",
            "success": "success",
            "question": "question",
            "warning": "warning",
            "failure": "failure",
            "danger": "danger",
            "bug": "bug",
            "example": "example",
            "quote": "quote",
        }
        return mapping.get(callout_type.lower(), "note")