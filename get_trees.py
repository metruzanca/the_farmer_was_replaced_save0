import util
import config

change_hat(Hats.Tree_Hat)
util.reset_position()

while(True):
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
		util.plant_tree()
		move(North)
	move(East)	