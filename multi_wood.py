import util

def drone():
	while(True):
		for i in range(get_world_size()):
			harvest()
			if (
			get_pos_x() % 2 == 0 and get_pos_y() % 2 == 0
			) or (get_pos_x() % 2 == 1 and get_pos_y() % 2 == 1):
				plant(Entities.Tree)
			else:
				plant(Entities.Bush)
			move(North)
		move(East)	

util.reset_position()
while num_drones() != max_drones():
	spawn_drone(drone)
	move(East)
	move(East)
drone()
