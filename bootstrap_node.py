#Import of the required classes/packages
import connection as vdc
import os
from libcloud.compute.deployment import ScriptDeployment
import allocate_ip_and_port_forwarding_rules as nodeCreator


#Assigning the connection driver
driver = vdc.getConn()

#Assigning the node to bootstrap on it
node = nodeCreator.nodeCreator.getNode()

#Defining the shell script which installs chef on a unix-based system
BOOTSTRAP_SCRIPT = ''' #!/usr/bin/env bash
curl -L https://www.opscode.com/chef/install.sh | sudo bash
'''
script = ScriptDeployment(script=BOOTSTRAP_SCRIPT)

#Run the shell script on the node
print 'Running shell script on node: ' + node.name
driver._connect_and_run_deployment_script(node=node,task=script,  ssh_hostname=node.public_ips[0], ssh_port=22,ssh_username='root', ssh_password=node.extra['password'], ssh_key_file=None, ssh_timeout=10, timeout=600, max_tries=3 )
print script.stdout
