from ui_event import UIEvent


class Top2BottomSlideEvent(UIEvent):

    def __init__(self, target_widget):
        self.target_widget = target_widget

    def trigger_event(self, target_device, target_logger):
        to_ret = False
        try:
            s_x = (self.target_widget.left + self.target_widget.right) / 2
            s_y = self.target_widget.top
            e_x = s_x
            e_y = self.target_widget.bottom
            to_ret = target_device.swipe(s_x, s_y, e_x, e_y)
        except Exception as e:
            target_logger.log_failure("Failed to Swipe Down on Widget:" + str(self.target_widget) + ":" + str(e.message))
        return to_ret

    def __str__(self):
        return "Top2BottomSlideEvent_" + str(self.target_widget)


class Bottom2TopSlideEvent(UIEvent):

    def __init__(self, target_widget):
        self.target_widget = target_widget

    def trigger_event(self, target_device, target_logger):
        to_ret = False
        try:
            s_x = (self.target_widget.left + self.target_widget.right) / 2
            s_y = self.target_widget.bottom
            e_x = s_x
            e_y = self.target_widget.top
            to_ret = target_device.swipe(s_x, s_y, e_x, e_y)
        except Exception as e:
            target_logger.log_failure("Failed to Swipe Top on Widget:" + str(self.target_widget) + ":" + str(e.message))
        return to_ret

    def __str__(self):
        return "Bottom2TopSlideEvent_" + str(self.target_widget)


class Left2RightSlideEvent(UIEvent):

    def __init__(self, target_widget):
        self.target_widget = target_widget

    def trigger_event(self, target_device, target_logger):
        to_ret = False
        try:
            s_x = self.target_widget.left
            s_y = (self.target_widget.top + self.target_widget.bottom) / 2
            e_x = self.target_widget.right
            e_y = s_y
            to_ret = target_device.swipe(s_x, s_y, e_x, e_y)
        except Exception as e:
            target_logger.log_failure("Failed to Swipe Left2Right on Widget:" + str(self.target_widget) + ":" +
                                      str(e.message))
        return to_ret

    def __str__(self):
        return "Left2RightSlideEvent_" + str(self.target_widget)


class Right2LeftSlideEvent(UIEvent):

    def __init__(self, target_widget):
        self.target_widget = target_widget

    def trigger_event(self, target_device, target_logger):
        to_ret = False
        try:
            s_x = self.target_widget.right
            s_y = (self.target_widget.top + self.target_widget.bottom) / 2
            e_x = self.target_widget.left
            e_y = s_y
            to_ret = target_device.swipe(s_x, s_y, e_x, e_y)
        except Exception as e:
            target_logger.log_failure("Failed to Swipe Right2Left on Widget:" + str(self.target_widget) + ":" +
                                      str(e.message))
        return to_ret

    def __str__(self):
        return "Right2LeftSlideEvent_" + str(self.target_widget)