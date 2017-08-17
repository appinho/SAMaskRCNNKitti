import numpy as np
from numpy.linalg import inv

class KalmanFilter(object):
    def __init__(self):
        self.Q = np.eye(4,4)
        self.R = np.eye(2,2)
        self.H = np.matrix([[1,0,0,0],[0,1,0,0]])
        self.Ht = np.eye(2,4)
        print self.Ht.shape,self.H.shape
    def predict(self,tracking_list,t):
        for track in tracking_list:
            track.xp[0] = track.x[0] + t * track.x[2]
            track.xp[1] = track.x[1] + t * track.x[3]
            track.xp[2] = track.x[2]
            track.xp[3] = track.x[3]
            track.Pp = track.P + self.Q
            """
            print track.x
            print track.xp
            print track.P
            print self.Q
            print track.Pp
            """
    def update(self,object_list,tracking_list,association):
        for pair in association:
            z = np.array([object_list[pair[0]].x[0:2]])
            z = z.T
            xp = tracking_list[pair[1]].xp
            Pp = tracking_list[pair[1]].Pp
            Hxp = np.dot(self.H,xp)
            y = np.subtract(z,Hxp)
            S=self.R + np.dot(np.dot(self.H,Pp),self.H.T)
            K = np.dot(Pp,np.dot(self.H.T,inv(S)))
            xnew = xp + np.dot(K,y)
            Pnew = np.dot(np.eye(4,4)-np.dot(K,self.H),Pp)
            tracking_list[pair[1]].x = xnew
            tracking_list[pair[1]].P = Pnew
            #self.display_kalman_filter(pair,z,xp,z,Pp,S,K,xnew,Pnew)
    def display_kalman_filter(self,pair,z,xp,y,Pp,S,K,xnew,Pnew):
        print "--Combine Object " + str(pair[0])+ " with Track " + str(pair[1]) + " --"
        print "z " + str(z)
        print "H " + str(self.H)
        print "xp " + str(xp)
        print "y " + str(y)
        print "R " + str(self.R)
        print "Pp " + str(Pp)
        print "S " + str(S)
        print "K " + str(K)
        print "xnew " + str(xnew)
        print "Pnew " + str(Pnew)