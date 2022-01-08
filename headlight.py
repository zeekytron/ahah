class Headlight:
	"""Define a headlight object that has an x and y axis controlled by servos"""
	
	#define 
	def __init__(self, x_servo_port, y_servo_port, x_servo_origin, y_servo_origin):
		self.x_servo_port = x_servo_port
		self.y_servo_port = y_servo_port
		self.x_servo_origin = x_servo_origin
		self.y_servo_origin = y_servo_origin
		print(self.tostring())
		
	def move(self, new_x, new_y):
		print("move the headlight to point at x:", new_x, ", y:", new_y)

	def tostring(self):
		return(f'''Headlight instance\n 
		x_servo_port {self.x_servo_port} \n
		y_servo_port {self.y_servo_port} \n
		x_servo_origin {self.x_servo_origin} \n
		y_servo_origin {self.y_servo_origin} \n
		''')
