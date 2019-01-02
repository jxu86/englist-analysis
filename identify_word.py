from pdf_service.pdf import PdfService
from mongo_service.mongodb import MongoService

class IdentifyWordService(object):
    def __init__(self):
        pdf_path = r'/Volumes/cat/project/python-note-book/data/Dynamics_of_Limit_Order_Books.pdf'
        self.pdf = PdfService(pdf_path)
        self.mongodb = MongoService()


    def read_pdf(self):
        words = self.pdf.parse()
        return words

    def identify_word(self):
        pdf_words = list(set(self.read_pdf()))[:10]
        print('pdf_words=>', pdf_words)
        print('words len=>', len(pdf_words))
        query = {
            'word': {'$in': pdf_words}
            # 'knowTag': {'$lt': 1}
        }
        field = {'_id': 0, 'word': 1, 'definition': 1}
        ret = self.mongodb.find(self.mongodb.vocabulary, query, field)
        print('ret ==>', ret)

def main():
    identify_word_service = IdentifyWordService()
    identify_word_service.identify_word()



if __name__ == '__main__':
    main()
