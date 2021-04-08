# Tutorial used:
# https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56
from setuptools import setup, Extension
from Cython.Build import cythonize

# module = Extension('cython_example', sources=['cython_example.pyx'], language='c++')
setup(
    name='lif',
    packages=['lif'],
    version='0.1',
    license='MIT',
    description='Lif lib',
    author='Yonlif & Eilonlif',
    author_email='yonlif@gmail.com',
    url='https://github.com/yonlif/lif',
    download_url='https://github.com/yonlif/lif/archive/refs/tags/0.1.tar.gz',
    keywords=['Large', 'Integer', 'Factorization', 'Lif'],
    install_requires=[],
    ext_modules=cythonize("cython_example.pyx", language='c++'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
)
