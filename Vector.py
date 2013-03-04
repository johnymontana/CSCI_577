class Vector_3D:
    # override operators??? => *
    def __class__(self):
        return Vector_3D
    def __init__(self, initial_x, initial_y, initial_z):
        self.x = initial_x
        self.y = initial_y
        self.z = initial_z
    def __str__(self):
        return "x: " + str(self.x) + " y: " + str(self.y) + " z: " + str(self.z) + " | "
    
    def __mul__(self, other):
        if isinstance(other, Vector_3D):
            x_product = self.x * other.x
            y_product = self.y * other.y
            z_product = self.z * other.z
            return Vector_3D(x_product, y_product, z_product)
        elif isinstance(other, int) or isinstance(other, float):
            x_product = self.x*other
            y_product = self.y*other
            z_product = self.z*other
            return Vector_3D(x_product, y_product, z_product)
    
    def __mod__(self, other):   # overload MOD operator to render magnitude of distance
        return self.magnitude_of_dist(self-other)
    
    def __add__(self, other):
        return Vector_3D(self.x+other.x, self.y+other.y, self.z+other.z)
    def __sub__(self, other):
        x_sub = self.x - other.x
        y_sub = self.y - other.y
        z_sub = self.z - other.z
        return Vector_3D(x_sub, y_sub, z_sub)
    
    def __div__(self, other):
        x_div = float64(self.x) / other.x
        y_div = float64(self.y) / other.y
        z_div = float64(self.z) / other.z
        return Vector_3D(x_div, y_div, z_div)
    
    def __pow__(self, power):
        self.x = self.x**power
        self.y = self.y**power
        self.z = self.z**power
        return self
    
    def magnitude_of_dist(self, r):
        return sqrt(r.x**2 + r.y**2 + r.z**2)
    
    def magnitude(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def raw_mag(self, r):
        return r.x**2 + r.y**2 + r.z**2
