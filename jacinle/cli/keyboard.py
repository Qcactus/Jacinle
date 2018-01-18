# -*- coding:utf-8 -*-
# File   : keyboard.py
# Author : Jiayuan Mao
# Email  : maojiayuan@gmail.com
# Date   : 18/01/2018
# 
# This file is part of Jacinle.


def str2bool(s):
    if s.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif s.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise ValueError('str2bool is undefined for: "{}".'.format(s))