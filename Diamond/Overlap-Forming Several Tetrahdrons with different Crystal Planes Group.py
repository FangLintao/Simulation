import numpy as np
import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D

def Tetrahedron(x,y):
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
# Forming Crystal Planes Groups {111} and {110} but all have positive vector 
    
    RX_Angle = random.uniform(4,9)
    RY_Angle = random.uniform(4,9)
    RZ_Angle = random.uniform(4,9)
    R_Angle = np.array([ np.pi/RX_Angle , np.pi/RY_Angle , np.pi/RZ_Angle ])
# Creating one Rotational Angle for each palne 

    RX_Matrix = np.array([[1., 0., 0.],[0., np.cos(R_Angle[0]), -np.sin(R_Angle[0])],[0., np.sin(R_Angle[0]), np.cos(R_Angle[0])]])
    RY_Matrix = np.array([[np.cos(R_Angle[1]), 0., np.sin(R_Angle[1])],[0., 1., 0.],[-np.sin(R_Angle[1]), 0., np.cos(R_Angle[1])]])
    RZ_Matrix = np.array([[np.cos(R_Angle[2]), -np.sin(R_Angle[2]), 0.],[np.sin(R_Angle[2]), np.cos(R_Angle[2]), 0.],[0., 0., 1.]])
    R_Matrix=np.dot( np.dot (RX_Matrix , RY_Matrix) , RZ_Matrix )
    R_Matrix=np.round(R_Matrix, decimals=3,out=None)
# Establish Rotation Matrix in 3-Dimensional Coordinates   

    Ro_Plane=np.dot(R_Matrix,CryP_Vector)
# Rotate Crystal Planes by using Rotation Matrix
    
    Inter_X=random.uniform(x[0],x[-1])
    Inter_Y=random.uniform(y[0],y[-1])
    Inter_Z=random.uniform(0,1)
    Inter_Point=np.array([Inter_X,Inter_Y,Inter_Z])
# Creating Intersection Point

    Height=np.full((len(x),len(y)),np.max(Ro_Plane))
    for i in Ro_Plane:
        P_Height = Inter_Point[2] - ( i[0]*(X-Inter_Point[0]) + i[1]*(Y-Inter_Point[1]) ) / i[2]
        Height=np.minimum(Height,P_Height)
# Calculate Planes' Height

    H_Bool=Height<=0
    Height[H_Bool]=0
    Height = np.round(Height, decimals=3,out=None)
# Make Data start from 0 in Z Axial
    
    return X,Y,Height
"""
N should be at least larger than 100
"""

x=np.linspace(0,5,500)
y=np.linspace(0,5,500)
X,Y,_=Tetrahedron(x,y)
Height=np.zeros(shape=(len(x),len(y)))

Num=input("How many Tetrahdrons you want:")
Num=eval(Num)
for i in range(Num):
    N=2
    while N!=1:
        _,_,Each_Height = Tetrahedron(x,y)
        Max_Height = np.max( Each_Height )
        Max_Height-=Max_Height//1
        Tem_Height=Each_Height-(Max_Height//1)
        Bool = ( np.round(Tem_Height,decimals=1) == np.round(Max_Height,decimals=1) )
        if len(Each_Height[Bool])==1:
            N=1
        else:
            N=2
# Guarantee that Crystal planes, after rotation, Would not be parallel to xy plane
    Height=np.maximum ( Height , Each_Height )

plt.pcolor(X,Y,Height,cmap=plt.cm.Blues)
plt.colorbar()
plt.xlabel("x (µm)")
plt.ylabel("y (µm)")
plt.title("{0:3d} Tetrahedrons,  $S_{{max}}$={1:.3f}µm".format(Num,np.max(Height)))
plt.show()
#Forming 2D plot

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y,Height, cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=0, )
ax.set_xlabel('X (µm)')
ax.set_ylabel('Y (µm)')
ax.set_zlabel('Z (µm)')
plt.show()
#Forming 3D plot