import os
__author__ = 'machiry'

"""
Package that contains all helper functions.
"""
# check all tools path

curr_file_path = os.path.dirname(os.path.relpath(__file__))
# get tools path
tools_path = os.path.join(curr_file_path, "../../tools")
assert os.path.exists(tools_path), "Tools Path Does not exit:" + str(tools_path)

# check existence of apk_tool
apk_tool_path = os.path.join(tools_path, "apk_tool.jar")
assert os.path.exists(apk_tool_path), "APK TOOL does not exist:" + str(apk_tool_path)
os.environ['APK_TOOL_PATH'] = apk_tool_path

