import os
import time
from glob import glob
from shutil import rmtree
from zipfile import ZipFile
from multiprocessing import Process
from importlib.machinery import SourceFileLoader

from .errors import *
from .task import *
from .student import *
from .classroom import *

def getZipFiles():
    return glob("*.zip")

def getTxtFiles():
    return glob("*.txt")

def cleanFiles(names):
    for name in names:
        os.remove(name)

def importFile(module):
    loader = SourceFileLoader(module, '%s.py'%module)
    return loader.load_module()

def convert2to3(file_name):
    os.system("2to3 -w %s"%file_name)

def fileExists(file):
    return os.path.isfile(file)

def cleanMACOS():
    rmtree('__MACOSX')

CURRENT_DIRECTORY = os.getcwd()
