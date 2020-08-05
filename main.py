import imdb

(names, casts, title_basics) = imdb.import_imdb_data()
(title_list, popular_count) = imdb.count_popular_cast(names, casts)
