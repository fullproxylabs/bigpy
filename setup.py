import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name="bigpy",
                 version="0.1",
                 description="BIGIP Authentication and REST Api handler",
                 author="Michael Forret",
                 author_email="michael.forret@fullproxy.com",
                 python_requires='>=3.7',
                 url="https://github.com/Mikeyspud/bigpy",
                 packages=setuptools.find_packages(),
                 long_description=long_description,
                 long_description_content_type="text/markdown")