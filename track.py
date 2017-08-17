import numpy as np

class Track(object):
    def __init__(self,object):
        self.number_of_states = 4
        self.x = object.x
        self.xp = np.zeros((self.number_of_states,1))
        self.P = np.zeros((self.number_of_states,self.number_of_states))
        self.Pp = np.zeros((self.number_of_states,self.number_of_states))

    def display_track(self):
        print("TRID " + str(self.track_id) +
              " X " + str(self.x) +
              " XP " + str(self.xp) +
              " P " + str(self.P) +
              " PP " + str(self.Pp))