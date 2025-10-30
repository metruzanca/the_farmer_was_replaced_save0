# Spawns as many drones as possible
# Farms 1x1 mazes
import util

def drone():
	while True:
		plant(Entities.Bush)
		use_item(Items.Weird_Substance)
		harvest()

for i in range(max_drones()):
	spawn_drone(drone)
	move(North)
	if num_drones() == max_drones():
		drone()
