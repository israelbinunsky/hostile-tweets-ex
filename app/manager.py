from fetcher import fetcher
from processor import processor

class manager:
    def __init__(self):
        self.fetcher = fetcher('mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/', 'IranMalDB', 'tweets')
        self.collection = self.fetcher.get_collection()
        self.processor = processor()
    def get_result(self):
        result = list()
        for document in self.collection:
            processing = self.processor.get_processing(document)
            result.append(processing)
        return result

