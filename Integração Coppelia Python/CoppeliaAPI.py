import sim
import time

#Conectando com o coppelia
def connect():
    sim.simxFinish(-1)  # Fecha todas as conexões existentes
    clientID = sim.simxStart('192.168.1.102', 19997,
                            waitUntilConnected=True,  # Aguardar conexão
                            doNotReconnectOnceDisconnected=False,  # Reconectar se desconectado
                            timeOutInMs=5000,  # Tempo limite em milissegundos
                            commThreadCycleInMs=5)  # Ciclo do thread de comunicação em milissegundos

    # Verificando se a conexão foi bem-sucedida
    if clientID != -1:
        print('Conectado ao CoppeliaSim Edu!')
    else:
        print('Falha ao conectar-se ao CoppeliaSim Edu!')
        exit()
    return clientID

def disconnect(clientID):
    sim.simxFinish(clientID)
    print('Desconectado do CoppeliaSim')

def start_simulation(clientID):
    res = sim.simxStartSimulation(clientID, sim.simx_opmode_oneshot_wait)

    if res == sim.simx_return_ok:
        print('Simulação iniciada com sucesso')
    else:
        print('Falha ao iniciar a simulação')
        exit()

def stop_simulation(clientID):
    res = sim.simxStopSimulation(clientID, sim.simx_opmode_oneshot_wait)

    if res == sim.simx_return_ok:
        print('Simulação parada com sucesso')
    else:
        print('Falha ao parar a simulação')
        exit()

def get_robot_handle(clientID):

    # Obter o handle do robô
    errorCode, botHandle = sim.simxGetObjectHandle(clientID, 'Pioneer_p3dx', sim.simx_opmode_blocking)

    # Verificar se a operação foi bem-sucedida
    if errorCode == sim.simx_return_ok:
        print('Handle do robô obtido com sucesso')
        return botHandle
    else:
        print('Falha ao obter o handle do robô')
        exit()


def move_robot(clientID):

    botHandle = get_robot_handle(clientID)

    start_simulation(clientID)

    #pegando o handle das juntas
    leftMotorHandle = sim.simxGetObjectHandle(clientID, 'Pioneer_p3dx_leftMotor', sim.simx_opmode_blocking)[1]
    rightMotorHandle = sim.simxGetObjectHandle(clientID, 'Pioneer_p3dx_rightMotor', sim.simx_opmode_blocking)[1]

    # definindo a velocidade das juntas para o robô girar
    sim.simxSetJointTargetVelocity(clientID, leftMotorHandle, 2.0, sim.simx_opmode_streaming)
    sim.simxSetJointTargetVelocity(clientID, rightMotorHandle, -2.0, sim.simx_opmode_streaming)

    # Executar por 5 segundos
    time.sleep(5)

    # Parar o robô
    sim.simxSetJointTargetVelocity(clientID, leftMotorHandle, 0.0, sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(clientID, rightMotorHandle, 0.0, sim.simx_opmode_oneshot)

    stop_simulation(clientID)

    
def main():
    clientID = connect()
    if clientID is None:
        return

    # girar o robô
    move_robot(clientID)

    # Aguardar um pouco antes de desconectar
    time.sleep(2)

    # Desconectar-se do CoppeliaSim
    disconnect(clientID)

main()



    