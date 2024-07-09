let carrinho = [];

function adicionarAoCarrinho(nomeProduto, precoProduto) {
    carrinho.push({ nome: nomeProduto, preco: precoProduto });
    atualizarCarrinho();
}

function removerDoCarrinho(index) {
    carrinho.splice(index, 1);
    atualizarCarrinho();
}

function calcularSubtotal() {
    return carrinho.reduce((total, item) => total + item.preco, 0);
}

function calcularFrete() {
    // Lógica de cálculo de frete (pode ser implementada conforme sua necessidade)
    return 0;
}

function atualizarCarrinho() {
    const listaCarrinho = document.getElementById('lista-carrinho');
    const subtotalElement = document.getElementById('subtotal');
    const freteElement = document.getElementById('frete');
    const totalGeralElement = document.getElementById('total-geral');

    listaCarrinho.innerHTML = '';
    
    carrinho.forEach((item, index) => {
        const li = document.createElement('li');
        li.innerHTML = `${item.nome} - R$ ${item.preco.toFixed(2)} <button onclick="removerDoCarrinho(${index})">Remover</button>`;
        listaCarrinho.appendChild(li);
    });

    const subtotal = calcularSubtotal();
    const frete = calcularFrete();
    const totalGeral = subtotal + frete;

    subtotalElement.textContent = `R$ ${subtotal.toFixed(2)}`;
    freteElement.textContent = `R$ ${frete.toFixed(2)}`;
    totalGeralElement.textContent = `R$ ${totalGeral.toFixed(2)}`;
}

function limparCarrinho() {
    carrinho = [];
    atualizarCarrinho();
}
