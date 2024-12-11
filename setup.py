# -*- coding: utf-8 -*-
import numpy as np
from Cython.Build import cythonize
from setuptools import Extension, setup

extensions = [
    Extension(
        "mattersim.datasets.utils.threebody_indices",
        ["src/mattersim/datasets/utils/threebody_indices.pyx"],
        include_dirs=[np.get_include()],
    )
]

setup(ext_modules=cythonize(extensions))
