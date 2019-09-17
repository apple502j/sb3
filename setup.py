from setuptools import setup, find_packages

with open("README.md", "r") as f:
    longdesc = f.read()

setup(
    name="sb3",
    version="0.1",
    description="sb3 parses SB3",
    long_description=longdesc,
    long_description_content_type="text/markdown",
    url="https://github.com/apple502j/sb3",
    author="apple502j",
    license="GPLv3+",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Natural Language :: Japanese",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    keywords="scratch parser sb3",
    packages=find_packages(),
    python_requires=">=3.6"
    )
