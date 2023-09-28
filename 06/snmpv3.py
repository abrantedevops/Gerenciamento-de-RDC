# -*- coding: utf-8 -*-

from pysnmp.hlapi import *
import time

# Configuração SNMPv3
usuario = 'thiago'
autenticacao_protocolo = usmHMACMD5AuthProtocol
senha_autenticacao = 'redesifpb'
encriptacao_protocolo = usmDESPrivProtocol
senha_encriptacao = 'redesifpb'
endereco_ip_agent = '192.168.121.119'

oid_interface = ObjectIdentity('IF-MIB', 'ifInOctets', 1)

# Inicialização das variáveis
media = 0

while True:
    
    iterator = getCmd(
        SnmpEngine(),
        UsmUserData(usuario, senha_autenticacao, senha_encriptacao, authProtocol=autenticacao_protocolo, privProtocol=encriptacao_protocolo),
        UdpTransportTarget((endereco_ip_agent, 161)),
        ContextData(),
        ObjectType(oid_interface)
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
    
        octetos_recebidos = int(varBinds[0][1])
        
    
        media = (media + octetos_recebidos) / 2
        
    
        if octetos_recebidos > 1.1 * media:
            print("Limite de tráfego excedido!")
        
        # Imprime o valor lido e a média atual
        print("Octetos Recebidos: {}, Média: {}".format(octetos_recebidos, media))
   
    time.sleep(10)