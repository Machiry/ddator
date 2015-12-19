from ui_event import UIEvent


class Top2BottomSlideEvent(UIEvent):

    def __init__(self, target_widget):
        self.target_widget = target_widget

    def trigger_event(self, target_device, target_logger):
        # TODO: Implement this.
        raise NotImplementedError("Trigger Event Not Implemented")

    def __str__(self):
        return "Top2BottomSlideEvent_" + str(self.target_widget)


class Bottom2TopSlideEvent(UIEvent):

    def __init__(self, target_widget):
        self.target_widget = target_widget

    def trigger_event(self, target_device, target_logger):
        # TODO: Implement this.
        raise NotImplementedError("Trigger Event Not Implemented")

    def __str__(self):
        return "Bottom2TopSlideEvent_" + str(self.target_widget)


class Left2RightSlideEvent(UIEvent):

    def __init__(self, target_widget):
        self.target_widget = target_widget

    def trigger_event(self, target_device, target_logger):
        # TODO: Implement this.
        raise NotImplementedError("Trigger Event Not Implemented")

    def __str__(self):
        return "Left2RightSlideEvent_" + str(self.target_widget)


class Right2LeftSlideEvent(UIEvent):

    def __init__(self, target_widget):
        self.target_widget = target_widget

    def trigger_event(self, target_device, target_logger):
        # TODO: Implement this.
        raise NotImplementedError("Trigger Event Not Implemented")

    def __str__(self):
        return "Right2LeftSlideEvent_" + str(self.target_widget)