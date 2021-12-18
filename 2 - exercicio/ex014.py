# TOCANDO UMA MÚSICA USANDO BIBLIOTECA EXTERNA
# NÃO ESQUEÇA DE INSTALAR A BIBLIOTECA EXTERNA NA LÂMPADA (PRA QUEM USA PYCHARM)
# ATUALIZADO DIA 18/12/2021 - PODE MUDAR COM O TEMPO

import pygame

pygame.mixer.init()     # se tirar o programa fecha antes de a música terminar
pygame.init()

pygame.mixer.music.load('ex014.mp3')
pygame.mixer.music.play()
pygame.event.wait()     # aguardar a música acabar para finalizar o programa


# Acoustic Breeze | Royalty Free Music
# Composer: Benjamin Tissot
# site: Bensound

