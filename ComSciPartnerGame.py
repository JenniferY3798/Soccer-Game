#########################################
# File Name: brickBreakerStarter.py
# Description: Starter code for Brick Breaker game
# Author: ICS2O
# Date: 08/11/2017
#########################################
import pygame
pygame.init()
WIDTH = 800
HEIGHT= 600
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))

TOP    = 0  
BOTTOM = HEIGHT
LEFT   = 0     
RIGHT  = WIDTH 
GREEN = (  0,255,  0)
BLUE  = (  0,  0,128)
WHITE = (255,255,255)
BLACK = (  0,  0,  0)
outline = 0

#---------------------------------------#
# functions                             #
#---------------------------------------#
def redrawGameWindow():
    gameWindow.fill(BLACK)
    pygame.draw.circle(gameWindow, WHITE, (ballX, ballY), ballR, outline)
    pygame.draw.rect(gameWindow, GREEN, (paddleX, paddleY, paddleW, paddleH), outline)
    pygame.draw.rect(gameWindow, GREEN, (paddleX2, paddleY2, paddleW2, paddleH2), outline)
    pygame.display.update()
        
#---------------------------------------#
# the main program begins here          #
#---------------------------------------#
print "Hit ESC to end the program."
#---------------------------------------#
# ball properties                       #
#---------------------------------------#
ballR  = 15
ballX  =  WIDTH/2
ballY  =  2*ballR
speedX =  1
speedY =  1

#---------------------------------------#
# paddle properties                     #
#---------------------------------------#
#player one uses ws, left side
paddleW  = 20
paddleH  = 120
paddleX = 0
paddleY = (HEIGHT-120)/2
paddleShift = 2

#player2 uses up down, right 
paddleW2 = 20
paddleH2 = 120
paddleX2 = 780
paddleY2 = (HEIGHT-120)/2
paddleShift2 = 2

#----------------------------------------#
inPlay = True
while inPlay:
    redrawGameWindow()
    pygame.time.delay(2)
    
# check for key eventsw
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        inPlay = False
    if keys[pygame.K_UP]:
        if  paddleY2 - paddleShift2 <0:
            paddleY2 = 0
        else:
            paddleY2 = paddleY2 - paddleShift2
    if keys[pygame.K_DOWN]:
        if  paddleY2+paddleH2 + paddleShift2 >HEIGHT:
            paddleY2 = HEIGHT-paddleH
        else:
            paddleY2 = paddleY2 + paddleShift2
    if keys[pygame.K_w]:
        if  paddleY - paddleShift <0:
            paddleY = 0
        else:
            paddleY = paddleY - paddleShift
    if keys[pygame.K_s]:
        if  paddleY+paddleH + paddleShift>HEIGHT:
            paddleY = HEIGHT-paddleH
        else:
            paddleY = paddleY + paddleShift

# bounce the ball from the paddle
    if ballX-ballR <= paddleX+paddleW and ballY <= paddleY+paddleH and ballY >= paddleY:
        speedX = -speedX
# bounce the ball from the second Paddle
    if ballX+ballR >= paddleX2 and ballY <= paddleY2+paddleH2 and ballY >= paddleY2:
        speedX = -speedX
# bounce the ball from left, right, and top borders
    if ballY>=BOTTOM or ballY<=0:
        speedY = -speedY

# move the ball
    ballX = ballX + speedX
    ballY = ballY + speedY    
    if ballX-ballR <=LEFT:
        print "Game Over!"
        inPlay = False
    if ballX+ballR >=RIGHT:
        print "Game Over!"
        inPlay = False
        
#---------------------------------------# 
pygame.quit()
