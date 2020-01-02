from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name = 'lytrax_afm',
    version = '1.0.1',
    author="Christos Lytras",
    author_email="christos.lytras@gmail.com",
    description="Greek AFM (TIN) Validator and Generator",
    url="https://github.com/clytras/afm-python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages = find_packages(exclude=["test"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)
