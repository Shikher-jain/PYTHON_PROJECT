import pygame
import chess
import chess.engine
from tkinter import Tk, Button

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
SQUARE_SIZE = WIDTH // 8
WHITE = (238, 238, 210)
BLACK = (118, 150, 86)
PIECE_IMAGES = {}

# for piece in ['p', 'r', 'n', 'b', 'q', 'k', 'P','R', 'N', 'B', 'Q', 'K']:
#     PIECE_IMAGES[piece] = pygame.transform.scale(
#         pygame.image.load(f'https://www.pychess.org/assets/pieces/{piece}.png'), (SQUARE_SIZE, SQUARE_SIZE)
#     )

for piece in ['bP','bR','bN','bB','bQ','bK','wP', 'wR', 'wN', 'wB', 'wQ', 'wK']:
    PIECE_IMAGES[piece] = pygame.transform.scale(
        pygame.image.load(f'F:/SHIKHER-VS/Advance-Python-SJ/Projects/Game/Photos/chess7/{piece}.svg'), (SQUARE_SIZE, SQUARE_SIZE)
    )

board = chess.Board()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")
    
def draw_board():
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces():
    for row in range(8):
        for col in range(8):
            square = chess.square(col, 7 - row)
            piece = board.piece_at(square)
            if piece:
                screen.blit(PIECE_IMAGES[piece.symbol()], (col * SQUARE_SIZE, row * SQUARE_SIZE))

# Main Loop
running = True
selected_square = None
while running:
    draw_board()
    draw_pieces()
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            col, row = x // SQUARE_SIZE, y // SQUARE_SIZE
            square = chess.square(col, 7 - row)
            
            if selected_square is None:
                selected_square = square
            else:
                move = chess.Move(selected_square, square)
                if move in board.legal_moves:
                    board.push(move)
                selected_square = None

pygame.quit()