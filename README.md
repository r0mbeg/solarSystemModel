# solarSystemModel
A simple model of the Solar System.


To run the code you need install the `graphics` and `tkinter` libraries.

To solve the n-body problem, we first consider two bodies with masses m1 and m2, coordinates (x1, y1) and (x2,y2), and velocities (vx1, vy1) and (vx2,vy2):

![Image alt](https://github.com/r0mbeg/solarSystemModel/blob/master/FormulasAndImages/2Bodies.png)

To calculate the trajectory of motion of bodies, we use Newton's second law and the potential energy gradient:

![Image alt](https://github.com/r0mbeg/solarSystemModel/blob/master/FormulasAndImages/Newton2.png)

The potential energy for our case:

![Image alt](https://github.com/r0mbeg/solarSystemModel/blob/master/FormulasAndImages/PotentialEnergy.png)

Acceleration of the first body on the OX-axis:

![Image alt](https://github.com/r0mbeg/solarSystemModel/blob/master/FormulasAndImages/AccelerationXfor2.png)

The Y-axis acceleration and the second body acceleration are calculated in the same way (function `update_acceleration_for2`). Then we get:

![Image alt](https://github.com/r0mbeg/solarSystemModel/blob/master/FormulasAndImages/Accelerationsfor2.png)

The new velocities of each of the objects in a small time interval Δt are calculated using the increment(function `update_velocity`):

![Image alt](https://github.com/r0mbeg/solarSystemModel/blob/master/FormulasAndImages/Velocitiesfor2.png)

Similarly, we calculate the new coordinates (function `update_coords`):

![Image alt](https://github.com/r0mbeg/solarSystemModel/blob/master/FormulasAndImages/Coordsfor2.png)

Calculating the acceleration of a body with the number i (function `update_acceleration`):

![Image alt](https://github.com/r0mbeg/solarSystemModel/blob/master/FormulasAndImages/Accelerations.png)

Calculating the coordinates of the body with the number i:

![Image alt](https://github.com/r0mbeg/solarSystemModel/blob/master/FormulasAndImages/Coords.png)

