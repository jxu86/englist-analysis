import sys
import re
import importlib

importlib.reload(sys)

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

# '''
#  解析pdf 文本，保存到txt文件中
# '''
#
# path = r'./data/Dynamics_of_Limit_Order_Books.pdf'
#
#
# def plot_wordloud(text):
#     wordcloud = WordCloud().generate(text)
#     plt.imshow(wordcloud, interpolation='bilinear')
#     plt.axis("off")


class PdfService(object):
    def __init__(self, path):
        self.path = path  # r'./data/Dynamics_of_Limit_Order_Books.pdf'

    def parse(self):
        words = []
        fp = open(self.path, 'rb')  # 以二进制读模式打开
        # 用文件对象来创建一个pdf文档分析器
        praser = PDFParser(fp)
        # 创建一个PDF文档
        doc = PDFDocument()
        # 连接分析器 与文档对象
        praser.set_document(doc)
        doc.set_parser(praser)

        # 提供初始化密码
        # 如果没有密码 就创建一个空的字符串
        doc.initialize()

        # 检测文档是否提供txt转换，不提供就忽略
        if not doc.is_extractable:
            raise PDFTextExtractionNotAllowed
        else:
            # 创建PDf 资源管理器 来管理共享资源
            rsrcmgr = PDFResourceManager()
            # 创建一个PDF设备对象
            laparams = LAParams()
            device = PDFPageAggregator(rsrcmgr, laparams=laparams)
            # 创建一个PDF解释器对象
            interpreter = PDFPageInterpreter(rsrcmgr, device)

            # 循环遍历列表，每次处理一个page的内容
            for page in doc.get_pages():  # doc.get_pages() 获取page列表
                interpreter.process_page(page)
                # 接受该页面的LTPage对象
                layout = device.get_result()
                # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等 想要获取文本就获得对象的text属性，
                for x in layout:
                    if (isinstance(x, LTTextBoxHorizontal)):
                        #                     with open(r'./pdftest.txt', 'a') as f:
                        results = x.get_text()
                        ret = re.findall('[a-zA-Z][a-zA-Z]+', results)
                        words.extend(ret)
                        #                     print('results=>',ret)
                        #                         print('results=>',results.split(" "))
                        #                         f.write(results + '\n')
        return words






def main():
    path = r'/Volumes/cat/project/python-note-book/data/Dynamics_of_Limit_Order_Books.pdf'
    pdf = PdfService(path)
    words = pdf.parse()
    print(words)


if __name__ == '__main__':
    main()