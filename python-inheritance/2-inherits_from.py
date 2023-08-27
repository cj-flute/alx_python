#!/usr/bin/python3
'''2-inherit_form.py'''


def inherits_from(obj, a_class):
    """inherit_from() fuction"""
    inherited_classses = type(obj).mro()
    return a_class in inherited_classses
