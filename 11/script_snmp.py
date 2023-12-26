from netmiko import ConnectHandler
from pysnmp.hlapi import *

roteadores = [
    {
        'device_type': 'cisco_ios',
        'host': '192.168.1.101',
        'username': 'ifpb',
        'password': 'ifpb',
    },
    {
        'device_type': 'cisco_ios',
        'host': '192.168.1.102',
        'username': 'ifpb',
        'password': 'ifpb',
    },
    {
        'device_type': 'cisco_ios',
        'host': '192.168.1.103',
        'username': 'ifpb',
        'password': 'ifpb',
    }
]

comunidades = ['rocommunity_R1', 'rocommunity_R2', 'rocommunity_R3']

for idx, roteador in enumerate(roteadores):
    conexao = ConnectHandler(**roteador)
    print(f"\nHabilitando SNMP no roteador {conexao.host}...\n")
    com_snmp = comunidades[idx]
    comando_snmp = f"snmp-server community {com_snmp} RO"
    saida = conexao.send_config_set(comando_snmp)
    print(saida)

while True:
    for idx, roteador in enumerate(roteadores):
        host = roteador['host']
        community = comunidades[idx]

        iterator = getCmd(
            SnmpEngine(),
            CommunityData(community, mpModel=0),
            UdpTransportTarget((host, 161)),
            ContextData(),
            ObjectType(ObjectIdentity('IF-MIB', 'ifInOctets', 1)),
            ObjectType(ObjectIdentity('IF-MIB', 'ifOutOctets', 1))
        )

        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

        if errorIndication:
            print(f"Erro ao consultar {host}: {errorIndication}")
        elif errorStatus:
            print(f"Erro de status: {errorStatus}")
        else:
            in_octets = varBinds[0][1].prettyPrint()
            out_octets = varBinds[1][1].prettyPrint()
            print(f"{host} = in : {in_octets} out : {out_octets}")

    import time
    time.sleep(10)
