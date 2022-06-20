import xml.dom.minidom
from ncclient import manager

m = manager.connect(
    host='192.168.1.13',
    port=830,
    username='cisco',
    password='cisco123!',
    hostkey_verify=False
)

netconf_data = '''
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>111</name>
                <description>TEST1</description>
                <ip>
                    <address>
                        <primary>
                            <address>100.100.100.100</address>
                            <mask>255.255.255.0</mask>
                        </primary>
                    </address>
                </ip>
            </Loopback>
        </interface>
    </native>
</config>
'''
reply = m.edit_config(target='running', config=netconf_data)
print(xml.dom.minidom.parseString(reply.xml).toprettyxml())