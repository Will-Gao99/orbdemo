import pygame
import os
import time

pygame.font.init()

WIN_HEIGHT = 720
WIN_WIDTH = 1280

PLAYER_IMGS = "to be determind"
BG_IMG = "to be determined"
ORB_IMG = "to be determined"

class Player:
    def __init__(self, x, y):
        pass

    def draw(self, win):
        win.blit(self.img, (self.x,self.y))


class Orb:
    def __init__(self, x, y):
        pass

    def draw(self, win):
        win.blit(self.img, (self.x,self.y))


def draw_window(win,player,orb):
    win.blit(BG_IMG, (0,0))
    player.draw(win)
    orb.draw(win)
    pygame.display.update()


def main():
    pass

if __name__ == "__main__":
    main()
