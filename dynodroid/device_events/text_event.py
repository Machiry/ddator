from ui_event import UIEvent


class TextEvent(UIEvent):

    def __init__(self, target_widget, text_to_insert=""):
        self.target_widget = target_widget
        self.text_to_insert = text_to_insert

    def trigger_event(self, target_device, target_logger):
        target_widget_obj = self.target_widget.get_ui_object(target_device)
        to_ret = False
        try:
            to_ret = target_widget_obj.set_text(self.text_to_insert)
        except Exception as e:
            target_logger.log_failure("Failed to Enter text on Widget:" + str(self.target_widget) + ":" +
                                      str(e.message))
        return to_ret

    def __str__(self):
        return "TextEvent_" + str(self.target_widget)
