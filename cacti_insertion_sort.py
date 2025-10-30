# --- Insertion Sort ---
def look_right():
	move(East)
	val = measure()
	move(West)
	return val
	
def tape_sort(length):
	for i in range(length):
		swapped = False
		for j in range(length - 1 - i):
			if measure() > look_right():
				swap(East)
				swapped = True
			move(East)
		for _ in range(length - 1 - i):
			move(West)
		if not swapped:
			return

# --- Main ---
import util
	
def drone(size = 22):
	# Plant
	for i in range(size):	
		util.make_till()
		plant(Entities.Cactus)
		move(East)
			
	# Go back
	for i in range(size):
		move(West)

	# Sort
	tape_sort(size)

	util.Harvest()

if __name__ == "__main__":
	util.reset_position()
	
	change_hat(Hats.Cactus_Hat)
	
	
	for i in range(max_drones() - 1):
		spawn_drone(util.repeat(drone))
		move(North)
		move(North)
	
	while True:
		drone()

		
		