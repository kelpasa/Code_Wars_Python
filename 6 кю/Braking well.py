'''
Braking distance d1 is the distance a vehicle will go from the point when it brakes to when it comes to a complete stop. It depends on the original speed v and on the coefficient of friction mu between the tires and the road surface.

The braking distance is one of two principal components of the total stopping distance. The other component is the reaction distance, which is the product of the speed and the perception-reaction time of the driver.
'''


import math
def dist(v, mu):
    return (v*0.277778)+((v*0.277778)**2)/(2*mu*9.81)

def speed(d, mu):
    b = -2 * mu * 9.81
    return round(3.6 * (b + math.sqrt(b*b - 4*b*d) ) / 2,2)
