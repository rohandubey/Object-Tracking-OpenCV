# Computer Vision - Object Tracking with OpenCV and Python
[![](https://img.shields.io/github/license/sourcerer-io/hall-of-fame.svg)](https://github.com/rohandubey/Object-Tracking-OpenCV/blob/master/LICENSE)
![pypi](https://img.shields.io/pypi/v/pybadges.svg)
![versions](https://img.shields.io/pypi/pyversions/pybadges.svg)
[![PyPI status](https://img.shields.io/pypi/status/trains-jupyter-plugin.svg)](https://pypi.python.org/pypi/trains-jupyter-plugin/) 
--------------------------------------------------------
## Description
<br><br>
In this project I have covered 6 types of Optical Image Tracking based on the image namely :
	1: Optical Flow
	2: Dense Optical Flow
	3: MeanShift
	4: CamShift
	5: Single Object Tracking
	6: Multi Object Tracking
  <br><br>
## Inplimentations
  1. **BOOSTING Tracker**: Based on the same algorithm used to power the machine learning behind Haar cascades (AdaBoost), but like Haar cascades, is over a decade old. This tracker is slow and doesn’t work very well. Interesting only for legacy reasons and comparing other algorithms. _(minimum OpenCV 3.0.0)_
  2. **MIL Tracker**: Better accuracy than BOOSTING tracker but does a poor job of reporting failure. _(minimum OpenCV 3.0.0)_
  3. **KCF Tracker**: Kernelized Correlation Filters. Faster than BOOSTING and MIL. Similar to MIL and KCF, does not handle full occlusion well. _(minimum OpenCV 3.1.0)_
  4. **CSRT Tracker**: Discriminative Correlation Filter (with Channel and Spatial Reliability). Tends to be more accurate than KCF but slightly slower. _(minimum OpenCV 3.4.2)_
  5. **MedianFlow Tracker**: Does a nice job reporting failures; however, if there is too large of a jump in motion, such as fast moving objects, or objects that change quickly in their appearance, the model will fail. _(minimum OpenCV 3.0.0)_
  6. **TLD Tracker**: I’m not sure if there is a problem with the OpenCV implementation of the TLD tracker or the actual algorithm itself, but the TLD tracker was incredibly prone to false-positives. I do not recommend using this OpenCV object tracker. _(minimum OpenCV 3.0.0)_
  7. **MOSSE Tracker**: Very, very fast. Not as accurate as CSRT or KCF but a good choice if you need pure speed. _(minimum OpenCV 3.4.1)_
  8. **GOTURN Tracker**: The only deep learning-based object detector included in OpenCV. It requires additional model files to run.(attached) _(minimum OpenCV 3.2.0)_
## Prerequisites
You need to have installed following softwares and libraries in your machine before running this project.
1. Python 3
2. Anaconda: It will install ipython notebook and most of the libraries which are needed like sklearn, pandas, seaborn, matplotlib, numpy, PIL.
3. OpenCV: Image processing library.
## Data 
_**Download Goturn caffemodel from**_ https://github.com/Mogball/goturn-files
1. 4 videos for different objct tracking scenarios.
2. _'haarcascade_frontalface_default.xml'_ for face detection.
3. GoTurn Model.

## Installing
1. Python 3: https://www.python.org/downloads/
2. Anaconda: https://www.anaconda.com/download/
3. OpenCV: ```pip3 install opencv-python```
4. Keras: ```pip3 install keras```
5. flask: ```pip3 install flask```
6. goturn(.caffemodel and .prototxt): Attached in the folder : Data/.
## Built With
* ipython-notebook - iPython Text Editor
* OpenCV - It is used for processing images
* Flask - Flask is a micro web framework written in Python. It is a lightweight WSGI web application framework.
* GoTurn(Caffe model) - Model for effective object tracking.
## Authors
Made with ❤️ by Rohan Dubey - Complete work
