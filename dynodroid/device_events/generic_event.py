
class GenericEvent(object):
    """
    This abstract class represents generic event.
    All events should inherit from this class.
    """

    def trigger_event(self, target_device, target_logger):
        """
        Trigger the event on the provided device.
        :param target_device: Target device on which this event needs to be trigerred.
        :param target_logger: Logger object to log any failures.
        :return:  True/False indicating success or failure respectively.
        """
        raise NotImplementedError("Trigger Event Not Implemented")
