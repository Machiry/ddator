from selection_strategy import SelectionStrategy
import random


class RandomSelection(SelectionStrategy):

    def __init__(self):
        self.current_available_widgets = []
        self.current_system_events = []

    def get_next_widget(self):
        to_ret = None
        if len(self.current_available_widgets) > 0 or len(self.current_system_events) > 0:
            to_ret = random.choice(self.current_available_widgets + self.current_system_events)
        return to_ret

    def update_new_screen(self, new_screen):
        self.current_available_widgets = new_screen.child_widgets

    def update_system_events(self, target_events):
        self.current_system_events.extend(target_events)

    def remove_system_event(self, system_event):
        self.current_system_events.remove(system_event)

    def update_triggered_widget(self, target_widget):
        pass

    def get_name(self):
        return "RandomSelection"
