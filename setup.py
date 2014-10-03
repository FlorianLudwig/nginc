import setuptools


setuptools.setup(
    name='nginc',
    version='0.0.1',
    desciption='run nginx from the commandline',
    author='Florian Ludwig',
    author_email='f.ludwig@greyrook.com',
    install_requires=['setuptools'],
    packages=['nginc'],
    package_data={'nginc': ['*.conf']},
    entry_points={
        'console_scripts': [
            'nginc = nginc:main',
        ],
    },
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
    ],
)