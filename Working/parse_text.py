import re
import sys

nodes = []
eWords = []
links = []
eID = 1

with open(r'C:\Users\denjn\Source\Repos\TextStudy\Working\rom1.txt') as f:
    lines = f.readlines()

btext = lines[0]
book_chapter = re.findall(r'\[([1-3A-Za-z]* [0-9]{1,3}:)[0-9]{1,3}\]', btext)[0] # finds full ref, e.g., [Ro 1:1]

# TODO: fill in book_chapter for hard-coding below
btext = re.sub(r'\[([0-9])\]', r'|[' + book_chapter + r'\1]', btext) # adds split char and full ref to verse
verses = btext.split('|')

# ***** begin loop through verses *****
for verse in verses:
    ref = re.findall(r'\[([1-3A-Za-z]* [0-9]{1,3}:[0-9]{1,3})\]', verse)[0] 

    words = re.findall(r'([A-Za-z]*)(g[0-9]{1,4})', verse)

    for word in words:
    
        eWord = word[0]
        gID = word[1]

        # is the word already in the list?
        try:
            eNode = ''
            eNode = next(item for item in nodes if item["wrd"] == eWord)
        except StopIteration:
            pass

        if eNode != '':
            eNode['cnt'] += 1
            if eNode['refs'].find(ref) == -1: 
                eNode['refs'] += "; " + ref
            eID = eNode['wrdID']
        else:
            eWords.append(eWord)
            eID = len(eWords)
            nodes.append({ "wrdID": eID, "wrd": eWord, "rt": "", "cnt": 1, "refs": ref })

        try:
            gNode = ''
            gNode = next(item for item in nodes if item["wrdID"] == gID)
        except StopIteration:
            pass

        if gNode != '':
            gNode['cnt'] += 1
            if gNode['refs'].find(ref) == -1: 
                gNode['refs'] += "; " + ref
        else:
            nodes.append({ "wrdID": gID, "wrd": "", "rt": "", "cnt": 1, "refs": ref })


        try:
            link = '' 
            link = next(item for item in links if (item["source"] == gID and item["target"] == eID))
        except StopIteration:
            pass

        if link != '':
            link['cnt'] += 1
        else:
            links.append({ "linkID": len(links), "source": gID, "target": eID, "cnt": 1 })

var = 1