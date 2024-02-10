from pathlib import Path

from setuptools import find_packages, setup

HERE = Path(__file__).parent

with open(HERE / "README.md", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    # add requirements here
]

EXTRAS_REQUIRE = {
    "docs": [
        "sphinx>3.1",
        "sphinx-autodoc-typehints",
        "sphinx-rtd-theme",
        "m2r2",  # mdinclude directive
    ],
    "tests": [
        "coverage>=5",  # pyproject.toml support
        "pytest>=6",  # pyproject.toml support
    ],
    "tools": [
        "black",
        "isort",
        "mypy",
        "pylint>=2.5",  # pyproject.toml support
        "tox>=3.4",  # pyproject.toml support
    ],
}

EXTRAS_REQUIRE["dev"] = EXTRAS_REQUIRE["docs"] + EXTRAS_REQUIRE["tests"] + EXTRAS_REQUIRE["tools"]

setup(
    name="workbench_core",
    version="0.0.1",
    description="Workbench core concepts and classes.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/workbench-io/workbench-core",
    author="Jean Dos Santos",
    author_email="jeandsantos88@gmail.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
    ],
    keywords=[
        # add keywords here
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.11",
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    project_urls={
        "Bug Reports": "https://github.com/workbench-io/workbench-core/issues",
        "Source": "https://github.com/workbench-io/workbench-core",
    },
)
