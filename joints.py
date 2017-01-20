import math
from pyrosim import PYROSIM
def finn_lengde_etter_vinkelflytting(vinkel,lengde):
    #x=tan(vinkel)*
    return math.tan(vinkel)*lengde

upper_ARM_LENGTH = 0.4

upper_ARM_RADIUS = upper_ARM_LENGTH / 11.0

lower_ARM_LENGTH = upper_ARM_LENGTH

lower_ARM_RADIUS = lower_ARM_LENGTH / 11.0

sim = PYROSIM(playPaused = False , evalTime = 1000)

sim.Send_Cylinder(objectID = 0 , x=0, y=0, z=upper_ARM_LENGTH/2.0 + upper_ARM_RADIUS, r1=0, r2=0, r3=1, length=upper_ARM_LENGTH, radius=upper_ARM_RADIUS , b=74)

sim.Send_Cylinder(objectID = 1 , x=0, y=lower_ARM_LENGTH/2.0, z=lower_ARM_LENGTH + lower_ARM_RADIUS, r1=0, r2=1, r3=0, length=lower_ARM_LENGTH, radius=lower_ARM_RADIUS)

ylengde=-lower_ARM_LENGTH/2.7
xflytting = finn_lengde_etter_vinkelflytting(math.pi/4, ylengde)

sim.Send_Cylinder(objectID = 2 , x=xflytting, y=ylengde, z=lower_ARM_RADIUS, r1=1, r2=1, r3=0, length=lower_ARM_LENGTH, radius=lower_ARM_RADIUS)

#sim.Send_Joint(jointID = 0, firstObjectID=0, secondObjectID=1, x=0, y=0, z=upper_ARM_LENGTH + lower_ARM_RADIUS, n1=1, n2=0, n3=0, lo=-3.14159/4.0, hi=+3.14159/4.0)
sim.Send_Joint(jointID = 0, firstObjectID=0, secondObjectID=1,      x=0, y=0,z=upper_ARM_LENGTH+ lower_ARM_RADIUS,    n1=0, n2=1, n3=0,   lo=-3.14159/4.0, hi=+3.14159/4.0)

sim.Send_Joint(jointID = 1, firstObjectID=0, secondObjectID=2,      x=0, y=0,z= lower_ARM_RADIUS,    n1=0, n2=1, n3=0)


sim.Start()



# sim.Collect_Sensor_Data()
