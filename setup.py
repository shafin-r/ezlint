from setuptools import setup, find_packages

setup(
    name="ezlint",                # Package name
    version="0.0.1",                         # Package version
    author="Shafin Rahman",                      # Author's name
    author_email="shafin808s@gmail.com",   # Author's email
    # Short description
    description="A simple and minimal linter made for JavaScript developed in Python.",
    long_description=open("README.md").read(),  # Long description from README
    # Format of README (Markdown, rst, etc.)
    long_description_content_type="text/markdown",
    # URL of project (GitHub, docs, etc.)
    url="https://github.com/shafin-r/ezlint",

    # Classifiers (optional but recommended)
    classifiers=[
        "Programming Language :: Python :: 3",  # Target Python version
        "License :: OSI Approved :: MIT License",  # License
        "Operating System :: OS Independent",  # OS compatibility
    ],

    # Keywords (optional)
    keywords="linter linting javascript",   # Keywords for package discovery

    # Automatically find packages inside the project
    packages=find_packages(),
    # Include non-Python files specified in MANIFEST.in
    include_package_data=True,
    # Dependencies
    install_requires=[],
    # Optional: Entry points for command-line scripts
    entry_points={
        "console_scripts": [
            "your-command=your_package.module:main_function",  # CLI command mapping
        ],
    },
    # Optional: Specify Python version support
    python_requires=">=3.6",  # Minimum Python version requirement

    # Optional: License
    license="MIT",  # License type (MIT, GPL, etc.)

    # Optional: Other metadata (project URLs)
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/your-repo/issues",
        "Documentation": "https://yourproject.readthedocs.io",
        "Source Code": "https://github.com/yourusername/your-repo",
    },
)
