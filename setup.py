import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TurtleOWL",
    version="0.0.1",
    author="Alessio Zamboni",
    author_email="zambotn@gmail.com",
    description="Simple library to bootstrap OWL ontologies using Turtle",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zambotn/TrutleOWL",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: GPL3 License",
        "Operating System :: OS Independent",
    ],
)
