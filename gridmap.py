import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

class GridMap(object):
    def __init__(self):
        self.x_num_cells = 400
        self.y_num_cells = 400
        self.cell_size = 0.5
        self.x_range = self.x_num_cells/2*self.cell_size
        self.y_range = self.y_num_cells/2*self.cell_size
        self.height_threshold = 0.5
        self.point_strider = 10
        self.reset_grids()
        
    def point_to_cell(self,point):
        x = int((self.x_range-point[0])/self.cell_size)
        y = int((self.y_range-point[1])/self.cell_size)
        return (x,y)

    def cell_to_obj(self,label_output):
        pos_x = (self.x_num_cells/2-label_output[0])*self.cell_size
        pos_y = (self.x_num_cells/2-label_output[1])*self.cell_size
        #print (label_output[0],pos_x)
        #print (label_output[1],pos_y)
        length = label_output[2]*self.cell_size
        width = label_output[3]*self.cell_size
        return (pos_x,pos_y,length,width)

    def reset_grids(self):
        self.gridmap = np.zeros((self.x_num_cells,self.y_num_cells), dtype=np.uint8)
        self.dict_gridmap = defaultdict(list)
    
    def fill_point_cloud_in_grid(self,pc):
        self.reset_grids()
        for point in pc[1::self.point_strider]:
            self.dict_gridmap[self.point_to_cell(point)].append(point[2])
        for cell in self.dict_gridmap:
            self.gridmap[cell[0]][cell[1]] =max(self.dict_gridmap[cell])-min(self.dict_gridmap[cell])>self.height_threshold
    def print_parameters(self):
        print("'#X", self.x_num_cells)
        print("'#Y", self.y_num_cells) 
        print("'CS", self.cell_size)
        print("'XR", self.x_range)
        print("'YR", self.y_range)
    def display_grid_map(self):
        plt.imshow(self.gridmap,cmap='Greys',  interpolation='nearest')
        plt.show()
