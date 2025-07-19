import pygame
pygame.init()
width,height = 500,500
display = pygame.display.set_mode((width,height))
pygame.display.set_caption("Rudransh")
background=pygame.image.load("backroundimage.jpeg")
background_image = pygame.transform.scale(background.convert(),(width,height))
character = pygame.image.load("ant.jpeg")
character_image=pygame.transform.scale(character.convert_alpha(),(200,200))
character_rect = character_image.get_rect(center=(width//2,height//2))
text = pygame.font.Font(None,36).render("Cheese",True,pygame.Color("yellow"))
done = False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True
    display.blit(background_image,(0,0))
    display.blit(character_image,character_rect)
    display.blit(text,text.get_rect(center=(width//2,height//2+20)))
    pygame.display.flip()