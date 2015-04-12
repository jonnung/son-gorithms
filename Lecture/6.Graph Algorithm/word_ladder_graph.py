# -*- coding: utf8 -*-

from lib.pythonds.graphs import Graph


def build_graph(word_file):
    d = {}
    g = Graph()

    wfo = open(word_file, 'r')

    # 한글자만 다른 단어 버켓을 만듬
    for line in wfo:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

    # 같은 버켓안에 단어들로 정점과 간선을 추가함
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g
