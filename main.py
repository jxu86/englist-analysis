from mongo_service.mongodb import MongoService
from pdf_service.pdf import PdfService
import nltk
import datetime
import csv

# nltk.download('averaged_perceptron_tagger')
# def main():
#     print('import start')
#     path = r'/Volumes/cat/project/python-note-book/data/Dynamics_of_Limit_Order_Books.pdf'
#     pdf = PdfService(path)
#     mongo = MongoService()
#     words = pdf.parse()
#     print('words=>',len(words))
#     print(words[:10])
#
#     words = set(words)
#     print('words=>', len(words))
#
#     words_tag = nltk.tag.pos_tag(words)
#
#     for word in words_tag:
#         data = {
#             'word': word[0],
#             'wordTag': word[1],
#             'createdAt': datetime.datetime.now(),
#             'updatedAt': datetime.datetime.now()
#         }
#         mongo.update(mongo.vocabulary, {'word': data['word']}, data)
#
#
#     print('import done')


def main():
    path = './data/COCA20000.csv'
    csv_data = open(path, 'r')
    dict_reader = csv.DictReader(csv_data)
    csv_dict = []
    mongo = MongoService()
    # d_len = len(dict_reader)
    i = 0
    pos = []
    for w in dict_reader:
        # csv_dict.append(w)
        # print('w=>',w)

        tmp = w['Definition'].split('. ')
        # definition = ''
        # pos = ''
        if len(tmp) > 0:
            pos.append(tmp[0])

        # data = {
        #     'word': w['Word'],
        #     'rank': int(w['Rank']),
        #     'collins': w['Collins'],
        #     'definition': w['Definition'],
        #     'tag': w['Tag'],
        #     'PoS': w['PoS'],
        #     # 'pos': w['Definition'].split('. ')[0],
        #     'createdAt': datetime.datetime.now(),
        #     'updatedAt': datetime.datetime.now()
        # }
        # mongo.update(mongo.vocabulary, {'word': data['word']}, data)
        i = i+1
        print('progress=>', i)
        # print('data=>',data)
    # print(csv_dict[:10])
    pos = set(pos)
    print('pos=>',pos)




if __name__ == '__main__':
    main()
