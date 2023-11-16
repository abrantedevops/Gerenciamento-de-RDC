<h1 align="center">Prática 04 - Atalhos são Caminhos mais curtos?</h1>

Existem alguns atalhos para colocar um Zabbix no ar mais rapidamente, por exemplo:

- VM pronta;
- Docker;
- Vagrant;
- Ansible

O desafio consiste em colocar o Zabbix para rodar usando pelo menos 2 das opções acima (uma entra as 2 primeiras e uma entre as duas últimas).

<hr>

### Docker

A primeira opção escolhida foi o Docker, para isso foi criado um arquivo docker-compose.yml com a configuração para subir os containers zabbix-server, zabbix-frontend, zabbix-mariadb e zabbix-agent. Para subir os containers entre no diretório "Docker" e execute o comando abaixo:

```bash
cd Docker
sudo docker-compose up -d
```

Após isso, basta acessar o endereço http://localhost:8080 para ter acesso a tela de login do Zabbix.

### Ansible 

O ansible foi a segunda opção escolhida, foram criados dois cenários distintos para a instalação do Zabbix, um com o auxílio do Vagrant para um ambiente mais controlado e outro sem o Vagrant. O hypervisor utilizado foi o VirtualBox, sendo assim necessário a instalação prévia do mesmo.

Com o Vagrant:

```bash
cd Ansible-Vagrant
vagrant up
vagrant ssh
sudo reboot
```

Após a execução do playbook e reinicialização da VM, basta acessar no browser o endereço http://192.168.57.13/zabbix para ter acesso ao Zabbix.

Para rodar o Zabbix sem o uso do Vagrant basta seguir o procedimento abaixo. Vale salientar que em ambos os cenários, o ansible é executado no sistema operacional <strong style="color:red;">Debian 11</strong>. Caso opte por utilizar um sistema operacional distinto é de responsabilidade do usuário todo o troubleshooting necessário para que o playbook funcione corretamente, ou se preferir, cogite a utilização do Vagrant. 

```bash
cd Ansible-Vagrant
sudo ansible-playbook -i inventory.ini playbook_zabbix.yml
sudo reboot
```

Nesse instante o Ansible irá iniciar todas as tarefas necessárias para o provisionamento do ambiente, após a execução do playbook e o sistema ser reiniciado, basta acessar no browser o endereço http://localhost/zabbix para ter acesso ao Zabbix.



