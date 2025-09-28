from setuptools import find_packages, setup

package_name = 'dummy'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lexij',
    maintainer_email='lexi.j.hanlon@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dummy_lidar = dummy.dummy_lidar:main',
            'dummy_gantry = dummy.dummy_gantry:main',
            'gantry_capture_service = dummy.dummy_service:main',
        ],
    },
)
