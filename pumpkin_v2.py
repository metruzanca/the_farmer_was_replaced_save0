import util
import coords
import config

change_hat(Hats.Pumpkin_Hat)

# Plants a pumpkin on all spaces
def plan_all():
	for ii in range(get_world_size()):
		for i in range(get_world_size()):
			if can_harvest() and get_entity_type() != Entities.Pumpkin:
				harvest()
	
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Pumpkin)
			move(North)
		move(East)


def haverst_mega():
	dead = []
	
	# Go over all and track the ones that died
	for ii in range(get_world_size()):
		for i in range(get_world_size()):
			if get_entity_type() == Entities.Dead_Pumpkin:
				dead.append((get_pos_x(), get_pos_y()))
		
			move(North)
		move(East)
	
	
	# Keep processing the list until no more dead pumpkins
	while True:
		
		for item in dead:
			
			coords.goto_pos(item)
			if get_entity_type() == Entities.Dead_Pumpkin:
				dead.append((get_pos_x(), get_pos_y()))
			
		
		
		if len(dead) == 0:
			break
	
	
	harvest()	
	
	
plan_all()
haverst_mega()
