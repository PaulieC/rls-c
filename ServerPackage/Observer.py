__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint1"
__credits__ = ["Pat, Tony"]


class Observer(object):
    """ abstract class for the Observer interface """

    def notify(self, msg):
        """
        must be implemented in all subclasses
        :param msg: the message object to apply to the notifications for observers
        :type msg: Message.Message
        """
        pass