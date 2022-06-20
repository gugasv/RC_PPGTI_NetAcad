from ncclient import manager

m = manager.connect(
    host='192.168.1.13',
    port=830,
    username='cisco',
    password='cisco123!',
    hostkey_verify=False
)

for capability in m.server_capabilities:
    print(capability)