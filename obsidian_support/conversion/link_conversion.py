import re
from mkdocs.structure.pages import Page
from overrides import override

from obsidian_support.conversion.abstract_conversion import AbstractConversion, SyntaxGroup

class LinkConversion(AbstractConversion):
    @property
    @override
    def obsidian_regex_pattern(self):
        return re.compile(r"(?<!!)(?:\[\[([^\]|]+)(?:\|([^\]]+))?\]\]|\[([^\]]+)\]\(([^\)]+)\))")

    @override
    def convert(self, syntax_groups: SyntaxGroup, page: Page, depth: int) -> str:
        if syntax_groups[0] is not None:  # Obsidian internal link
            link_path, link_text = syntax_groups[0], syntax_groups[1]
            if link_text is None:
                link_text = link_path
            return self._convert_internal_link(link_text, link_path, page)
        else:  # Markdown link
            link_text, link_path = syntax_groups[2], syntax_groups[3]
            return f"[{link_text}]({link_path})"

    def _convert_internal_link(self, link_text: str, link_path: str, page: Page) -> str:
        # Convert the link path to a relative URL
        # This is a simplified version; you might need to implement more complex logic
        # to handle different file structures and link types
        link_path = link_path.replace(' ', '-').lower() + '.md'
        return f"[{link_text}]({link_path})"