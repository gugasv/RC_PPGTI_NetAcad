from netmiko import ConnectHandler

def showIp(client):
    output = client.send_command('show ip int brief')
    print(output)

def createLoopback(client, interface, ipaddress, mask, description):
    config_command = [
        f'int {interface}',
        f'ip address {ipaddress} {mask}',
        f'description {description}'
    ]
    output = client.send_config_set(config_command)
    print(output)

sshCli = ConnectHandler(
    device_type='cisco_ios',
    host='192.168.1.13',
    port=22,
    username='cisco',
    password='cisco123!'
)

showIp(sshCli)
createLoopback(sshCli, 'loopback 3', '2.2.2.2', '255.255.255.0', 'Lab-2.2-3')
showIp(sshCli)