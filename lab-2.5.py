import json
from venv import create
import requests

requests.packages.urllib3.disable_warnings()

class IETFInterfaces:

    api_url = 'https://192.168.1.13/restconf/data/ietf-interfaces:interfaces/'
    headers = {
        'Accept': 'application/yang-data+json',
        'Content-type': 'application/yang-data+json'
    }
    basic_auth = ('cisco', 'cisco123!')

    def __parse_name(self, name):
        return name.strip().replace(' ', '')

    def get_interfaces(self):
        req = requests.get(self.api_url, auth=self.basic_auth, headers=self.headers, verify=False)
        print(json.dumps(req.json(), indent=4))

    def put_interface(self, interface, ipaddress, mask, description):
        print(self.__parse_name(interface))
        yangConfig = {
            "ietf-interfaces:interface": {
                "name": self.__parse_name(interface),
                "description": description,
                "type": "iana-if-type:softwareLoopback",
                "enabled": True,
                "ietf-ip:ipv4": {
                    "address": [
                        {
                            "ip": ipaddress,
                            "netmask": mask
                        }
                    ]
                },
                "ietf-ip:ipv6": {}
            }
        }
        req = requests.put(f'{self.api_url}interface={self.__parse_name(interface)}', data=json.dumps(yangConfig), auth=self.basic_auth, headers=self.headers, verify=False)
        return req.status_code >= 200 and req.status_code <= 299

    def delete_interface(self, interface):
        req = requests.delete(f'{self.api_url}interface={interface}', auth=self.basic_auth, headers=self.headers, verify=False)
        return req.status_code >= 200 and req.status_code <= 299

if __name__ == '__main__':
    ietf = IETFInterfaces()
    
    # created = ietf.put_interface('Loopback 98', '4.4.4.4', '255.255.255.0', 'Lab-2.5')
    # if created:
    #     ietf.get_interfaces()
    # else:
    #     print('não foi possível criar a interface')
    
    deleted = ietf.delete_interface('Loopback3')
    if deleted:
        print('Interface removida com sucesso')
        ietf.get_interfaces()
    else:
        print('Falha ao remover interface')
