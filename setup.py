import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "mcgrading",
    version = "0.0.0",
    author = "Juan Barbosa",
    author_email = "js.barbosa10@uniandes.edu.co",
    description = (read('README')),
    #description = ("An demonstration of how to create, document, and publish "
                                #    "to the cheese shop a5# pypi.org."),
    license = "GPL",
    keywords = "example documentation tutorial",
    url = "http://github.com/jsbarbosa/mcgrading",
    packages=['mcgrading'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Utilities",
        "License :: GPL License",
    ],
)
