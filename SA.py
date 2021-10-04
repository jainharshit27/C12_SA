import pygame, pymunk
import pymunk.pygame_util

#Create create_arrow() function here

pygame.init()

height = 600
width = 690
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#pymunk space
gravity = 1000
wind = 200
space = pymunk.Space()
space.gravity = wind, gravity
draw_options = pymunk.pygame_util.DrawOptions(screen)

vs_rect = [(1, -80), (1, 80), (-1, 80), (-1, -80)]
target_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
target_shape = pymunk.Poly(target_body, vs_rect)
target_body.position = 600,400
space.add(target_body, target_shape)

#Put the arrow in the function create_arrow() and return arrow_body and arrow_shape
vs = [(-80, 0), (0, 2), (10, 0), (0, -2)]
arrow_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
arrow_shape = pymunk.Poly(arrow_body, vs)
arrow_shape.density = 0.1
arrow_body.position = 100,140
space.add(arrow_body, arrow_shape)

while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                arrow_body.body_type = pymunk.Body.DYNAMIC
                
                #Add flying_arrows.append() with arrow_body as parameter
                #Call function create_arrow() and assign the values to arrow_body and arrow_shape like arrow_body, arrow_shape = create_arrow()
                #Add arrow_body and arrow_shape to space
                
    space.debug_draw(draw_options)
    
    pygame.display.update()
    
    #space reload
    space.step(1/60)
    clock.tick(60)
