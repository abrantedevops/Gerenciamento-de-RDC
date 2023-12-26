from netmiko import ConnectHandler

switches = [
    {
        'device_type': 'cisco_ios',
        'host': '1.1.1.1',
        'username': 'ifpb',
        'password': 'ifpb',
    },
    {
        'device_type': 'cisco_ios',
        'host': '1.1.1.3',
        'username': 'ifpb',
        'password': 'ifpb',
    },
    {
        'device_type': 'cisco_ios',
        'host': '1.1.1.4',
        'username': 'ifpb',
        'password': 'ifpb',
    }
]

vlans = [(2, 'Alunos'), (3, 'Professores'), (4, 'Técnicos')]

switch_connections = []
for switch in switches:
    connection = ConnectHandler(**switch)
    switch_connections.append(connection)

for switch_conn in switch_connections:
    print(f"\nConfigurando VLANs no switch {switch_conn.host}...\n")
    for vlan_id, vlan_name in vlans:
        commands = [
            f"vlan {vlan_id}",
            f"name {vlan_name}",
            "exit"
        ]
        output = switch_conn.send_config_set(commands)
        print(output)

for switch_conn in switch_connections:
    print(f"\nVerificando VLANs no switch {switch_conn.host}...\n")
    output = switch_conn.send_command("show vlan brief")
    print(output)

for switch_conn in switch_connections:
    print(f"\nSalvando configurações no switch {switch_conn.host}...\n")
    output = switch_conn.save_config()
    print(output)
