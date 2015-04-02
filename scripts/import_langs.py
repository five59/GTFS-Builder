#!/env/bin/python
from gtfs.models import *

def run():
    fi=open('data/languages.txt')
    for la in fi:
        da = la.split('|')
        c = Language()
        c.iso_639_1 = da[0]
        c.name = da[1]
        print("".join(["Adding ",c.iso_639_1, " as ", c.name, "..."]))
        c.save()
    fi.close()
