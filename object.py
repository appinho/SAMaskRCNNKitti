class Object(object):
    def __init__(self,label_out,grid):
        pos_x,pos_y,length,width = grid.cell_to_obj(label_out)
        self.grid_x = label_out[0]
        self.grid_y = label_out[1]
        self.grid_l = label_out[2]
        self.grid_w = label_out[3]
        self.length = length
        self.width = width
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = 0
        self.vel_y = 0

    def display_object(self):
        print("PX " + str(self.pos_x) +
              " PY " + str(self.pos_y) +
              " VX " + str(self.vel_x) +
              " VY " + str(self.vel_y) +
              " LE " + str(self.length) +
              " WI " + str(self.width))