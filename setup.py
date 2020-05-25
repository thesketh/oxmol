from setuptools import setup

version, section = None, None
with open("Cargo.toml") as cargo_toml:
    for line in cargo_toml:
        if line.startswith('['):
            section = line[1:line.index(']')]
        elif section == "package" and line.startswith("version"):
            version = line.split("=")[1].lstrip()
            version = line.replace("\"", "")
            break
if not version:
    raise ValueError("No package version string in `Cargo.toml`.")

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="oxmol",
    version=version,
    author="Travis Hesketh",
    author_email="travis@hesketh.scot",
    description="A Python wrapper around `molecule.rs`.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thesketh/oxmol",
    packages=["oxmol"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Programming Language :: Rust",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Chemistry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: MacOS",
        "Typing :: Typed"
    ],
    python_requires='>=3.6',
)
