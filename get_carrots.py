import util
import config

change_hat(Hats.Carrot_Hat)

while(True):
	for ii in range(get_world_size()):
		for i in range(get_world_size()):
			util.try_water()
			
			harvest()
			plant(Entities.Carrot)
			
			move(North)
		move(East)
	
	