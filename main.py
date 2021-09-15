#Kinematics Visualizer 
import pygame,sys,math 
WIDTH,HEIGHT = 900,600
pygame.init()
SCREEN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Kinematics Visualizer")

#global variables
GRAVITY = -1

#defining the projectile motion function 
def projectile(x,y,angle,vel):
	global GRAVITY,B1_INIT_VEL

	#for y 
	y_distance = (vel*(math.sin(angle))) + (GRAVITY/2)
	vel = vel + GRAVITY

	y-=y_distance

	#for x 
	x_distance = (B1_INIT_VEL*(math.cos(angle))) + (GRAVITY/2)
	x += x_distance


	return x,y,angle,vel


#defining the ball class
class Ball:
	def __init__(self,x,y):
		self.radius = 20 
		self.x,self.y = x,y

	def draw(self):
		pygame.draw.circle(SCREEN,(255,255,0),(self.x,self.y),self.radius)



if __name__ == '__main__':
	b1x,b1y = 100,500
	b1_angle = 60/57.2958
	b1_init_vel = 20
	B1_INIT_VEL = 20 
	do_projectile = False 
	FONT  = pygame.font.Font("freesansbold.ttf",35)
	reset_font = FONT.render("Reset",True,(255,255,255))
	start_font = FONT.render("Start",True,(255,255,255))
	start_box_x,stat_box_y = 0,0
	box_width,box_height = 100,50
	reset_box_x,reset_box_y = 500,0
	while True :
		for event in pygame.event.get():
			if event.type==pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
				pygame.quit()
				sys.exit()

		SCREEN.fill((0,0,0))
		pygame.draw.line(SCREEN,(255,255,255),(0,500),(900,500))

		b = Ball(b1x,b1y)
		b.draw()

		if start_box_x+box_width>=pygame.mouse.get_pos()[0]>=start_box_x and stat_box_y+box_height>=pygame.mouse.get_pos()[1]>=stat_box_y:
			pygame.draw.rect(SCREEN,(0,255,0),pygame.Rect(start_box_x,stat_box_y,box_width,box_height))
			if True in pygame.mouse.get_pressed():
				do_projectile = True 
		else :
			pygame.draw.rect(SCREEN,(0,128,0),pygame.Rect(start_box_x,stat_box_y,box_width,box_height))

		if do_projectile:
			if (not b1y > 500):
				b1x,b1y,b1_angle,b1_init_vel = projectile(b1x,b1y,b1_angle,b1_init_vel)
			else:	
				b1y = 500
				b1_angle = 60/57.2958
				b1_init_vel = 20
				B1_INIT_VEL = 20 
				do_projectile = False 

		if reset_box_x+box_width>=pygame.mouse.get_pos()[0]>=reset_box_x and reset_box_y+box_height>=pygame.mouse.get_pos()[1]>=reset_box_y:
			pygame.draw.rect(SCREEN,(0,0,255),(reset_box_x,reset_box_y,box_width,box_height))
			if True in pygame.mouse.get_pressed():
				b1x = 100
		else:
			pygame.draw.rect(SCREEN,(0,0,128),(reset_box_x,reset_box_y,box_width,box_height))

		SCREEN.blit(start_font,(0,0))
		SCREEN.blit(reset_font,(500,0))

		pygame.time.Clock().tick(100)
		pygame.display.update()