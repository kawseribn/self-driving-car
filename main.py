#!/usr/bin/env python
# coding: utf-8

# In[83]:


import pygame
pygame.init()


# In[84]:


drive = True
clock = pygame.time.Clock()

window = pygame.display.set_mode((1200, 400))
track = pygame.image.load('track.png')
car = pygame.image.load('tesla.png')
car  = pygame.transform.scale(car, (30, 60))
red = pygame.image.load('red.png')
red  = pygame.transform.scale(red, (30, 55))
green = pygame.image.load('green.png')
green  = pygame.transform.scale(green, (30, 55))

timer = 0
red1=True
green1 = True
car_x = 193
car_y = 300
focal_dist = 35
direction = "up"
cam_x_offset=0
cam_y_offset=0
#window.blit(track,(0,0))
#window.blit(car, (car_x,car_y))
#window.blit(red,(270,113))
#pygame.display.update()


# In[85]:


while drive:
    timer+=1
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False
            exit()
    #detect road
    
    cam_x = car_x+cam_x_offset+15
    cam_y = car_y + cam_y_offset + 15
    
    up_px = window.get_at((cam_x, cam_y - focal_dist))[0]
    down_px = window.get_at((cam_x, cam_y + focal_dist))[0]
    right_px = window.get_at((cam_x + focal_dist, cam_y ))[0]
    print(up_px, right_px, down_px)
    #take turn
    if direction == "up" and up_px!= 255 and right_px == 255:
        direction = "right"
        cam_x_offset = 30
        print(str(up_px)+"baal"+ str(right_px)+ str(down_px))
        car = pygame.transform.rotate(car, -90)
        
    elif direction == 'right' and right_px!=255 and down_px == 255:
        direction = 'down'
        print("ghure")
        car_x = car_x + 30
        cam_x_offset = 0
        cam_y_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'down' and down_px != 255 and right_px == 255:
        direction = 'right'
        car_y = car_y + 30
        cam_x_offset = 30
        cam_y_offset = 0
        car = pygame.transform.rotate(car, 90)
    elif direction == 'right' and right_px != 255 and up_px == 255:
        direction = 'up'
        car_x = car_x + 30
        cam_x_offset = 0
        car = pygame.transform.rotate(car, 90)
        
    #drive    
    if direction == "up" and up_px == 255:
        car_y = car_y - 2   
    elif direction == "right" and right_px == 255:
        car_x = car_x + 2
    elif direction == "right" and right_px == 255 or (right_px>=85 and right_px<=95):
        car_x = car_x + 2
    elif direction == 'down' and down_px == 255:
        car_y = car_y + 2
    window.blit(track,(0,0))
    window.blit(car, (car_x,car_y))
    if timer<200:
        window.blit(red,(270,113))
    else:
        window.blit(green,(270,113))
    
    pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)
    pygame.display.update()
    


# In[ ]:





# In[ ]:




