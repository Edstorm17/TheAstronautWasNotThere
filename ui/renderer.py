from game.entity import entities


def draw_background(screen):
    screen.fill("darkorchid4")

def draw_game_layer(screen):

    entities.get_group().draw(screen)

def draw_all(screen):
    draw_background(screen)
    draw_game_layer(screen)