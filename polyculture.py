# Uses second drone to go harvest previous crop

# --- utils ---
def goto_absolute(x, y):
	pass
	
# --- main ---
def harvest_previous(x, y):
	def drone():
		pass
		# goto previous spot
		# harvest
		# die
	return spawn_drone(drone)

if __name__ == "__main__":
	harvester_drone = None
	
	plant(Entities.Carrot)
	while True:
		current_x = get_pos_x()
		current_y = get_pos_y()
		plant_type, (x, y) = get_companion()
		goto_absolute(x, y)
		plant(plant_type)
		if harvester_drone == None or wait_for(harvester_drone):
			harvester_drone = harvest_previous(current_x, current_y)