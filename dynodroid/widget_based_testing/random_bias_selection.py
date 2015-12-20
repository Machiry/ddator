from selection_strategy import SelectionStrategy
import random
import itertools


class RandomBiasSelection(SelectionStrategy):

    def __init__(self):
        self.current_available_widget_frequency = {}

    def get_next_widget(self):
        to_ret = None
        if len(self.current_available_widget_frequency) > 0:
            freq_rev = sorted(self.current_available_widget_frequency.keys())
            totals = list(itertools.accumulate(freq_rev))
            target_freq = None
            n = random.uniform(0, totals[-1])
            for i, total in enumerate(totals):
                if n <= total:
                    target_freq = freq_rev[len(totals) - 1 - i]
                    to_ret = random.choice(self.current_available_widget_frequency[target_freq])
                    break
            if target_freq is not None and to_ret is not None:
                updated_frequency = target_freq + 1
                self.current_available_widget_frequency[target_freq].remove(to_ret)
                if len(self.current_available_widget_frequency[target_freq]) == 0:
                    del self.current_available_widget_frequency[target_freq]
                if updated_frequency not in self.current_available_widget_frequency:
                    self.current_available_widget_frequency[updated_frequency] = []
                self.current_available_widget_frequency[updated_frequency].append(to_ret)
        return to_ret

    def update_new_screen(self, new_screen):
        if len(new_screen.child_widgets) > 0:
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

    @staticmethod
    def get_selection_name():
        return "RandomBiasBased"

    def get_name(self):
        return RandomBiasSelection.get_selection_name()
