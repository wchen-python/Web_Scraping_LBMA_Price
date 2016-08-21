# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 18:18:37 2016

@author: wy.c
"""

import os
import requests
from lxml import etree
import numpy as np
url = 'http://lbma.oblive.co.uk/table'
content = requests.get(url).content
html = etree.HTML(content)
date = html.xpath('//td[@class="left"]/node()')
price = html.xpath('//td[@class="bold"]/node()')
if len(date)*2 == len(price)+1:
    price[1] = np.nan
AMprice = price[0::2]
PMprice = price[1::2]

os.system("pause")
    
