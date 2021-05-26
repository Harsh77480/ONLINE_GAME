# ONLINE_GAME
A Realtime White-Board Game made using WEBSOCKTS<br>
<h3 >
 Technologies used - 
 </h3>
 <br>
 <h3 >
  Redis, Django channels, Javascript, HTML, CSS 
 </h3>
  
 # HOW IT WORKS 
 
 
 
 <h4>-> I have used Combination of http and Websocket request i.e.</h4>
 <h4> both sync and acsync python Code for this project </h4>
 <h4>-> For Rendering Drawing Canvas's  Base64Image is Used </h4>
  
# Pairing up the Players :
form simple django view player creates a "GAME" Model and random six word code is generated
which works as "GROUP" for different "CHANNELS" that are connected through redis.
This Way To Two Players are Connected with Same Websocket through Redis!
![alt text](Animations/Join-min.gif "Logo Title Text 1")

# ,

 # Automatically changing Turns if Timesup : 
<!--  If Timer is up Js Sends Request With websocket  -->
Frontend Js is Responsible for Sending Websocket all the Messages 
including Correct One if TimesUp ,
"Game_ON" Websocket Consumer Changes "Game" model acc. to Each Message.

![alt text](Animations/turns.gif "Logo Title Text 1")

# ,

# Restricting Players if Rooms if Game is Started :
No of Players is Limited To 2 ,
Django "Game" Model Will Not allow another "Player" Model,
![alt text](Animations/Restrict.gif "Logo Title Text 1")
 


  

 

