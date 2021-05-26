# ONLINE_GAME
A Realtime White-Board Game made using WEBSOCKTS<br>
<h3 >
 Technologies used - 
 </h3>
 <br>
 <h3 >
  '''
 - Redis, Django channels, Javascript, HTML, CSS
 '''
 </h3>
  
 # HOW IT WORKS :
 
 <h5>-> I have used Combination of http and Websocket request i.e. 
 both sync and acsync python Code for this project </h5>
 <h5>-> For Rendering Drawing Canvas's  Base64Image is Used </h5>
  
# Pairing up the Players :
<p> From simple django view player creates a "GAME" Model and random six word code is generated<p><br>
<p> which works as "GROUP" for different "CHANNELS" that are connected with redis.<p><br>
<p> This Way To Two Players are Connected with Same Websocket through Redis!<p><br>
 
![alt text](Animations/Join-min.gif "Logo Title Text 1")

# ,

 # Automatically changing Turns if Time is up : 
<p>Frontend Js is Responsible for Sending Websocket all the Messages <p><br>
<p>including Correct One if TimesUp ,<p><br>
<p>"Game_ON" Websocket Consumer Changes "Game" model acc. to Each Message.<p><br>

![alt text](Animations/turns.gif "Logo Title Text 1")

# ,

# Restricting Players if Game is Started :
<p>No of Players is Limited To 2 ,<p><br>
<p>Django "Game" Model Will Not allow another "Player" Model,<p><br>

![alt text](Animations/Restrict.gif "Logo Title Text 1")
 



 

