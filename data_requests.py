import requests
import random
import string
import json

def convert_date(stg):
	date=(stg.split()[0]).strip().split('-')
	time=stg.split()[1]
	# print date,time
	new_format="%s-%s-%s %s"%(date[2],date[1],date[0],time)
	return new_format

def get_meter(mid=''):
	print "mid :",mid
	print "\n######################## METER GET START ##########################"
	url="http://127.0.0.1:8000/meter/%s"%mid
	req=requests.get(url,timeout=5)	#url+"1/"
	print "\nreq :",req
	print "\nreq.content :",req.content
	print "\n######################## METER GET FINISH #########################"
get_meter('00100175')

def post_meter(mid):
	print "\n######################## METER POST START #########################"
	url="http://127.0.0.1:8000/meter/"
	params=dict(meter_id=mid)
	print "\nparams :",type(params),params
	req=requests.post(url,data=params)
	print "\nreq :",req
	print "\nreq.content :",req.content
	print "\n######################## METER POST FINISH ########################"
# post_meter(12345)

def get_data():
	print "\n######################## DATA GET START ##########################"
	url="http://127.0.0.1:8000/data/"
	req=requests.get(url,timeout=5)	#url+"1/"
	print "\nreq :",req
	print "\nreq.content :",req.content
	print "\n######################## DATA GET FINISH #########################"
# get_data()

# mid,sid,ts,st="991571163,001022D6,16-02-2016 11:22,Connected".split(',')

def post_data(mid,sid,ts,st):
	print "\n######################## DATA POST START #########################"
	data_url="http://127.0.0.1:8000/data/"
	data_params=dict(
		sequence_id= sid,
		timestamp=ts,
		connection_status= st,
		meter=mid )
	print "\ndata_params :",type(data_params),data_params
	data_req=requests.post(data_url,data=data_params)
	print "\ndata_req :",data_req
	print "\ndata_req.content :",data_req.content
	print "\n######################## DATA POST FINISH ########################"
	return data_req.status_code,data_req.content
