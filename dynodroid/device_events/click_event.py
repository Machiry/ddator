from ui_event import UIEvent


class ClickEvent(UIEvent):

    def __init__(self, target_widget):
        self.target_widget = target_widget

    def trigger_event(self, target_device, target_logger):
        # TODO: Implement this.
        raise NotImplementedError("Trigger Event Not Implemented")

    def __str__(self):
        return "ClickEvent_" + str(self.target_widget)


class LongClickEvent(UIEvent):

    def __init__(self, target_widget):
        self.target_widget = target_widget

    def trigger_event(self, target_device, target_logger):
        # TODO: Implement this.
        raise NotImplementedError("Trigger Event Not Implemented")

    def __str__(self):
        return "LongClickEvent_" + str(self.target_widget)