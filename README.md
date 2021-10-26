# How to launch

To run the code you need install the `graphics` and `tkinter` libraries

After you have run the file `Model.py` you will see a window:

![Image alt](https://github.com/r0mbeg/solarSystemModel/blob/master/FormulasAndImages/interface.png)

In this window, you can click `Run the sample model` to run an example of a pre-created system or create your own, which will be shown below.

If you decided to create your own model, then here, in the input fields, you can enter the parameters of the object you are adding. For example, let's add the planet Earth. It will be blue. Its radius will be 7 pixels, and its mass will be 0.00001 units. The initial coordinates on the screen are (500, 500), the initial velocity vector is (0.3):

![Image alt](https://github.com/r0mbeg/solarSystemModel/blob/master/FormulasAndImages/earth.png)

Then you need to fill in the input fields like this and click `Add object`:

![Image alt](https://github.com/r0mbeg/solarSystemModel/blob/master/FormulasAndImages/earthEntry.png)

After adding another object, it will appear in the list at the bottom of the window:

![Image alt](https://github.com/r0mbeg/solarSystemModel/blob/master/FormulasAndImages/objectsList.png)

After adding all the desired objects, click `Configure interaction`. You will see an adjacency matrix showing the gravitational interactions between objects:

![Image alt](https://github.com/r0mbeg/solarSystemModel/blob/master/FormulasAndImages/matrix.png)

If you want, here you can disable the gravitational interactions between the added objects. For example, remove the interaction between object 1 and object 3.

After you finish configuring the interaction, click `Run model`. You will see a window with the visualization:

![Image alt](https://github.com/r0mbeg/solarSystemModel/blob/master/FormulasAndImages/run.gif)




# Mathematical description

To solve the n-body problem, we first consider two bodies with masses m1 and m2, coordinates (x1, y1) and (x2,y2), and velocities (vx1, vy1) and (vx2,vy2):

![Image alt](https://github.com/r0mbeg/solarSystemModel/blob/master/FormulasAndImages/2Bodies.png)

To calculate the trajectory of motion of bodies, we use Newton's second law and the potential energy gradient:

![Image alt](https://latex.codecogs.com/gif.latex?\LARGE&space;\vec{F}=m\vec{a}=-\frac{\partial&space;U}{\partial&space;r})

The potential energy for our case:

![Image alt](https://github.com/r0mbeg/solarSystemModel/blob/master/FormulasAndImages/PotentialEnergy.png)

Acceleration of the first body on the OX-axis:

![Image alt](https://github.com/r0mbeg/solarSystemModel/blob/master/FormulasAndImages/AccelerationXfor2.png)

The Y-axis acceleration and the second body acceleration are calculated in the same way (function `update_acceleration_for2`). Then we get:

![Image alt](https://github.com/r0mbeg/solarSystemModel/blob/master/FormulasAndImages/Accelerationsfor2.png)

The new velocities of each of the objects in a small time interval Δt are calculated using the increment (function `update_velocity`):

![Image alt](https://github.com/r0mbeg/solarSystemModel/blob/master/FormulasAndImages/Velocitiesfor2.png)

Similarly, we calculate the new coordinates (function `update_coords`):

![Image alt](https://github.com/r0mbeg/solarSystemModel/blob/master/FormulasAndImages/Coordsfor2.png)

Calculating the acceleration of a body with the number i (function `update_acceleration`):

![Image alt](https://github.com/r0mbeg/solarSystemModel/blob/master/FormulasAndImages/Accelerations.png)

Calculating the coordinates of the body with the number i:

![Image alt](https://github.com/r0mbeg/solarSystemModel/blob/master/FormulasAndImages/Coords.png)

