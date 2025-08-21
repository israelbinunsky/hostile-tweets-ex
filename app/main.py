from fetcher import  fetcher

a = fetcher('mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/','IranMalDB', 'tweets')
print(a.get_collection())