import xml.dom.minidom
import xmltodict
from ncclient import manager

m = manager.connect(
    host='192.168.1.13',
    port=830,
    username='cisco',
    password='cisco123!',
    hostkey_verify=False
)

netconf_filter = '''
<filter>
    <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
</filter>
'''

reply = m.get(filter=netconf_filter)
reply_dict = xmltodict.parse(reply.xml)

for interface in reply_dict['rpc-reply']['data']['interfaces-state']['interface']:
    print(f'Name: {interface["name"]} MAC: {interface["phys-address"]} Input: {interface["statistics"]["in-octets"]} Output: {interface["statistics"]["out-octets"]}')