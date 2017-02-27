# Simple Python OCR  
[![Build Status](https://travis-ci.org/RedFantom/simple-ocr-opencv.svg?branch=master)](https://travis-ci.org/RedFantom/simple-ocr-opencv)
[![Build status](https://ci.appveyor.com/api/projects/status/cu0fn9l5asbg4k02?svg=true)](https://ci.appveyor.com/project/RedFantom/simple-ocr-opencv)
[![codecov](https://codecov.io/gh/RedFantom/simple-ocr-opencv/branch/master/graph/badge.svg)](https://codecov.io/gh/RedFantom/simple-ocr-opencv)

This repository is a fork of [simple-ocr-opencv](https://github.com/goncalopp/simple-ocr-opencv) by Goncalopp, with the
goal of turning this engine-project with examples into a working library for everyone
to use. This project is available under the [GNU AGPLv3 License](https://www.gnu.org/licenses/agpl-3.0.txt), a copy 
should be available in LICENSE. If not, check out the link to learn more.

    Copyright (C) 2016-2017 by Goncalopp and RedFantom
    All authors are the copyright owners of their respective additions
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU AGPLv3 License, as found in LICENSE.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.    

Originally inspired by [this question](http://stackoverflow.com/questions/9413216/simple-digit-recognition-ocr-in-opencv-python) on StackOverflow.

### Essential Concepts

#### Segmentation

In order for OCR to be performed on a image, several steps must be 
performed on the source image. Segmentation is the process of 
identifying the regions of the image that represent characters. 

This project uses rectangles to model segments. 

#### Supervised learning with a classification problem

The [classification problem][] consists in identifying to which class a 
observation belongs to (i.e.: which particular character is contained 
in a segment).

[Supervised learning][] is a way of "teaching" a machine. Basically, an 
algorithm is *trained* through *examples* (i.e.: this particular 
segment contains the character `f`). After training, the machine 
should be able to apply its aquired knowledge to new data.

The [k-NN algorithm], used in this project, is one of the simplest  
classification algorithm.

#### Grounding

Creating a example image with already classified characters, for 
training purposes.
See [ground truth][].

[classification problem]: https://en.wikipedia.org/wiki/Statistical_classification
[Supervised learning]: https://en.wikipedia.org/wiki/Supervised_learning
[k-NN algorithm]: https://en.wikipedia.org/wiki/K-nearest_neighbors_classification
[ground truth]: https://en.wikipedia.org/wiki/Ground_truth

#### How to understand this project

Unfortunately, documentation is a bit sparse at the moment (I 
gladly accept contributions).
The project is well-structured, and most classes and functions have 
docstrings, so that's probably a good way to start.

If you need any help, don't hesitate to contact me. You can find my 
email on my github profile.


#### How to use

Please check `example.py` for basic usage with the existing pre-grounded images.

You can use your own images, by placing them on the `data` directory. 
Grounding images interactively can be accomplished by using `grouding.UserGrounder`.
For more details check `example_grounding.py`
