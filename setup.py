from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name        = 'jetbrains_bbo',
    packages    = find_packages(),
    version     = '0.0.1',
    description = 'Jetbrains Research Black Box Optimization via Learning Search Space Partition for Local Bayesian Optimization',
    long_description=long_description
)
