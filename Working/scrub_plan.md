

# Data Preperation For Connections

## Nodes
{ "wrdID": "g1401", "wrd": "???????", "rt": "???????", "cnt": 1, "refs": "Ro 1:1" },
{ "wrdID": "e1", "wrd": "servant", "rt": "servant", "cnt": 1, "refs": "Ro 1:1" }

* wrdID. e####, g####, h####
* wrd. word
* rt. lematized word (e.g., running --> run)
* cnt. count of times it appears 
* refs. semi-colon delimited reference list

## Links
{ "linkID": "l1", "source": "g1401", "target": "e1", "cnt": "1" }

* linkID
* source
* target
* cnt. Number of times this connection occurs

## Process
1. Break into verses: split at r'\[[0-9]*\]'
2. Find first occurance of r'\[([1-3A-Za-z]* [0-9]{1,3}:[0-9]{1,3})\] ([A-Za-z]*)(g[0-9]{1,4})' --> $1 = ref; $2 = English; $3 = Greek
3. Nodes: Search for existing [Greek] wrdID [English] wrd 
   a. If found: then cnt++, new ref
   b. If not: write
4. Links: Search for existing source / target
   a. If found: then cnt++
   b. If not: write




# Example
[Ro 1:1] Paulg3972, a servantg1401 of Jesusg2424 Christg5547, calledg2822 to be an apostleg652, separatedg873 untog1519 the gospelg2098 of Godg2316, [2] (Whichg3739 he had promised aforeg4279 byg1223 hisg846 prophetsg4396 ing1722 the holyg40 scripturesg1124,) 