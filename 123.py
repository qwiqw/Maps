import sys
import requests
import os
import pygame

pygame.init()
size = width, height = 600, 450
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Maps')

url = 'https://static-maps.yandex.ru/v1'

params = {
    'apikey': "4e60121e-3e68-41f0-bd84-eced30775d1c",
    'll': '37.617649,55.755115',
    'z': 15,
}


def get_map():
    response = requests.get(url=url, params=params)

    if not response:
        print(f'{response.status_code}{response.reason}')
        sys.exit(1)

    with open('map.png', mode='wb') as map_file:
        map_file.write(response.content)

    return pygame.image.load('map.png')


running = True

map_image = get_map()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                params['z'] += 1
                if params['z'] >= 21:
                    params['z'] = 21
                map_image = get_map()
            if event.key == pygame.K_PAGEDOWN:
                params['z'] -= 1
                if params['z'] <= 1:
                    params['z'] = 1
                map_image = get_map()

    screen.blit(map_image, (0, 0))
    pygame.display.flip()
os.remove('map.png')

pygame.quit()
