from time import time
from typing import List
import pygame, sys, time, random

from pygame.mixer import set_num_channels

pygame.init()

# Global Constants
width = 800
height = 800
player_color = (66, 245, 78)
food_color = (240, 130, 41)
block_dimension = 80
snake_direction = ""

food = [0, 0]
snake = [[0, 0]]
tail_to_add = []

game_board = pygame.display.set_mode([width, height])

def Update_Food_Location():
    # Update the food list
    while True:
        food[0] = random.randrange(1, 10) * block_dimension
        food[1] = random.randrange(1, 10) * block_dimension
        if food not in snake:
            break

def Draw_Food():
    # Draws food to the game board using the food list
    pygame.draw.rect(
        game_board,
        food_color,
        pygame.Rect(
            food[0], food[1], 
            block_dimension, block_dimension))

def Draw_Player_Snake():
    # Draws snake to the game board using the snake list
    for block in snake:
        pygame.draw.rect(
            game_board, 
            player_color, 
            pygame.Rect(
                block[0], block[1], 
                block_dimension, block_dimension))

def Append_Tail_Block_To_Snake():
    if len(tail_to_add) != 0:
        if tail_to_add[0] not in snake:
            snake.append(tail_to_add[0])

def Update_Player_Snake():
    # Update the position tuples in snake list

    #####################
    ## New Logic Below ##
    #####################

    if snake[0][0] == food[0] and snake[0][1] == food[1]:
        # snake.insert([food[0], food[1]], 0)
        snake.insert(0, [food[0], food[1]])
        Update_Food_Location()
    else:
        if snake_direction == "left":
            snake.insert(0, [snake[0][0] - block_dimension, snake[0][1]])
            if snake[0][0] < 0:
                snake[0][0] = width - block_dimension
            snake.pop()
        if snake_direction == "right":
            snake.insert(0, [snake[0][0] + block_dimension, snake[0][1]])
            if snake[0][0] >= width:
                snake[0][0] = 0
            snake.pop()
        if snake_direction == "up":
            snake.insert(0, [snake[0][0], snake[0][1] - block_dimension])
            if snake[0][1] < 0:
                snake[0][1] = height - block_dimension
            snake.pop()
        if snake_direction == "down":
            snake.insert(0, [snake[0][0], snake[0][1] + block_dimension])
            if snake[0][1] >= height:
                snake[0][1] = 0
            snake.pop()
        


# Run until the user asks to quit
running = True

while running:
    # Look for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_direction = "left"
            if event.key == pygame.K_RIGHT:
                snake_direction = "right"
            if event.key == pygame.K_UP:
                snake_direction = "up"
            if event.key == pygame.K_DOWN:
                snake_direction = "down"

    # Fill the background of the gameboard
    game_board.fill((0, 0, 0))

    # pygame.draw.rect(game_board, player_color, pygame.Rect(0, 0, 80, 80))
    # pygame.draw.rect(game_board, player_color, pygame.Rect(720, 0, 80, 80))
    # pygame.draw.rect(game_board, player_color, pygame.Rect(0, 720, 80, 80))
    # pygame.draw.rect(game_board, player_color, pygame.Rect(720, 720, 80, 80))

    Update_Player_Snake()

    # if food[0] == 0 and food[1] == 0:
    #     Update_Food_Location()

    Draw_Food()

    Draw_Player_Snake()

    time.sleep(0.5)

    # Flip the display
    pygame.display.flip()

# Time to QUIT!
pygame.quit()
sys.exit()
