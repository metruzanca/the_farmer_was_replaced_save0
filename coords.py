def goto(x, y):
	while get_pos_x() > x:
		move(West)
	while get_pos_y() > y:
		move(South)

def reset_position():
	goto(0,0)

def goto_pos(pos):
	goto(pos[0], pos[1])