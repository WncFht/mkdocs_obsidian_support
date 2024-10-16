import re
from abc import ABC, abstractmethod
from typing import List, Tuple, Union
import dataclasses
from mkdocs.structure.pages import Page

# 定义一个数据类来存储代码块的语法信息
CODE_BLOCK_PATTERN = re.compile(r'(?P<code_block>^[`~]{3,})(?P<language>[a-zA-Z\-]*)', re.MULTILINE)
BACKQUOTES_CODE_PATTERN = re.compile(r"`[^\n`]+`")
HTML_TAG_PATTERN = re.compile(r'<(?P<tag>\S*?)[\s\S]*?>[\s\S]*?</\1>')

@dataclasses.dataclass
class CodeBlockSyntax:
    start: int
    end: int
    code_block_type: str
    language: str

# 定义 SyntaxGroup 类型
SyntaxGroup = List[str]

class AbstractConversion(ABC):
    @property
    @abstractmethod
    def obsidian_regex_pattern(self):
        pass

    @abstractmethod
    def convert(self, syntax_groups: SyntaxGroup, page: Page, depth: int) -> str:
        pass

    def markdown_convert(self, markdown: str, page: Page, depth: int = 0) -> str:
        converted_markdown = ""
        index = 0
        excluded_indices = get_exclude_indices(markdown)

        for obsidian_syntax in self.obsidian_regex_pattern.finditer(markdown):
            start = obsidian_syntax.start()
            end = obsidian_syntax.end()

            if is_overlapped(start, end, excluded_indices):
                continue

            syntax_groups = list(obsidian_syntax.groups())

            mkdocs_syntax = self.convert(syntax_groups, page, depth)
            converted_markdown += markdown[index:start]
            converted_markdown += mkdocs_syntax
            index = end

        converted_markdown += markdown[index:]
        return converted_markdown

def get_exclude_indices(markdown: str) -> List[Tuple[int, int]]:
    exclude_indices = []
    code_block_matches = {}

    for code_block_match in CODE_BLOCK_PATTERN.finditer(markdown):
        code_block_syntax = code_block_match.group("code_block")
        size = len(code_block_syntax)
        start = code_block_match.start()
        end = code_block_match.end()
        language = code_block_match.group("language")

        if size not in code_block_matches:
            code_block_matches[size] = []
        code_block_matches[size].append(CodeBlockSyntax(start, end, code_block_syntax[0], language))

    for code_block_size in sorted(code_block_matches.keys(), reverse=True):
        code_block_matches_with_same_size = code_block_matches[code_block_size]
        current_syntax = None
        nested_code_block_syntax = None

        for code_block_syntax in code_block_matches_with_same_size:
            if current_syntax is None:
                current_syntax = code_block_syntax
            elif current_syntax.code_block_type == code_block_syntax.code_block_type and \
                    not is_overlapped(current_syntax.start, code_block_syntax.end, exclude_indices):
                if not current_syntax.language.startswith("ad-") and not current_syntax.language == "tabs":
                    exclude_indices.append((current_syntax.start, code_block_syntax.end))
                current_syntax = None
            elif (current_syntax.language.startswith("ad-") or current_syntax.language == "tabs") and \
                    current_syntax.code_block_type != code_block_syntax.code_block_type and \
                    nested_code_block_syntax is None:
                nested_code_block_syntax = code_block_syntax
            elif nested_code_block_syntax is not None and \
                    code_block_syntax.code_block_type == nested_code_block_syntax.code_block_type:
                if not nested_code_block_syntax.language.startswith("ad-") and \
                        not nested_code_block_syntax.language == "tabs":
                    exclude_indices.append((nested_code_block_syntax.start, code_block_syntax.end))
                nested_code_block_syntax = None

    for code_match in BACKQUOTES_CODE_PATTERN.finditer(markdown):
        if not is_overlapped(code_match.start(), code_match.end(), exclude_indices):
            exclude_indices.append((code_match.start(), code_match.end()))

    for html_tag_match in HTML_TAG_PATTERN.finditer(markdown):
        if not is_overlapped(html_tag_match.start(), html_tag_match.end(), exclude_indices):
            exclude_indices.append((html_tag_match.start(), html_tag_match.end()))

    return exclude_indices

def is_overlapped(start: int, end: int, exclude_indices_pairs: List[Tuple[int, int]]) -> bool:
    for exclude_indices_pair in exclude_indices_pairs:
        if exclude_indices_pair[0] <= start and end <= exclude_indices_pair[1]:
            return True
    return False