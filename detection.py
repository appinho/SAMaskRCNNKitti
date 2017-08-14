from object import Object
from skimage import measure
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import cv2

class Detection(object):
    def __init__(self):
        self.connectivity = 8
    
    def find_objects(self,grid):
        self.labels = measure.label(grid.gridmap)
        self.blobs_labels = measure.label(grid.gridmap, background=0)

    def find_opencv_objects(self,grid):
        ret,thresh = cv2.threshold(grid.gridmap,0,255,cv2.THRESH_BINARY)
        output = cv2.connectedComponentsWithStats(thresh, self.connectivity, cv2.CV_32S)
        self.labels = output[1]
        self.create_objects(output[2][1:],grid)
        self.num_objects = output[0]-1
        print "Objects found " + str(self.num_objects)

    def create_objects(self,label_out,grid):
        obj_list = []
        for row in label_out:
            obj = Object(row,grid)
            obj_list.append(obj)
        self.objects = obj_list

    def display_detection(self,grid):
        fig, ax = plt.subplots(1)
        ax.imshow(self.labels, cmap='nipy_spectral')
        for obj in self.objects:
            Object.display_object(obj)
            rect=patches.Rectangle((obj.grid_x-0.5,
                                    obj.grid_y-0.5),
                                    obj.grid_l, obj.grid_w,
                                    linewidth=1, edgecolor='r', facecolor='none')
            ax.add_patch(rect)
        plt.show()