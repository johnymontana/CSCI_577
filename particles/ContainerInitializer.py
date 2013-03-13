import numpy as np
import Container
from math import sqrt

class ContainerInitializer(object):

    def __init__(self, init_string):
        c = Container.Container()
        Lx = 10.
        Ly = 10.
        Lz = 0.
        dist = Lx / 5.
        vel = dist / 5.

        if init_string == 'one':
            c.Lx = Lx
            c.Ly = Ly
            c.Lz = Lz

            c.add_particle(0., dist, 0., 0., 0., 0.)

        elif init_string == 'two':
            c.Lx = Lx
            c.Ly = Ly
            c.Lz = Lz

            c.add_particle(1., 5., 0., 0.4, 0., 0.)
            c.add_particle(3., 5., 0., -0.4, 0., 0.)

        elif init_string == 'eight':
            lx = 10.
            ly = 10.
            dist = lx / 5.
            vel = dist / 5.
            #c.L = Vector_3D(10., 10., 0.)
            c.Lx = 10.
            c.Ly = 10.
            c.Lz = 0.
            c.add_particle(-dist+5,0.+5, 0., vel,0.,0.)
            c.add_particle(dist+5,0.+5,0., -vel,0.,0.)
            c.add_particle(0.+5,dist+5,0., 0.,-vel,0.)
            c.add_particle(0.+5,-dist+5,0., 0.,vel,0.)
            c.add_particle(dist/sqrt(2)+5,dist/sqrt(2)+5,0. , -vel/sqrt(2),-vel/sqrt(2),0.)
            c.add_particle(-dist/sqrt(2)+5,dist/sqrt(2)+5,0. , vel/sqrt(2),-vel/sqrt(2),0.)
            c.add_particle(-dist/sqrt(2)+5,-dist/sqrt(2)+5,0., vel/sqrt(2),vel/sqrt(2),0.)
            c.add_particle(dist/sqrt(2)+5,-dist/sqrt(2)+5,0., -vel/sqrt(2),vel/sqrt(2),0.)

        elif init_string == 'eight-zeros':
            lx = 10.
            ly = 10.
            dist = lx / 5.
            vel = dist / 5.
            #c.L = Vector_3D(10., 10., 0.)
            c.Lx = 10.
            c.Ly = 10.
            c.Lz = 0.
            c.add_particle(-dist+5,0.+5, 0., 0. ,0.,0.)
            c.add_particle(dist+5,0.+5,0., 0. , 0.,0.)
            c.add_particle(0.+5,dist+5,0., 0., 0. ,0.)
            c.add_particle(0.+5,-dist+5,0., 0.,vel,0.)
            c.add_particle(dist/sqrt(2)+5,dist/sqrt(2)+5,0. , 0., 0. , 0.)
            c.add_particle(-dist/sqrt(2)+5,dist/sqrt(2)+5,0. , 0., 0., 0.)
            c.add_particle(-dist/sqrt(2)+5,-dist/sqrt(2)+5,0., 0., 0., 0.)
            c.add_particle(dist/sqrt(2)+5,-dist/sqrt(2)+5,0., 0., 0. ,0.)

        if init_string == 'square_lattice':
            N = 8             # Particles per row
            Lx = 9.
            Ly = Lx
            #c.Ly = c.Lx       # Extents determined by Lx input
            # TODO: set L
            #c.L = Vector_3D(30., 30., 0.)
            c.Lx = 9.
            c.Ly = 9.

            d = 2.**(1/6.)    # Particle diameter
            x = np.linspace(d/2,Lx-d/2,N)
            y = np.linspace(d/2.,Lx-d/2,N)
            for i in range(x.size):
                for j in range(y.size):
                    c.add_particle(x[i],y[j],0., 0., 0., 0.)
                    #c.addParticle(x, y, z, vx, vy, ax, ay, mass)

        self.c = c


    def getContainer(self):
        return self.c



