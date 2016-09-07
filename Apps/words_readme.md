# Words Explorer

## Start
* all English words show on entry
* size indicates usage count (logarithmic?)

## Use Cases

### Word-Centered
* user clicks word
  * other words disappear
  * related Greek/Hebrew words appear (size = frequency)
  * panel: word, links to verse refs

### Passage-Centered
user enters passage
* Start here
  * TODO: Pick random passage
* Greek/Hebrew words appear (single size, color = language)
* words not referencing that passage disappear
* links between words
  * TODO: Words Parser -> ignore capitalization when checking for previous
  * TODO: Words -> add Greek word to words.json, Greek definitions to full_text.json
* panel: passage ref, verse quote in several versions, highlight unique words
  * TODO: Color words same as circle color

### Word-In-Passage-Centered
* user clicks word from passage-centered or reference from word-centered
  * word in center
  * Greek/Hebrew word appears
  * other English words that are translated from that word show up (size = frequency, color = language)
  * panel: verse, bolded word, Strong's definition


## Input Options
1. Verse entry
2. Click on node
3. Back button?

