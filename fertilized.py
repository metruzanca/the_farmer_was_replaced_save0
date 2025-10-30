import util
import config

util.random_hat()

while(True):
	for i in range(get_world_size()):
		harvest()
		util.make_till()
		plant(Entities.Sunflower)
		use_item(Items.Fertilizer)
		move(North)
	move(East)	