# import json
#
#
# f = open('positional_index.json')
# data = json.load(f)
#
# l=0
# total=0
#
# for i in data['najis']:
#     l = len(i[1])
#     total = total + l
#     print(total)
#
#     # l = len(data['definisi'][0][1])
# print(l)
#
# # print(l)
#
# from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
# word = "mensucikan"
#
# factory = StemmerFactory()
# ps = factory.create_stemmer()
# w = ps.stem(word)
# print(w)

# filename = 'data_txt/1.txt'
# f = open(filename, "r", encoding="UTF8").readlines()
# for line in f:
#     if "hadats" in line:
#         print(line)

# query = 'shalat kusuf'
# queries = list(query.split())
# print (queries)
#
# with open('data_txt/1.txt', 'r+') as f:
#    for line in f:
#        for i in range(len(queries)):
#            if queries[i] in line:
#                a = line.split("\n")
#                a[1] = a[1].replace('', '...')
#                print(a)
#                break
#            else:
#                continue
#            i+=1

import nltk

nltk.download('popular')
