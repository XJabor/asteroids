import pygame, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print ("Starting Asteroids!")
    # print (f"Screen width: {SCREEN_WIDTH}")
    # print (f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group() ### should I call this something else?
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)
    Shot.containers = (shots_group, updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots_group)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        # this is my movement controls
        updateable.update(dt)

        # check for collisions

        for obj in asteroids:
            if player.collision(obj):
                print ("Game over!")
                sys.exit()

        # draw everything
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        #limit framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
