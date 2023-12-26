<h1 align="center">Gerenciamento de Redes de Computadores</h1>

<p align="center"><img src="./bki/grc.png" alt="Scope" style="max-width:70%"></p>

<p align="justify">Este repositório tem a função de armazenar o conteúdo desenvolvido durante a disciplina de Gerenciamento de Redes de Computadores, ministrada pelo professor Thiago Gouveia do curso de Tecnologia de Redes de Computadores do Instituto Federal de Educação, Ciência e Tecnologia da Paraíba - IFPB. O material disponibilizado possui como característica o uso de containers para a execução das ferramentas que são abordadas na disciplina, além disso optei por utilizar os simuladores GNS3 e PnetLab para o desenvolvimento das topologias de rede. Por fim espera-se que este espaço possa auxiliar no aprendizado de todos os alunos ou interessados.</p>

<p align="center">
  <a href="#objetivo">Objetivo</a> •
  <a href="#tecnologias">Tecnologias</a> •
    <a href="#dependências">Dependências</a> •
  <a href="#contribuição">Contribuição</a> •
  <a href="#licença">Licença</a> •
  <a href="#autor">Autor</a>
</p>

### Objetivo
<p align="justify">O objetivo da disciplina consiste em conhecer os métodos para administrar e gerenciar uma rede de computadores, manusear ferramentas com interface por linhas de comando como interface 
gráfica, ler e compreender os gráficos gerados pelas ferramentas de gerência, tomar decisões através de políticas estabelecidas ou falhas apresentadas e realizar as principais 
operações de troubleshooting.</p>

### Tecnologias
As seguintes tecnologias foram utilizadas para o desenvolvimento das práticas:

- [Zabbix](https://www.zabbix.com/)
- [Grafana](https://grafana.com/)
- [GNS3](https://www.gns3.com/)
- [PnetLab](https://pnetlab.com/)
- [MariaDB](https://mariadb.org/)
- [Prometheus](https://prometheus.io/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Vagrant](https://www.vagrantup.com/)
- [Ansible](https://www.ansible.com/)
- [Linux](https://www.linux.org/)
- [Windows Server](https://www.microsoft.com/pt-br/windows-server)
- [Cisco IOS](https://www.cisco.com)
- [iSpy](https://www.ispyconnect.com/)
- [TrueNAS](https://www.truenas.com/)
- [Sys-ControlVMs](https://github.com/abrantedevops/Sys-ControlVMs)
- [Fortinet](https://www.fortinet.com/)
- [Moodle](https://moodle.org/)


### Dependências para iniciar as ferramentas por meio de containers Docker
Para iniciar as ferramentas por meio de containers é essencial ter instalado em sua máquina o Docker e o Docker Compose. Há um script que instala as dependências necessárias juntamente com o GNS3, basta seguir o procedimento abaixo (distribuição Ubuntu).

#### Clone este repositório
```bash 
$ git clone https://github.com/abrantedevops/Gerenciamento-de-RDC.git
```

#### Acesse a pasta do projeto no terminal/cmd
```bash
$ cd Gerenciamento-de-RDC
```

#### Caso for necessário torne o script de instalação das dependências executável
```bash
$ chmod +x pkgs.sh
```

#### Execute com privilégios de super usuário
```bash
$ sudo ./pkgs.sh
```

### Contribuição
Este projeto é para fins de estudo, então sinta-se à vontade para contribuir com sugestões, dicas, melhores práticas e quaisquer outras alterações.

1. Faça um fork do projeto.
2. Crie uma nova branch com suas alterações;
3. Salve suas alterações e crie uma mensagem de commit comentando as alterações feitas;
4. Após criar e salvar suas alterações no seu branch, envie um Pull Request para o repositório original.

### Licença
MIT License

Copyright (c) 2012-2023 Thiago Abrante de Souza

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

### Autor
Mantido por [Thiago Abrante](mailto:thiago.abrante@academico.ifpb.edu.br)
