from network import Network
from player import Player









def main():
	n = Network()
	p1 = n.getP()
	run = True
    

	while run:
            x = input()
            p1.camid = x
            
            p2 = n.send(p1)
		
		
main()
