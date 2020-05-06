# -*- coding: utf-8 -*-
"""
Created on Wed May  6 12:40:04 2020

@author: REETAM
"""
#if you are using Anaconda, then you have to pip install two python libraries -> pyqrcode and pypng

import pyqrcode
x="Enter the text/link that you want to include in the qr code"
qr=pyqrcode.create(x)
qr.png("qr.png", scale =2)
qr.show()
