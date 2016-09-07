import regex as re
import sys
import json

nodes = []
eWords = []
links = []
full_text = []
eID = 1
book = "Rom "

# TODO: check out re's -- maybe precompiles -- what's that do to my re statements?
# TODO: whole book in 1 text file -- need to append book name to beginning of chapter starts [2:1]
# TODO: save results to json
# https://www.blueletterbible.org/lang/lexicon/lexicon.cfm?Strongs=G3972&t=KJV&ss=1

with open(r'C:\Users\denjn\Source\Repos\TextStudy\Working\rom.txt') as f:
    lines = f.readlines()

bible_text = lines[0]

# loop through chapters, adding in the chapter & : before each verse number
# then replace the verse references with chapter:verse references
for chapter_number in range(1,17):
    verse_refs = re.findall(r'\[([0-9]{1,3})\].*(?=\[' + str(chapter_number + 1) + ':)', bible_text, overlapped=True)
    for verse_ref in verse_refs:
        bible_text = re.sub(r'\[(' + verse_ref + ')\]', r'[' + str(chapter_number) + r':\1]', bible_text, 1)
        
    
# TODO: fill in book_chapter for hard-coding below
bible_text = re.sub(r'(\[[0-9]{1,3}:[0-9]{1,3}\])', r'|\1', bible_text) # adds split char and full ref to verse
verses = bible_text.split('|')

# ***** begin loop through verses *****
for verse in verses:
    if len(verse) == 0: 
        continue

    ref = book + re.findall(r'\[([0-9]{1,3}:[0-9]{1,3})\]', verse)[0] 
    words = re.findall(r'([A-Za-z]*)(g[0-9]{1,4})', verse)
    text = re.sub(r'\[[0-9]{1,3}:[0-9]{1,3}\]\xa0', '', verse).replace("  ", " ").strip()
    text = re.sub(r'(g[0-9]{1,5})', r' (\1)', text)

    # Bible Text
    full_text.append({ "ref": ref, "text": re.sub('  ', ' ', text) })


    for word in words:
    
        eWord = word[0]
        gID = word[1]

        # English Words
        try: # has this been recorded before?
            eNode = ''
            eNode = next(item for item in nodes if item["word"].lower() == eWord.lower())
        except StopIteration:
            pass

        if eNode != '':  # existing entry
            eNode['cnt'] += 1
            if eNode['refs'].find(ref) == -1: 
                eNode['refs'] += "; " + ref
            eID = eNode['id']
        else: # new entry
            eWords.append(eWord)
            eID = len(eWords)
            nodes.append({ "id": eID, "word": eWord, "lang": "e", "cnt": 1, "refs": ref })
        
        # Greek Words
        try:
            gNode = ''
            gNode = next(item for item in nodes if item["id"] == gID)
        except StopIteration:
            pass

        if gNode != '': #existing entry
            gNode['cnt'] += 1
            if gNode['refs'].find(ref) == -1: 
                gNode['refs'] += "; " + ref
        else: # new entry
            nodes.append({ "id": gID, "word": gID, "lang": "g", "cnt": 1, "refs": ref })

        # Links
        try:
            link = '' 
            link = next(item for item in links if (item["source"] == gID and item["target"] == eID))
        except StopIteration:
            pass

        if link != '': #existing entry
            link['cnt'] += 1
            if link['refs'].find(ref) == -1: 
                link['refs'] += "; " + ref
        else: #new entry
            links.append({ "id": len(links), "source": gID, "target": eID, "cnt": 1, "refs": ref  })


with open(r'C:\Users\denjn\Source\Repos\TextStudy\Working\nodes.json', 'w') as outfile:
    json.dump(nodes, outfile)
with open(r'C:\Users\denjn\Source\Repos\TextStudy\Working\links.json', 'w') as outfile:
    json.dump(links, outfile)
with open(r'C:\Users\denjn\Source\Repos\TextStudy\Working\full_text.json', 'w') as outfile:
    json.dump(full_text, outfile)

