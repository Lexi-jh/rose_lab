from setuptools import find_packages
from setuptools import setup

setup(
    name='gantry_lidar_interfaces',
    version='0.0.0',
    packages=find_packages(
        include=('gantry_lidar_interfaces', 'gantry_lidar_interfaces.*')),
)
