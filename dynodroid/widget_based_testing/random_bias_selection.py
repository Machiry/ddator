from selection_strategy import SelectionStrategy
import random
import itertools


class RandomBiasSelection(SelectionStrategy):
    """
    This is Random Bias Selection.
    The selection of event is not completely random, but biased towards events rarely.
    """

    def __init__(self):
        self.current_available_widget_frequency = {}
        self.app_system_event_frequency = {}

    def get_next_widget(self):
        to_ret = None
        target_dict = None
        dict_choices = []
        if len(self.current_available_widget_frequency) > 0:
            # give higher preference to ui widgets
            dict_choices.extend([self.current_available_widget_frequency, self.current_available_widget_frequency])
        if len(self.app_system_event_frequency) > 0:
            dict_choices.append(self.app_system_event_frequency)
        if len(dict_choices) > 0:
            # randomly choose ui or system event
            target_dict = random.choice(dict_choices)
        if target_dict is not None:
            freq_rev = sorted(target_dict.keys())
            totals = list(itertools.accumulate(freq_rev))
            target_freq = None
            n = random.uniform(0, totals[-1])
            for i, total in enumerate(totals):
                if n <= total:
                    target_freq = freq_rev[len(totals) - 1 - i]
                    to_ret = random.choice(target_dict[target_freq])
                    break
            if target_freq is not None and to_ret is not None:
                updated_frequency = target_freq + 1
                target_dict[target_freq].remove(to_ret)
                if len(target_dict[target_freq]) == 0:
                    del target_dict[target_freq]
                if updated_frequency not in target_dict:
                    target_dict[updated_frequency] = []
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
        return "RandomBiasBased"

    def get_name(self):
        return RandomBiasSelection.get_selection_name()
