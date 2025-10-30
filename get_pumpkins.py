# Deterministic. Can re-run script after pausing/harvesting
# and it won't start the farm over

import util
import config

def get_pumpkin(setup = False):
	dead = False
	size = get_world_size()
	
	for ii in range(size):
		for i in range(size):
			
			type = get_entity_type()
			
			# If previous crop, harvest and replant
			if type!= Entities.Pumpkin:
				harvest()
	
			# till takes 1 tick
			if setup == True:
				util.make_till()
				
			# If was dead, mark as dead
			if type!= Entities.Pumpkin:
				dead = True
				plant(Entities.Pumpkin)
				use_item(Items.Fertilizer)

			move(North)
		move(East)
	
	if dead == False:
		#use_item(Items.Fertilizer)
		util.Harvest()


if __name__ == "__main__":
	change_hat(Hats.Traffic_Cone)
	util.reset_position()
	change_hat(Hats.Pumpkin_Hat)
	get_pumpkin(True)
	while(True):
		get_pumpkin()
