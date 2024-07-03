import pygame                     #import the pip install pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Ball properties
ball_radius = 20
ball_color = white
ball_speed_x = 3
ball_speed_y = 3

# Initialize the ball position
ball_pos_x = screen_width // 2
ball_pos_y = screen_height // 2

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Ball")

# Clock object to control the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update ball position
    ball_pos_x += ball_speed_x
    ball_pos_y += ball_speed_y

    # Check for collisions with the screen boundaries
    if ball_pos_x - ball_radius <= 0 or ball_pos_x + ball_radius >= screen_width:
        ball_speed_x = -ball_speed_x

    if ball_pos_y - ball_radius <= 0 or ball_pos_y + ball_radius >= screen_height:
        ball_speed_y = -ball_speed_y

    # Fill the screen with black
    screen.fill(black)

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (ball_pos_x, ball_pos_y), ball_radius)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
