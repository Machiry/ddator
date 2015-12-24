class Screen(object):
    """
    This represents a snapshot of device screen.
    It consists of:
        package_name: Name of the app to which this screen belongs.
        screen_dump: view hierarchy of the screen.
        child_widgets: Widgets that are contained with in the screen.
    """

    def __init__(self, screen_dump='', package_name='', child_widgets=list()):
        self.screen_dump = screen_dump
        self.package_name = package_name
        self.child_widgets = []
        self.child_widgets.extend(child_widgets)

    def add_child(self, child_widget):
        """
        Add the provided widget as child widget of this screen.
        :param child_widget: widget to be added
        :return:  None
        """
        new_widgets = set(self.child_widgets)
        new_widgets.add(child_widget)
        self.child_widgets = list(new_widgets)

    def get_dump(self):
        """
        Returns the view hierarchy dump of the screen.
        :return: string (in xml) representing view hierarchy of the screen.
        """
        return self.screen_dump

    def __hash__(self):
        return hash(self.get_dump() + '_' + self.package_name)

    def __eq__(self, other):
        if not isinstance(other, Screen):
            return False
        return self.get_dump() == other.get_dump() and self.package_name == self.package_name
