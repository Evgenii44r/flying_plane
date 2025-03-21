import pygame
pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("самолетики")


background = pygame.image.load("resources/sky.jpg")
player1_img = pygame.image.load("resources/plane1.png")
player2_img = pygame.image.load("resources/plane2.png")


background = pygame.transform.scale(background, (width, height))
player1_img = pygame.transform.scale(player1_img, (150, 150))
player2_img = pygame.transform.scale(player2_img, (150, 150))


player1_pos = [100, 300]
player2_pos = [700, 300]
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1_pos[1] -= 5
    if keys[pygame.K_s]:
        player1_pos[1] += 5
    if keys[pygame.K_a]:
        player1_pos[0] -= 5
    if keys[pygame.K_d]:
        player1_pos[0] += 5
    player1_pos[0] = max(0, min(player1_pos[0], width - 150))
    player1_pos[1] = max(0, min(player1_pos[1], height - 150))
    mouse_pos = pygame.mouse.get_pos()
    player2_pos[0] = max(0, min(mouse_pos[0] - 75, width - 150))
    player2_pos[1] = max(0, min(mouse_pos[1] - 75, height - 150))
    screen.blit(background, (0, 0))
    screen.blit(player1_img, player1_pos)
    screen.blit(player2_img, player2_pos)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()