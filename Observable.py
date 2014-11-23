__author__= 'Dan and Pat'
#Describes an Observable object. 
#includes methods to notify all observers
#and to add/delete them

#class for Observable
class Observable(object):

    def __init__(self):
        self.observer_list = []

    #notify all observers
    def notify_all(self, msg):
        for obs in self.observer_list:
            obs.notify(msg)
            
    #add observer to the list
    def add_observer(self, observer):
        if observer not in self.observer_list:
            self.observer_list.append(observer)
 
    #delete all observers
    def delete_all_observers(self):
        del self.observer_list[:]
    
