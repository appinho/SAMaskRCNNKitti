import numpy as np

class Track(object):
    def __init__(self,object):
        self.number_of_states = 4
        self.x = object.x
        self.xp = np.zeros((self.number_of_states,1))
        self.P = np.eye(self.number_of_states,self.number_of_states)
        self.Pp = np.eye(self.number_of_states,self.number_of_states)

    def display_track(self):
        print " X "
        print self.x
        print " XP "
        print self.xp
        print " P "
        print self.P
        print " PP "
        print self.Pp