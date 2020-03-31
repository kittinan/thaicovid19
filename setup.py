import setuptools

import thaicovid19

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="thaicovid19",
    version=thaicovid19.VERSION,
    author="Kittinan Srithaworn",
    description="Thai Covid-19 API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    install_requires=["requests"],
    keywords="thaicovid19",
    url="https://github.com/kittinan/thaicovid19",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Bug Reports": "https://github.com/kittinan/thaicovid19/issues",
        "Source": "https://github.com/kittinan/thaicovid19",
    },
)
