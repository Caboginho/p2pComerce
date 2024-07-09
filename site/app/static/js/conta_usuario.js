// Simulação de dados de usuários e histórico de pedidos (substituir com autenticação real no backend)
let usuarios = [
    { username: 'usuario1', senha: 'senha1', nome: 'Nome do Usuário 1', historico: [] },
    { username: 'usuario2', senha: 'senha2', nome: 'Nome do Usuário 2', historico: [] }
];

let usuarioLogado = null;

function registrarUsuario(username, senha, nome) {
    const novoUsuario = { username, senha, nome, historico: [] };
    usuarios.push(novoUsuario);
    return novoUsuario;
}

function loginUsuario(username, senha) {
    const usuario = usuarios.find(u => u.username === username && u.senha === senha);
    if (usuario) {
        usuarioLogado = usuario;
        alert('Login bem-sucedido!');
    } else {
        alert('Credenciais inválidas. Tente novamente.');
    }
}

function logoutUsuario() {
    usuarioLogado = null;
    alert('Logout bem-sucedido!');
}

function exibirPerfil() {
    if (usuarioLogado) {
        alert(`Nome: ${usuarioLogado.nome}\nUsername: ${usuarioLogado.username}`);
    } else {
        alert('Nenhum usuário logado.');
    }
}

function exibirHistorico() {
    if (usuarioLogado) {
        const historico = usuarioLogado.historico;
        if (historico.length > 0) {
            alert('Histórico de Pedidos:\n' + historico.join('\n'));
        } else {
            alert('Nenhum histórico de pedidos disponível.');
        }
    } else {
        alert('Nenhum usuário logado.');
    }
}
