import io
import os.path
from setuptools import setup

VERSION_PATH = os.path.join(
    os.path.dirname(__file__), 'src/VERSION.txt')
with io.open(VERSION_PATH, 'r', encoding='utf-8') as f:
  version = f.read().strip()

setup(
    name = "img_resize_tools",        # what you want to call the archive/egg
    version = version,
    packages=["img_resize_tools"],    # top-level python modules you can import like
                                #   'import foo'
    dependency_links = [],      # custom links to a specific project
    install_requires=[],
    extras_require={},      # optional features that other packages can require
                            #   like 'helloworld[foo]'
    package_data = {"img_resize_tools": ["VERSION.txt"]},
    package_dir={'': 'src'},
    author="pacman testing",
    author_email = "pacmantesting@gmail.com",
    description = "The familiar example program in Python",
    license = "Apache 2.0",
    keywords= "example documentation tutorial",
    url= "https://github.com/X05HUA/python-img_resize_tools"
)
