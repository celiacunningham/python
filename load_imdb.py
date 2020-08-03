import numpy as np
import pandas as pd
    
def import_imdb():
    filename_namebasics='C:\\Users\\cecunningham\\Downloads\\namebasics.tsv'
    filename_titleprincipals='C:\\Users\\cecunningham\\Downloads\\titleprincipals.tsv'
    filename_titlebasics='C:\\Users\\cecunningham\\Downloads\\titlebasics.tsv'
    print("Loading '%s' ..."%filename_namebasics)
    names = pd.read_csv(filename_namebasics, sep='\t')
    print("Loading '%s' ..."%filename_titleprincipals)
    casts = pd.read_csv(filename_titleprincipals, sep='\t')
    print("Loading '%s' ..."%filename_titlebasics)
    titlebasics = pd.read_csv(filename_titlebasics, sep='\t')
    print("Loading complete")
    return (names, casts, titlebasics)
