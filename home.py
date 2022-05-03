from flask import Flask, render_template, request
from frameset import VerbService
from verb_sense_reader import AdesseHandler
from main import verblist, args
import json

app = Flask(__name__)
# $ python3 home.py

@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/annotate')
def create_annotation():
    return render_template('annotate.html')

@app.route('/verbs')
def get_all_verbs():
    # Create all sample JSON object for demonstration 
    verb_service = VerbService()
    verbs = verb_service.create_example_verbs()
    return render_template('verbs.html', verbs=verbs)

@app.route('/frameset')
def get_frameset():
    pass

@app.route('/create')
def create_frameset():
    data = {
            "args": args,
            "verblist": verblist
    }
    return render_template('create_frameset.html', data=data)

@app.route('/verb')
def get_verb():
    #verb = get_verb(verb_lemma)
    verb_service = VerbService()
    verbs = verb_service.create_example_verbs()
    verb = verbs[1]
    return render_template('verb.html', verb=verb)

@app.route('/adesse')
def get_adesse_senses():
    verblemma = request.args['verblemma']
    handler = AdesseHandler()
    verb_senses = handler.get_verb_senses(verblemma)
    response = {}
    response['adesse_verb_senses'] = verb_senses
    return response


if __name__ == '__main__':
    app.run()