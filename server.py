import socket
from _thread import *
import sys
from player import Player
import pickle


server = "0.0.0.0"
port = 1224

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((server, port))

except socket.error as e:
	print(str(e))

s.listen()
print("Waiting for a connection, Server started")



players = [Player(0), Player(-1)]


def threaded_client(conn, currentPlayer):
	conn.send(pickle.dumps(players[currentPlayer]))
	reply = ""
	while True:
		try:
			data = pickle.loads(conn.recv(2048))
			players[currentPlayer] = data
			

			if not data:
				print("Disconnected")
				break
			else:
				if currentPlayer == 1:
					reply = players[0]
				else:
					reply = players[1]
				print("Received:", players[0].camid)
				#print("Sending:", reply)

			conn.sendall(pickle.dumps(reply))
		except:
			break

	print("Lost connection")
	conn.close()

	
currentPlayer = 0
while True:
	conn, addr = s.accept()
	print("Connected to:", addr)

	start_new_thread(threaded_client, (conn, currentPlayer))
	if currentPlayer == 0:
		currentPlayer += 1
	else:
	        pass
