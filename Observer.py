__author__ = 'Pat and Tony'

#abstract class for the Observer interface
class Observer(object):

    #must be implemented in all subclasses
    def notify(self, msg):
        pass