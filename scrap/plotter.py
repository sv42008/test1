import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

del_theta = (0.9/360)*(2*np.pi/360)
a = 80

def actual_del_r(r):
    del_r = del_theta*(4*a**2 - r**2)**(1/2)
    return del_r

def graph():
    x=[]
    position_along_x = 1
    for i in range(50000):
      #print(actual_del_r(position_along_x))
      position_along_x = position_along_x + actual_del_r(position_along_x)
      x.append(position_along_x)
    return x



def circle_generator(r):
    del_r = actual_del_r(r)
    numberofpoints = 2*np.pi*r/del_r
    x=[]
    y=[]
    #generates circle equidistant.
    scaled_numberofpoints = int(numberofpoints/2500)
    del_phi = 2*np.pi/scaled_numberofpoints
    for i in range(scaled_numberofpoints):
      phi = i*del_phi
      x.append(r*np.cos(phi))
      y.append(r*np.sin(phi))

    else:
      print(numberofpoints)
      return
    return x, y





#fig2 = plt.figure()
#ax = fig2.add_subplot(111)
x = graph()
x_every = x[0::2500]
#y=[]
#for i in range(len(x_every)):
  #y.append(0)
#plt.scatter(x_every, y)

print(x_every)
del x_every[0]
del x_every[8]
del x_every[7]
del x_every[6]

fig = plt.figure()
ax = fig.add_subplot(111)
plt.xlim(-180,180)
plt.ylim(-180,180)
ax.set_aspect('equal', adjustable='box')
for Rad in x_every:
  x_cood = circle_generator(Rad)[0]
  y_cood = circle_generator(Rad)[1]

  plt.scatter(x_cood, y_cood, c='b', marker=".", s=1)

plt.scatter(0, 0, c='b', marker='.', s = 1)
plt.show()
  