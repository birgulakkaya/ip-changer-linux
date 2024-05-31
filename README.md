# IP Changer Tool

This tool is used to change the IP address of a network interface in Linux operating systems.

## Usage

You can use the tool by following the steps below:

1. Install the required Python packages: `pip install -r requirements.txt`
2. Run the tool from the command line: `python ip_changer.py -i [interface] -ip [ip_address] -n [netmask]`
   - `interface`: The name of the network interface you want to change the IP address for
   - `ip_address`: The new IP address
   - `netmask`: The new netmask
3. Verify the last IP address and netmask after the operation completes.

## Example

You can change the IP address using the following example commands:
``````
+ python ip_changer.py -i eth0 -ip 192.168.0.100 -n 255.255.255.0
``````
``````
+ python ip_changer.py --interface eth0 -ipaddress 192.168.0.100 -netmask 255.255.255.0
``````