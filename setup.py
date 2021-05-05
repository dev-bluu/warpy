import setuptools
import os
import codecs

cwd = os.path.abspath(os.path.dirname(__file__))


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
        else:
            raise RuntimeError("Unable to find version string.")


setuptools.setup(
    name='warpy',
    version=get_version('warpy/__init__.py'),
    author='yunwah',
    description='An asynchronous API wrapper for the unofficial WarframeStat.us API.',
    url='https://github.com/yunwah/warpy',
    packages=setuptools.find_packages()
)