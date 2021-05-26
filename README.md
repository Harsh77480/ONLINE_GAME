# ONLINE_GAME
A Realtime White-Board Game made using WEBSOCKTS<br>
<h3 >
 Technologies used - 
 </h3>
 <h3 >
  Redis, Django channels, Javascript, HTML, CSS
 </h3>
  
 # HOW IT WORKS :
 
 <h5>-> I have used Combination of http and Websocket request i.e. 
 both sync and acsync python Code for this project </h5>
 <h5>-> For Rendering Drawing Canvas's  Base64Image is Used </h5>
  
# Pairing up the Players :
 From simple django view player creates a "GAME" Model and random six word code is generated<br>
 which works as "GROUP" for different "CHANNELS" that are connected with redis.<br>
 This Way To Two Players are Connected with Same Websocket through Redis!<br>
 
![alt text](Animations/Join-min.gif "Logo Title Text 1")

# ,

 # Automatically changing Turns if Time is up : 
Frontend Js is Responsible for Sending Websocket all the Messages <br>
including Correct One if TimesUp ,<br>
"Game_ON" Websocket Consumer Changes "Game" model acc. to Each Message.<br>

![alt text](Animations/turns.gif "Logo Title Text 1")

# ,

# Restricting Players if Game is Started :
No of Players is Limited To 2 ,<br>
Django "Game" Model Will Not allow another "Player" Model,<br>

![alt text](Animations/Restrict.gif "Logo Title Text 1")
 



 

