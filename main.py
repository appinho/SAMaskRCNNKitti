from dataset import DataSet
from gridmap import GridMap
from detection import Detection
from tracking import Tracking
import time

# Choose scenario
path = '/home/simonappel/KITTI/raw/'
date = '2011_09_26'
drive = '0001'
frame_range = range(0,100,1)

# Construct objects
dataset = DataSet(path,date,drive,frame_range)
grid =GridMap()
detector = Detection()
tracker = Tracking()

# Loop through frames
for frame in range(0,2,1):
    print "-----Frame " + str(frame) + "-----"
    point_cloud = dataset.get_point_cloud(frame)
    pose = dataset.get_pose(frame)
    timeframe = dataset.get_timeframe(frame)
    print "Pose " +str(pose)
    print "Timeframe " + str(timeframe)
    t0 = time.time()
    grid.fill_point_cloud_in_grid(point_cloud)
    t1 = time.time()
    print "Fill grid in " + str(t1-t0) + "s"
    #grid.display_grid_map()

    # Detect objects
    #detector.find_objects(grid)
    t2 = time.time()
    detector.find_opencv_objects(grid)
    t3 = time.time()
    print "Detect objects in " + str(t3-t2) + "s"
    #detector.display_detection(grid)

    # Track objects
    t4 = time.time()
    tracker.update(detector.objects,timeframe)
    t5 = time.time()
    print "Track object in " + str(t5-t4) + "s"
    print "# Tracks " + str(tracker.number_of_tracks())
