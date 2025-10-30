import util
import config

change_hat(Hats.Tree_Hat)
util.reset_position()

while(True):
	for i in range(get_world_size()):
		harvest()
		if (
		get_pos_x() % 2 == 0 and get_pos_y() % 2 == 0
		) or (get_pos_x() % 2 == 1 and get_pos_y() % 2 == 1):
			plant(Entities.Tree)
		elif get_pos_x() % 2 == 0:
			plant(Entities.Grass)
		else:
			plant(Entities.Carrot)
		move(North)
	move(East)	