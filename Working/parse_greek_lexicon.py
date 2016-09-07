import regex as re
import json
import xml.etree.ElementTree as ET

tree = ET.parse(r'C:\Users\denjn\Source\Repos\TextStudy\Working\greek_lexicon.xml')
root = tree.getroot()

gWords = []

for child in root[1]: 
  
  id = "g" + int(root[1][0].attrib['strongs'])
   
  gWords.append({ "id": id, "greek": "", "def": "" })
  print (child.tag, child.attrib)


e = 1

