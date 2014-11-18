__author__ = 'Pat and Tony'

#abstract class for the Observer interface
class Observer(object):

    #replaces the normal notify method
    #must be implemented in all subclasses
    def launchICBM(self, msg):
        pass