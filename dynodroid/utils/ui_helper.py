from ..ui_elements.screen import Screen
from ..ui_elements.widget import Widget

"""
Module that contains helper functions to deal with scrapping UI from the device.
"""


def get_current_screen(target_device):
    """
    Parse the device and get info about the screen currently on the device.
    :param target_device: target device for which the screen object need to be fetched.
    :return: target screen object.
    """
    uiauto_object = target_device.get_ui_handle()
    curr_screen_dump = uiauto_object.dump()
    curr_package_name = get_current_package(target_device)
    curr_screen_obj = Screen(screen_dump=curr_screen_dump, package_name=curr_package_name)
    curr_screen_widgets = []
    for curr_wid_obj in uiauto_object():
        curr_wid_info = curr_wid_obj.info
        class_name = curr_wid_info['className']
        if not (class_name.startswith('android') and 'Layout' in class_name):
            widget_text = curr_wid_info['text']
            is_clickable = curr_wid_info['clickable']
            is_long_clickable = curr_wid_info['longClickable']
            is_scrollable = curr_wid_info['scrollable']
            is_text_field = class_name in 'EditText'
            is_checkable = curr_wid_info['checkable']
            b_x = curr_wid_info['bounds']["left"]
            b_y = curr_wid_info['bounds']["bottom"]
            b_x_end = curr_wid_info['bounds']["right"]
            b_y_end = curr_wid_info['bounds']["top"]
            info_text = curr_wid_info
            curr_widget = Widget(curr_screen_obj, text=widget_text, is_clickable=is_clickable,
                                 is_long_clickable=is_long_clickable, is_scrollable=is_scrollable,
                                 is_text_field=is_text_field, is_checkable=is_checkable,
                                 b_x=b_x, b_x_end=b_x_end, b_y=b_y, b_y_end=b_y_end, ui_info=info_text,
                                 target_ui_obj=curr_wid_obj)
            curr_screen_widgets.append(curr_widget)
    return curr_screen_obj


def get_current_package(target_device):
    """

    :param target_device:
    :return:
    """
    return target_device.get_ui_handle().info['currentPackageName']
