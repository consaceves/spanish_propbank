from io import open
import json
from conllu import parse_incr, parse_tree

from verb_sense_reader import AdesseHandler

"""
    Dictionary to store verb lemmas found in corpus.
    Keys: verb lemmas
    Values: TokenTree lists
"""
verb_lemmas = {}
args = {}
file = open('PropBankAnnotations.json')
annotation_guideline = json.load(file)
args = annotation_guideline['arguments']


data_file = open("UD_Spanish-AnCora/es_ancora-ud-dev.conllu", "r", encoding="utf-8")


#print(sentences.__next__().to_tree().print_tree())
#print(sentence.metadata)
#print(sentence.children)

"""
    Most tree roots are verbs. 
    However, we would like to find all verb instances
    and avoid adding dictionary keys that are not verbs.
    So, each tree must be iterated through and the nodes
    that are verbs isolated.
"""
def get_corpus_verbs():
    sentences = parse_incr(data_file)
    for sentence in sentences:
        tree = sentence.to_tree()
        dic = tree.__dict__
        if dic['token']['upos'] == 'VERB':
            add_verb_lemma(dic['token']['lemma'], sentence)
        for child in tree.children:
            child_dic = child.__dict__
            if child_dic['token']['upos'] == 'VERB':
                add_verb_lemma(child_dic['token']['lemma'], sentence)

def add_verb_lemma(verb_lemma, tree):
    if not verb_lemma in verb_lemmas:
            verb_lemmas[verb_lemma] = [tree]
    else: 
        verb_lemmas[verb_lemma].append(tree)

def verb_sense_selection():
    pass

def print_arguments():
    file = open('PropBankAnnotations.json')
    annotation_guideline = json.load(file)
    arguments = annotation_guideline['arguments']
    for argument in arguments:
        print(argument['role'] + ": " + argument['description'])
    args = arguments

get_corpus_verbs()
verblist = verb_lemmas.keys()

