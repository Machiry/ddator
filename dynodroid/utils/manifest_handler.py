__author__ = 'machiry'

import os
import sys
import tempfile
import traceback
import xml.dom.minidom
from logger import DDLogger


class ManifestParser:

    def __init__(self, manifest_fp):
        """

        :param manifest_fp:
        :return:
        """
        self.src_manifest_fp = None
        self.manifest_info = None
        if not os.path.exists(manifest_fp):
            DDLogger.write_failure_message("Provided Manifest File:" + str(manifest_fp) + " Does not exist!")
        else:
            self.src_manifest_fp = manifest_fp
