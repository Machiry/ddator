class Widget(object):

    def __init__(self, parent_screen, text='', is_clickable=False, is_long_clickable=False, is_scrollable=False,
                 is_text_field=False, is_checkable=False, b_x=0, b_x_end=0, b_y=0, b_y_end=0, ui_info='',
                 target_ui_obj=None):
        self.parent_screen = parent_screen
        self.text = text
        self.is_clickable = is_clickable
        self.is_long_clickable = is_long_clickable
        self.is_scrollable = is_scrollable
        self.is_text_field = is_text_field
        self.is_checkable = is_checkable
        self.left = b_x
        self.right = b_x_end
        self.top = b_y
        self.bottom = b_y_end
        self.target_ui_info = ui_info
        self.target_ui_obj = target_ui_obj
        self.parent_screen.add_child(self)

    def get_ui_object(self, target_device):
        target_device.get_ui_handle().screen.on()
        return self.target_ui_obj

    def __hash__(self):
        return hash(self.parent_screen) ^ hash(str(self))

    def __eq__(self, other):
        if not isinstance(other, Widget):
            return False
        return self.parent_screen == other.parent_screen and str(self) == str(other)

    def __str__(self):
        to_ret = str(self.target_ui_info)
        return to_ret
