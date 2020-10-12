from setuptools import setup

package_name = 'spike_gyro'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='o.s.gervais@gmail.com',
    description='Minimal pitch, roll, and yaw gyroscope publisher',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
           'publisher = spike_gyro.gyro_publisher:main'
        ],
    },
)
