import xml.dom.minidom
from ncclient import manager

m = manager.connect(
    host='192.168.1.13',
    port=830,
    username='cisco',
    password='cisco123!',
    hostkey_verify=False
)

# reply = m.get_config(source='running')
# print(reply)

# print(xml.dom.minidom.parseString(reply.xml).toprettyxml())

netconf_filter = '''
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
'''
reply = m.get_config(source='running', filter=netconf_filter)
print(xml.dom.minidom.parseString(reply.xml).toprettyxml())