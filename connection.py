#import of libcloud libraries
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

#create a driver for VDC
VDCDriver=get_driver(Provider.CLOUDSTACK)

#set VDC connection details
vdc_apikey= 'INSERT YOUR VDC ACCOUNT API KEY HERE'
vdc_secretkey= 'INSERT YOUR VDC ACCOUNT SECRET KEY HERE'
vdc_url= 'INSERT YOUR VDC ACCESS URL HERE'

#create connection to VDC
conn=VDCDriver(key=vdc_apikey, secret=vdc_secretkey, url=vdc_url)

#Method getConn
#Returns the connection
def getConn():
	return conn
