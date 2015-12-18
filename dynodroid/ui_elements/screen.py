class Screen(object):

    def __init__(self, screen_dump='', package_name='', child_widgets=list()):
        self.screen_dump = screen_dump
        self.package_name = package_name
        self.child_widgets = []
        self.child_widgets.extend(child_widgets)

    def add_child(self, child_widget):
        self.child_widgets = list(set(self.child_widgets).add(child_widget))

    def get_dump(self):
        return self.screen_dump

    def __hash__(self):
        return hash(self.get_dump() + '_' + self.package_name)

    def __eq__(self, other):
        if not isinstance(other, Screen):
            return False
        return self.get_dump() == other.get_dump() and self.package_name == self.package_name
