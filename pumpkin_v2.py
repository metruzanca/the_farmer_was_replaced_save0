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
	for ii in range(get_world_size()):
		for i in range(get_world_size()):
			
			
			
			
			move(North)
		move(East)
	
	
	
	
plan_all()


while(True):
	
	dead = False
	
	for ii in range(get_world_size()):
		for i in range(get_world_size()):
			#util.try_water()
			
			cost = get_cost(Entities.Pumpkin)[Items.Carrot]
			
			if num_items(Items.Carrot) > cost:
				if get_entity_type() == Entities.Dead_Pumpkin or get_entity_type() == None:
					plant(Entities.Pumpkin)
					dead = True
			else:
				plant(Items.Carrot)
			
			#plant(Entities.Pumpkin)
			move(North)
		move(East)
	
	if dead == False:
		harvest()