from django.db import models

#for generating unique code
import string
import random
def generate_unique_game_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Game.objects.filter(game_code=code).count() == 0:
            break
    return code
def generate_unique_player_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Player.objects.filter(p_code=code).count() == 0:
            break
    return code    


# Create your models here.
class Game(models.Model):
    game_code = models.CharField(max_length=8, default=generate_unique_game_code ) #, unique=True)
    started = models.BooleanField(default = False)
    round_no = models.IntegerField(default = 0)
    p = models.CharField(max_length=8 , null = True) #, unique=True)
    word = models.CharField(max_length=100 , null = True ,default="0") #, unique=True)
    

    def __str__(self):
        return self.game_code

class Player(models.Model):
    p_code = models.CharField(max_length=8, default=generate_unique_player_code ) #, unique=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE , default = None ,null = True) 
    score = models.IntegerField(default = 0)
    

    def __str__(self):
        return self.p_code
