import requests
import csv
import datetime
from mongo_service.mongodb import MongoService
class IcibaService(object):
    def __init__(self):
        self.base_url = 'http://www.iciba.com/index.php?a=getWordMean&c=search&word='

    def get_word_means(self, word):
        word_url = self.base_url + word
        req = requests.get(word_url)
        info = req.json()
        return info

    def import_word_from_csv(self):
        pass


def main():
    path = './data/COCA20000.csv'
    csv_data = open(path, 'r')
    dict_reader = csv.DictReader(csv_data)
    iciba = IcibaService()
    mongo = MongoService()
    dict_reader = list(dict_reader)
    dict_reader = dict_reader[::-1]
    # check_words = ['eighteenth-century', 'one-quarter', 'prize-winning', 'multimillion-dollar', 'six-year-old', 'credit-card', 'six-year', 'defensively', 'medium-size', 'three-year-old', 'thirty-two', 'land-use', 'single-family', 'pre-service', 'million-dollar', 'faith-based', 'much-needed', 'regular-season', 'thirty-six', 'one-day', 'self-reported', 'Arab-Israeli', 'web-based', 'one-fifth', 'one-fourth', 'seven-year', 'grudgingly', 'number-one', 'four-day', 'multi-ethnic', 'seven-year-old', 'three-month', 'sixty-five', 'longer-term', 'five-day', 'at-bat', 'one-hour', 'multi-party', 'small-business', 'thirty-four', 'school-based', 'mid-size', 'civil-military', 'eight-year-old', 'teacher-librarian', 'three-time', 'mid-afternoon', 'English-language', 'thirty-seven', 'thirty-one', 'three-story', 'four-year-old', 'stainless-steel', 'pre-dawn', 'Washington-based', 'second-floor', 'thirty-eight', 'US-led', 'mid-morning', 'fifty-five', 'he/she', 'computer-generated', 'five-minute', 'co-director', 'private-sector', 'nine-year-old', 'Israeli-Palestinian', 'health-related', 'co-write', 'underly', 'two-year-old', 'at-large', 'Mexican-American', 'student-athlete', 'co-chair', 'belatedly', 'single-parent', 'half-mile', 'well-documented', 'first-person', 'grandkid', 'all-white', 'seventeenth-century', 'Spanish-speaking', 'fourth-quarter', 'lasagna', 'one-room', 'eight-year', 'old-growth', 'marginalized', 'forty-three', 'co-host', 'campaigning', 'ten-year-old', 'drug-related', 'khakis', 'test-retest', 'gendered', 'aghast', 'hour-long', 'extra-virgin', 'ballgame', 'medium-low', 'low-wage', 'forty-four', 'Likert-type', 'school-age', 'politicization', 'parent-child', 'four-hour', 'molester', 'quarter-century', 'eighth-grade', 'second-year', 'Sandinista', 'sixth-grade', 'thirty-nine', 'forty-seven', 'three-week', 'fifth-grade', 'third-largest', 'gray-haired', 'uncharacteristically', 'ten-year', 'stained-glass', 'co-found', 'Spanish-language', 'sixteenth-century', 'eighty-five', 'big-screen', 'three-bedroom', 'long-term-care', 'one-party', 'age-related', 'old-school', 'six-week', 'video-game', 'first-quarter', 'three-part', 'second-round', 'chain-link', 'fifty-two', 'early-morning', 'Euro-American', 'black-owned', 'forty-six', 'hideout', 'cutthroat', 'no-fly', 'above-average', 'anti-drug', 'state-sponsored', 'lightbulb', 'fourth-grade', 'long-held', 'free-trade', 'public-relations', 'one-bedroom', 'mental-health', 'half-million', 'reflexively', 'deep-water', 'first-place', 'evidence-based', 'seven-day', 'science-fiction']

    nopos = []
    pos_2 = []
    # print('dict_reader=>', dict_reader[0])
    i = 0
    for w in dict_reader:
        # if w['Word'] not in check_words:
        #     continue
        # info = iciba.get_word_means(w['Word'])
        # print('w =>', w['Word'])
        # print('info =>', info)
        # pos = ''
        # try:
        #     if len(info['baesInfo']['symbols']) < 1:
        #         nopos.append(w['Word'])
        #         continue
        # except:
        #     nopos.append(w['Word'])
            # continue

        # if len(info['baesInfo']['symbols']) > 1:
        #     pos_2.append(w['Word'])
        #
        # if info or info['baesInfo']['symbols'][0]['parts']:
        #
        #     for symbol in info['baesInfo']['symbols']:
        #
        #         parts = symbol['parts']
        #         print('parts =>', parts)
        #         for p in parts:
        #             pos += p['part'] + ' '

        # print('pos ==>', pos)
        data = {
            'word': w['Word'],
            # 'pos': pos,
            'rank': int(w['Rank']),
            # 'collins': w['Collins'],
            # 'definition': w['Definition'],
            # 'tag': w['Tag'],
            # 'PoS': w['PoS'],
            # 'pos': w['Definition'].split('. ')[0],
            # 'createdAt': datetime.datetime.now(),
            'updatedAt': datetime.datetime.now()
        }
        mongo.update(mongo.vocabulary, {'word': data['word']}, data)
        i += 1
        print('i=>', i)
        # info['word'] = w['Word']
        # mongo.update(mongo.iciba, {'word': info['word']}, info)

    # print('nopos=>', nopos)
    # print('pos_2=>', pos_2)
    # info = iciba.get_word_means('desk')
    # print('info=>', info)

    # pos = ''
    # if info or info['baesInfo']['symbols']['parts']:
    #     parts = info['baesInfo']['symbols'][0]['parts']
    #     print('parts =>', parts)
    #     for p in parts:
    #         pos += p['part'] + ' '
    #
    #     print('pos ==>', pos)

if __name__ == '__main__':
    main()