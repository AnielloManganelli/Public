#!/bin/python3
import io as i
import socket as sk
import string as s
import sys as sy
import os as o
import base64 as b

q=quit;

file_path="/mnt/var/lib/jenkins/jobs/a/config.xml"

open_file = i.FileIO(file_path,'rb');
print(i.TextIOWrapper(open_file).read());

j_ip="127.0.0.1:";
j_port=8090;

s_ip="";
s_port=0;

usr="admin:";
pswd="1";
crd=bytes(usr+pswd,"ascii");

buff_size=20000;

option_letter=list();
option_letter.append("A");
option_letter.append("a");
lc=0;
jenkins_base_path="/var/lib";
jenkins_home="/jenkins";
jenkins_jobs="/jobs";
jenkins_logs="/builds";

parameter_list=['<job','<name','<build','<number'];
qstring= ["","api/json?tree=jobs[name]","jobs/jobname/api/xml?tree=builds[number]"];
month_list=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
def setupSk(ip, port):
	global sk0;
	sk0 = sk.socket();
	sk0.connect((ip,port));

def setupSk0(ip, port):
	global sk1;
	sk1 = sk.socket();
	sk1.bind((ip,port));

def readWrite(query, in_put):
	query.send(in_put);
	global out_put;
	out_put = query.recv(buff_size);

def toS(string):
	string = str.lstrip(str.rstrip(str(b.b64encode(string)),"\'\""),"b\'\"");
	return string;

def mStr(string,extra):
	string = str.lstrip(str.rstrip(str(string),"\'\""+extra),"b\'\"");
	return string;

def findVal(recv_buff,first_="",second_="",offset=0):
	recv_buff=str(recv_buff);
	pos_holder=recv_buff.find(first_,offset=0);
	pos_holder0=recv_buff.find(second_,pos_holder);
	return pos_holder0;

def findByte(recv_buff,third_="",fourth_="",offset=0):
	global new_holder;
	new_holder=0;
	recv_buff=str(recv_buff);
	pos_holder=recv_buff.find(third_,offset=0);
	pos_holder0=recv_buff.find(fourth_,pos_holder);
	new_holder=pos_holder0-pos_holder;
	new_holder=new_holder-1;
	return new_holder,pos_holder;

def add_to_list(arg_):
	if not name_list:
		name_list.append(arg_);
	else:
		name_list.append(arg_);
	return  name_list;

def S_out_put(out_put,new_holder=0,pos_holder=0,string=0):
	out_put0=str(out_put);
	global name_list;
	name_list=list();
	global out_put_string;
	out_put_string="";
	string=0;
	while string is not new_holder:
		pos_holder=pos_holder+1;
		out_put_string=out_put_string+out_put0[pos_holder];
		string=string+1
	add_to_list(out_put_string);

def OnDiskSort(cmd_,opt,part):
	handle = o.popen(cmd_+opt+part);
	handle = handle.read();
	handle = str(handle).split("/\n");
	handle.pop();
	return handle;




def SortString(handle_):
	global month_;
	month_=list();
	x=0;x0=0;it=0;
	for i in handle_:
		it=0;x0=0;
		while it is 0:
			if str(handle_[x]).find(month_list[x0]) is not -1:
				month_.append(handle_[x][28:34])
				x=x+1;
			else:
				x0=x0+1;



jquery=bytes("GET /"+qstring[0]+" HTTP/1.1\r\nHost: "+
		j_ip+str(j_port)+"\r\nAuthorization: Basic "+
		toS(crd)+"\r\nUser-"+option_letter[0]+"gent: curl/7.62.0\r\n\r\n","ascii");

response=bytes("HTTP/1.1 200 OK\r\n"+
		"Content-type: text/html"+
		"\r\nContent-length: 2\r\n\r\nHi\r\n","ascii");









