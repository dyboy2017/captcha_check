# -*- coding:utf-8 -*-
import numpy as np
from PIL import Image
from util import vec2text, text2vec
import tensorflow as tf


img = Image.open('./q7wy.jpg')
img_data = np.array(img)
# if len(img_data) > 2:
#     img_data = np.mean(img_data, -1)
#

# img = Image.fromarray(img_data)
# img.show()
# print(img_data.shape)

code = '1234'

vec2 = text2vec(code)
print(vec2)
y = vec2text(vec2)
# t = tf.reshape(code, [2, 2])
print(y)




