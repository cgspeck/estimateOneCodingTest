import setuptools
from distutils.core import setup


def filter_requirements(fn):
    with open(fn) as fh:
        filtered_requirements = []
        for line in fh.readlines():
            if line[0] in ['#', ' ', '-']:
                continue
            filtered_requirements.append(line)
    return filtered_requirements


required = filter_requirements('requirements.txt')
required_test = filter_requirements('requirements-test.txt')
required_dev = filter_requirements('requirements-dev.txt')
required_dev += required_test

setup(
    name='EstimateOne Coding Challenge',
    author="Chris Speck",
    version='1.0.1',
    packages=['scorer'],
    license='proprietary',
    long_description=open('README.md').read(),
    url="https://github.com/cgspeck/e1-coding-challenge",
    platforms=["POSIX", "Windows", "MaxOS"],
    entry_points={
        'console_scripts': [
            'scorer = scorer.cli:main',
        ]
    },
    install_requires=required,
    setup_requires=['wheel'],
    extras_require={
        'dev': required_dev,
        'test': required_test
    }
)
