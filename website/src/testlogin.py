'''
    Run this file to test the code on console
    or run the gui file
'''

import re

import nltk.corpus
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from website.src.query import to_postfix
from website.src.indexer import InvertedIndex
from website.src.indexer import PositionalInvertedIndex

index = {}
pos_index = {}


def load_index():

    # Load inverted index from disk.

    global index
    global pos_index
    index = InvertedIndex()
    index.read_index()
    pos_index = PositionalInvertedIndex()
    pos_index.read_index()


def run_proximity_search(query):

    # This method runs proximity search to satisfy proximity queries.
    # Returns the list of documents ids.

    l1 = pos_index.get_postings_list(query[0])
    l2 = pos_index.get_postings_list(query[1])
    k = int(query[2]) + 1
    print(l1,l2)
    return pos_index.positional_intersect(l1, l2, k)

def run_boolean_search(postfix):

    # This method runs simple boolean search to satisfy boolean queries.
    # Takes a postfix expression and evaluates on the basis of standard precedence
    # Returns the list of documents ids.

    stack = []
    i = 0
    while i < len(postfix):
        if postfix[i] not in ['and', 'or', 'not']:
            stack.append(index.get_postings_list(postfix[i]))

        elif postfix[i] == 'not':
            stack.append(postfix[i])

        else:
            query_segment = []
            while len(query_segment) < 2:
                w1 = stack.pop()
                if w1 == "not":
                    query_segment.append((stack.pop(), w1))
                else:
                    query_segment.append((w1, ""))
            query_segment.append(postfix[i])

            # evaluating the query segment

            p1 = query_segment[0][0]
            p2 = query_segment[1][0]

            if query_segment[0][1] == "not":
                p1 = index.invert(p1)
            if query_segment[1][1] == "not":
                p2 = index.invert(p2)

            if query_segment[2] == "and":
                res = index.intersection(p1, p2)
            else:
                res = index.union(p1, p2)

            stack.append(res)

        i += 1
    return stack[0]


def process_query(query):

    stop_list = stopwords.words('indonesian')
    factory = StemmerFactory()
    ps = factory.create_stemmer()
    query = query.split()
    clean_tokens = [word for word in query if word not in stop_list]
    # print(clean_tokens)
    for (i,q) in enumerate(clean_tokens):
        q = q.replace('-', '')
        q = re.sub(r'[^a-z1-9/]+', '', q.lower())
        query[i] = ps.stem(q)

    if query[-1].startswith('/'):
        query[-1] = query[-1][1:]
        print('aaa',query)
        return run_proximity_search(query)
    else:
        print('bbb',query)
        postfix = to_postfix(query)
        # print('ccc',postfix)
        return run_boolean_search(postfix)

def runn2(y):
    load_index()
    result = process_query(y)
    return result




if __name__ == "__main__":

    # Test code from console

    print("loading....")
    load_index()
    query = input("Masukkan query: ")
    result = process_query(query)
    print("Hasil:", result)
