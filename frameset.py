import uuid
import json
from io import open
from pathlib import Path

# Frameset and Verb classes should be db models
"""
VERB

lemma: verb lemma
framesets: list of Frameset objects
"""
#TODO: Verb lemma will be primary key in db
class Verb():
    def __init__(self, lemma, framesets=[]):
        self.lemma = lemma
        self.framesets = framesets
    
    def add_frameset(self, frameset):
        self.framesets.append(frameset)

"""
FRAMESET

id: frameset identifier
verb: verb or verb sense
comment: usage notes and case restrictions
arguments: argument number and description

"""
class Frameset():
    def __init__(self, verb, numarguments, argcomments, comment = ""):
        self.id = self._generate_id()
        self.verb = verb
        self.comment = comment
        self.roles = self._create_arguments(numarguments, argcomments)

    def edit_frameset():
        pass

    def _create_arguments(self, numarguments, argcomments):
        args =  {}
        for x in range(numarguments):
            arg_name = 'arg' + str(x)
            args[arg_name] = argcomments[x]
        return args
    
    def _generate_id(self):
        return uuid.uuid4()
    
    def print_frameset(self):
        print('–––––––––––––––––––––––––––––')
        print(self.verb + ": " + self.comment)
        print('–––––––––––––––––––––––––––––')
        for argument in self.roles:
            print(argument + ": " + self.roles[argument])
        print('–––––––––––––––––––––––––––––')
        print(self.id)


class FramesetService():
    def __init__(self):
        pass

    def get_frameset(self, req):
        pass

    def get_all_framesets(self, req):
        pass

    def create_frameset(self, frameset_data):
        pass


class VerbService():
    def __init__(self):
        pass

    def get_all_verbs(self, request):
        # TODO: fetch all verb instances from database     
        pass

    def create_verb(self, data):
        # TODO: check if verb exists in database
        new_verb = Verb(lemma=data['lemma'], framesets=[])
        for frameset in data['framesets']:
            verb = data['lemma'] + str(len(new_verb.framesets))
            comment = frameset['comment']
            numarguments = len(frameset['roles'])
            argcomments = []
            for role in frameset['roles']:
                argcomments.append(frameset['roles'][role])
            new_frameset = Frameset(verb, numarguments, argcomments, comment)
            new_verb.add_frameset(new_frameset)
        return new_verb

    def create_example_verbs(self):
        data_directory = Path("data/verb-examples")
        verbs = []
        for json_file in data_directory.glob('*.json'):
            file = open(json_file)
            data = json.load(file)
            new_verb = self.create_verb(data)
            verbs.append(new_verb)
        return verbs

