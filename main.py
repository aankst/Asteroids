import pygame
from logger import log_state
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from logger import log_event
from circleshape import CircleShape
import sys
from shot import Shot

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt = 0

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots)

    asteroid = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        shots.update(dt)

        for astroid in asteroids:
            if CircleShape.collides_with(astroid, player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for astroid in asteroids:
            for shot in shots:
                if CircleShape.collides_with(astroid, shot):
                    log_event("asteroid_shot")
                    astroid.split()
        
        screen.fill("black")
        for drawabl in drawable:
            drawabl.draw(screen)
        for shot in shots:
            shot.draw(screen)

        pygame.display.flip()

        Clock.tick(60)
        dt = Clock.tick(60) / 1000


if __name__ == "__main__":
    main()
