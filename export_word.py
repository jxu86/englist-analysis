from mongo_service.mongodb import MongoService
import csv

class ExportWordService(object):
    def __init__(self):
        self.mongodb = MongoService()
        csvfile = open("./data/COCOA20000_1.csv", "w")
        self.writer = csv.writer(csvfile)
        self.writer.writerow(['rank', 'word', 'konwTag', 'definition'])


    def read_all_word(self):
        field = {'_id': 0, 'rank': 1, 'word': 1, 'knowTag': 1, 'definition': 1}
        ret = self.mongodb.find(self.mongodb.vocabulary, {}, field)
        return list(ret)

    def export_word_csv(self):
        i = 0
        ret = self.read_all_word()
        for r in ret:

            definition = ''
            try:
                if r['definition']:
                    definition = r['definition']
            except:
                pass

            tmp = [r['rank'], r['word'], r['knowTag'], definition]
            self.writer.writerow(tmp)
            i += 1
            print('i=>', i)


def main():
    export_word_service = ExportWordService()
    export_word_service.export_word_csv()



if __name__ == '__main__':
    main()
