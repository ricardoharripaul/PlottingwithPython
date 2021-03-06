# -*- coding: utf-8 -*-
# moviewriter.py
import numpy as np
import pylab as p
import matplotlib.animation as an

# Create an FFMPEG writer.
ffwriter=an.writers['ffmpeg']

# Metadata is good practice.
metadata=dict(title='Example',artist='Ricardo Harripaul')

# Specify some features.
writer = ffwriter(fps = 15, metadata = metadata)
fig = p.figure()

l,=p.plot([],[],'ko')

p.xlim(-3,3); p.ylim=(-3,3)

x0=np.zeros(10.0)
y0=np.zeros(10.0)

with writer.saving(fig,'example.mp4', 200):

#4 is position 5 is velocity
    for i in range(200):
        print x0
        print y0
        x0 += 0.1 * np.random.randn(10)
        y0 += 0.1 * np.random.randn(10)
    
    #Specify new x and y data for position and velocity
        l.set_data(x0,y0)
        writer.grab_frame()  
