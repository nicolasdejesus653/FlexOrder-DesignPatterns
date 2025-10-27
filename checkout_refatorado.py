from abc import ABC, abstractmethod

class EstrategiaPagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass

class PagamentoPix(EstrategiaPagamento):
    def pagar(self, valor):
        print(f"Pagando R${valor:.2f} via Pix (aprovado).")
        return True

class PagamentoCredito(EstrategiaPagamento):
    def pagar(self, valor):
        if valor < 1000:
            print(f"Pagando R${valor:.2f} via Cartão de Crédito (aprovado).")
            return True
        print("Pagamento REJEITADO (limite excedido).")
        return False
class EstrategiaFrete(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass

class FreteNormal(EstrategiaFrete):
    def calcular(self, valor):
        frete = valor * 0.05
        print(f"Frete Normal: R${frete:.2f}")
        return frete

class FreteExpresso(EstrategiaFrete):
    def calcular(self, valor):
        frete = valor * 0.10 + 15
        print(f"Frete Expresso: R${frete:.2f}")
        return frete
class PedidoBase:
    def __init__(self, valor):
        self._valor = valor

    def get_valor(self):
        return self._valor

class DecoradorPedido:
    def __init__(self, pedido):
        self._pedido = pedido

class DescontoPix(DecoradorPedido):
    def get_valor(self):
        print("Aplicando 5% de desconto PIX.")
        return self._pedido.get_valor() * 0.95

class DescontoGrande(DecoradorPedido):
    def get_valor(self):
        print("Aplicando 10% de desconto para pedidos grandes.")
        return self._pedido.get_valor() * 0.90

class TaxaEmbalagemPresente(DecoradorPedido):
    def get_valor(self):
        print("Adicionando R$5.00 de embalagem para presente.")
        return self._pedido.get_valor() + 5.0
pedido = PedidoBase(600)
pedido = DescontoGrande(pedido)
pedido = TaxaEmbalagemPresente(pedido)
print(pedido.get_valor())  # aplica os dois
class SistemaEstoque:
    def atualizar(self):
        print("Estoque atualizado.")

class GeradorNotaFiscal:
    def gerar(self):
        print("Nota fiscal emitida.")

class CheckoutFacade:
    def __init__(self, estrategia_pagamento, estrategia_frete):
        self.pagamento = estrategia_pagamento
        self.frete = estrategia_frete
        self.estoque = SistemaEstoque()
        self.nota = GeradorNotaFiscal()

    def finalizar_pedido(self, pedido):
        print("=== CHECKOUT MODERNO ===")
        valor = pedido.get_valor()
        frete = self.frete.calcular(valor)
        total = valor + frete
        print(f"Total a pagar: R${total:.2f}")
        if self.pagamento.pagar(total):
            self.estoque.atualizar()
            self.nota.gerar()
            print("Pedido finalizado com sucesso!")
        else:
            print("Falha no pagamento.")
if __name__ == "__main__":
    # Pedido 1 - PIX com frete normal
    pedido1 = PedidoBase(230)
    pedido1 = DescontoPix(pedido1)

    pagamento = PagamentoPix()
    frete = FreteNormal()
    checkout = CheckoutFacade(pagamento, frete)
    checkout.finalizar_pedido(pedido1)

    print("\n--- Próximo Pedido ---")

    # Pedido 2 - Cartão, frete expresso, embalagem presente
    pedido2 = PedidoBase(600)
    pedido2 = DescontoGrande(pedido2)
    pedido2 = TaxaEmbalagemPresente(pedido2)

    pagamento = PagamentoCredito()
    frete = FreteExpresso()
    checkout = CheckoutFacade(pagamento, frete)
    checkout.finalizar_pedido(pedido2)
