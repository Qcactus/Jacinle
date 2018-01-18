# -*- coding:utf-8 -*-
# File   : enum.py
# Author : Jiayuan Mao
# Email  : maojiayuan@gmail.com
# Date   : 18/01/2018
# 
# This file is part of Jacinle.

import enum


class JacEnum(enum.Enum):
    """A customized enumeration class, adding helper functions for string-based argument parsing."""

    @classmethod
    def from_string(cls, value):
        value = _canonize_enum_value(value)
        return cls(value)

    @classmethod
    def type_name(cls):
        return cls.__name__

    @classmethod
    def choice_names(cls):
        return list(filter(lambda x: not x.startswith('_'), dir(cls)))

    @classmethod
    def choice_values(cls):
        return [getattr(cls, name).value for name in cls.choice_names()]

    @classmethod
    def is_valid(cls, value):
        value = _canonize_enum_value(value)
        return value in cls.choice_values()

    @classmethod
    def assert_valid(cls, value):
        assert cls.is_valid(value), 'Invalid {}: "{}". Supported choices: {}.'.format(
            cls.type_name(), value, ','.join(cls.choice_values()))


def _canonize_enum_value(value):
    if type(value) is str:
        value = value.lower()
    return value