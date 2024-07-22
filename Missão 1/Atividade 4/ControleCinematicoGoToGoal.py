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
robotHandle = sim.getObject('/PioneerP3DX')    
robotLeftMotorHandle  = sim.getObject('/PioneerP3DX/leftMotor')
robotRightMotorHandle = sim.getObject('/PioneerP3DX/rightMotor')
    
referenceHandle = sim.getObject('/Ponto_2')

# Raio do chassi
#L = 0.085
# raio da roda
#r = 0.035
L = 0.331
r = 0.09751
#velocidade maxima linear e angular
maxv = 1.0
maxw = np.deg2rad(45)

rho = np.inf

sim.startSimulation()
while rho > 0.05:

    #pega posição do goal
    goalPosition = getCurrentlyPosition(referenceHandle)
    #pega a posição atual do robô
    robotConfig = getCurrentlyPosition(robotHandle)

    #calcula erro
    #dx, dy, dth = goalPosition - robotConfig
    dx = goalPosition[0] - robotConfig[0]
    dy = goalPosition[1] - robotConfig[1]
    dth = goalPosition[2] - robotConfig[2] 

    # distancia do centro do robo até o goal
    rho = np.sqrt((dx**2) + (dy**2))
    print(rho)
    # quao longe a orientação do robo está do alvo
    alpha = normalizeAngle(-robotConfig[2] + np.arctan2(dy,dx))
    # erro entre a orientação atual e a orientação desejada
    beta = normalizeAngle(goalPosition[2] - np.arctan2(dy,dx))

    # constantes de estabilidade
    kr = 3 / 20
    ka = 8 / 20
    kb = -1.5 / 20

    # calcula velocidade linear e angular
    v = kr*rho
    w = ka*alpha + kb*beta
    
    # limitando v e w para os limites definidos anteriormente       
    v = np.clip(v, -maxv, maxv)
    w = np.clip(w, -maxw, maxw)
    
    # definindo velocidade das rodas
    wr = ((2.0*v) + (w*L))/(2.0*r)
    wl = ((2.0*v) - (w*L))/(2.0*r)

    sim.setJointTargetVelocity(robotRightMotorHandle, wr)
    sim.setJointTargetVelocity(robotLeftMotorHandle, wl)
    
    
print("objetivo atingido!")
sim.setJointTargetVelocity(robotRightMotorHandle, 0)
sim.setJointTargetVelocity(robotLeftMotorHandle, 0)

sim.stopSimulation()
