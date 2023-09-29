# -*- coding: utf-8 -*-
from config import snmp_username, snmp_auth_key, snmp_priv_key, snmp_target, snmp_oid
import subprocess
import time

def snmp_read():
    snmp_cmd = "snmpget -u {} -l authPriv -a MD5 -x DES -A {} -X {} {} {}::{}.{}".format(
        snmp_username,
        snmp_auth_key,
        snmp_priv_key,
        snmp_target,
        snmp_oid[0],
        snmp_oid[1],
        snmp_oid[2]
    )

    try:
        output = subprocess.check_output(snmp_cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        return int(output.split(" ")[-1])
    except subprocess.CalledProcessError as e:
        print("Erro ao executar o comando SNMP: {}".format(e.output))
    except Exception as e:
        print("Erro: {}".format(str(e)))
    return None

def calcular_media(valores):
    if len(valores) > 0:
        return sum(valores) / len(valores)
    return 0

limite_percentual = 10
valores_octetos = []

while True:
    valor_atual = snmp_read()

    if valor_atual is not None:
        print("Octetos Recebidos: {}".format(valor_atual))
        valores_octetos.append(valor_atual)
        valores_octetos = valores_octetos[-10:]

        media = calcular_media(valores_octetos)
        if valor_atual > (media * (1 + limite_percentual / 100.0)):
            print("Limite de tráfego excedido!")

    time.sleep(10)