from selection_strategy import SelectionStrategy
import random


class FrequencyBasedSelection(SelectionStrategy):
    """
    This is frequency based selection strategy.
    Least frequently exercised widgets are given preference.
    Refer paper for more details.
    """

    def __init__(self):
        self.current_available_widget_frequency = {}
        self.app_system_event_frequency = {}

    def get_next_widget(self):
        to_ret = None
        current_min = None
        target_dict = None
        if len(self.current_available_widget_frequency) > 0:
            current_min = min(self.current_available_widget_frequency.keys())
            target_dict = self.current_available_widget_frequency
        if current_min is None or (len(self.app_system_event_frequency) > 0 and
                                   min(self.app_system_event_frequency.keys()) < current_min):
            current_min = min(self.app_system_event_frequency.keys())
            target_dict = self.app_system_event_frequency
        if current_min is not None:
            # Sanity
            assert target_dict is not None
            # pick a random widget
            to_ret = random.choice(target_dict[current_min])
            # update the frequency
            updated_frequency = current_min + 1
            if updated_frequency not in target_dict:
                target_dict[updated_frequency] = []
            target_dict[current_min].remove(to_ret)
            if len(target_dict[current_min]) == 0:
                del target_dict[current_min]
            target_dict[updated_frequency].append(to_ret)
        return to_ret

    def update_new_screen(self, new_screen):
        self.current_available_widget_frequency = {}
        if len(new_screen.child_widgets) > 0:
            self.current_available_widget_frequency[0] = []
            self.current_available_widget_frequency[0].extend(list(new_screen.child_widgets))

    def update_system_events(self, target_events):
        if 0 not in self.app_system_event_frequency:
            self.app_system_event_frequency[0] = []
        self.app_system_event_frequency[0].extend(target_events)

    def remove_system_event(self, system_event):
        for freq_key in self.app_system_event_frequency:
            if system_event in self.app_system_event_frequency[freq_key]:
                self.app_system_event_frequency[freq_key].remove(system_event)
                break

    def update_triggered_widget(self, target_widget):
        pass

    @staticmethod
    def get_selection_name():
        return "FrequencyBased"

    def get_name(self):
        return FrequencyBasedSelection.get_selection_name()
