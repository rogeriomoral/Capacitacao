import math
from coppeliasim_zmqremoteapi_client import *
import numpy as np 

# Normalize angle to the range [-pi,pi)
def normalizeAngle(angle):
    return np.mod(angle+np.pi, 2*np.pi) - np.pi

def getCurrentlyPosition(handle):
    robotPos = sim.getObjectPosition(handle, -1)
    robotOri = sim.getObjectOrientation(handle, -1)        
    return np.array([robotPos[0], robotPos[1], robotOri[2]])

# Conectando ao Coppelia
client = RemoteAPIClient()
sim = client.getObject('sim')
    
# Handles do robô e das juntas
robotHandle = sim.getObject('/robozao')    
robotLeftMotorHandle  = sim.getObject('/robozao/motor_esquerdo')
robotRightMotorHandle = sim.getObject('/robozao/motor_direito')
    
# configuração do Goal (x, y, theta)
goalPosition = np.array([2, 0, np.deg2rad(90)])
#qgoal = np.array([-2, -4, np.deg2rad(180)])

# Raio do chassi
L = 0.085
# raio da roda
r = 0.02
#velocidade maxima linear e angular
maxv = 1.0
maxw = np.deg2rad(45)

rho = np.inf

sim.startSimulation()
while rho > .10:

    #pega a posição atual do robô
    robotConfig = getCurrentlyPosition(robotHandle)

    #calcula erro
    dx, dy, dth = goalPosition - robotConfig

    # distancia do centro do robo até o goal
    rho = np.sqrt(dx**2 + dy**2)
    print(rho)
    # quao longe a orientação do robo está do alvo
    alpha = normalizeAngle(-robotConfig[2] + np.arctan2(dy,dx))
    # erro entre a orientação atual e a orientação desejada
    beta = normalizeAngle(goalPosition[2] - np.arctan2(dy,dx))

    # constantes de estabilidade
    kr = 3 / 14
    ka = 8 / 14
    kb = -1.5 / 14

    # calcula velocidade linear e angular
    v = kr*rho
    w = ka*alpha + kb*beta
    
    # limitando v e w para os limites definidos anteriormente
    v = max(min(v, maxv), -maxv)
    w = max(min(w, maxw), -maxw)        
    
    # definindo velocidade das rodas
    wr = ((2.0*v) + (w*L))/(2.0*r)
    wl = ((2.0*v) - (w*L))/(2.0*r)
    
    sim.setJointTargetVelocity(robotRightMotorHandle, wr)
    sim.setJointTargetVelocity(robotLeftMotorHandle, wl)
    
    
print("objetivo atingido!")
sim.setJointTargetVelocity(robotRightMotorHandle, 0)
sim.setJointTargetVelocity(robotLeftMotorHandle, 0)

sim.stopSimulation()
