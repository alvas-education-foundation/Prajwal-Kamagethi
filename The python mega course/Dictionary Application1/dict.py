
import difflib
#from difflib import SequenceMatcher
from difflib import get_close_matches
import json 
data = json.load(open("data.json"))
def translate(w):
 w = w.lower()
 if w in data:
  return data[w]
 elif len(get_close_matches(w,data.keys())) > 0:
  in1 = input("Did you mean %s instead? Enter Y if yes, or N if no : " % get_close_matches(w,data.keys())[0]) 
  if in1 == "Y" :
   return data[get_close_matches(w,data.keys())[0]]
  elif in1 == "N" :
   return "The entered word doesn't exist"
  else : 
   return "Check and re enter the word"
 else :
  return "The word does not exist"
word = input("Enter the word to be searched : ")

output = translate(word)
if type(output) == list:
 for i in output:
  print(i)
else:
 print(output)
