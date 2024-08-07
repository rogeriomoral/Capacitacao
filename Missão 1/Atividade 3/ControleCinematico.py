from coppeliasim_zmqremoteapi_client import *
import numpy as np 

client = RemoteAPIClient()
sim = client.getObject('sim')

handle_robo = sim.getObject('/robozao')

roda_direita = sim.getObject('/robozao/motor_direito')
roda_esquerda = sim.getObject('/robozao/motor_esquerdo')

# Dados do robo P3DX
# L = diametro do chassi
L = 0.17
# r = raio da roda
r = 0.02


wr = np.deg2rad(270)
wl = np.deg2rad(-270)

sim.setJointTargetVelocity(roda_direita, wr)
sim.setJointTargetVelocity(roda_esquerda, wl)

sim.startSimulation()

while (t := sim.getSimulationTime()) < 10:

    pos = sim.getObjectPosition(handle_robo, -1)
    print(pos)

sim.stopSimulation()