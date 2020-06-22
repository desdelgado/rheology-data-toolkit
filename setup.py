import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rheodata", 
    version="0.0.5",
    author="David Delgado",
    author_email="daviddelgado2020@u.northwestern.com",
    description="Packge to help process rheology data",
    url="https://github.com/desdelgado/rheology-data-toolkit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)