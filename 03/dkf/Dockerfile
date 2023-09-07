
FROM nginx

RUN apt-get update && apt-get install -y wget && \
    wget https://repo.zabbix.com/zabbix/5.4/debian/pool/main/z/zabbix-release/zabbix-release_5.4-1+debian11_all.deb && \
    dpkg -i zabbix-release_5.4-1+debian11_all.deb && \
    apt-get update && \
    apt-get install -y zabbix-agent && \
    apt-get clean

COPY zabbix_agentd.conf /etc/zabbix/zabbix_agentd.conf

RUN mkdir -p /var/log/zabbix/

RUN chmod 777 /var/log/zabbix/

EXPOSE 80

CMD service zabbix-agent start && nginx -g "daemon off;"
