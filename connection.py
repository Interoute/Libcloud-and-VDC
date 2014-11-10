#! /usr/bin/env python
#import libcloud stuffs
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
import libcloud.security

#create a driver for VDC
VDCDriver=get_driver(Provider.CLOUDSTACK)

#set VDC connection details
vdc_apikey="INSERT YOUR VDC'S ACCOUNT API KEY HERE"
vdc_secretkey="INSERT YOUR VDC'S ACCOUNT SECRET KEY HERE"
vdc_url="https://myservices.interoute.com/myservices/api/vdc"
#create connection to VDC
vdc_conn=VDCDriver(key=vdc_apikey, secret=vdc_secretkey, url=vdc_url)
