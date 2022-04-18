
import imp
from flask import Flask, render_template, request
import bd
from correiro import *
app = Flask(__name__)

#ABRE CHAMADO
@app.route('/')
def abre_pagina_princioal():
    return render_template('menu.html')

#pagina de abertura de chamada
@app.route('/abertura')
def abre_pagina_abertura_chamado():
    return render_template('abertura.html')

#pagina q exibe a lista de chamadas abertas 
@app.route('/exibe_chamado')
def abre_pagina_exibe_chamado():
    return render_template('exibe_chamado.html')



@app.route('/abertura', methods=['POST'])
def abertura_chamado():
    nome = request.form['nome_resp']
    setor = request.form['setor_chamado']
    local = request.form['local_chamado']
    comentario = request.form['comentario_chamado']
    mens = bd.abre_chamado(nome=nome, local=local, setor=setor,
        comentario=comentario)
    enviar_email_aberto(setor=setor, comentario=comentario)
    return mens


@app.route('/lista_chamados')
def abre_pagina_lista_chamados():
    return render_template('exibe_chamado.html', lista = bd.listar_chamados())


#FECHA CHAMADO
@app.route('/concluir_chamado', methods=['POST'])
def concluir_chamado():
    id_chamado = request.form['id_chamado']
    bd.atualiza_chamados(id_chamado)
    enviar_email_fechado()
    return render_template('exibe_chamado.html', lista = bd.listar_chamados())


if __name__ == "__main__":
    app.run()