import setuptools


setuptools.setup(
    name='nginc',
    version='0.0.2',
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
    url='https://github.com/FlorianLudwig/nginc',
    license="http://www.apache.org/licenses/LICENSE-2.0",
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
    ],
)