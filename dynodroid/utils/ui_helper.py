from ..ui_elements.screen import Screen
from ..ui_elements.widget import Widget
from common_utils import get_all_leaf_elements


def get_current_screen(target_device):
    uiauto_object = target_device.get_ui_handle()
    curr_screen_dump = uiauto_object.dump()
    curr_package_name = get_current_package(target_device)
    curr_screen_obj = Screen(screen_dump=curr_screen_dump, package_name=curr_package_name)
    curr_screen_widgets = []
    for curr_leaf_element in get_all_leaf_elements(curr_screen_dump):
        widget_text = curr_leaf_element.getAttribute('text')
        is_clickable = curr_leaf_element.getAttribute('clickable') == "true"
        is_long_clickable = curr_leaf_element.getAttribute('long-clickable') == "true"
        is_scrollable = curr_leaf_element.getAttribute('scrollable') == "true"
        is_text_field = "EditText" in curr_leaf_element.getAttribute('class')
        is_checkable = curr_leaf_element.getAttribute('checkable') == "true"
        is_password = curr_leaf_element.getAttribute('password') == "true"
        curr_widget = Widget(curr_screen_obj, text=widget_text, is_clickable=is_clickable,
                             is_long_clickable=is_long_clickable, is_scrollable=is_scrollable,
                             is_text_field=is_text_field, is_checkable=is_checkable, is_password=is_password)
        curr_screen_widgets.append(curr_widget)
    return curr_screen_obj


def get_current_package(target_device):
    return target_device.get_ui_handle().info['currentPackageName']
