__author__ = 'machiry'
from app_handler import AppHandler


class ApkHandler(AppHandler):

    def build_app(self):
        # Nothing to do for APK.
        return True
