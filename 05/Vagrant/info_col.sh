#!/bin/bash

# Configurações SNMP
community="pratc05"
target_host="localhost"

# Função para realizar uma consulta SNMP e exibir o resultado de forma legível
function snmp_query {
    oid="$1"
    label="$2"
    result=$(snmpwalk -v 2c -c "$community" "$target_host" "$oid" | awk -F ": " '{gsub(/^[ \t]+|[ \t]+$/, "", $2); print $2}')
    
    # Verifica se o resultado está vazio
    if [ -z "$result" ]; then
        result="N/A"
    fi
    
    # Adiciona unidades métricas apropriadas
    if [[ "$label" == *"Uso da CPU"* ]]; then
        result="$result %"
    elif [[ "$label" == *"Uso de Rede"* ]]; then
        result="$result bytes/s"
    elif [[ "$label" == *"Quantidade de Memória"* ]]; then
        result="$result KB"
    fi
    
    echo "$label: $result"
}

# Coleta e exibe informações SNMP
snmp_query "1.3.6.1.2.1.1.5.0" "Nome da Máquina"
snmp_query "1.3.6.1.2.1.1.3.0" "Tempo de Atividade"
snmp_query "1.3.6.1.4.1.2021.11.11.0" "Uso da CPU"
snmp_query "1.3.6.1.2.1.2.2.1.10.1" "Uso de Rede (Entrada)"
snmp_query "1.3.6.1.2.1.2.2.1.16.1" "Uso de Rede (Saída)"
snmp_query "1.3.6.1.2.1.25.2.2.0" "Quantidade de Memória Total"
snmp_query "1.3.6.1.2.1.25.2.3.1.6.1" "Quantidade de Memória Usada"
snmp_query "1.3.6.1.2.1.6.10.0" "Número de Conexões TCP Ativas"
snmp_query "1.3.6.1.2.1.25.1.6.0" "Número de Processos em Execução"