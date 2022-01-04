from os import path
from codecs import open
from setuptools import setup, find_packages

# get current directory
here = path.abspath(path.dirname(__file__))

# get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# # read the API version from disk
# with open(path.join(here, 'vantage6', 'tools', 'VERSION')) as fp:
#     __version__ = fp.read()

# setup the package
setup(
    name='v6_boilerplate_py',
    version="1.0.0",
    description='vantage6 biolerplate',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/IKNL/v6_boilerplate-py',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'vantage6-client==2.1.0',
        'pandas',
        'sparqlwrapper',
        'rdflib'
    ]
    # ,
    # extras_require={
    # },
    # package_data={
    #     'vantage6.tools': [
    #         'VERSION'
    #     ],
    # }
)
