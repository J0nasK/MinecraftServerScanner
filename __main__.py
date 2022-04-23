import socket
import threading
import sys
import argparse
import sys
from mcstatus import MinecraftServer
import checkServer

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("ipv4")
    parser.add_argument("scanningThreads")
    args = parser.parse_args(sys.argv[1:])

    def thredFunk():
        while True:
            global ip1
            global ip2

            ip1 += 1

            if ip1 >= 255:
                ip1 = 0
                ip2 += 1

            if ip2 >= 255:
                exit()


            ip = str(args.ipv4[0]) + "." + str(args.ipv4[1]) + "." + str(ip2) + "." + str(ip1)

            serverData = checkServer.checkServer(ip)
            if serverData != None:
                if serverData.players.online != 0:
                    if serverData.players.online != 0:
                        try:
                            query = MinecraftServer(ip).query()
                            players = query.players.names
                            print(str(ip) + ", " + str(serverData.version.name) + ", " + str(serverData.players.online) + "        -       " + str(players))

                        except socket.timeout:
                            pass

                        except OSError:
                            pass

                else:
                    print(str(ip) + ", " + str(serverData.version.name) + ", " + str(serverData.players.online))

    ip1 = 1
    ip2 = 1

    for i in range(0,int(args.scanningThreads)):
        x = threading.Thread(target=thredFunk)
        x.start()
        print(i)
