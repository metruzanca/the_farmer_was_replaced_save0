import util
import coords

def create_maze(size = 2):
	plant(Entities.Bush)
	substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)

def treasure_checker():
	while True:
		if get_entity_type() == Entities.Treasure:
			harvest()
				
def main_drone():
	create_maze(2)
	while True:
		type = get_entity_type()
		if type != Entities.Hedge or type != Entities.Treasure:
			create_maze()
			pass
			
		if type == Entities.Treasure:
			harvest()

change_hat(Hats.Traffic_Cone)
set_world_size(4)

util.reset_position()

def make_2x2():
	# place drone in every space
	spawn_drone(treasure_checker)
	move(North)
	spawn_drone(treasure_checker)
	move(East)
	spawn_drone(treasure_checker)
	move(South)
	util.try_spawn(main_drone)

make_2x2()
move(East)
make_2x2()



