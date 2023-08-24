<h2 align="center">Prática 01</h2>

### Objetivo
<p align="justify">Instalação do Zabbix Server. Colocá-lo para gerenciar 3 ativos de redes: 1 Máquina Linux, 1 Máquina Windows e um roteador. Adicionar gerenciamento do máximo de informações possível: HD, Networking, Ram, Disco, [...]. Além disso, adicione gráficos e alertas ao servidor e faça a integração com o Grafana.</p>

### Zabbix
<p align="justify">O Zabbix é um software de monitoramento de redes e sistemas que é capaz de monitorar a disponibilidade e o desempenho de diversos ativos de rede, como servidores, estações de trabalho, roteadores, switches e outros dispositivos de rede. O Zabbix usa uma arquitetura cliente-servidor e técnicas de monitoramento distribuído, que permitem monitorar desempenho e disponibilidade de servidores e outros equipamentos de rede, independentemente da sua localização física. O Zabbix funciona coletando dados de ativos de rede usando diferentes métodos, como o protocolo SNMP, agentes Zabbix instalados em sistemas monitorados e outras interfaces de monitoramento. Esses dados são processados, armazenados e exibidos em painéis e relatórios que auxiliam os administradores a entender o estado da infraestrutura de TI. O Zabbix ainda oferece flexibilidade nas notificações, permitindo que os administradores configurem alertas para serem enviados por vários meios. Além disso, a integração do Zabbix com outras ferramentas, como o Grafana, amplia as capacidades de visualização e análise dos dados monitorados, permitindo criar painéis mais detalhados e personalizados.</p>

### Grafana
<p align="justify">O Grafana é uma ferramenta de análise e visualização de código aberto. É possível consultar, visualizar, alertar e explorar inúmeros métricas, independentemente de onde estejam armazenadas. Ele fornece recursos de painel para permitir que você visualize seus dados em tempo real, além de recursos de compartilhamento e colaboração. Ele suporta vários backends de dados, como Zabbix, Prometheus, Loki, Elasticsearch, InfluxDB, Graphite, OpenTSDB, AWS CloudWatch, TempoDB e muitos outros.</p>

### GNS3
<p align="justify">O GNS3 é um simulador gráfico de redes que permite a simulação de redes complexas. Ele permite executar uma pequena rede composta por apenas alguns dispositivos, para redes complexas com muitos dispositivos, em vários servidores, que podem ser distribuídos em vários locais geográficos. O GNS3 usa imagens de dispositivos reais para permitir construir redes virtuais do mundo real. O GNS3 é usado por empresas, profissionais de rede, desenvolvedores e estudantes em todo o mundo para emular, configurar, testar e solucionar problemas de redes virtuais e reais.</p>

### Execução do docker-compose
```bash
$ docker-compose up -d
```

### Acesso ao Zabbix
```bash
http://localhost:8080
```

### Acesso ao Grafana
```bash
http://localhost:3000
```




