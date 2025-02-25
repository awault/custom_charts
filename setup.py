from setuptools import setup, find_packages

setup(
    name="custom_charts",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "matplotlib"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)