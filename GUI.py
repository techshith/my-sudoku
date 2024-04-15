import pygame
from sudokuSolverAlgo import *
from sudokuSolverAlgo import solve_sudoku

pygame.init()

WIDTH, HEIGHT = 540, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Sudoku")

# Basic colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 9x9 board with some zeros
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

font = pygame.font.SysFont("comicsans", 40)

def draw_grid(win, board, selected):
    gap = WIDTH // 9
    for i in range(9):
        for j in range(9):
            x = j * gap
            y = i * gap
            if board[i][j] != 0:
                text = font.render(str(board[i][j]), True, BLACK)
                win.blit(text, (x + 15, y + 10))
            if selected == (i, j):
                pygame.draw.rect(win, (255, 0, 0), (x, y, gap, gap), 3)

    for i in range(10):
        thick = 3 if i % 3 == 0 else 1
        pygame.draw.line(win, BLACK, (0, i * gap), (WIDTH, i * gap), thick)
        pygame.draw.line(win, BLACK, (i * gap, 0), (i * gap, WIDTH), thick)

def get_clicked_pos(pos):
    gap = WIDTH // 9
    x, y = pos
    row = y // gap
    col = x // gap
    return (row, col)

def main():
    selected = None
    run = True
    while run:
        WIN.fill(WHITE)
        draw_grid(WIN, board, selected)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                selected = get_clicked_pos(pos)

            if event.type == pygame.KEYDOWN:
                if selected is not None:
                    row, col = selected
                    if (
                        0 <= row < 9 and 0 <= col < 9 and
                        board[row][col] == 0 and
                        event.unicode.isdigit() and
                        1 <= int(event.unicode) <= 9
                    ):
                        board[row][col] = int(event.unicode)

                if event.key == pygame.K_s:
                    solve_sudoku(board)

        pygame.display.update()

    pygame.quit()

main()
