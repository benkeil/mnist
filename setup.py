from setuptools import setup

# Do not edit these constants. They will be updated automatically
# by scripts/update-client.sh.
CLIENT_VERSION = "0.1.0"
PACKAGE_NAME = "mnist-playground"
DEVELOPMENT_STATUS = "1 - Beta"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

EXTRAS = {}
REQUIRES = []
with open('requirements.txt') as f:
    for line in f:
        line, _, _ = line.partition('#')
        line = line.strip()
        if ';' in line:
            requirement, _, specifier = line.partition(';')
            for_specifier = EXTRAS.setdefault(':{}'.format(specifier), [])
            for_specifier.append(requirement)
        else:
            REQUIRES.append(line)

with open('test-requirements.txt') as f:
    TESTS_REQUIRES = f.readlines()

setup(
    name=PACKAGE_NAME,
    version=CLIENT_VERSION,
    description="MNIST Playground",
    author_email="",
    author="benkeil",
    license="Apache License Version 2.0",
    url="https://github.com/benkeil/mnist",
    keywords=["KI", "AI", "MNIST", "Machine Learning", "Deep Learning"],
    install_requires=REQUIRES,
    tests_require=TESTS_REQUIRES,
    extras_require=EXTRAS,
    packages=[],
    include_package_data=True,
    long_description="""\
    Deep learning algorithm for MNIST
    """,
    classifiers=[
        "Development Status :: %s" % DEVELOPMENT_STATUS,
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)