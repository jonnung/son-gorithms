#-*- coding: utf-8 -*-

from lib.pythonds.graphs import Graph


def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile,'r')
    
    # 한글자만 다른 단어의 버켓을 만듬  
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

    # 정점들을 추가하고, 같은 버켓안에 단어들마다 간선을 만듬  
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g


