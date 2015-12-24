from generic_event import GenericEvent


class UIEvent(GenericEvent):
    """
    This class represents a generic UI event.
    """

    def trigger_event(self, target_device, target_logger):
        raise NotImplementedError("Trigger Event Not Implemented")


