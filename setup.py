"""
Install the viewser package
"""
import setuptools

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
        name="viewser",
        version="0.0.1",
        author="Peder G. Landsverk",
        author_email="pedlan@prio.org",
        description="Client library for interacting with ViEWS cloud",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/uppsalaconflictdataprogram/viewser",
        packages=setuptools.find_packages(),
        python_requires="==3.8.5",
        install_requires=[
            "pyarrow==2.0.0",
            "pandas==1.2.0",
            "requests==2.25.1",
            "fire==0.3.1"
        ],
        scripts=[
            "bin/vsr"
            ]
)
