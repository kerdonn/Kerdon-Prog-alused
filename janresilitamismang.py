import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Silita seda pedepoissi!")

# Gay pride flag colors (Red, Orange, Yellow, Green, Blue, Purple)
pride_colors = [
    (255, 0, 0),  # Red
    (255, 127, 0),  # Orange
    (255, 255, 0),  # Yellow
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
    (139, 0, 255)  # Purple
]

# Load the pet image (replace with the path to your own image file)
pet_image = pygame.image.load('IMG_4074.jpeg')  # Your image file
pet_image = pygame.transform.scale(pet_image, (600, 100))  # Scale the image to fit

# Position of the pet image
pet_rect = pet_image.get_rect()
pet_rect.center = (400, 400)  # Center the image in the window

# Font for the name
font = pygame.font.Font(None, 36)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Mouse click event
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pet_rect.collidepoint(event.pos):
                print("Sa silitasid oma boytoy Janret!")

    # Fill the background with rainbow pride colors
    stripe_height = screen.get_height() // len(pride_colors)  # Height for each stripe
    for i, color in enumerate(pride_colors):
        pygame.draw.rect(screen, color, (0, i * stripe_height, screen.get_width(), stripe_height))

    # Draw the pet image (Janre)
    screen.blit(pet_image, pet_rect.topleft)

    # Display the pet name "Janre"
    text = font.render("Janre", True, (0, 0, 0))  # Black text
    screen.blit(text, (pet_rect.centerx - text.get_width() // 2, pet_rect.bottom + 10))

    # Update the screen
    pygame.display.flip()
