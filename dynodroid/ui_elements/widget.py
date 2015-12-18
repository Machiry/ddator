class Widget(object):

    def __init__(self, parent_screen, text='', is_clickable=False, is_long_clickable=False, is_scrollable=False, is_text_field=False,
                 is_checkable=False, is_password=False):
        self.parent_screen = parent_screen
        self.text = text
        self.is_clickable = is_clickable
        self.is_long_clickable = is_long_clickable
        self.is_scrollable = is_scrollable
        self.is_text_field = is_text_field
        self.is_checkable = is_checkable
        self.is_password = is_password
        self.parent_screen.add_child(self)

    def __hash__(self):
        return hash(self.parent_screen) ^ hash(str(self))

    def __eq__(self, other):
        if not isinstance(other, Widget):
            return False
        return self.parent_screen == other.parent_screen and str(self) == str(other)

    def __str__(self):
        to_ret = str(self.text) + ',' + str(self.is_clickable) + ',' + str(self.is_long_clickable) + ',' + \
                 str(self.is_scrollable)
        to_ret += str(self.is_text_field) + ',' + str(self.is_checkable) + ',' + str(self.is_password)
        return to_ret
