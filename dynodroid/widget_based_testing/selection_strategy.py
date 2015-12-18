class SelectionStrategy(object):

    def get_next_widget(self):
        raise NotImplementedError("get_next_widget not Implemented")

    def update_new_screen(self, new_screen):
        raise NotImplementedError("update_new_screen not Implemented")

    def update_triggered_widget(self, target_widget):
        raise NotImplementedError("update_triggered_widget not Implemented")

    def update_system_events(self, target_events):
        raise NotImplementedError("update_system_events not Implemented")

    def remove_system_event(self, system_event):
        raise NotImplementedError("remove_system_events not Implemented")

    def get_name(self):
        return "GenericSelection"

    def __str__(self):
        return "SelectionStrategy_" + self.get_name()
