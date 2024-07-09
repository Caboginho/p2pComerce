<?php

// Verifica se os dados foram enviados via POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    
    // Conexão com o banco de dados (substitua pelos seus próprios detalhes de conexão)
    $servername = "localhost";
    $username = "seu_usuario";
    $password = "sua_senha";
    $dbname = "seu_banco_de_dados";
    $conn = new mysqli($servername, $username, $password, $dbname);
    
    // Verifica se a conexão foi bem sucedida
    if ($conn->connect_error) {
        die("Conexão falhou: " . $conn->connect_error);
    }
    
    // Recebe os dados do formulário
    $nome = $_POST['nome'];
    $descricao = $_POST['descricao'];
    $preco = $_POST['preco'];
    
    // Query para inserir o produto na tabela de produtos
    $sql = "INSERT INTO produtos (nome, descricao, preco) VALUES ('$nome', '$descricao', '$preco')";
    
    // Verifica se a inserção foi bem sucedida
    if ($conn->query($sql) === TRUE) {
        echo "Produto cadastrado com sucesso!";
    } else {
        echo "Erro ao cadastrar o produto: " . $conn->error;
    }
    
    // Fecha a conexão com o banco de dados
    $conn->close();
} else {
    // Se os dados não foram enviados via POST, redireciona para a página de cadastro de produtos
    header("Location: cadastro_produto.html");
    exit();
}

?>
