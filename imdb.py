import numpy
import pandas


def import_imdb_data():
    # load those data files

    filename_name_basics = 'C:\\Users\\celia\\Documents\\imdb\\namebasics.tsv'
    filename_title_principals = 'C:\\Users\\celia\\Documents\\imdb\\titleprincipals.tsv'
    filename_title_basics = 'C:\\Users\\celia\\Documents\\imdb\\titlebasics.tsv'
    print("Loading '%s' ..." % filename_name_basics)
    names = pandas.read_csv(filename_name_basics, sep='\t')
    print("Loading '%s' ..." % filename_title_principals)
    casts = pandas.read_csv(filename_title_principals, sep='\t')
    print("Loading '%s' ..." % filename_title_basics)
    title_basics = pandas.read_csv(filename_title_basics, sep='\t')
    print("Loading complete")
    return names, casts, title_basics


def count_popular_cast(names, casts):
    # for each title, how many cast members are known for something?

    title_set = set(casts['tconst'])
    title_list = list(title_set)  # list of unique titles
    nt = len(title_list)
    popular_count = numpy.zeros(nt)
    for t in range(nt - 10, nt):
        cast = casts[casts['tconst'] == title_list[t]]  # list the cast in each title
        for cast_member in cast['nconst']:
            if all(names[names['nconst'] == cast_member][
                       'knownForTitles'] != '\\N'):  # select names where knownForTitles has 1 or more values
                popular_count[t] = popular_count[t] + 1  # add one count for each popular cast members
    print("Cast check complete")
    # print(popular_count[nt-10:])

    return title_list, popular_count

    # collect most popular title_principals:tconst

    # for each tconst, lookup title_basics:primaryTitle
