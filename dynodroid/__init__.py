__author__ = 'machiry'
import imp

"""
Check all the required python modules.
"""
try:
    imp.find_module("uiautomator")
except ImportError:
    print('Unable to find Module: uiautomator')
    print('Run Command: sudo pip install uiautomator or Install from: https://github.com/xiaocong/uiautomator')
