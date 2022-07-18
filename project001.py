from flask import Flask, jsonify #comunicar com um sistema jsonify

#variavel
app = Flask(__name__)

#decorador(Atribuir funcionalidade) / rota 
@app.route('/')
#função
def raiz():
    #(print) 
    return '<h1>Hello World<h1>'

@app.route('/rota2')
def rota2():
    return '<h1>Ohayo sekay good morning World<h1>'
#parametro dentro da rota
@app.route('/pessoas/<string:nome>/<string:cidade>')
#parametro passado dentro da URL
def pessoas(nome,cidade):
    return jsonify ({'nome': nome,'cidade': cidade})

#reinicia o servidor e salva edição (debug=True)
app.run(debug=True) 


#route -> TcasT.com/contatos --> o que vem depois do seu dominio.
#função -> o que você quer exibir em uma página
#app.run -> colocar o site no ar.