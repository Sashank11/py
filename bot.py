import discord

import os

4 from time import sleep

6 TOKEN = 'OTA3MTKOODI1MTgxMzc2NTYy.YYjpBQ.sB3PtxSqanndZSwo50nSR3uNxU4

8 client discord.Client()

9 10 @client.event

11 async def on_ready():

12 print("We have logged in as .format(client.user))

13

14 @client.event

15 async def on_message(message):

16 if message.author == client.user:

17 18

19

return

if message.content.startswith('$SCAN'):

20 print("ok-----")

21 with open(/var/log/snort/alert","r") as file:

22

23

24

a = file.read()

file.close()

awatt message.channel.send(a[len(a)-1780:]+\n THE SYSTEM IS ACTING RESPECTIVELY ON THESE PACKETS BASED ON THE RULES THAT WERE DEFINED BEFORE..\n\n SUBMITTED TO: Prof. Chandra Mohan B. \n SUBMITTED BY: Mickey kumar Rouniyar, Prason Poudel

and Sashank Rijal.")

25 26

if message.content.startswith("SRESP): 27 awatt message.channel.send("Diagnosting system and analyzing the attack for proper action.") 28 #take_action()

29