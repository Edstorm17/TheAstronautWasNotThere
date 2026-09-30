import pygame

import config

class Item:
    def __init__(self, name, image):
        self.name = name
        self.amount = 0

        raw_img = pygame.image.load(f"assets/{image}")
        self.image = pygame.transform.scale(raw_img, (config.ITEM_SIZE, config.ITEM_SIZE))

        items[name] = self

    def get_amount(self):
        return self.amount

items = {}

def get_for_render():
    return items.values()

gold = Item("gold", "gold.png")
argon = Item("argon", "argon.png")
