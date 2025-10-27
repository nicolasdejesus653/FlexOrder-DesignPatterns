# FlexOrder-DesignPatterns
O sistema foi refatorado para corrigir problemas do código antigo, que tinha tudo misturado em uma única classe.
Agora, cada parte (pagamento, frete, descontos e finalização) tem sua própria função, seguindo os princípios SRP e OCP do SOLID.

Strategy 

Usado para separar os tipos de pagamento e frete.
Antes havia vários if/elif, agora cada tipo tem sua própria classe.
Facilita adicionar novos métodos sem mudar o código principal.

Decorator

Usado para aplicar descontos e taxas extras (como a embalagem de presente).
Cada desconto é uma camada que pode ser adicionada ao pedido.
 Evita mexer no código base e mantém o sistema flexível.

Facade

Usado para simplificar o processo de compra.
A classe CheckoutFacade faz todo o processo (pagamento, frete e nota fiscal) com um único método.
 Deixa o uso do sistema mais simples e organizado.
