# CODE GOAL:
# Obtain the location of a particular device in a cluster of wifi networks
#
# Alvaro Gomez Inesta - Junction hackathon, Nov 25 2018
#
# See also:
# https://github.com/meraki/dashboard-api-python/blob/master/meraki.py

from meraki import meraki
import json as pyjson

########################
# Inputs
########################
# Name of the device we want to track
client_name = 'Hollyhelen.local' # This is an example


########################
# Get the network ID
########################
apikey = "0d79271f7401f39b20630d7de9ad999c594cb403"
myOrgs = meraki.myorgaccess(apikey)
print(myOrgs)
orgid = myOrgs[0]['id']

print('##### Analizing networks...')
myNetworks = meraki.getnetworklist(apikey, orgid)
#networkid = myNetworks['id']
# WE DO NOT HAVE PERMISSION TO GET THE INFO FROM NETWORKLIST, BUT WE CAN
#USE THE NETWORK ID THEY GAVE US (IN A REAL CASE, THE CODE ABOVE IS CORRECT):
networkid = 'N_658651445502946234'


########################
# Get the info from all clients
########################
# Get the serial number of the wifi point (device)
# (there were three Cisco wifi points in the venue of the hackathon)
devices = meraki.getnetworkdevices(apikey,networkid)
serialnum = devices[1]['serial'] # Cisco stand MR53

# Get the info from all clients
print('##### Requesting clients data...')
clients = meraki.getclients(apikey, serialnum)


########################
# Find our client MAC address
########################
for i in range(len(clients)):
    name = clients[i]['mdnsName']
    #print(name)
    if name == client_name:
        identifier = clients[i]['id']

# We choose a client by its identifier, e.g. Juulia's iPhone
print('##### Extracting',client_name,'mac address...')
client = meraki.getclient(apikey, networkid, identifier) #, suppressprint=False)
client_mac = client['mac']


########################
# Find our client location
########################
# Dictionary with all the data from clients
print('##### Reading present info received from server...')
clients_dict = pyjson.loads(open("clients_info.out").read())

for i in range(len(clients_dict['data']['observations'])):
    client_i = clients_dict['data']['observations'][i]
    if client_i['clientMac'] == client_mac:
        client_loc = [client_i['location']['lat'],client_i['location']['lng']]# Latitude and longitude of the client

client_loc_dict = {'client_name': client_name, 'lat': client_loc[0], 'lng': client_loc[1]}

########################
# Save client location to .out file
########################
print('##### Save location of ',client_name,'as <client_name_loc.out file')
file = open((client_name+"_loc.out"), "w")
file.write(pyjson.dumps(client_loc_dict))
file.close()
