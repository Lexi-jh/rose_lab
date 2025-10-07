

class TrajMap:
    def __init__(self, sx, sy, ex, ey, width, smooth_val = 50, bounds = None):
        print("hi, you initialized")
        self.sx = sx
        self.sy = sy
        self.ex = ex
        self.ey = ey
        self.width = width
        self.smooth_val = smooth_val
        self.bounds = bounds

    def scale(self):
        #scale from unit functions to boundary conditions
        pass

    def unit_raster(self, sx, sy, b_bound, t_bound, l_bound, r_bound):
        sl_dist = l_bound - sx

        pass
