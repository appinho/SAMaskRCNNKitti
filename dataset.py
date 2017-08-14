import pykitti
import itertools

class DataSet(object):
    def __init__(self,basedir,date,drive,frame_range):
        # Change this to the directory where you store KITTI data
        self.basedir = basedir
        # Specify the dataset to load
        self.date = date
        self.drive = drive
        self.frame_range = frame_range
        self.raw_data = pykitti.raw(basedir, date, drive, frames=frame_range)
    def get_point_cloud(self,current_frame):
        point_cloud = next(itertools.islice(self.raw_data.velo, current_frame, None))
        return point_cloud
    def get_pose(self,current_frame):
        pose = next(itertools.islice(self.raw_data.oxts, current_frame, None))
        return pose.packet.lat,pose.packet.lon,pose.packet.alt
    def get_timeframe(self,current_frame):
        timeframe = self.raw_data.timestamps[current_frame+1]-self.raw_data.timestamps[current_frame]
        return timeframe.total_seconds()
