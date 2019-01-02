import requests
import csv
import datetime
from mongo_service.mongodb import MongoService



class ImportService(object):
    def __init__(self):
        self.csv_path = './data/COCA20000去重.csv'
        self.mongodb = MongoService()

    def import_word_to_mongodb(self, word, field):
        self.mongodb.update(self.mongodb.vocabulary, {'word': word}, field)

    def import_word_from_csv(self):
        csv_data = open(self.csv_path, 'r')
        dict_reader = csv.DictReader(csv_data)
        dict_reader = list(dict_reader)
        dict_reader = dict_reader[::-1]
        i = 0
        for w in dict_reader:
            knowTag = w['knowTag'] or '0'
            knowTag = int(knowTag)
            data = {
                'word': w['Word'],
                'knowTag': knowTag,
                # 'pos': pos,
                # 'rank': int(w['Rank']),
                # 'collins': w['Collins'],
                # 'definition': w['Definition'],
                # 'tag': w['Tag'],
                # 'PoS': w['PoS'],
                # 'pos': w['Definition'].split('. ')[0],
                # 'createdAt': datetime.datetime.now(),
                'updatedAt': datetime.datetime.now()
            }
            self.import_word_to_mongodb(data['word'], data)
            i += 1
            print('i=>', i)




def main():
    import_service = ImportService()
    import_service.import_word_from_csv()


if __name__ == '__main__':
    main()

