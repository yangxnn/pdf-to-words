'''
Author       : yangxing(yangxnn@outlook.com)
Date         : 2022-05-01 17:53:32
LastEditors  : yangxing(yangxnn@outlook.com)
LastEditTime : 2022-05-04 18:55:44
FilePath     : /pdf-to-words/main.py
Description  : 

Copyright (c) 2022 by yangxnn@outlook.com, All Rights Reserved. 
'''

import sys
from functools import reduce
from collections import OrderedDict
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator, TextConverter
from pdfminer.layout import LAParams, LTTextBox
from sympy import Order

INVALID_CHAR = {
    '(', ')', '+', '-', '=', '_', '!', '@', '#', '$', '%', '^', '&', '*', '~', '`', '{', '[', '}', ']', '|', '\\', ';', '"', '\'', ':', ',', '<', '>', '.', '?', '/', '\n', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
}

def replace_words(words):
    words = map(lambda x: x.strip(), words)
    words = map(lambda x: x.lower(), words)
    return words

def filter_words(words, filter_len_thre=4):
    """filter according to whether len of word less than thre and whether contains chars of INVALID_CHAR

    Args:
        words (list): 
        filter_len_thre (int, optional): _description_. Defaults to 4.
    """
    def is_need(word):
        if len(word) < filter_len_thre or len(set(word) & INVALID_CHAR) > 0:
            return False
        return True
    
    words = filter(lambda x: is_need(x), words)
    return words

def reduce_words(words):
    """drop duplicates and sort

    Args:
        words (_type_): _description_

    Returns:
        _type_: _description_
    """
    word2cnt = {}
    for word in iter(words):
        if word not in word2cnt:
            word2cnt[word] = 0
        word2cnt[word] += 1
    words = sorted(word2cnt.items(), key=lambda x: x[1], reverse=True)
    return words

def pdf_to_words(fname):
    words = []
    rsrcmgr = PDFResourceManager(caching=True)
    device = PDFPageAggregator(rsrcmgr=rsrcmgr, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr=rsrcmgr, device=device)
    with open(fname, 'rb') as f:
        for page in PDFPage.get_pages(f, caching=True):
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                if isinstance(x, LTTextBox):
                    words.extend(x.get_text().split(' '))
    return words

def parse_pdf(fname):
    words = pdf_to_words(fname)
    words = replace_words(words)
    words = filter_words(words)
    words = reduce_words(words)
    print(words)

if __name__ == '__main__':
    assert len(sys.argv) == 2
    fname = sys.argv[1]
    parse_pdf(fname)