
#1. Introduction

This repository contains sample scripts which illustrate how [Apache Libcloud](http://libcloud.apache.org/) can be used to perform basic operations on [Interoute's Virtual Data Centre](http://cloudstore.interoute.com/main/WhatInterouteVDC) cloud platform. For example, creating virtual machines ('nodes' in Libcloud terminology) and networks, assigning a public IP address to a virtual machine, applying port forwarding rules, and bootstrapping (running some initial commands to install software and configure the machine) a newly-deployed virtual machine.

The [CLOUDSTACK driver](https://libcloud.readthedocs.org/en/latest/compute/drivers/cloudstack.html) for Libcloud is used, which is compatible with the [Virtual Data Centre API](http://cloudstore.interoute.com/main/knowledge-centre/library/vdc-api-introduction-api).

#2. Prerequisites

Python 2.5 or later should be installed.

You should install the Python installer program, pip. ([Install pip](https://pip.pypa.io/en/latest/installing.html))

#3. Installation

Type in the terminal/command prompt:

`pip install apache-libcloud` 

#4. Running the Libcloud scripts

First, you should edit the connection.py file to insert the API key, Secret key and access URL for your VDC account. ([Instructions for finding VDC access keys](http://cloudstore.interoute.com/main/knowledge-centre/library/vdc-api-introduction-api#d56e140))

Then, you can run the libcloud scripts by typing in a terminal / command prompt: 

`python <filename>.py` 

#5. Supported Libcloud commands

The table below shows the list of Libcloud commands, as contained in the CLOUDSTACK driver, which are supported by the VDC 2.0 API. Any Libcloud commands that are not in this list, are not supported for VDC 2.0.


| Libcloud Command                | VDC 2.0 API Command                                                                                                                            |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| list_images                     | [listTemplates](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listTemplates)                                |
| list_volumes                    | [listVolumes](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listVolumes)                                    |
| list_snapshots                  | [listSnapshots](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listSnapshots)                                |
| list_sizes                      | [listServiceOfferings](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listServiceOfferings)                  |
| list_nodes                      | [listVirtualMachines](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listVirtualMachines)                    |        
| list_locations                  | [listZones](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listZones)                                        |
| list_key_pairs                  | [listSSHKeyPairs](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listSSHKeyPairs)                            |
| import_key_pair_from_string     | [registerSSHKeyPair](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/registerSSHKeyPair)                      |
| get_image                       | No Equivalent VDC command                                                                                                                      |
| ex_start                        | [startVirtualMachine](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/startVirtualMachine)                    |
| ex_stop                         | [stopVirtualMachine](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/stopVirtualMachine)                      |        
| ex_reboot                       | [rebootVirtualMachine](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/rebootVirtualMachine)                  | 
| ex_release_public_ip            | [disassociateIpAddress](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/disassociateIpAddress)                |
| ex_register_iso                 | [registerIso](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/registerIso)                                    |
| ex_list_public_ips              | [listPublicIpAddresses](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listPublicIpAddresses)                |
| ex_list_port_forwarding_rules   | [listPortForwardingRules](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listPortForwardingRules)            |
| ex_list_os_types                | [listOsTypes](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listOsTypes)                                    |
| ex_list_nics                    | [listNics](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listNics)                                          |
| ex_list_networks                | [listNetworks](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listNetworks)                                  |
| ex_list_network_offerings       | [listNetworkOfferings](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listNetworkOfferings)                  |
| ex_list_keypairs                | [listSSHKeyPairs](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listSSHKeyPairs)                            |
| ex_list_firewall_rules          | [listFirewallRules](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listFirewallRules)                        |
| ex_list_egress_firewall_rules   | [listEgressFirewallRules](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listEgressFirewallRules)            |
| ex_list_disk_offerings          | [listDiskOfferings](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listDiskOfferings)                        |
| ex_limits                       | [listResourceLimits](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listResourceLimits)                      |
| ex_import_keypair_from_string   | [registerSSHKeyPair](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/registerSSHKeyPair)                      |        
| ex_detach_nic_from_node         | [removeNicFromVirtualMachine](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/removeNicFromVirtualMachine)    |
| ex_delete_tags                  | [deleteTags](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteTags)                                      |
| ex_delete_port_forwarding_rule  | [deletePortForwardingRule](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deletePortForwardingRule)          |
| ex_delete_network               | [deleteNetwork](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteNetwork)                                |
| ex_delete_keypair               | [deleteSSHKeyPair](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteSSHKeyPair)                          |
| ex_delete_ip_forwarding_rule    | [deleteIpForwardingRule](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteIpForwardingRule)              |
| ex_delete_firewall_rule         | [deleteFirewallRule](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteFirewallRule)                      |        
| ex_delete_egress_firewall_rule  | [deleteEgressFirewallRule](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteEgressFirewallRule)          |
| ex_create_tags                  | [createTags](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createTags)                                      |
| ex_create_snapshot_template     | [createSnapshot](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createSnapshot)                	           |
| ex_create_port_forwarding_rule  | [createPortForwardingRule](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createPortForwardingRule)          |
| ex_create_network               | [createNetwork](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createNetwork)                                |
| ex_create_keypair               | [createSSHKeyPair](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createSSHKeyPair)                          |
| ex_create_ip_forwarding_rule    | [createIpForwardingRule](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createIpForwardingRule)              |
| ex_create_firewall_rule         | [createFirewallRule](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createFirewallRule)                      |        
| ex_create_egress_firewall_rule  | [createEgressFirewallRule](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createEgressFirewallRule)          |
| ex_attach_nic_to_node           | [addNicToVirtualMachine](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/addNicToVirtualMachine)              |
| ex_allocate_public_ip           | [associateIpAddress](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/associateIpAddress)                      |        
| detach_volume                   | [detachVolume](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/detachVolume)                                  |
| destroy_volume_snapshot         | [deleteSnapshot](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteSnapshot)                              |
| destroy_volume                  | [deleteVolume](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteVolume)                                  |
| destroy_node                    | [destroyVirtualMachine](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/destroyVirtualMachine)                |
| delete_key_pair                 | [deleteSSHKeyPair](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteSSHKeyPair)                          |
| delete_image                    | [deleteTemplate](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteTemplate)                              |
| create_volume_snapshot          | [createSnapshot](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createSnapshot)                              |
| create_volume                   | [createVolume](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createVolume)                                  |
| create_node                     | [deployVirtualMachine](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deployVirtualMachine)                  |
| create_key_pair                 | [createSSHKeyPair](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createSSHKeyPair)                          |
| create_image                    | [createTemplate](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createTemplate)                              |
| copy_image                      | [copyTemplate](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/copyTemplate)                                  |
| attach_volume                   | [attachVolume](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/attachVolume)                                  |
| balancer_attach_member          | [assignToLoadBalancerRule](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/assignToLoadBalancerRule)          |
| balancer_detach_member          | [removeFromLoadBalancerRule](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/removeFromLoadBalancerRule)      |
| balancer_list_members           | [listLoadBalancerRuleInstances](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listLoadBalancerRuleInstances)|
| create_balancer                 | [createLoadBalancer](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createLoadBalancer)                      |        
| destroy_balancer                | [deleteLoadBalancer](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteLoadBalancer)                      |        
| get_balancer                    | No Equivalent VDC command                                                                                                                      |
| list_balancers                  | [listLoadBalancerRules](http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listLoadBalancerRules)                |
| list_protocols                  | No Equivalent VDC command                                                                                                                      |
