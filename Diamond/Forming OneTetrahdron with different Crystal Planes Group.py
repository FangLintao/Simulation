import numpy as np
import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):    
    def __init__(self, xs, ys, zs, *args, **kwargs):
        arrow_prop_dict = dict(mutation_scale=20, arrowstyle='-|>', color='k', shrinkA=0, shrinkB=0) # default parameters
        for key in kwargs :
            arrow_prop_dict[key] = kwargs[key] # overwrite the default values if there is a conflict
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **arrow_prop_dict)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

class npArrow3D(Arrow3D):
    """
    #Arrow3D that can be defined with numpy (3,1) Arrays
    """
    def __init__(self, start,end,*args, **kwargs):
        """
        #start and end are numpy column matrices
        """
        arrow_prop_dict = dict(mutation_scale=20, arrowstyle='-|>', color='k', shrinkA=0, shrinkB=0) # default parameters
        for key in kwargs :
            arrow_prop_dict[key] = kwargs[key] # overwrite the default values if there is a conflict
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **arrow_prop_dict)
        self._verts3d = [start[0,0],end[0,0]], [start[1,0],end[1,0]], [start[2,0],end[2,0]]

    def draw(self, renderer):
        Arrow3D.draw(self,renderer)
        
#class annotated_Arrow3D(npArrow3D):
#     def __init__(self,start,end,arrowprops={},label='',textprops={}):
#          npArrow3D.__init__(self,start,end,arrowprops)
#          self.
def draw_npArrow3D(ax,start,end=None,delta=None,arrowprops={},label=None,textprops={}):
    """
    
    """
    if end is None :
        if delta is not None :
            end =start + delta;
        else :
            raise AssertionError('Missing Argument end or delta')

    lc=[ax.add_artist(npArrow3D(start,end,**arrowprops))]
    if label is not None :
        lc.append(nptext3D(ax,end,label,**textprops))
    return lc

def nptext3D(ax,loc,string,**kwargs):
    """
    write text at the location given by a (3,1) numpy array
    """
    return ax.text(loc[0,0],loc[1,0],loc[2,0],string,**kwargs)
# Create Plane Vectors to match corresponding Crystal Plane

def Tetrahedron(Inter_Point,R_Angle,x,y):
    xl=x.reshape(-1,1)
    yl=y.reshape(1,-1)
    X,Y= np.ones_like(yl)*xl,np.ones_like(xl)*yl
# Establish X and Y Axials
    
    CryP_Vector_3 = np.array([[1., 1., 1.],[-1., 1., 1.],[1., -1., 1],[-1., -1., 1]])
    CryP_Vector_2 = np.array([[0., 1., 1.],[0., -1., 1.],[1., 0., 1],[-1., 0., 1]])
    T=random.randint(0,2)
    if T == 0:
        CryP_Vector = np.delete(CryP_Vector_3,random.randint(0,3),0)
# Forming Crystal Planes Group {1 1 1} but all have positive vector

    elif T == 1:
        CryP_Vector = np.delete(CryP_Vector_2,random.randint(0,3),0)
# Forming Crystal Planes Group {1 1 0} but all have positive vector        
    else:
        CryP_Vector=np.zeros(shape=(3,3))
        S=random.randint(0,1)
        if S==0:
            CryP_Vector_T=np.delete(np.delete(CryP_Vector_3,random.randint(0,3),0),random.randint(0,2),0)
            for t in range(len(CryP_Vector_T)):
                CryP_Vector[t]=CryP_Vector_T[t]
            CryP_Vector[2]=CryP_Vector_2[random.randint(0,3)]
        else:
            CryP_Vector_T=np.delete(np.delete(CryP_Vector_2,random.randint(0,3),0),random.randint(0,2),0)
            for t in range(len(CryP_Vector_T)):
                CryP_Vector[t]=CryP_Vector_T[t]
            CryP_Vector[2]=CryP_Vector_3[random.randint(0,3)]
# Forming Crystal Planes Group of {111} and {110} but all have positive vector 

    RX_Matrix = np.array([[1., 0., 0.],[0., np.cos(R_Angle[0]), -np.sin(R_Angle[0])],[0., np.sin(R_Angle[0]), np.cos(R_Angle[0])]])
    RY_Matrix = np.array([[np.cos(R_Angle[1]), 0., np.sin(R_Angle[1])],[0., 1., 0],[-np.sin(R_Angle[1]), 0., np.cos(R_Angle[1])]])
    RZ_Matrix = np.array([[np.cos(R_Angle[2]), -np.sin(R_Angle[2]), 0],[np.sin(R_Angle[2]), np.cos(R_Angle[2]), 0.],[0., 0., 1]])
    R_Matrix=np.dot( np.dot (RX_Matrix , RY_Matrix) , RZ_Matrix )
# Establish Rotation Matrix in 3-Dimensional Coordinates   

    Ro_Plane=np.dot(R_Matrix,CryP_Vector)
# Rotate Crystal Planes by using Rotation Matrix
  
    Height=np.full((len(x),len(y)),np.max(Ro_Plane))
    for i in Ro_Plane:
        P_Height = Inter_Point[2] - ( i[0]*(X-Inter_Point[0]) + i[1]*(Y-Inter_Point[1]) ) / i[2]
        Height=np.minimum(Height,P_Height)
# Calculate Planes' Height

    H_Bool=Height<=0
    Height[H_Bool]=0
# Make Data start from 0 in Z Axial
    
    print('the Result of Crystal Plane Vector is: \n {}'.format(CryP_Vector))
    print('the Result of Rotational Matrix is: \n {}'.format(R_Matrix))
    print('the Result of Rotational Crystal Plane is : \n {}'.format(Ro_Plane))
    return X,Y,Height,Ro_Plane,CryP_Vector
"""
N should be at least larger than 100
"""
x=np.linspace(-10,10,500)
y=np.linspace(-10,10,500)

Inter_X=random.uniform(x[0],x[-1])
Inter_Y=random.uniform(y[0],y[-1])
Inter_Point=np.array([Inter_X,Inter_Y,1])
Vector_Point=np.array([Inter_Point[0],Inter_Point[1],0]) 

RX_Angle=random.uniform(4,8)
RY_Angle=random.uniform(4,8)
RZ_Angle=random.uniform(4,8)
R_Angle=np.array([ np.pi/RX_Angle , np.pi/RY_Angle , np.pi/RZ_Angle ])

X,Y,Height,Ro_Plane,CryP_Vector=Tetrahedron(Inter_Point,R_Angle,x,y)


plt.pcolor(X,Y,Height,cmap=plt.cm.Blues)
plt.colorbar()
plt.xlabel("x (µm)")
plt.ylabel("y (µm)")
plt.title("One Tetrahedron,  $S_{{max}}$={:.3f}µm".format(np.max(Height)))
plt.show()
#Forming 2D plot

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y,Height, cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=0, )
draw_npArrow3D(ax,Vector_Point.reshape(-1,1),delta=Ro_Plane[0].reshape(-1,1),label=str(CryP_Vector[0]))
draw_npArrow3D(ax,Vector_Point.reshape(-1,1),delta=Ro_Plane[1].reshape(-1,1),label=str(CryP_Vector[1]))
draw_npArrow3D(ax,Vector_Point.reshape(-1,1),delta=Ro_Plane[2].reshape(-1,1),label=str(CryP_Vector[2]))  
ax.set_xlabel('X (µm)')
ax.set_ylabel('Y (µm)')
ax.set_zlabel('Z (µm)')
plt.show()
#Forming 3D plot