import util
import config

change_hat(Hats.Pumpkin_Hat)

while(True):
	
	dead = False
	
	for ii in range(get_world_size()):
		for i in range(get_world_size()):
			#util.try_water()
			
			cost = get_cost(Entities.Pumpkin)[Items.Carrot]
			
			if get_entity_type() == Entities.Carrot and can_harvest():
				harvest()
			
			if num_items(Items.Carrot) > cost:
				if get_entity_type() == Entities.Dead_Pumpkin or get_entity_type() == None:
					plant(Entities.Pumpkin)
					dead = True
			else:
				plant(Entities.Carrot)
			
			#plant(Entities.Pumpkin)
			move(North)
		move(East)
	
	if dead == False:
		harvest()