import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_SIZE = (800, 600)
WHITE = (255, 255, 255)

# Create Pygame window
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Virtual Showroom")

# Load product images (replace with your images)
product1 = pygame.image.load('product1.jpg')
product2 = pygame.image.load('product2.jpg')

# Create a list of products
products = [(product1, "Product 1 Description", 100),
            (product2, "Product 2 Description", 150)]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Display products on the screen
    x_position = 50
    for product, description, price in products:
        screen.blit(product, (x_position, 50))
        x_position += 250  # Adjust the spacing between products

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
