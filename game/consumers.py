# # chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer,WebsocketConsumer
from .models import Game,Player
from django.shortcuts import get_object_or_404

import random
words = ['bridge', 'crack', 'lemon', 'fork', 'mouth', 'bathroom', 'float', 'candy', 'chicken', 'coat', 'motorcycle', 'helicopter', 
'eye', 'light', 'owl', 'egg', 'popsicle', 'dinosaur', 'zebra', 'bracelet', 'hamburger', 'spider', 'alligator', 'branch', 'pie',
 'night', 'door', 'grass', 'jacket', 'nail', 'hat', 'shirt', 'suitcase', 'hook', 'fly', 'milk', 'ladybug', 'bear', 'face', 'curl', 
'balloon', 'cube', 'chair', 'horse', 'turtle', 'duck', 'beach', 'pen', 'beak', 'shoe', 'neck', 'bus', 'wheel', 'love', 'dog', 'giraffe',
 'Mickey Mouse', 'socks', 'cow', 'apple', 'ghost', 'tail', 'fish', 'octopus', 'moon', 'triangle', 'airplane', 'bird', 
'fire', 'heart', 'nail', 'cat', 'rock', 'key', 'girl', 'tree', 'caterpillar', 'monster', 'doll', 'zigzag', 'mountains',
 'bench', 'kite', 'whale', 'lion', 'chicken', 'ants', 'jail', 'bumblebee', 'sheep', 'kitten', 'angel', 'plant', 
 'ice cream cone', 'arm', 'dream', 'love', 'river', 'bat', 'snail', 'head', 'cherry', 'boat', 'leaf', 'legs', 'rocket',
  'train', 'pillow', 'flag', 'bed', 'swimming pool', 'inchworm', 'spider web', 'bunk bed', 'island', 'grass', 'bird', 'heart', 'bread',
   'camera', 'worm', 'cloud', 'kite', 'starfish', 'person', 'star', 'ladybug', 'boy', 'face', 'square', 'house', 'orange', 'car', 
   'spoon', 'carrot', 'stairs', 'water', 'duck', 'cookie', 'sunglasses', 'clock', 'snowman', 'alive', 'arm', 'music', 'sun', 'river', 
   'bat', 'bunny', 'socks', 'daisy', 'man', 'nose', 'frog', 'lips', 'fish', 'crab', 'mountain', 'lollipop', 'jellyfish', 'king', 'connect', 
   'silverware', 'jar', 'lake', 'fishing pole', 'circus', 'dragon', 'firefighter', 'platypus', 'corner', 'sack', 'zookeeper', 'crown',
    'noon', 'shape', 'sprinkler', 'pajamas', 'black hole', 'lightsaber', 'unicorn', 'step', 'garage', 'eraser', 'shake', 'seashell', 'whisk',
     'gum', 'gingerbread man', 'lucky', 'safety goggles', 'swim', 'cocoon', 'kiss', 'juice', 'stapler', 'puddle', 'ceiling fan', 'reindeer',
      'cricket', 'pineapple', 'carpet', 'pilot', 'garden', 'collar', 'blueprint', 'hug', 'saw', 'front porch', 'church', 'peck']
      

class game_Waiting(WebsocketConsumer):
    def connect(self):
        p_name = self.scope['url_route']['kwargs']['p_name']

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

        #start if 2 players have joined!
        code = self.scope['url_route']['kwargs']['room_name']
        game = get_object_or_404(Game,game_code = code)
        ps = Player.objects.filter(game = game)
        
        
        if(len(ps) > 1):
            game.started = True
            game.save()
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': "start"
                }
            )


    def disconnect(self, close_code):
        # Leave room group

        p_name = self.scope['url_route']['kwargs']['p_name']
        room_name = self.scope['url_route']['kwargs']['room_name']
        
        game = get_object_or_404(Game , game_code = room_name)
        print(game)

        if(not game.started): #do this only if game hasnot begin

            # p = Player.objects.filter(p_code = p_name).delete()#delete player on disconnect

            # p = Player.objects.filter(game = game)
            # if(len(p) < 1):
            game.delete() #delete game when no one is there        
        

        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        
        
        

    # Receive message from WebSocket
    # def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['message']


    #     # Send message to room group
    #     async_to_sync(self.channel_layer.group_send)(
    #         self.room_group_name,
    #         {
    #             'type': 'chat_message',
    #             'message': message
    #         }
    #     )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))




class Game_On(WebsocketConsumer):
    def connect(self):
        self.p_name = self.scope['url_route']['kwargs']['p_name']

        self.game_name = self.scope['url_route']['kwargs']['room_name']
        self.game_group_name = 'GameOn_%s' % self.game_name    

        #adding players to group
        async_to_sync(self.channel_layer.group_add)(
            self.game_group_name,
            self.channel_name
        )

        game_name = self.game_name 
        
        try:#if any player is dissconnect game will be deleted hence using try
            game = get_object_or_404(Game , game_code = game_name)
            p1 = Player.objects.filter(game = game)[0] #taking any player

            game.p = p1.p_code #this player has 1st chance to draw and doesnot particularly the player accessing this consumer

            if(game.word == "0"):#if another player already accesed the consumer game.word is already setup
                game.word = random.choice(words)
            game.save()

            message = "Round : 1" 
            
            self.accept()

            self.send(text_data=json.dumps({
                'message': message,
                'player' : game.p,
                'word' : game.word ,
                'settimer' : "True", # message to start timer
                'image' : ""

            }))            
        except:    
            self.close()

    def receive(self, text_data):#receive message from html by self user
        try:#incase a player is disconnected game will be deleted
            text_data_json = json.loads(text_data)
            message = text_data_json['message'] #get the message form from frontend
            timeup = text_data_json['timeup'] #check if message is send automatically(if timesup) or not
            image = text_data_json['image'] #the drawing

            game = get_object_or_404(Game , game_code = self.game_name)

            settimer = "False" #True only if round changes

            p = self.scope['url_route']['kwargs']['p_name'] #player which send the message

            p1 = Player.objects.filter(p_code = p ,game = game)
            p2 = Player.objects.filter(game = game)
            p2 = p2 | p1
            p2 = p2.difference(p1) #getting opponent of player who sent message

            p1 = p1[0] #player object who sent message
            p2 = p2[0] #opponent of player object who sent message

            if(message == game.word and p != game.p ): #if guessed message is right and player who sent is not one who had to draw
                
                game.round_no = game.round_no + 1 #update round
                game.p = p #switch player who has to draw
                game.word = random.choice(words)#change word
                game.save()
                settimer = "True"
                image = ""
  
                if(game.round_no%2 == 0): #if both player has drawn one one time show total round 
                    message = "Round : " + str((game.round_no/2) + 1)

                #updating player score    
                if(timeup=="False"):#if time was not up
                    p1.score = p1.score + 2
                    p2.score = p2.score + 1
                else:
                    p2.score = p2.score + 1
                p1.save()
                p2.save()

                
            if(game.round_no > 5):#endGame and decide the winner
                settimer = "endGame"
                if(p1.score > p2.score):
                    game.p = p1.p_code 
                elif(p2.score > p1.score):
                    game.p = p2.p_code 
                else:
                    game.p = ''
                game.started = False
                game.save()    

            async_to_sync(self.channel_layer.group_send)(#from self user to all users in the group
                self.game_group_name,
                {
                    'type': 'game_message',
                    'message': message ,
                    'word':  game.word,
                    'player' : game.p ,
                    'settimer' : settimer,
                    'image' : image
                }
            )
        except:
            self.close();    

    def disconnect(self, close_code):
        # game_name = self.game_name 
        game = Game.objects.filter(game_code = self.game_name)[0]
        if(game.started):
            game.delete()

        async_to_sync(self.channel_layer.group_discard)(
            self.game_group_name,
            self.channel_name
        )
        
  
    
    def game_message(self, event):#used to send messsage to group
            message = event['message']
            player = event['player']
            word = event['word']
            settimer = event['settimer']
            image = event['image']

            self.send(text_data=json.dumps({
                'message': message,
                'player' : player,
                'word' : word,
                'settimer' : settimer,
                'image' : image
            }))