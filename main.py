import imdb
(names, casts, titlebasics)=imdb.import_imdb_data()
(title_list, popular_count)=imdb.count_popular_cast(names, casts, titlebasics)
