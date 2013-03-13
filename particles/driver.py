import Container
import Force
import Integrator
import ContainerInitializer

import numpy as np
import matplotlib.pyplot as plt

FRAME_RATE = 50

c = ContainerInitializer.ContainerInitializer("eight-zeros").getContainer()
f = Force.Force(c)
i = Integrator.Integrator(0.01, f)

state_list = []
count = 0

while count < 4000:
    print "--------- BEGIN TIMESTEP " + str(count) + " --------------"
    i.integrate()
    #plt.plot(c.x, c.y)
    #plt.show()
    if count % FRAME_RATE == 0:
        print "c.x"
        print c.x
        print "c.y"
        print c.y
        for particle in range(c.x.size):
            part_x = 0.
            part_y = 0.
            #particles[particle] = {"x": c.x[particle], "y": c.y[particle]}
            plt.xlim((0, 10))
            plt.ylim((0, 10))
            plt.plot(c.x[particle], c.y[particle], 'o')
        plt.show()

    count += 1


