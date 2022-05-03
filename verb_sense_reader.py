from bs4 import BeautifulSoup
import requests

link = "http://adesse.uvigo.es/data/verbos.php?verbo=SENTIR"
f = requests.get(link)

class AdesseHandler():
    def __init__(self):
        self.constant_link = "http://adesse.uvigo.es/data/verbos.php?verbo="
    
    def get_verb_senses(self, verb):
        html_text = self._get_html_text(verb)
        res, table = self._get_verb_info(html_text)
        if res == 'single-sense-verb':
            verb_sense = self._get_single_verb_sense(verb, table)
            return [verb_sense]
        else:
            verb_senses = self._get_multiple_verb_senses(table)
            self.display_verb_senses(verb_senses)
            return verb_senses
    
    def display_verb_senses(self, verb_sense_list):
        for verb_sense in verb_sense_list:
            print('–––––––––––––––––––––––––––––––––––––––––––––')
            print(verb_sense[0])
            print('–––––––––––––––––––––––––––––––––––––––––––––')
            print(verb_sense[1])
            print('–––––––––––––––––––––––––––––––––––––––––––––')

    def _get_html_text(self, verb_lemma):
        new_link = self.constant_link + verb_lemma
        html_text = requests.get(new_link).text
        text = BeautifulSoup(html_text, 'html.parser')
        return text
    
    def _get_verb_info(self, text):
        verb_definition = text.find(id="definicion")
        if not verb_definition:
            table = text.find_all(class_="ResultsRowB")
            return 'multiple-senses-verb', table
        else: 
            tds = verb_definition.find_all("td")
            return 'single-sense-verb', tds
    
    def _get_multiple_verb_senses(self, table):
        verb_senses = []
        for t in table:
            verb_sense = []
            for child in t:
                #TODO: Remove '[+]' from additional verb sense info
                verb_sense.append(child.text)
            verb_senses.append(verb_sense)
        return verb_senses
    
    def _get_single_verb_sense(self, verb_lemma, verb_div):
        verb_sense = verb_div[0].text
        verb = verb_lemma.upper()
        return [verb, verb_sense]
