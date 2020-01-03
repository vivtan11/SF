import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span

#use nltk to split text into sentences
import nltk.data
from nltk.tokenize import sent_tokenize


nlp = spacy.load('en_core_web_sm')

def main() :
    with open("wiki-abstracts-only-small.txt", "r") as fin:
        for line in fin:
            # split into sentences
            lines = sent_tokenize(line)
			      # process each sentence
            for sentence in lines:
				        # get the subject and object
                entity_pair = get_entities(sentence)
				        # get the relationship
                reln = get_relation(sentence)
				        # if all three are valid, print result
                if (entity_pair[0]) and (reln) and (entity_pair[1]):
                   print('[' + entity_pair[0] + '] : [' + reln + '] : [' + entity_pair[1] + ']')



# find the root verb, append any prepositions or agent words
def get_relation(sent):

  # run nlp 
  doc = nlp(sent)

  # Matcher class object
  matcher = Matcher(nlp.vocab)

  #define the pattern
  pattern = [{'DEP':'ROOT'},
            {'DEP':'prep','OP':"?"},
            {'DEP':'agent','OP':"?"},
            {'POS':'ADJ','OP':"?"}]

  matcher.add("matching_1", None, pattern)

  matches = matcher(doc)
  k = len(matches) - 1

  span = doc[matches[k][1]:matches[k][2]]

  return(span.text)



# get subject and object; add compound words and modifiers that preceed them
def get_entities(sent):
    subj = ""
    # dobj (direct obj) is preferred; if missing, using pobj (predicate obj)
    dobj = ""
    pobj = ""
    prefix = ""

    for tok in nlp(sent):
        # if compound word or modifier, build the prefix
        if (tok.dep_ == "compound") or (tok.dep_.endswith("mod")):
            # build the prefix
            if (prefix == ""):
                prefix = tok.text
            else:
                prefix = prefix + " " + tok.text

        # if subject, append any prefix to it
        elif (tok.dep_.find("subj") != -1):
            if (prefix == ""):
                subj = tok.text
            else:
                subj = prefix + " "+ tok.text
            prefix = ""

        # if object, append any prefix to it
        elif (tok.dep_.find("dobj") != -1):
            if (prefix == ""):
                dobj = tok.text
            else:
                dobj = prefix + " "+ tok.text
            prefix = ""

        elif (tok.dep_.find("pobj") != -1):
            # there can be multiple
            if (prefix == ""):
                pobj = tok.text
            else:
                pobj = prefix + " "+ tok.text
            prefix = ""

    obj = dobj
    if (obj == ""):
        obj = pobj
    return [subj.strip(), obj.strip()]

# for debugging
def print_for_debug(sentence):
    doc = nlp(sentence)
    for tok in doc:
        print(tok.text, "...", tok.dep_)


main()
