import dragonfly
from aenea.lax import Key, Text

import context
reload(context)

vlc = {
    "full-screen": Key("f"),
    "pause": Key("space"),
    "quit": Key("c-q"),
}

totem = {
    "full-screen": Key("f"),
    "pause": Key("space"),
    "quit": Key("q"),
}

mplayer = {
    "full-screen": Key("f"),
    "pause": Key("space"),
    "quit": Key("q"),
}

vlc_context = context.cls("vlc")
totem_context = context.cls("Totem")
mplayer_context = context.cls("MPlayer")

grammar = dragonfly.Grammar("media_player")
grammar.add_rule(dragonfly.MappingRule(name = "vlc", mapping = vlc, context = vlc_context))
grammar.add_rule(dragonfly.MappingRule(name = "totem", mapping = totem, context = totem_context))
grammar.add_rule(dragonfly.MappingRule(name = "mplayer", mapping = mplayer, context = mplayer_context))
grammar.load()

def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
