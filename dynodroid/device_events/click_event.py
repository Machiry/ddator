from ui_event import UIEvent


class ClickEvent(UIEvent):

    def __init__(self, target_widget):
        self.target_widget = target_widget

    def trigger_event(self, target_device, target_logger):
        target_widget_obj = self.target_widget.get_ui_object(target_device)
        to_ret = False
        try:
            to_ret = target_widget_obj.click()
        except Exception as e:
            target_logger.log_failure("Failed to Click on Widget:" + str(self.target_widget) + ":" + str(e.message))
        return to_ret

    def __str__(self):
        return "ClickEvent_" + str(self.target_widget)


class LongClickEvent(UIEvent):

    def __init__(self, target_widget):
        self.target_widget = target_widget

    def trigger_event(self, target_device, target_logger):
        target_widget_obj = self.target_widget.get_ui_object(target_device)
        to_ret = False
        try:
            to_ret = target_widget_obj.long_click()
        except Exception as e:
            target_logger.log_failure("Failed to Long Click on Widget:" + str(self.target_widget) + ":" + str(e.message))
        return to_ret

    def __str__(self):
        return "LongClickEvent_" + str(self.target_widget)


class CheckEvent(UIEvent):

    def __init__(self, target_widget):
        self.target_widget = target_widget

    def trigger_event(self, target_device, target_logger):
        target_widget_obj = self.target_widget.get_ui_object(target_device)
        to_ret = False
        try:
            to_ret = target_widget_obj.click()
        except Exception as e:
            target_logger.log_failure("Failed to Click on Widget:" + str(self.target_widget) + ":" + str(e.message))
        return to_ret

    def __str__(self):
        return "CheckEvent_" + str(self.target_widget)