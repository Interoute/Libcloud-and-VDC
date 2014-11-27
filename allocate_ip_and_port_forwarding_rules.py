#Import of the connection driver
import connection as vdc
#Import of the node creation script
import create_node as nodeCreator

#Assigning the connection driver
driver = vdc.getConn()

#Allocation of the public ip of the node
node = nodeCreator.getNode()[0]
nic = driver.ex_list_nics(node)[0]
zone_id = [net for net in driver.ex_list_networks() if nic.network_id in net.id][0].zoneid
location = [location for location in driver.list_locations() if zone_id in location.id][0]
ip = driver.ex_allocate_public_ip(network_id=nic.network_id, location=location)

#Creation of the port forwarding rules
print 'Creating port forwarding rules for node: ' + node.name
SSH_rule = driver.ex_create_port_forwarding_rule(address=ip, private_port=22,public_port=22, protocol= 'TCP', node=node)
HTTP_rule = driver.ex_create_port_forwarding_rule(address=ip, private_port=80,public_port=80, protocol= 'TCP', node=node)
print 'You can access the created node via SSH at: ' + str(node.public_ips[0])
