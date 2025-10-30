import util

def drone():
	while(True):
		for i in range(get_world_size()):
			harvest()
			plant(Entities.Grass)
			move(North)
		move(East)	

util.reset_position()
while num_drones() != max_drones():
	spawn_drone(drone)
	move(East)
	move(East)
	move(East)
drone()
