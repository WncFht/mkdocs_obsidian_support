from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mkdocs-obsidian-support",
    version="0.1.0",
    author="wnc",
    author_email="2130212584@qq.com",
    description="A MkDocs plugin for supporting Obsidian syntax",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WncFht/mkdocs-obsidian-support",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'mkdocs>=1.1',
        'overrides>=6.1.0',
    ],
    entry_points={
        'mkdocs.plugins': [
            'obsidian_support = obsidian_support.plugin:ObsidianSupportPlugin',
        ]
    },
)