import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "gitToolsPy",
    version = "0.0.1",
    author = "Joli Holmes",
    author_email = "holmesjoli@gmail.com",
    description = "Git data archiving functions",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/holmesjoli/gitToolPy",
    packages = setuptools.find_packages(),
    install_requires = []
)

