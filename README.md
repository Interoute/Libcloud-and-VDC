
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
* Firstly you should edit the connection.py file with your VDC API and secret key.<br/>
* Then, you can run the libcloud scripts by typing in terminal / command prompt: <br/>
`python <filename>.py` 

#5. Supported Libcloud Commands:

<p>The table below shows the list of libcloud commands that are supported on VDC 2.0. Any libcloud commands that are not in this list, are not supported by Interoute's VDC 2.0.</p>


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
  </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>list_images</td>
  <td class=xl6832583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listTemplates"
  target="_parent">listTemplates</a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>list_volumes</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listVolumes"
  target="_parent"><span style='color:blue'>listVolumes</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>list_volume_snapshots</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listVMSnapshot"
  target="_parent"><span style='color:blue'>listVMSnapshot</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>list_snapshots</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listSnapshots"
  target="_parent"><span style='color:blue'>listSnapshots</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>list_sizes</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listServiceOfferings"
  target="_parent"><span style='color:blue'>listServiceOfferings</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>list_nodes</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listVirtualMachines"
  target="_parent"><span style='color:blue'>listVirtualMachines</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>list_locations</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listZones"
  target="_parent"><span style='color:blue'>listZones</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>list_key_pairs</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listSSHKeyPairs"
  target="_parent"><span style='color:blue'>listSSHKeyPairs</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>import_key_pair_from_string</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/registerSSHKeyPair"
  target="_parent"><span style='color:blue'>registerSSHKeyPair</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>get_image</td>
  <td class=xl7032583 style='border-top:none;border-left:none'>No Equivalent
  VDC command</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_start</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/startVirtualMachine"
  target="_parent"><span style='color:blue'>startVirtualMachine</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_stop</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/stopVirtualMachine"
  target="_parent"><span style='color:blue'>stopVirtualMachine</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_reboot</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/rebootVirtualMachine"
  target="_parent"><span style='color:blue'>rebootVirtualMachine</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_release_public_ip</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/disassociateIpAddress"
  target="_parent"><span style='color:blue'>disassociateIpAddress</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_register_iso</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/registerIso"
  target="_parent"><span style='color:blue'>registerIso</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_list_public_ips</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listPublicIpAddresses"
  target="_parent"><span style='color:blue'>listPublicIpAddresses</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_list_port_forwarding_rules</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listPortForwardingRules"
  target="_parent"><span style='color:blue'>listPortForwardingRules</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_list_os_types</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listOsTypes"
  target="_parent"><span style='color:blue'>listOsTypes</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_list_nics</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listNics"
  target="_parent"><span style='color:blue'>listNics</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_list_networks</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listNetworks"
  target="_parent"><span style='color:blue'>listNetworks</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_list_network_offerings</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listNetworkOfferings"
  target="_parent"><span style='color:blue'>listNetworkOfferings</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_list_keypairs</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listSSHKeyPairs"
  target="_parent"><span style='color:blue'>listSSHKeyPairs</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_list_firewall_rules</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listFirewallRules"
  target="_parent"><span style='color:blue'>listFirewallRules</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_list_egress_firewall_rules</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listEgressFirewallRules"
  target="_parent"><span style='color:blue'>listEgressFirewallRules</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_list_disk_offerings</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listDiskOfferings"
  target="_parent"><span style='color:blue'>listDiskOfferings</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_limits</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listResourceLimits"
  target="_parent"><span style='color:blue'>listResourceLimits</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_import_keypair_from_string</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/registerSSHKeyPair"
  target="_parent"><span style='color:blue'>registerSSHKeyPair</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_detach_nic_from_node</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/removeNicFromVirtualMachine"
  target="_parent"><span style='color:blue'>removeNicFromVirtualMachine</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_delete_tags</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteTags"
  target="_parent"><span style='color:blue'>deleteTags</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_delete_port_forwarding_rule</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deletePortForwardingRule"
  target="_parent"><span style='color:blue'>deletePortForwardingRule</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_delete_network</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteNetwork"
  target="_parent"><span style='color:blue'>deleteNetwork</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_delete_keypair</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteSSHKeyPair"
  target="_parent"><span style='color:blue'>deleteSSHKeyPair</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_delete_ip_forwarding_rule</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteIpForwardingRule"
  target="_parent"><span style='color:blue'>deleteIpForwardingRule</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_delete_firewall_rule</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteFirewallRule"
  target="_parent"><span style='color:blue'>deleteFirewallRule</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_delete_egress_firewall_rule</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteEgressFirewallRule"
  target="_parent"><span style='color:blue'>deleteEgressFirewallRule</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_create_tags</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createTags"
  target="_parent"><span style='color:blue'>createTags</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_create_snapshot_template</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createSnapshot"
  target="_parent"><span style='color:blue'>createSnapshot</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_create_port_forwarding_rule</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createPortForwardingRule"
  target="_parent"><span style='color:blue'>createPortForwardingRule</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_create_network</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createNetwork"
  target="_parent"><span style='color:blue'>createNetwork</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_create_keypair</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createSSHKeyPair"
  target="_parent"><span style='color:blue'>createSSHKeyPair</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_create_ip_forwarding_rule</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createIpForwardingRule"
  target="_parent"><span style='color:blue'>createIpForwardingRule</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_create_firewall_rule</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createFirewallRule"
  target="_parent"><span style='color:blue'>createFirewallRule</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_create_egress_firewall_rule</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createEgressFirewallRule"
  target="_parent"><span style='color:blue'>createEgressFirewallRule</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_attach_nic_to_node</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/addNicToVirtualMachine"
  target="_parent"><span style='color:blue'>addNicToVirtualMachine&nbsp;</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>ex_allocate_public_ip</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/associateIpAddress"
  target="_parent"><span style='color:blue'>associateIpAddress</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>detach_volume</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/detachVolume"
  target="_parent"><span style='color:blue'>detachVolume&nbsp;</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>destroy_volume_snapshot</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteSnapshot"
  target="_parent"><span style='color:blue'>deleteSnapshot</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>destroy_volume</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteVolume"
  target="_parent"><span style='color:blue'>deleteVolume</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>destroy_node</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/destroyVirtualMachine"
  target="_parent"><span style='color:blue'>destroyVirtualMachine</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>delete_key_pair</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteSSHKeyPair"
  target="_parent"><span style='color:blue'>deleteSSHKeyPair</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>delete_image</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteTemplate"
  target="_parent"><span style='color:blue'>deleteTemplate</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>create_volume_snapshot</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createSnapshot"
  target="_parent"><span style='color:blue'>createSnapshot</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>create_volume</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createVolume"
  target="_parent"><span style='color:blue'>createVolume</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>create_node</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deployVirtualMachine"
  target="_parent"><span style='color:blue'>deployVirtualMachine</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>create_key_pair</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createSSHKeyPair"
  target="_parent"><span style='color:blue'>createSSHKeyPair</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>create_image</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createTemplate"
  target="_parent"><span style='color:blue'>createTemplate</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>copy_image</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/copyTemplate"
  target="_parent"><span style='color:blue'>copyTemplate&nbsp;</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl6732583 style='height:15.0pt;border-top:none'>attach_volume</td>
  <td class=xl6932583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/attachVolume"
  target="_parent"><span style='color:blue'>attachVolume</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl7132583 style='height:15.0pt;border-top:none'>balancer_attach_member</td>
  <td class=xl7232583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/assignToLoadBalancerRule"
  target="_parent"><span style='color:#00359E'>assignToLoadBalancerRule</span></a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl7132583 style='height:15.0pt;border-top:none'>balancer_detach_member</td>
  <td class=xl6832583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/removeFromLoadBalancerRule"
  target="_parent">removeFromLoadBalancerRule</a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl7132583 style='height:15.0pt;border-top:none'>balancer_list_members</td>
  <td class=xl6832583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listLoadBalancerRuleInstances"
  target="_parent">listLoadBalancerRuleInstances</a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl7132583 style='height:15.0pt;border-top:none'>create_balancer</td>
  <td class=xl6832583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/createLoadBalancer"
  target="_parent">createLoadBalancer</a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl7132583 style='height:15.0pt;border-top:none'>destroy_balancer</td>
  <td class=xl6832583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/deleteLoadBalancer"
  target="_parent">deleteLoadBalancer</a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl7132583 style='height:15.0pt;border-top:none'>get_balancer</td>
  <td class=xl7032583 style='border-top:none;border-left:none'>No Equivalent
  VDC command</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl7132583 style='height:15.0pt;border-top:none'>list_balancers<font
  class="font532583">()</font></td>
  <td class=xl6832583 style='border-top:none;border-left:none'><a
  href="http://cloudstore.interoute.com/main/knowledge-centre/library/api-article/vdc/20/listLoadBalancerRules"
  target="_parent">listLoadBalancerRules</a></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl7132583 style='height:15.0pt;border-top:none'>list_protocols<font
  class="font532583">()</font></td>
  <td class=xl7032583 style='border-top:none;border-left:none'>No Equivalent
  VDC command</td>
 </tr>

</table>
</div>
