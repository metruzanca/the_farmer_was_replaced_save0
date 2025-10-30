import util
import coords
import config
import list

## WIP!

change_hat(Hats.Pumpkin_Hat)

# Plants a pumpkin on all spaces
def plan_all():
	for ii in range(get_world_size()):
		for i in range(get_world_size()):
			# Cleanup previous crop
			harvest()
			
			# Pumpkins need tilled soil
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Pumpkin)
			move(North)
		move(East)

# Keep processing the list until no more dead pumpkins
def process_dead(item, index):
	pass
	coords.goto_pos(item)
	if get_entity_type() == Entities.Dead_Pumpkin:
		dead.append((get_pos_x(), get_pos_y()))


def haverst_mega():
	dead = []
	
	# Go over all and track the ones that died
	for ii in range(get_world_size()):
		for i in range(get_world_size()):
			if get_entity_type() == Entities.Dead_Pumpkin:
				dead.append((get_pos_x(), get_pos_y()))
		
			move(North)
		move(East)
	
	


	while True:
		list.foreach(dead, process_dead)
		
		if len(dead) == 0:
			break
	
	harvest()	
	
	
plan_all()
haverst_mega()
