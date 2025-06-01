from flask import Flask, render_template, request, session, jsonify

app = Flask(__name__)
app.secret_key = 'votre_cle_secrete'

@app.route('/')
def accueil():
    return render_template('prix.html')

@app.route('/ajouter_panier', methods=['POST'])
def ajouter_panier():
    article = request.json
    if 'panier' not in session:
        session['panier'] = []
    session['panier'].append(article)
    session.modified = True
    return jsonify({'message': 'Ajouté!', 'panier': session['panier']})

@app.route('/voir_panier')
def voir_panier():
    return jsonify({'panier': session.get('panier', [])})

@app.route('/vider_panier', methods=['POST'])
def vider_panier():
    session['panier'] = []
    session.modified = True
    return jsonify({'message': 'Panier vidé!'})

if __name__ == '__main__':
    app.run(debug=True)