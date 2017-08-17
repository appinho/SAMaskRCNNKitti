from data_association import DataAssociation
from kalman_filter import KalmanFilter
from track import Track

class Tracking(object):
    def __init__(self):
        self.tracking_list = []
        self.data_association = DataAssociation()
        self.tracking_filter = KalmanFilter()
        pass
    def update(self,object_list,timeframe):
        if not self.tracking_list:
            for object in object_list:
                self.init_track(object)
        else:
            self.tracking_filter.predict(self.tracking_list,timeframe)
            asso = self.data_association.nearest_neighbor(object_list,self.tracking_list)
            self.tracking_filter.update(object_list,self.tracking_list,asso)
    def init_track(self,object):
        tr = Track(object)
        self.tracking_list.append(tr)
    def number_of_tracks(self):
        return len(self.tracking_list)
    def display_tracks(self):
        for track in self.tracking_list:
            Track.display_track(track)