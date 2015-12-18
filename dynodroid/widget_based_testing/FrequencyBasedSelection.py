from selection_strategy import SelectionStrategy
import random


class FrequencyBasedSelection(SelectionStrategy):

    def __init__(self):
        self.current_available_widget_frequency = {}

    def get_next_widget(self):
        to_ret = None
        if len(self.current_available_widget_frequency) > 0:
            min_freqeuncy = min(self.current_available_widget_frequency.keys())
            to_ret = random.choice(self.current_available_widget_frequency[min_freqeuncy])
            updated_frequency = min_freqeuncy + 1
            if updated_frequency not in self.current_available_widget_frequency:
                self.current_available_widget_frequency[updated_frequency] = []
            self.current_available_widget_frequency[min_freqeuncy].remove(to_ret)
            if len(self.current_available_widget_frequency[min_freqeuncy]) == 0:
                del self.current_available_widget_frequency[min_freqeuncy]
            self.current_available_widget_frequency[updated_frequency].append(to_ret)
        return to_ret

    def update_new_screen(self, new_screen):
        if 0 not in self.current_available_widget_frequency:
            self.current_available_widget_frequency[0] = []
        self.current_available_widget_frequency[0].extend(list(new_screen.child_widgets))

    def update_system_events(self, target_events):
        if 0 not in self.current_available_widget_frequency:
            self.current_available_widget_frequency[0] = []
        self.current_available_widget_frequency[0].extend(target_events)

    def remove_system_event(self, system_event):
        for freq_key in self.current_available_widget_frequency:
            if system_event in self.current_available_widget_frequency[freq_key]:
                self.current_available_widget_frequency[freq_key].remove(system_event)
                break

    def update_triggered_widget(self, target_widget):
        pass

    def get_name(self):
        return "FrequencyBasedSelection"
