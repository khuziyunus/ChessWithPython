import pygame


class Square:
    def __init__(self ,x ,y ,width ,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.abs_x = x * height 
        self.abs_y = y * height
        self.abs_pos = (self.abs_x, self.abs_y)
        self.abs = (x, y)
        self.colour = 'light' if (x+y)%2 == 0 else 'dark'
        self.draw_colour = (220,208,194) if self.colour == 'light' else (53,53,53)
        self.highlight_colour = (100,249,83) if self.colour == 'light' else (0,228, 10)
        self.occupying_piece = None
        self.coord = self.get_coord()
        self.highlight = False
        self.rect = pygame.Rect(
            self.abs_x,
            self.abs_y
            self.width,
            self.height
        )

        # get the formal notation of the tile
    def get_coord(self):
        columns = 'abcdefgh'
        return columns[self.x] + str(self.y + 1)

    def draw(self, display):
        # configures if tile should be light or dark or highlighted tile
        if self.highlight:
            pygame.draw.rect(display, self.highlight_color, self.rect)
        else:
            pygame.draw.rect(display, self.draw_color, self.rect)
        # adds the chess piece icons
        if self.occupying_piece != None:
            centering_rect = self.occupying_piece.img.get_rect()
            centering_rect.center = self.rect.center
            display.blit(self.occupying_piece.img, centering_rect.topleft)