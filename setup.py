import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="Topsis-Jashan-102003206",
    version="1.0.0",
    description="It squares the number",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://pypi.python.org/pypi/Topsis-Jashan-10203206",
    author="Jashan Arora",
    author_email="jarora_be20@thapar.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    packages=["topsis"],
    include_package_data=True,
    install_requires=['numpy', 'pandas', 'sys'],
    entry_points={
        "console_scripts": [
            "topsis=topsis.__main__:main",
        ]
    },
    python_requires='>=3.6',
)
