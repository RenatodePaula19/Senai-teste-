<h3>fipeexcel</h3>
Projeto desenvolvido no SENAI BETIM, inspirado na ideia do aluno Bruno Gomes.

<h2>FIPEXCEL</h2>
Uma concessionária de veículos realiza consultas online a tabela FIPE(tabela de valores de automóveis) mensalmente. O tempo gasto nessas consultas é em média 2 horas diárias, pois são consultados cerca de 400 veículos. Visando solucionar esse problema criamos um sistema que consulta os dados online e os armazena em uma planilha excel. Utilizando o sistema o tempo gasto na consulta cai para em média 5 minutos.

<h3>Requisitos Funcionais do Sistema</h3>
RF-001: O sistema deve permitir a busca de informação dos veículos a partir de um código e ano de fabricação.

RF-002: O sistema deve gravar os dados retornados pela consulta em um arquivo Excel, os dados armazenados são: Código do Veículo, Marca, Modelo, Ano, Preço, Tipo de Combustível, Mês de Referência da Consulta.

<h3>Requisitos Não Funcionais</h3>
RNF: 001 - O sistema deve salvar o arquivo em XLSX versão 2007 ou superior.

RNF:002 - O sistema deve ter acesso a internet 

RNF:003 - O usuário deve ter instalado em seu computador o python na versao 3.8.10 ou superior 

<h3>Regras de Negócio</h3> 

1 - Consulta a tabela fipe a consulta a tabela fipe deve ser feita pelo código oficial do veiculo todo veículo possui um código gerenciado pela organização que cuida da fipe. requisito funcional 001

<h3>CASO DE USO: ENVIAR RELATORIO POR EMAIL </h3>


![imagem teste senai falta de documentaçao](https://user-images.githubusercontent.com/103609825/164120693-db1aa8c3-474c-48e3-abaa-5f3cf4d27da4.jpg)


O usuário deve acessar a opção de envio da planilha gerada por e-mail.O usuário insere o e-mail desejado e clica no botão seleionar para buscar o relátorio no excel 
Ele então seleciona o relátorio e clica na opção enviar. O sistema emite um alerta dizendo que o email com o relatorio foi enviado com sucesso. 

<h3> caso de uso: gerar planilha excel baseado na tabela FIPE </h3>
# -----------------------------------------------
o usuário acessa o sistema e seleciona uma caixa de seleção o tipo de veículo que ele está buscando (caminhão,carro ou moto),deve informar também o ano inicial da busca e o ano final da busca.após o usuário clicar no botão é gerado a planilha e o sistema começa a busca baseado nos parâmetros informados(caso de uso: consulta FIPE).Após gerar o relatório o sistema deve emitir um alerta dizendo que a atividade foi concluída com sucesso.No arquivo excel devem ser exibidos os seguintes dados: códigos FIPE do veículo,Nome do veículo,Marca do veículos,Valor,Ano e tipo de combustível.  


<h3> caso de uso: gerar planilha excel baseado na tabela FIPE </h3>
# -----------------------------------------------

O sistema deve realizar uma busca através de uma API Web que traz dados oficias 
