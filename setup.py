import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setuptools.setup(
    name="onepyece",
    version="0.0.2",
    author="Rémi JARA",
    author_email="remi.jara4@gmail.com",
    description="A package to use the One-Piece API : https://api-onepiece.com/",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/icepick4/onepyece",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["onepyece"],
    python_requires=">=3.6",
    install_requires=["requests"],
)
