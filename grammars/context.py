import aenea

def cls(name):
    return aenea.ProxyAppContext(cls = name, match = "exact")

terminal = cls("URxvt")
bash = terminal & aenea.ProxyAppContext(title = "sol@x200: ")
vim = terminal & aenea.ProxyAppContext(title = "^.* - VIM$", match = "regex")
