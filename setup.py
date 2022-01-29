from setuptools import setup, find_packages
import nimporter

import os
from shutil import copy, rmtree
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

targetDir = "batchsend"
rmtree(targetDir, ignore_errors=True)
os.makedirs(targetDir, exist_ok=True)

srcFiles = [ "batchsend.nim", "nim.cfg", "test.py"]
for index, fileName in enumerate(srcFiles):
    fullFileName = os.path.join(this_directory + "/src/", fileName)
    if os.path.isfile(fullFileName):
        copy(fullFileName, targetDir + "/" + fileName)

with open(targetDir + "/__init__.py", "w") as text_file:
    text_file.write("from batchsend.batchsend import *")

setup(
    name = "batchsend",
    version = "0.3.1",
    author = "Marco Mengelkoch",
    author_email = "MMengelkoch@gmx.de",
    install_requires=['nimporter'],
    scripts = ["batchsend/__init__.py"],
    description = "Nim / Python library to feed HTTP server quickly with custom messages",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    keywords = "nim, tcp, http-client",
    url = "https://github.com/marcomq/batchsend",
    license = "MIT",
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License"
    ],
    ext_modules = nimporter.build_nim_extensions(danger=True, exclude_dirs=["test", "src"]),
    packages=["batchsend"]
)