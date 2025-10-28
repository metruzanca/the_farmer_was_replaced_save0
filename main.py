import util
import config

util.random_hat()

while(True):
	for i in range(get_world_size()):
		harvest()
		util.make_till()
		util.water()
		util.plantNext()
		move(North)
	move(East)	