"""A setuptools based setup module.
"""

from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='three_five',

    version='1.0.0',

    description='A Python based project that prints numbers from 1 to 100.',

    long_description=long_description,

    long_description_content_type='text/markdown',

    url='https://github.com/amakarudze/three-five',

    author='Anna Makarudze',

    # This should be a valid email address corresponding to the author listed
    # above.
    author_email='anna@makarudze.com',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    keywords='three five',

    py_modules=["three_five"],

    python_requires='>=3.5.',

    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    project_urls={  # Optional
        'Bug Reports': 'https://github.com/amakarudze/three-five/issues',
        'Source': 'https://github.com/amakarudze/three-five/',
    },
)
