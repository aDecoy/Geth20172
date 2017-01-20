from pyrosim import PYROSIM

sim = PYROSIM()
sim = PYROSIM(playPaused=True, evalTime=1000)#before objects

sim.Send_Cylinder(objectID=0,x=0,y=0,z=0.7, length=1,radius=0.1,r=245)
sim.Send_Cylinder(objectID=1,r1=0.8,r2=0,r3=0,x=0.5,y=0,z=1.2, length=1,radius=0.1, b=245)


sim.Start()
