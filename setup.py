import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), "capacity", "__version__.py")) as version_file:
    exec(version_file.read())

setup(name="capacity",
      classifiers = [
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: BSD License",
          "Programming Language :: Python :: 2.6",
          ],
      description="Data types to describe capacity",
      license="BSD",
      author="Rotem Yaari",
      author_email="vmalloc@gmail.com",
      version=__version__,
      packages=find_packages(exclude=["tests"]),
      scripts=[],
      )
