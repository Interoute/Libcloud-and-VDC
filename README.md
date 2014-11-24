
#1. Quick Overview
This repository stores different sample scripts which illustrate how libcloud can be used to perform different operations on Interoute's cloud platform (VDC 2.0). For example: Creating Virtual Machines, Networks, Storage, Templates, Firewall rules, etc...

#2. Prerequisites:
* Python 2.5+ should be installed
* You should install pip.

#3. Installation:
* Type in terminal / command prompt:
<br/>
`pip install apache-libcloud` 

#4. Running the libcloud scripts:
* You can run the libcloud scripts by typing in terminal / command prompt: <br/>
`python <filename>.py` 

#5. Supported Libcloud Commands:

<p>The table below shows the list of libcloud commands that are supported on VDC 2.0.</p>


<div id="Libcloud Commands_2055" align=center x:publishsource="Excel">

<table border=1 cellpadding=0 cellspacing=0 width=794 style='border-collapse:
 collapse;table-layout:fixed;width:595pt'>
 <col width=407 style='mso-width-source:userset;mso-width-alt:14884;width:305pt'>
 <col width=387 style='mso-width-source:userset;mso-width-alt:14153;width:290pt'>
 <tr height=20 style='mso-height-source:userset;height:15.0pt'>
  <td rowspan=4 height=80 class=xl682055 width=407 style='height:60.0pt;
  width:305pt'><b>Libcloud Commands</b></td>
  <td rowspan=4 class=xl682055 width=387 style='width:290pt'><b>VDC 2.0 API
  Commands</b></td>
 </tr>
 <tr height=20 style='mso-height-source:userset;height:15.0pt'>
 </tr>
 <tr height=20 style='mso-height-source:userset;height:15.0pt'>
 </tr>
 <tr height=20 style='mso-height-source:userset;height:15.0pt'>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>list_volumes</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listVolumes"><span
  style='color:blue'>listVolumes</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>list_volume_snapshots</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listVMSnapshot"><span
  style='color:blue'>listVMSnapshot</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>list_snapshots</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listSnapshots"><span
  style='color:blue'>listSnapshots</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>list_sizes</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listServiceOfferings"><span
  style='color:blue'>listServiceOfferings</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>list_nodes</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listVirtualMachines"><span
  style='color:blue'>listVirtualMachines</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>list_locations</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listZones"><span
  style='color:blue'>listZones</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>list_key_pairs</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listSSHKeyPairs"><span
  style='color:blue'>listSSHKeyPairs</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>import_key_pair_from_string</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/registerSSHKeyPair"><span
  style='color:blue'>registerSSHKeyPair</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>import_key_pair_from_file</td>
  <td class=xl6720307 style='border-top:none;border-left:none'>Not Supported</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>get_image</td>
  <td class=xl7120307 style='border-top:none;border-left:none'><span
  style='orphans: auto;text-align:start;widows: auto;-webkit-text-stroke-width: 0px'>Supported
  (No Equivalent VDC command)</span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_start</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/startVirtualMachine"><span
  style='color:blue'>startVirtualMachine</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_stop</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/stopVirtualMachine"><span
  style='color:blue'>stopVirtualMachine</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_reboot</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/rebootVirtualMachine"><span
  style='color:blue'>rebootVirtualMachine</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_revoke_security_group_ingress</td>
  <td class=xl6720307 style='border-top:none;border-left:none'>Not Supported</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_replace_network_acllist</td>
  <td class=xl6720307 style='border-top:none;border-left:none'>Not Supported</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_release_public_ip</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/disassociateIpAddress"><span
  style='color:blue'>disassociateIpAddress</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_register_iso</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/registerIso"><span
  style='color:blue'>registerIso</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_list_vpcs</td>
  <td class=xl6720307 style='border-top:none;border-left:none'>Not Supported</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_list_vpc_offerings</td>
  <td class=xl6720307 style='border-top:none;border-left:none'>Not Supported</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_list_security_groups</td>
  <td class=xl6720307 style='border-top:none;border-left:none'>Not Supported</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_list_routers</td>
  <td class=xl6720307 style='border-top:none;border-left:none'>Not Supported</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_list_public_ips</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listPublicIpAddresses"><span
  style='color:blue'>listPublicIpAddresses</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_list_projects</td>
  <td class=xl6720307 style='border-top:none;border-left:none'>Not Supported</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_list_port_forwarding_rules</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listPortForwardingRules"><span
  style='color:blue'>listPortForwardingRules</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_list_os_types</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listOsTypes"><span
  style='color:blue'>listOsTypes</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_list_nics</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listNics"><span
  style='color:blue'>listNics</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_list_networks</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listNetworks"><span
  style='color:blue'>listNetworks</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_list_network_offerings</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listNetworkOfferings"><span
  style='color:blue'>listNetworkOfferings</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_list_network_acllists</td>
  <td class=xl6720307 style='border-top:none;border-left:none'>Not Supported</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_list_network_acl</td>
  <td class=xl6720307 style='border-top:none;border-left:none'>Not Supported</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_list_keypairs</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listSSHKeyPairs"><span
  style='color:blue'>listSSHKeyPairs</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_list_firewall_rules</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listFirewallRules"><span
  style='color:blue'>listFirewallRules</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_list_egress_firewall_rules</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listEgressFirewallRules"><span
  style='color:blue'>listEgressFirewallRules</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_list_disk_offerings</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listDiskOfferings"><span
  style='color:blue'>listDiskOfferings</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_limits</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listResourceLimits"><span
  style='color:blue'>listResourceLimits</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_import_keypair_from_string</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/registerSSHKeyPair"><span
  style='color:blue'>registerSSHKeyPair</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_import_keypair</td>
  <td class=xl6720307 style='border-top:none;border-left:none'>Not Supported</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_detach_nic_from_node</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/removeNicFromVirtualMachine"><span
  style='color:blue'>removeNicFromVirtualMachine</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_delete_vpc</td>
  <td class=xl6720307 style='border-top:none;border-left:none'>Not Supported</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_delete_tags</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteTags"><span
  style='color:blue'>deleteTags</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_delete_security_group</td>
  <td class=xl6720307 style='border-top:none;border-left:none'>Not Supported</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_delete_port_forwarding_rule</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deletePortForwardingRule"><span
  style='color:blue'>deletePortForwardingRule</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_delete_network</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteNetwork"><span
  style='color:blue'>deleteNetwork</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_delete_keypair</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteSSHKeyPair"><span
  style='color:blue'>deleteSSHKeyPair</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_delete_ip_forwarding_rule</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteIpForwardingRule"><span
  style='color:blue'>deleteIpForwardingRule</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_delete_firewall_rule</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteFirewallRule"><span
  style='color:blue'>deleteFirewallRule</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_delete_egress_firewall_rule</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteEgressFirewallRule"><span
  style='color:blue'>deleteEgressFirewallRule</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_create_vpc</td>
  <td class=xl6720307 style='border-top:none;border-left:none'>Not Supported</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_create_tags</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createTags"><span
  style='color:blue'>createTags</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_create_snapshot_template</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createSnapshot"><span
  style='color:blue'>createSnapshot</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_create_security_group</td>
  <td class=xl6720307 style='border-top:none;border-left:none'>Not Supported</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_create_port_forwarding_rule</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createPortForwardingRule"><span
  style='color:blue'>createPortForwardingRule</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_create_network_acllist</td>
  <td class=xl6720307 style='border-top:none;border-left:none'>Not Supported</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_create_network_acl</td>
  <td class=xl6720307 style='border-top:none;border-left:none'>Not Supported</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_create_network</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createNetwork"><span
  style='color:blue'>createNetwork</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_create_keypair</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createSSHKeyPair"><span
  style='color:blue'>createSSHKeyPair</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_create_ip_forwarding_rule</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createIpForwardingRule"><span
  style='color:blue'>createIpForwardingRule</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_create_firewall_rule</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createFirewallRule"><span
  style='color:blue'>createFirewallRule</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_create_egress_firewall_rule</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createEgressFirewallRule"><span
  style='color:blue'>createEgressFirewallRule</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_authorize_security_group_ingress</td>
  <td class=xl6720307 style='border-top:none;border-left:none'>Not Supported</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_attach_nic_to_node</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/addNicToVirtualMachine"><span
  style='color:blue'>addNicToVirtualMachine&nbsp;</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>ex_allocate_public_ip</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/associateIpAddress"><span
  style='color:blue'>associateIpAddress</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>detach_volume</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/detachVolume"><span
  style='color:blue'>detachVolume&nbsp;</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>destroy_volume_snapshot</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteSnapshot"><span
  style='color:blue'>deleteSnapshot</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>destroy_volume</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteVolume"><span
  style='color:blue'>deleteVolume</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>destroy_node</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/destroyVirtualMachine"><span
  style='color:blue'>destroyVirtualMachine</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>deploy_node</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deployVirtualMachine"><span
  style='color:blue'>deployVirtualMachine</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>delete_key_pair</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteSSHKeyPair"><span
  style='color:blue'>deleteSSHKeyPair</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>delete_image</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteTemplate"><span
  style='color:blue'>deleteTemplate</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>create_volume_snapshot</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createSnapshot"><span
  style='color:blue'>createSnapshot</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>create_volume</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createVolume"><span
  style='color:blue'>createVolume</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>create_node</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deployVirtualMachine"><span
  style='color:blue'>deployVirtualMachine</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>create_key_pair</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createSSHKeyPair"><span
  style='color:blue'>createSSHKeyPair</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>create_image</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createTemplate"><span
  style='color:blue'>createTemplate</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>copy_image</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/copyTemplate"><span
  style='color:blue'>copyTemplate&nbsp;</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6520307 style='height:15.0pt;border-top:none'>attach_volume</td>
  <td class=xl6620307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/attachVolume"><span
  style='color:blue'>attachVolume</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl7020307 style='height:15.0pt;border-top:none'><span
  style='orphans: auto;text-align:start;widows: auto;-webkit-text-stroke-width: 0px'>balancer_attach_compute_node</td>
  </span>
  <td class=xl6720307 style='border-top:none;border-left:none'>Not Supported</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl7020307 style='height:15.0pt;border-top:none'><span
  style='orphans: auto;text-align:start;widows: auto;-webkit-text-stroke-width: 0px'>balancer_attach_member</span></td>
  <td class=xl7320307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/assignToLoadBalancerRule"
  style='outline: 0px;font-stretch: inherit;orphans: auto;text-align:start;
  widows: auto;-webkit-text-stroke-width: 0px'><span style='color:#00359E'>assignToLoadBalancerRule</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl7020307 style='height:15.0pt;border-top:none'><span
  style='orphans: auto;text-align:start;widows: auto;-webkit-text-stroke-width: 0px'>balancer_detach_member</span></td>
  <td class=xl7220307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/removeFromLoadBalancerRule"
  style='outline: 0px;font-stretch: inherit;orphans: auto;text-align:start;
  widows: auto;-webkit-text-stroke-width: 0px'>removeFromLoadBalancerRule</a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl7020307 style='height:15.0pt;border-top:none'><span
  style='orphans: auto;text-align:start;widows: auto;-webkit-text-stroke-width: 0px'>balancer_list_members</span></td>
  <td class=xl7220307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listLoadBalancerRuleInstances"
  style='outline: 0px;font-stretch: inherit;orphans: auto;text-align:start;
  widows: auto;-webkit-text-stroke-width: 0px'>listLoadBalancerRuleInstances</a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl7020307 style='height:15.0pt;border-top:none'><span
  style='orphans: auto;text-align:start;widows: auto;-webkit-text-stroke-width: 0px'>connectionCls</span></td>
  <td class=xl6720307 style='border-top:none;border-left:none'>Not Supported</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl7020307 style='height:15.0pt;border-top:none'><span
  style='orphans: auto;text-align:start;widows: auto;-webkit-text-stroke-width: 0px'>create_balancer</span></td>
  <td class=xl7220307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createLoadBalancer"
  style='outline: 0px;font-stretch: inherit;orphans: auto;text-align:start;
  widows: auto;-webkit-text-stroke-width: 0px'>createLoadBalancer</a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl7020307 style='height:15.0pt;border-top:none'><span
  style='orphans: auto;text-align:start;widows: auto;-webkit-text-stroke-width: 0px'>destroy_balancer</span></td>
  <td class=xl7220307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteLoadBalancer"
  style='outline: 0px;font-stretch: inherit;orphans: auto;text-align:start;
  widows: auto;-webkit-text-stroke-width: 0px'>deleteLoadBalancer</a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl7020307 style='height:15.0pt;border-top:none'><span
  style='orphans: auto;text-align:start;widows: auto;-webkit-text-stroke-width: 0px'>get_balancer</span></td>
  <td class=xl7120307 style='border-top:none;border-left:none'><span
  style='orphans: auto;text-align:start;widows: auto;-webkit-text-stroke-width: 0px'>Supported
  (No Equivalent VDC command)</span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl7020307 style='height:15.0pt;border-top:none'>list_balancers<font
  class="font520307">()</font></td>
  <td class=xl7220307 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listLoadBalancerRules"
  style='outline: 0px;font-stretch: inherit;orphans: auto;text-align:start;
  widows: auto;-webkit-text-stroke-width: 0px'>listLoadBalancerRules</a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl7020307 style='height:15.0pt;border-top:none'>list_protocols<font
  class="font520307">()</font></td>
  <td class=xl7120307 style='border-top:none;border-left:none'>Supported (No
  Equivalent VDC command)</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl7020307 style='height:15.0pt;border-top:none'>list_supported_algorithms<font
  class="font520307">()</font></td>
  <td class=xl6720307 style='border-top:none;border-left:none'>Not Supported</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl7020307 style='height:15.0pt;border-top:none'><span
  style='orphans: auto;text-align:start;widows: auto;-webkit-text-stroke-width: 0px'>update_balancer</span></td>
  <td class=xl6720307 style='border-top:none;border-left:none'>Not Supported</td>
 </tr>

</table>
</div>
