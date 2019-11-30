from setuptools import setup, find_packages
setup(
    name = 'braincomputer',
    version = '0.1.0',
    author = 'Ela Kadosh',
    description = 'hardware that can read minds',
    packages = find_packages(),
    install_requires = ['click', 'flask'],
    tests_require = ['pytest', 'pytest-cov'],
)