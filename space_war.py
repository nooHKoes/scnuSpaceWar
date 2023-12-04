import pygame
import random
import math
import keyboard
from collections import deque
import sys
from os import path
from pygame.locals import *
from database import Database
import time
import sqlite3
from sprites import (all_sprites,meteorite_sprites,bullet_sprites,bullet_sprites_2,bullet_sprites_3,
                     bullet_sprites_4,bullet_sprites_5,bullet_sprites_6,bulletup_sprites,ultbulletup_sprites,
                     speedup_sprites,healthup_sprites,liveup_sprites,enemy1_sprites,enemy2_sprites,
                     roundbullet_sprites,boss1_sprites,laser1_sprites,dart_sprites,enemy3_sprites,boss2_sprites,
                     x_sprites,boss3_sprites,boss4_sprites, boss5_sprites,shieldup_sprites,shield_sprites,
                     missileup_sprites,missile_sprites,player1,player2)


