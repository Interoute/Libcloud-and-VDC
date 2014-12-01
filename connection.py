#import of libcloud libraries
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

#create a driver for VDC
VDCDriver=get_driver(Provider.CLOUDSTACK)

#set VDC connection details
vdc_apikey= '61C08D-OJFE4bur88saOa9z_gZSFOCixiaVcqGzSkQcdTPnHyRePyibeR2KeADvH1Jo6T8aUhVwTMVT5KCuArA'
vdc_secretkey= 'ObAgu3Wp3xXs1n8YXGntc2nUAhsBuuVQHRmHNECTn_f9anITv75lK_QRDt2XwrTruFaflcWpOSXH2A2khNtnQg'
vdc_url= 'https://myservices.interoute.com/myservices/api/vdc'

#create connection to VDC
conn=VDCDriver(key=vdc_apikey, secret=vdc_secretkey, url=vdc_url)

#Method getConn
#Returns the connection
def getConn():
	return conn
