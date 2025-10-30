import util
import coords

def create_maze():
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, 2)

def treasure_checker():
	while True:
		if get_entity_type() == Entities.Treasure:
			harvest()
				
def main_drone():
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

# place drone in every space
spawn_drone(main_drone)
move(North)
spawn_drone(treasure_checker)
move(East)
spawn_drone(treasure_checker)
move(South)
create_maze()
treasure_checker()






