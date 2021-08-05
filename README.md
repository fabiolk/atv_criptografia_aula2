# Criptografia por chave simétrica usando a lib fernet em python
 
  Trabalho realizado como parte da disciplina de auditoria e segurança de sistemas.
 
## Obejtivos
* Fazer melhorias no código disponibilizado em https://github.com/grakshith/p2p-chat-python de modo a implementar a funcionalidade de chave simétrica da lib fernet
* Fazer a troca encriptada de mensagem entre dois clientes
* Interceptar pacotes usando wireshark e comprovar que as mensagens não estão legíveis   
  
## Conhecimentos usados
* Python
* Criptografia simétrica
* Sockets 
* Wireshark

## Melhorias
* A criptografia simétrica precisa compartilhar a chave que descriptografa entre os clientes, a internet não é um meio seguro portanto recomenda-se usar em conjunto a criptografia assimétrica
* O código desse projeto foi implementado para aprendizado e rocomenda-se não disponibilizar a chave em texto pleno dentro do código fonte. Uma forma para contornar isso poderia salvar a chave em um arquivo de texto
