__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint1"
__credits__ = ["Dan, Pat"]


class Observable(object):
    """
    Describes an Observable object.
    includes methods to notify all observers
    and to add/delete them

    Attributes:
        observer_list: the list of registered observer instances
    """
    def __init__(self):
        self.observer_list = []

    def notify_all(self, msg):
        """
        notify all observers
        :param msg: the message to be sent to the observers
        :type msg: Message.Message
        """
        for obs in self.observer_list:
            obs.notify(msg)

    def add_observer(self, observer):
        """
        add observer to the list
        :param observer: the observer object to register to this observable
        :type observer: Observer
        """
        if observer not in self.observer_list:
            self.observer_list.append(observer)

    def delete_all_observers(self):
        """ delete all observers """
        del self.observer_list[:]