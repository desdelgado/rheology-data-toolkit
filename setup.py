import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rheodata", 
    version="0.0.6",
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
    install_requires=[
        'h5py>=2.10.0',
        'tables>=3.6.1',
        'jsonschema>=3.2.0',
        'pickleshare>=0.7.5',
        'pandas>=1.0.4',
        'xlrd>=1.2.0'
    ]
)