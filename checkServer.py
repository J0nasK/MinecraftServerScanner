import socket
from mcstatus import MinecraftServer

def checkServer(ip):
    server = MinecraftServer(ip)
    try:
        data = server.status()


        foundServer = str(ip) + ", " + str(data.version.name) + ", " + str(data.players.online)
        print(foundServer)

        return data


    except socket.timeout:
        pass


    except OSError:
        pass
