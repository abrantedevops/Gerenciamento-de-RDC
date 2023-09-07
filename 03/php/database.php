<?php
// Configurações do banco de dados
$servername = "10.200.0.10"; // IP do container MariaDB
$username = "root";
$password = "zabbix";
$dbname = "pratica03";

// Cria a conexão
$conn = new mysqli($servername, $username, $password, $dbname);

// Verifica a conexão
if ($conn->connect_error) {
    die("Erro na conexão com o banco de dados: " . $conn->connect_error);
}

echo "Conexão com o banco de dados MariaDB estabelecida com sucesso!";
echo "\n";
phpinfo();
?>
