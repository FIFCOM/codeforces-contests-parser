import os
import urllib.request
import json
import datetime
from prettytable import PrettyTable

contest_url = "https://codeforces.com/api/contest.list"
cur_timestamp = int(datetime.datetime.now().timestamp())

def get_contest_list():
    response = urllib.request.urlopen(contest_url)
    data = json.loads(response.read().decode())
    ret = []
    if data['status'] == 'OK':
        for c in data['result']:
            if c['phase'] == 'BEFORE':
                
                ret.append([c['id'], c['name'], c['startTimeSeconds']])

    ret.sort(key=lambda x: x[2])
    return ret

def list_to_table(contest_list):
    ret = PrettyTable(['ID', 'Name', 'Start At'])
    for c in contest_list:
        # convert timestamp to d H:M
        start_time = datetime.datetime.fromtimestamp(
            c[2] - cur_timestamp).strftime('%d d %Hh%Mm')
        ret.add_row([c[0], c[1], start_time])
    return ret

print("Please wait...")
li = get_contest_list()
# clear terminal
os.system("cls")
print(list_to_table(li))
contest_id = input("Enter the contest ID to register:")
os.system("start https://codeforces.com/contestRegistration/" + contest_id)
