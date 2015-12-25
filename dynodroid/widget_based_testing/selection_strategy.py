class SelectionStrategy(object):
    """
    This is an abstract class that represents a selection strategy that
    a widget based testing uses.
    """

    def get_next_widget(self):
        """
        Get the next widget that needs to be exercised.
        :return: Widget that needs to be exercised next or None if no widget exist.
        """
        raise NotImplementedError("get_next_widget not Implemented")

    def update_new_screen(self, new_screen):
        """
        Update the strategy with new screen.
        :param new_screen: New screen that appeared on the device.
        :return: None
        """
        raise NotImplementedError("update_new_screen not Implemented")

    def update_triggered_widget(self, target_widget):
        """
        Update the strategy that a specific widget has been exercised.
        :param target_widget: Widget that was exercised.
        :return: None
        """
        raise NotImplementedError("update_triggered_widget not Implemented")

    def update_system_events(self, target_events):
        """
        Update new system event that are relevant to the app under test.
        :param target_events: List of the system events that are relevant.
        :return: None
        """
        raise NotImplementedError("update_system_events not Implemented")

    def remove_system_event(self, system_event):
        """
        Update the strategy to remove the provided system event.
        :param system_event: target system event that needs to be removed.
        :return: None
        """
        raise NotImplementedError("remove_system_events not Implemented")

    def get_name(self):
        return "GenericSelection"

    def __str__(self):
        return "SelectionStrategy_" + self.get_name()
