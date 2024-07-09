function realizarCheckout() {
    const totalGeral = calcularTotalGeral(); // Implemente a lógica para calcular o total geral

    // Simulando um pagamento (não seguro - apenas para fins de exemplo)
    const opcaoPagamento = prompt("Escolha a opção de pagamento:\n1. Cartão de Crédito\n2. Cartão de Débito\n3. Transferência Bancária");

    if (opcaoPagamento) {
        alert(`Pagamento realizado com sucesso!\nTotal: R$ ${totalGeral.toFixed(2)}`);
        limparCarrinho(); // Limpar carrinho após o pagamento (simulação)
    } else {
        alert("Pagamento cancelado.");
    }
}

function calcularTotalGeral() {
    const subtotal = parseFloat(document.getElementById('subtotal').innerText.replace("R$ ", ""));
    const frete = parseFloat(document.getElementById('frete').innerText.replace("R$ ", ""));
    return subtotal + frete;
}
