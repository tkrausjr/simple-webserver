from setuptools import setup, find_packages


setup (
    name             = "app",
    version          = "0.1",
    description      = "My simple Python Flask Application with Static Page.",
    packages         = find_packages(),
    install_requires = ["flask"],
)