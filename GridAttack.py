import os
import pygame
import pygame.font
from pygame.locals import *
import random
import time

pygame.init()

# Constants
board_rows = 10
board_columns = 15
tile_size = 25
buffer_zone = 25
empty_tile_color = (255, 255, 255)
barrier_tile_color = (100, 100, 100)
player_tile_color = (0, 255, 0)
text_color = (255, 255, 255)
barrier_density = 0.15
gen_alpha = 200
menu_columns = 5

font = pygame.font.Font("Code New Roman.ttf", tile_size)

# Calculated Constants
game_width = (board_rows + menu_columns) * tile_size + buffer_zone * 3
game_height = board_columns * tile_size + buffer_zone * 3
board_color_dict = {'_': empty_tile_color,
                    'X': barrier_tile_color,
                    'O': player_tile_color}

# Variables
board = [[]]

# Generates the game board
def generate_board():
    row_number = 0
    column_number = 0
    total_barriers = 0
    
    while row_number < board_rows:
        board.append([])
        while column_number < board_columns:
            total = row_number * board_rows + column_number
            barrier_ratio = total_barriers / (total) if total != 0 else barrier_density
            
            # This formula's weird. If the barrier ratio is not at the barrier density, I add a value to make
            # the next barrier more or less likely to occur to compensate.
            chance = barrier_density + ((0 if row_number == 0 else 1) * gen_alpha * (barrier_density - barrier_ratio)) / 100
            if chance < 0:
                chance = 0
            if chance > 1:
                chance = 1
                
            if random.uniform(0, 1) > chance:
               board[row_number].append('_')
            else:
               board[row_number].append('X')
               total_barriers = total_barriers + 1
            
            column_number = column_number + 1
            
        row_number = row_number + 1
        column_number = 0
            

# Displays the game board
def draw_board():
    row_number = 0
    column_number = 0
    
    for row in board:
        for tile in row:
            # _ is empty, X is barrier, O is player.
            rectangle = pygame.Surface((tile_size, tile_size))
            rectangle.fill(board_color_dict[tile])
            screen.blit(rectangle, (row_number + buffer_zone, column_number + 2 * buffer_zone))

            text_surface = font.render("Board", True, text_color)
            screen.blit(text_surface, (buffer_zone + 6 * tile_size, buffer_zone))
            
            column_number = column_number + tile_size
            
        row_number = row_number + tile_size
        column_number = 0
            
# Displays the menu
def draw_menu():
    menu = pygame.Surface((tile_size * menu_columns, tile_size * board_rows))
    menu.fill(empty_tile_color)
    screen.blit(menu, (board_rows * tile_size + buffer_zone * 2, buffer_zone * 3))
    
screen = pygame.display.set_mode((game_width, game_height))
game_status = "running"

generate_board()
while game_status == "running":
    draw_board()
    draw_menu()
    
    for event in pygame.event.get():
        
        
        '''
        # Check for KEYDOWN event; KEYDOWN is a constant defined in pygame.locals, which we imported earlier
        if event.type == KEYDOWN:
            # If the Esc key has been pressed set running to false to exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event; if QUIT, set running to false
        elif event.type == QUIT:
            running = False
        '''
    pygame.display.flip()

