# Tutorial used:
# https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56
from setuptools import setup, Extension


ext_modules = [
    Extension('cython_api', sources=['lif/cython_api.pyx',
                                     'lif/cpp_code/bigint.cpp',
                                     'lif/cpp_code/fft.cpp',
                                     'lif/cpp_code/algorithms_interface.cpp',
                                     'lif/cpp_code/algorithms/trail_division_algorithm.cpp'], language='c++'),
]  # TODO: Turn that to glob("**/*.cpp")

for e_m in ext_modules:
    e_m.compiler_directives = {"language_level": "3"}

setup(
    name='lif',
    packages=['lif'],
    version='0.1.7',
    license='MIT',
    description='Lif lib',
    author='Yonlif & Eilonlif',
    author_email='yonlif@gmail.com',
    url='https://github.com/yonlif/lif',
    download_url='https://github.com/yonlif/lif/archive/refs/tags/0.1.7.tar.gz',
    keywords=['Large', 'Integer', 'Factorization', 'Lif'],
    scripts=["./scripts/lif"],
    install_requires=[],
    ext_modules=ext_modules,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
)
