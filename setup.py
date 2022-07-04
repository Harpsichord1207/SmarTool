import pathlib
from setuptools import setup

read_me = pathlib.Path(__file__).parent.joinpath('README.md').read_text()

setup_args = {
    'name': 'SmarTool',
    'version': '1.0.9',
    'description': 'A set of tools that keep Python sweeter.',
    'long_description': read_me,
    'long_description_content_type': 'text/markdown',
    'author': 'Harpsichord',
    'author_email': 'tliu1217@163.com',
    'license': 'MPL 2.0',
    'packages': ['SmarTool'],
    'package_dir': {'SmarTool': 'src'},
    'url': 'https://github.com/Harpsichord1207/SmarTool',
    'install_requires': [],
    'classifiers': [
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Intended Audience :: Developers'
    ],
    'keywords': 'Python Util Tool Convenience',
    'platforms': 'any',
    'zip_safe': True
}

setup(**setup_args)
