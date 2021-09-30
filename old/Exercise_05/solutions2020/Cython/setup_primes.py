from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

xt = [Extension('primes_cython', ['primes_wrapper.pyx', 'primes_pure_c.c'],extra_compile_args=['-g'],
                extra_link_args=['-g', '-pthread'])]

setup(
    name="Cython build for primes",
    cmdclass={'build_ext':build_ext},
    ext_modules = xt
)