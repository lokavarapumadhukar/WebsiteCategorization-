# -*- coding: utf-8 -*-
"""website_classifier_dependencies.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vfprVO0sAwNdMiEThJK6rgmRkczSm802
"""

import pandas as pd
import numpy as np
import tensorflow as tf
import keras
import sklearn.model_selection
import sklearn.preprocessing
import string
from tensorflow.keras.layers import TextVectorization
from bs4 import BeautifulSoup
import requests