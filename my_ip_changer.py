import subprocess
import argparse
import re

def user_inputs():
    parse_object = argparse.ArgumentParser()
    parse_object.add_argument("-i","--interface",dest="interface",help="the interface to be changed")
    parse_object.add_argument("-ip","--ipaddress",dest="ip_address",help="new ip address")
    parse_object.add_argument("-n","--netmask",dest="netmask",help="new netmask")

    return parse_object.parse_args() #tuple returns

def change_ip_address(user_interface,user_ip,user_netmask):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,user_ip,"netmask",user_netmask])
    subprocess.call(["ifconfig",user_interface,"up"])

def control_new_ip(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface])
    new_ip_address = re.search(r"inet (\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})",ifconfig.decode("utf-8"))
    new_netmask = re.search(r"netmask (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",ifconfig.decode("utf-8"))

    if new_ip_address and new_netmask:
        return new_ip_address.group(1), new_netmask.group(1)
    else:
        return None, None

print("IP changer started")
user_input = user_inputs()
change_ip_address(user_input.interface,user_input.ip_address,user_input.netmask)

last_ip_netmask = control_new_ip(user_input.interface) #last_ip_netmask is a tuple

if last_ip_netmask[0] == user_input.ip_address and last_ip_netmask[1] == user_input.netmask:
    print("Success!")
else:
    print("Error!")