# Cone
![image](https://github.com/FangLintao/Simulation/blob/master/Cone/images/Cone.png)  
this project is to simulate a scene that a ball falls down towards a cone. 
# Scene
* Properties -> this ball and cone both have static electrons, for example, positive electrons, uniformly distributing on their surface;  
* Background -> a ball is falling down towards to a cone, and because of electrostatic force, this ball will suffer from electrostatic force, gravity and other potential forces;  
* Main Analysis -> in this project, we mainly analyze on electrostatic force acting both on ball's surface and cone' surface;  
* Analytic parameters -> pressure and deformation.  
# Results
below shows the result from this scene
### Brief Analysis
* When this ball is falling down, the closest distance to this ball is the top of this cone, so the pressure always reaches maximum value on the position of this top cone. At the same time, deformation is first occured at this position as well  
* As falling down, the distance is getting closer, then pressure and deformation get larger  
![image](https://github.com/FangLintao/Simulation/blob/master/Cone/images/Combination.png)  
By using following code -> [the Cone](https://github.com/FangLintao/Simulation/blob/master/Cone/Cone_Contact_Mechanics.ipynb), you should achieve this result  

        Cone_Contact_Mechanics.ipynb

# Error
External_load & Max_Pressure  
![image](https://github.com/FangLintao/Simulation/blob/master/Cone/images/Plot%20of%20External_load%20%26%20Max_Pressure.png)  
Offset & Contact_Area  
![image](https://github.com/FangLintao/Simulation/blob/master/Cone/images/Plot%20of%20Offset%20%26%20Contact_Area.png)  
Offset & External_load  
![image](https://github.com/FangLintao/Simulation/blob/master/Cone/images/Plot%20of%20Offset%20%26%20External_load.png)  
Offset & Max_Pressure  
![image](https://github.com/FangLintao/Simulation/blob/master/Cone/images/Plot%20of%20Offset%20%26%20Max_Pressure.png)
# Reference
PyCo, Prof. Dr. Lars Pastewka, Sanner Antoine, [simulation Group of Uni Freiburg](https://www.imtek.uni-freiburg.de/professuren/simulation/simulation)  
[Contact Mechanics](https://www.cambridge.org/core/books/contact-mechanics/E3707F77C2EBCE727C3911AFBD2E4AC2), K. L. Johnson, Cambridge University,1985,9781139171731 
