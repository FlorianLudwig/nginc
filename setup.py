import setuptools


setuptools.setup(
    name='nginc',
    version='0.0.1',
    author='Florian Ludwig',
    install_requires=['setuptools'],
    packages=['nginc'],
    package_data={'nginc': ['*.conf']},
    entry_points={
        'console_scripts': [
            'nginc = nginc:main',
        ],
    },
)