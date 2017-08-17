import numpy as np
class Object(object):
    def __init__(self,label_out,grid,label_id):
        pos_x,pos_y,length,width = grid.cell_to_obj(label_out)
        self.grid_x = label_out[0]
        self.grid_y = label_out[1]
        self.grid_l = label_out[2]
        self.grid_w = label_out[3]
        self.length = length
        self.width = width
        self.x = np.array([pos_x,pos_y,0,0])
        self.label_id = label_id

    def display_object(self):
        print("ID " + str(self.label_id) +
              " PX " + str(self.x[0]) +
              " PY " + str(self.x[1]) +
              " VX " + str(self.x[2]) +
              " VY " + str(self.x[3]) +
              " LE " + str(self.length) +
              " WI " + str(self.width))