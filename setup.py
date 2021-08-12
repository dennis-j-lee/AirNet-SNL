#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    raise RuntimeError('setuptools is required')

DESCRIPTION = ('AirNet-SNL is a Python library for computed ' +
               'tomography (CT) reconstruction with applications ' +
               'in X-ray phase contrast imaging(XPCI) ' +
               'given sparse data.')

LONG_DESCRIPTION = """
AirNet-SNL is a Python package for computed tomography (CT).
The AirNet-SNL model is an end-to-end neural network that
combines physics-based iterative reconstruction with
convolutional neural networks for sparse data.

Documentation:

D. J. Lee, J. Mulcahy-Stanislawczyk, E. Jimenez, D. West,
R. Goodner, C. Epstein, K. Thompson, and A. L. Dagel,
"AirNet-SNL: End-to-End Training of Iterative Reconstruction
and Deep Neural Network Regularization for Sparse-Data XPCI CT,"
 OSA Imaging and Applied Optics Congress, 2021.

Source code: https://github.com/dennis-j-lee/asnl
"""

DISTNAME = 'AirNet-SNL'
MAINTAINER = "Dennis Lee"
LICENSE = 'Revised BSD'
URL = 'https://github.com/dennis-j-lee/asnl'

TESTS_REQUIRE = [
    'pytest',
]

INSTALL_REQUIRES = [
    'numpy>=1.15.0',
    'scikit-image',
    'imageio',
    'tqdm',
    'typing',
    'torch=1.9.0+gpu',
    'torch_radon'
]

DOCS_REQUIRE = [
    'sphinx == 2.2.0'
]

EXTRAS_REQUIRE = {
    'optional': ['ruptures'],
    'test': TESTS_REQUIRE,
    'doc': DOCS_REQUIRE
}

EXTRAS_REQUIRE['all'] = sorted(set(sum(EXTRAS_REQUIRE.values(), [])))

SETUP_REQUIRES = ['setuptools_scm']

CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Operating System :: OS Independent',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python :: 3',
    'Topic :: Scientific/Engineering'
]

PACKAGES = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])

setup(
    name=DISTNAME,
    use_scm_version=True,
    packages=PACKAGES,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    tests_require=TESTS_REQUIRE,
    setup_requires=SETUP_REQUIRES,
    ext_modules=[],
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    maintainer=MAINTAINER,
    license=LICENSE,
    classifiers=CLASSIFIERS,
    url=URL
)