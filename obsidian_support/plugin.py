# plugin.py
from mkdocs.plugins import BasePlugin
from obsidian_support.conversion.image_internal_link import ImageInternalLinkConversion
from obsidian_support.conversion.link_conversion import LinkConversion
from obsidian_support.conversion.callout_conversion import CalloutConversion

class ObsidianSupportPlugin(BasePlugin):
    def __init__(self):
        super().__init__()
        self.image_internal_link_conversion = ImageInternalLinkConversion()
        self.link_conversion = LinkConversion()
        self.callout_conversion = CalloutConversion()

    def on_page_markdown(self, markdown, page, config, files):
        markdown = self.image_internal_link_conversion.markdown_convert(markdown, page)
        markdown = self.link_conversion.markdown_convert(markdown, page)
        markdown = self.callout_conversion.markdown_convert(markdown, page)
        return markdown