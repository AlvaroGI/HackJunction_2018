# FinGO
Software developed for the Junction Hackathon (Helsinki, Nov 23-25, 2018) by Álvaro Gómez Iñesta and Víctor Gómez Iñesta.

# In a nutshell
Ever had trouble to take your small children shopping? Ever wanted to stay playing at home when your parents wanted to take you shopping as a child? Children and parents are OPPOSITES. Our goal is to BRING THE OPPOSITES CLOSE.

# How it works (user POV)
Before going shopping, parents can specify in FinGO the items they plan to buy, or shops they are interested in. When arriving to the mall, their smartphone will be linked to their children's. Then, an arrow will show a path to the children to find minigames. This arrow will thake the family to one of the items/shops given previously. After that, a cooperative AR-based minigame will pop up in both smartphones. Parent and child will have to work together to solve the puzzle in order to advance to the next item/shop.

Elevators and escalators will also provide a minigame. In this case, it is not AR-based but a trivia question related to the products they will buy or shops they will visit. 

The path that the family will follow is pre-established, and that allows to generate compatible paths between all the users in order to prevent jams, which are quite common in peak hours. 

# GOals
  -Strengthen parental bonds by building a bridge between two commonly OPPOSITE and conflictive activities: shopping and playing.
  -Educate on healthy lifestyle and responsible consumption with the trivia questions.
  -Predict people flows and direct them to prevent jams.

# How it works (developer POV)
We employ the Cisco Meraki software to analyze the data of the wifi devices in the shopping center.
Using Python, we extract the exact location of the family smartphones.
Then, we use that as input for our Unity code. We have developed an AR game that guides the families through the mall. When their location corresponds to a pre-specified item/shop, a minigame appears. These minigames have been built using Unity and Vuforia, to create 3D AR interactive structures.

# Software required
  -Python 3

  -Flask
  
  -Cisco Meraki for Python (https://github.com/meraki/dashboard-api-python.git)
  
  -Cisco Meraki CMX receiver based on Python with Flask (https://github.com/dexterlabora/cmxreceiver-python.git)

  -Unity
  
# Python code
First, clone this repo: https://github.com/dexterlabora/cmxreceiver-python.git. Then, update cmxreceiver.py by our modified version. Place our database_to_client.py in the same folder. Then, inside this file, substitute the variable 'client_name' by the name of the device you want to track.

To get the location of the user, do the following. First, execute:
```
python3 cmxreceiver.py -v <validator> -s <secret>
```
In parallel (another terminal window), execute
```
ssh -R findshop.serveo.net:80:localhost:8555 serveo.net
```
to get the info from all clients every second. Then, use
```
python3 database_to_client.py
```
to generate a client_name_loc.out file with the latitude and longitude of the user.

*note: some information (related to wifi devices, e.g. validator and secret) used in the project demo must be kept private and therefore there are some holes to fill in the code we post here. See Cisco Meraki Documentation for more info.

# Unity code
Unity code can be found at https://drive.google.com/drive/folders/1ZIoYW84mXPkD0A-mhzIQyVF1Jcq6q0MV?usp=sharing.
