#Task: Creating a VM on Interoute's VDC 2.0
#
#With this program the user chooses from lists of resources to put together the configuration to create a VM

import pprint
import inputchooser

#Import the connection driver
import connection as vdc

from libcloud.compute.base import NodeAuthPassword

#Choose the location (equals the VDC zone)
#[Note: is it possible to pass parameter available=true ?]

locations = vdc.getConn().list_locations()

location_ids= [l.id for l in locations]

location_names = [l.name for l in locations]

choice = -1
              
while choice == -1:
    choice = inputchooser.choose_item_from_list(
            location_names,
            prompt='Select your zone:'
             )
    if choice == -1:
            print()
            print('Please select a zone.')

location_num = choice
location_id = location_ids[location_num]

print('Selected location (zone): %s (id: %s)' % (location_names[location_num],location_id))


#Choose the image (equals the template in VDC)

images = vdc.getConn().list_images(locations[location_num]) 
image_ids= [l.id for l in images]
image_names = [l.name for l in images]

choice = -1
              
while choice == -1:
    choice = inputchooser.choose_item_from_list(
            image_names,
            prompt='Select your image (template): '
             )
    if choice == -1:
            print()
            print('Please select an image.')

image_num = choice
image_id = image_ids[choice]

print('Selected image: %s (id: %s)' % (image_names[choice], image_id))

#Enter the VM name
vm_name = raw_input('Please enter the name for the VM (you can use letters, digits and hyphens - do not use space or underscore): ')


#Choose the size (equals the service offering in VDC)

sizes = vdc.getConn().list_sizes(locations[location_num])
cpu_list = range(1,13)
ram_list = [512,1024,2048,4096,6144,8192,16384,24576,32768,65536,131072]

choice_ram = -1
              
while choice_ram == -1:
    choice_ram = inputchooser.choose_item_from_list(
            map(lambda x: float(x)/1024, ram_list),
            prompt='Select your RAM size (GBytes):'
             )
    if choice_ram == -1:
            print()
            print('Please select a RAM size.')

choice_cpu = -1
              
while True:
    choice_cpu = raw_input('Please type in the number of CPUs (a number between 1 and 12):')

    choice_cpu = int(float(choice_cpu))
    
    if 1 <= choice_cpu <= 12:  
         break;

#image_id = location_ids[choice-1]

vm_size = [sz for sz in sizes if sz.name == '%d-%d'% (ram_list[choice_ram],choice_cpu)][0]

print('Selected CPU and RAM size: %s-%s (id: %s)'  % (ram_list[choice_ram], choice_cpu, sz.id))

#VDC will always attach a new VM to a network if 1 network exists in the zone; if more than one network, user must choose 
#(can be multiple networks, but here only single choice)
networks1 = vdc.getConn().ex_list_networks()
#Select only networks in the location (zone) selected
networks = [netw for netw in networks1 if netw.zoneid == location_id]
if len(networks)>1:
    choice = -1
    while choice == -1:
       choice = inputchooser.choose_item_from_list(
                [netw.name for netw in networks],
                prompt='Select your network: '
             )
       if choice == -1:
            print()
            print('Please select a network.')
    networksparam = [networks[choice]]
    print('Selected network: %s (id: %s)'  % (networksparam[0].name, networksparam[0].id))

#Ready to create the node
try: 
    print("Creating node (may take some time)...")
    if len(networks)>1:
        ##print("creating with networkparam")
        node = vdc.getConn().create_node(name=vm_name, image=images[image_num], size=vm_size, location=locations[location_num], networks = networksparam)
    else:
        ##print("creating")
        node = vdc.getConn().create_node(name=vm_name, image=images[image_num], size=vm_size, location=locations[location_num])
    pprint.pprint('NODE CREATED: %s' % node)
    print('Password: ' + node.extra['password'])
except:
    print("ERROR IN create_node. Traceback:")
    raise


