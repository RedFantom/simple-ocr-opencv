from setuptools import setup
import os

setup(
    name="simpleocr",
    packages=["simpleocr"],
    version="1.0.0",
    description="A library for simple OCR in Python using OpenCV",
    author="The simple-ocr-opencv authors",
    url="https://www.github.com/goncalopp/simple-ocr-opencv",
    download_url="https://www.github.com/goncalopp/simple-ocr-opencv/archive/1.0.0.tar.gz",
    keywords=["OCR", "OpenCV"],
    license="AGPL",
    classifiers=["Programming Language :: Python :: 2.7",
                 "Programming Language :: Python :: 3",
                 "License :: OSI Approved :: GNU Affero General Public License v2 or later (AGPLv2+)"],
    include_package_data=True,
    install_requires=[] if "TRAVIS" in os.environ else ["opencv-python"]
)
