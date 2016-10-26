import os.path
import yaml
import natlink
import dragonfly

def update_vocabulary():
    file_name = os.path.join(os.path.dirname(__file__), "vocabulary.yaml")

    with open(file_name, "r") as stream:
        vocabulary = yaml.load(stream)

    for word in vocabulary["add"]:
        natlink.addWord(word)

    for word in vocabulary["delete"]:
        try:
            natlink.deleteWord(word)
            print "removed " + repr(word) + " from vocabulary"
        except natlink.UnknownName:
            pass

update_vocabulary()

class UpdateVocabulary(dragonfly.CompoundRule):
    spec = "update vocabulary"
    def _process_recognition(self, node, extras):
        update_vocabulary()

grammar = dragonfly.Grammar("update_vocabulary")
grammar.add_rule(UpdateVocabulary())
grammar.load()

def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
