from setuptools import setup, find_packages
from pathlib import Path

lines = Path("sphinx_book_theme").joinpath("__init__.py")
for line in lines.read_text().split("\n"):
    if line.startswith("__version__ ="):
        version = line.split(" = ")[-1].strip('"')
        break

setup(
    name="sphinx-book-theme",
    version=version,
    python_requires=">=3.7",
    author="Executable Books",
    author_email="executablebooks@gmail.com",
    url="https://sphinx-book-theme.readthedocs.org/",
    project_urls={
        "Documentation": "https://sphinx-book-theme.readthedocs.org/",
        "Funding": "https://executablebooks.org",
        "Source": "https://github.com/executablebooks/sphinx-book-theme/",
        "Tracker": "https://github.com/executablebooks/sphinx-book-theme/issues",
    },
    # this should be a whitespace separated string of keywords, not a list
    keywords="reproducible science jupyter books sphinx scholarship notebook",
    description="A clean book theme for scientific explanations and documentation with Sphinx",  # noqa: E501
    long_description=Path("./README.md").read_text(),
    long_description_content_type="text/markdown",
    license="BSD",
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4>=4.6.1,<5",
        "docutils==0.17.1",
        'importlib-resources>=3.0,<3.5; python_version < "3.7"',
        "pydata-sphinx-theme~=0.7.2",
        "pyyaml",
        "sphinx>=4,<7",
    ],
    # docutils 0.18, 0.19 need a patch fix https://sourceforge.net/p/docutils/patches/195/, un-pin when 0.20 is released
    extras_require={
        "code_style": ["pre-commit~=2.7.0"],
        "sphinx": [
            "ablog~=0.10.13",
            "ipywidgets",
            "folium",
            "numpy",
            "matplotlib",
            "myst-nb~=0.13",
            "nbclient",
            "pandas",
            "plotly",
            "sphinx-design",
            "sphinx-copybutton",
            "sphinx-tabs<=3.4.0", # sphinx-tabs 3.4.1 needs docutils >.17, which would conflict with our pin above
            "sphinx-togglebutton",
            "sphinx-thebe",
            "sphinxcontrib-bibtex~=2.2",
            "sphinxext-opengraph",
        ],
        "testing": [
            "beautifulsoup4",
            "coverage",
            "myst_nb~=0.13",
            "pytest~=6.0.1",
            "pytest-cov",
            "pytest-regressions~=2.0.1",
            "sphinx_thebe",
        ],
        "live-dev": ["sphinx-autobuild", "web-compile~=0.2.1"],
    },
    entry_points={"sphinx.html_themes": ["sphinx_book_theme = sphinx_book_theme"]},
    include_package_data=True,
)
