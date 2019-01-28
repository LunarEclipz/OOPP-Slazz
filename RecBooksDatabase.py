import shelve

db = shelve.open('bookRecommendations')
genres = ['Adventure', 'Art', 'Astrology', 'Autobiography', 'Biography', 'Biology', 'Chemistry',
              "Children's Literature", 'Comic Book', 'Coming-of-age', 'Cookbook', 'Crime', 'Diary', 'Drama',
              'Educational', 'Encyclopedia', 'Fairytale', 'Food', 'Geology', 'Guide', 'Health', 'History', 'Horror',
              'IT', 'Math', 'Memoir', 'Mystery', 'Non-Fiction', 'Paranormal', 'Physics', 'Physiology',
              'Poetry', 'Political Thriller', 'Prayer', 'Psychology', 'Religion', 'Review', 'Romance', 'Satire',
              'Sci-fi', 'Self Help', 'Suspense', 'Textbook', 'Thriller', 'Travel', 'Young Adult']
for i in genres:
    list = []
    db[i] = list

db.close()
