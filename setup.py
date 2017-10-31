try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

config = {
    'description': 'db',
    'author': 'Neil Seward',
    'author_email': 'sealneaward@gmail.com',
    'version': '0.0.1',
    'packages': find_packages(),
    'name': 'db'
}

setup(**config)
