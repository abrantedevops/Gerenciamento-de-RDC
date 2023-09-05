#!/bin/bash

instalar_docker() {
    sudo apt update
    sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    echo "deb [signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt update
    sudo apt install -y docker.io
    sudo systemctl start docker
    sudo systemctl enable docker
}

instalar_docker_compose() {
    sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    
}

#Práticas em que o uso do gns3 se faz necessário
instalar_gns3() {
    sudo add-apt-repository ppa:gns3/ppa
    sudo apt update
    sudo apt install -y gns3-gui gns3-server
}

main() {
    echo "Iniciando a instalação..."
    instalar_docker
    echo "Docker instalado com sucesso!"
    instalar_docker_compose
    echo "Docker Compose instalado com sucesso!"
    instalar_gns3
    echo "GNS3 instalado com sucesso!"
    echo "Instalação concluída!"
}

main
