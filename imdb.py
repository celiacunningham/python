import numpy as np
import pandas as pd

def import_imdb_data():
#load those data files

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

def count_popular_cast(names, casts, titlebasics):
#for each title, how many cast members are known for something?

    title_set=set(casts['tconst'])
    title_list=list(title_set) # list of unique titles
    nt=len(title_list)
    popular_count=np.zeros(nt)
    for t in range(nt-10,nt):
        cast=casts[casts['tconst']==title_list[t]] #list the cast in each title
        for cast_member in cast['nconst']:
            if all(names[names['nconst']==cast_member]['knownForTitles']!='\\N'): #select names where knownForTitles has 1 or more values
                popular_count[t]=popular_count[t]+1 # add one count for each popular cast members
    print("Cast check complete")
    #print(popular_count[nt-10:])

    return (title_list, popular_count)

    #collect most popular titleprincipals:tconst

    #for each tconst, lookup titlebasics:primaryTitle
