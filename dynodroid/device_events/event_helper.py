from click_event import *
from slide_event import *
from text_event import *
from ..utils.common_utils import get_random_text


def get_all_possible_ui_events(target_widget):
    to_ret = []
    if target_widget.is_clickable:
        to_ret.append(ClickEvent(target_widget))
    if target_widget.is_long_clickable:
        to_ret.append(LongClickEvent(target_widget))
    if target_widget.is_checkable:
        to_ret.append(CheckEvent(target_widget))
    if target_widget.is_scrollable:
        to_ret.append(Top2BottomSlideEvent(target_widget))
        to_ret.append(Bottom2TopSlideEvent(target_widget))
        to_ret.append(Left2RightSlideEvent(target_widget))
        to_ret.append(Right2LeftSlideEvent(target_widget))
    if target_widget.is_text_field:
        to_ret.append(TextEvent(target_widget, text_to_insert=get_random_text()))
    return to_ret
