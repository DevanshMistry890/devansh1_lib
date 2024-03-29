from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.2'
DESCRIPTION = 'various projetcs'
LONG_DESCRIPTION = 'A package that allows to dircet run project by Devansh Mitry'

# Setting up
setup(
    name="devansh1",
    version=VERSION,
    author="DevanshMistry",
    author_email="<devanshmistry890@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['Flask','numpy','pandas','scikit_learn'],
    keywords=['python', 'devansh', 'flask'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
    ]
)