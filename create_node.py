#Import of the connection driver
import connection as vdc
from libcloud.compute.base import NodeAuthPassword
import random


#Task: Creating a VM on Interoute's VDC 2.0
#Setting the configuration details for the VM to be created
image = [image for image in vdc.getConn().list_images() if 'IRT-CENTOS-6.5' in image.name][0]
size = [size for size in vdc.getConn().list_sizes() if size.name == '6144-2'][0]
net = [network for network in vdc.getConn().ex_list_networks() if 'London' in network.name]
location = [location for location in vdc.getConn().list_locations() if 'London' in location.name][0]
name = 'Interoute-Node' + str(random.randint(0, 100))

#Creating the VM - Equivalent libcloud command: create_node
print 'Creating node: ' + name
if len(net) == 0 :
  node = [vdc.getConn().create_node(name=name, image=image, size=size, location=location)]
else:
  node = [vdc.getConn().create_node(name=name, image=image, size=size, location=location, networks=[net[0]])]
print 'Created node: ' + name
print 'Password: ' + node[0].extra['password']

#Method getNode
#Returns the node
def getNode():
        return node[0]
