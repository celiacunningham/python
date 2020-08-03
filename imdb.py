def process_imdb2(names, casts, titlebasics):
    #select names where knownForTitles has 1 or more values
    popular_names=names[names['knownForTitles']!='\\N']
    print('popular names set')
    #popular_names.primaryName

    #for each title, how many cast members are popular names?
    title_set=set(casts['tconst'])
    title_list=list(title_set) # list of unique titles
    print('unique titles set')
    for t in title_list[6380994:6381994]:
        #print("title '%s"%t)
        c=casts[casts['tconst']==t] #list the cast
        for n in c['nconst']:
            if n in popular_names['nconst']:
                print(popular_names[popular_names['nconst']==n]['primaryName'])
                #titlebasics[titlebasics['tconst']==titles]['popular_name_count']=titlebasics[titlebasics['tconst']==titles]['popular_name_count']+1

    print("Cast check complete")
    return

    #collect most popular titleprincipals:tconst

    #for each tconst, lookup titlebasics:primaryTitle


