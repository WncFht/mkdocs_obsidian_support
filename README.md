# MkDocs Obsidian Support Plugin

[![PyPI version](https://badge.fury.io/py/mkdocs-obsidian-support.svg)](https://badge.fury.io/py/mkdocs-obsidian-support)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A MkDocs plugin that provides support for Obsidian-style syntax, allowing you to easily convert your Obsidian vault into a MkDocs site.

## Features

- Converts Obsidian-style internal links (`[[Link]]`) to standard Markdown links
- Supports Obsidian image syntax (`![[image.png]]`)
- Handles Obsidian callouts and converts them to MkDocs admonitions
- Preserves your Obsidian folder structure
- Compatible with other MkDocs plugins and themes

## Installation

You can install the MkDocs Obsidian Support Plugin using pip:

```bash
pip install mkdocs-obsidian-support
```

## Usage

1. After installation, add the plugin to your `mkdocs.yml`:

```yaml
plugins:
  - search
  - obsidian_support
```

2. If you have other plugins, make sure to list `obsidian_support` in your plugins.

3. Run `mkdocs build` to build your site or `mkdocs serve` to preview it.

## Configuration

Currently, the plugin works out of the box without any additional configuration. Future versions may include customizable options.

## Supported Obsidian Syntax

### Internal Links

Obsidian: `[[Page Name]]` or `[[Page Name|Display Text]]`
Converted to: `[Page Name](page-name.md)` or `[Display Text](page-name.md)`

### Images

Obsidian: `![[image.png]]` or `![[image.png|alt text]]`
Converted to: `![image.png](image.png)` or `![alt text](image.png)`

### Callouts

Obsidian:
```
> [!NOTE]
> This is a note
```

Converted to:
```
!!! note
    This is a note
```

## Known Limitations

- The plugin currently doesn't support Obsidian's graph view.
- Some advanced Obsidian features like dataview queries are not supported.

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please make sure to update tests as appropriate and adhere to the [Python Style Guide (PEP 8)](https://www.python.org/dev/peps/pep-0008/).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the MkDocs team for creating such a flexible static site generator.
- Inspired by the Obsidian note-taking app and its vibrant community.

## Support

If you encounter any problems or have any questions, please [open an issue](https://github.com/WncFht/mkdocs-obsidian-support/issues) on GitHub.

---

Made with ❤️ by wnc