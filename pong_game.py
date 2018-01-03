import pygame, sys, math, random

#setting up global colours
WHITE = (255,255,255)
BLACK = (0,0,0)

#creates the player's bar
def player_bar(screen, bar_pos_y):
	pygame.draw.rect(screen, WHITE, [50, bar_pos_y, 15, 150])

def computer_bar(screen, x_screen, bar_pos_c_y):
	pygame.draw.rect(screen, WHITE, [x_screen-65, bar_pos_c_y, 15, 150])

#creates the ball
def ball(screen, x_ball, y_ball):
	pygame.draw.rect(screen, WHITE, [x_ball, y_ball, 10, 10])
	
def net(screen, x_screen, y_screen):
	pygame.draw.rect(screen, WHITE, [x_screen/2 - 3, 0, 6, y_screen])
	
def main():

	pygame.init()
	
	#setting up screen
	x_screen, y_screen = 1400, 800
	screen_size = (x_screen, y_screen)
	SCREEN_DISPLAY = pygame.display.set_mode(screen_size)
	pygame.display.set_caption('pong')
	#import text
	text_font = pygame.font.Font("C:/windows/fonts/vgafix.fon",40)
	
	#setting up clock for fps
	clock = pygame.time.Clock()
	
	#for main game loop
	quit_game = False
	#players initial settings
	bar_pos_y = y_screen/2 - (150/2)
	bar_pos_c_y = y_screen/2 - (150/2)
	y_speed = 0
	ball_pos_x = x_screen/2
	ball_pos_y = y_screen/2
	rand_direction_x = random.choice([1,-1]) #to set the random direction of the ball
	rand_direction_y = random.choice([1,-1])
	ball_speed_x = 8 * rand_direction_x
	ball_speed_y = random.choice([8,9,10]) * rand_direction_y
	player_score = 0
	computer_score = 0
	
	while quit_game == False: #main game loop
	
		for event in pygame.event.get(): #user did something
		
			if event.type == pygame.QUIT: #user wants to quit
				quit_game = True
				
			#below is for moving the player_bar
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w:
					y_speed = -6
				if event.key == pygame.K_s:
					y_speed = 6

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w:
					y_speed = 0
				if event.key == pygame.K_s:
					y_speed = 0
		
		SCREEN_DISPLAY.fill(BLACK)
		
		#ball animation / physics:
		rand_direction_x = random.choice([1,-1]) #to reset the random direction of the ball
		rand_direction_y = random.choice([1,-1])
		#stops ball from going off screen
		if ball_pos_x < 0:
			computer_score += 1 #if computer gets ball past player, add to score and reset ball
			ball_pos_x = x_screen/2
			ball_pos_y = y_screen/2
			ball_speed_x = 8 * rand_direction_x
			ball_speed_y = random.choice([6,7,8]) * rand_direction_y
		if ball_pos_x > x_screen-10:
			player_score += 1 #if player gets ball past opponent, add to score and reset ball
			ball_pos_x = x_screen/2
			ball_pos_y = y_screen/2
			ball_speed_x = 8 * rand_direction_x
			ball_speed_y = random.choice([6,7,8]) * rand_direction_y
		
		#if ball hits top or bottom of screen, it bounces off
		if ball_pos_y < 0 or ball_pos_y > y_screen-10:
			ball_speed_y = ball_speed_y * -1
			
		#player and computer bar physics
		#if ball makes contact with player bar, it bounces off
		if ball_pos_y > bar_pos_y and ball_pos_y < bar_pos_y + 150 and ball_pos_x < 65 and ball_pos_x >55:
			ball_speed_x = ball_speed_x * -1
		
		#if ball makes contact with the computer bar, it bounces off
		if ball_pos_y > bar_pos_c_y and ball_pos_y < bar_pos_c_y + 150 and ball_pos_x > x_screen-65 and ball_pos_x < x_screen - 55:
			ball_speed_x = ball_speed_x * -1
		
		#AI mechanics
		if ball_pos_y > bar_pos_c_y and ball_pos_y < bar_pos_c_y + 150:
			bar_pos_c_y += ball_speed_y/abs(ball_speed_y) *6
		elif ball_pos_y < bar_pos_c_y + 60:
			bar_pos_c_y -= 6
		elif ball_pos_y > bar_pos_c_y + 90:
			bar_pos_c_y += 6
			
		#ball velocity
		ball_pos_x += ball_speed_x
		ball_pos_y += ball_speed_y
		#player bar animation
		bar_pos_y += y_speed #allows players to move by adding pixels/frame
		
		#stops bars from going off screen
		if bar_pos_y >= y_screen - 150:
			bar_pos_y = y_screen - 150
		if bar_pos_y <= 0:
			bar_pos_y = 0
		if bar_pos_c_y >= y_screen - 150:
			bar_pos_c_y = y_screen - 150
		if bar_pos_c_y <= 0:
			bar_pos_c_y = 0
		
		#drawing components
		#background:
		#scores for player and computer:
		text = text_font.render("player: "+ str(player_score), True, WHITE)
		SCREEN_DISPLAY.blit(text, [x_screen/2 - 100, 5])
		text = text_font.render("computer: "+ str(computer_score), True, WHITE)
		SCREEN_DISPLAY.blit(text, [x_screen/2 + 20, 5])
		
		net(SCREEN_DISPLAY, x_screen, y_screen) #draws the net
		player_bar(SCREEN_DISPLAY, bar_pos_y) #draws the players bar
		computer_bar(SCREEN_DISPLAY, x_screen, bar_pos_c_y)
		ball(SCREEN_DISPLAY, ball_pos_x, ball_pos_y) #draws the ball
		
		#draws to the screen
		pygame.display.flip()
		
		#runs games at 60 fps
		clock.tick(60)
	
	#outside the main game loop, closes game
	pygame.quit()
	sys.exit()

if __name__ == '__main__':
	main()