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

PACKAGE_NAME = 'v6_boilerplate_rdf_py'

# setup the package
setup(
    name=PACKAGE_NAME,
    version="1.0.0",
    description='vantage6 boilerplate (RDF)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jaspersnel/v6-boilerplate-py/tree/rdf',
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=[
        'vantage6-client==2.1.0',
        'pandas',
        'sparqlwrapper',
    ],
    include_package_data=True,
    package_data={PACKAGE_NAME: ['query.sparql']}
    # ,
    # extras_require={
    # },
    # package_data={
    #     'vantage6.tools': [
    #         'VERSION'
    #     ],
    # }
)
