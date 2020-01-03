import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.sem import relextract
import re
import pprint


def main() :
    pattern = 'NP: {<DT>?<JJ>*<NN>}'

    with open("wiki-abstracts-only.txt", "r") as fin:
        for line in fin:
            sent = nltk.word_tokenize(line)
            #augment with POS tags
            sent = nltk.pos_tag(sent)
            cp = nltk.RegexpParser(pattern)
            cs = cp.parse(sent)
            ne_tree = nltk.ne_chunk(pos_tag(word_tokenize(line)))
            pairs = relextract.tree2semi_rel(ne_tree)
            reldicts = relextract.semi_rel2reldict(pairs)
            for r in reldicts:
                # remove POS tags
                sub = r['subjtext'].replace('/NNPS','').replace('/NNP','').replace('/JJ','');
                obj = r['objtext'].replace('/NNPS','').replace('/NNP','');
                vb = r['filler'].replace('/NNS','').replace('/NNP','').replace('/NN','').replace('/CC','').\
                replace('/PRP$','').replace('/DT','').replace('/CD','').replace('/JJ','').replace('/PRP','').\
                replace('/WP','').replace('/IN',"").replace('/VBD','').replace('/VBN','');
				        # print result
                print('[' + sub + '] : [' + vb + '] : [' + obj + ']')

main()
