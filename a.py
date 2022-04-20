import openmesh as om
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d as m3d


from matplotlib.tri import Triangulation as Tri
import json
import sys
import numpy.linalg as alg
from mpl_toolkits.mplot3d import proj3d
import sympy as sp
import sympy.plotting as spplot
import math
from functools import reduce
import sympy.functions as spf


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
for spine in ax.spines.values():
    spine.set_position('center')
    pass

def test():
    p=np.array(([np.array([1,1,1]),np.array([2,2,2])]))
    p=np.mat(p)
    a=math.pi/4
    t=[[1,0,0],[0,math.cos(a), -math.sin(a)],[0,math.sin(a), math.cos(a)]]
    #t=np.mat(t)
    t=np.array(t)
    pp=t*p.transpose()
    pp=pp.transpose()
    pts=[]
    pts.extend(np.array(p))
    pts.extend(np.array(pp))
    #pts=[p, np.array(pp)
    #return pts


    for pt in pts:
        pass
        ax.scatter([pt[0]], [pt[1]],[pt[2]] )

    # fig.show()
    
    #return p, t,pp
    return ax

def hammer():
    dense=0.1
    
    def head_end(): #the octagon part
        w, x_start, x_end=3,2,6
        
        rw=np.linspace(0.-w/2., w/2., w/dense)
        face_btm=[ np.array([x_end, y,z]) for y in rw for z in rw]
        face_btm=np.array([p for p in filter(lambda p: abs(p[1])+abs(p[2])<w*math.sqrt(2)/2, face_btm)])

        t=w*math.sqrt(2)/4
        ry=np.linspace(0-t/2, t/2, t/dense)
        rx=np.linspace(x_start, x_end, (x_end-x_start)/dense)
        side=np.array([ np.array([x, y, w/2]) for x in rx for y in ry])
        
        return face_btm, side

    def head_end_allside():
        face_btm, face_side=head_end()
        angles=[x*math.pi/4 for x in range(1,8)]
        co=[np.mat([ [1,0,0],
                     [0,math.cos(a), -math.sin(a)],
                     [0,math.sin(a), math.cos(a)]
        ]) for a in angles]

        face_otherside=[ np.array((k*face_side.transpose()).transpose())  for k in co ]
        sides=[face_btm]
        sides.append(face_side)
        sides.extend(face_otherside)
        return sides
    
    def head_middle():
        w, x_start, x_end=3,-2,2
        
        rw=np.linspace(-w/2., w/2., w/dense)
        ry=rw
        rx=np.linspace(x_start, x_end, (x_end-x_start)/dense)
        side=np.array([ np.array([x, y, w/2]) for x in rx for y in ry])
        #return side
        angles=[x*math.pi/2 for x in range(1,4)]
        co=[np.mat([ [1,0,0],
                     [0,math.cos(a), -math.sin(a)],
                     [0,math.sin(a), math.cos(a)]
        ]) for a in angles]

        otherside=[ np.array((k*side.transpose()).transpose())  for k in co ]
        otherside.append(side)
        return otherside
    
    def head_end_opposit():
        pass

    def cylinder_handle():
        r,z_start,z_end=1.8, 1.5, 8
        ang_num=100
        a_range=np.linspace(0, math.pi*2, ang_num)
        z_range=np.linspace(z_start, z_end, (z_end-z_start)/dense)
        side=np.array([ np.array([r*math.cos(a), r*math.sin(a), z]) for z in z_range for a in a_range ])
        xy_range=np.linspace(-r, r, (z_end-z_start)/dense)
        btm=np.array([ np.array([r*math.cos(a), r*math.sin(a), z_end])  for x in xy_range for y in xy_range ])
        return [side]
        
    sides_head_end=head_end_allside()
    sides_head_middle=head_middle()
    sides_head_end_opposite=head_end_opposit()
    cylinder=cylinder_handle()
    sides=[]
    sides.extend(sides_head_end)
    sides.extend(sides_head_middle)
    sides.extend(cylinder)

    use_mlab=True
    if(use_mlab):
        import mayavi.mlab as mlab
        
    print(len(sides))
    #return
    for side in sides:
        if use_mlab:
            mlab.points3d(side[:,0], side[:,1], side[:,2], opacity=0.5)#, c='b')
        else:
            ax.scatter(side[:,0], side[:,1], side[:,2])#, c='b')

    for side in sides_head_end:
        if use_mlab:
            mlab.points3d(side[:,0]*-1, side[:,1], side[:,2],opacity=0.5)#, c='b')
        else:
            ax.scatter(side[:,0]*-1, side[:,1], side[:,2])#, c='b')

    if use_mlab:
        mlab.show()
    else:
        fig.show()        

if __name__=='__main__':
    test()
