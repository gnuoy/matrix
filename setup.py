import os
from setuptools import setup, find_packages

this_dir = os.path.abspath(os.path.dirname(__file__))
reqs_file = os.path.join(this_dir, 'requirements.txt')
with open(reqs_file) as f:
    reqs = [line for line in f.read().splitlines()
            if not line.startswith('--')]

SETUP = {
    'name': "jujumatrix",
    'packages': find_packages(),
    'version': "0.10.0",
    'author': "Juju Developers",
    'author_email': "juju@lists.ubuntu.com",
    'url': "https://github.com/juju-solutions/matrix",
    'license': "Apache 2 License",
    'long_description': open('README.md').read(),
    'entry_points': {
        'console_scripts': [
            # Script can be invoked as a matrix plugin: `juju matrix`
            'juju-matrix = matrix.main:main',
            # The following script is deprecated:
            'matrix = matrix.main:main',
        ]
    },
    'install_requires': reqs,
    'package_data': {'matrix': ['matrix.yaml']},
}


if __name__ == '__main__':
    setup(**SETUP)
