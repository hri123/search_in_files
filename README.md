# search_in_files

## Semantic Search / Fuzzy Search

Fuzzy String Matching in Python:
https://github.com/seatgeek/fuzzywuzzy

How Fuzzy Wuzzy Works:
http://chairnerd.seatgeek.com/fuzzywuzzy-fuzzy-string-matching-in-python/
https://dirkmjk.nl/nl/node/397
https://marcobonzanini.com/2015/02/25/fuzzy-string-matching-in-python/

node library:
https://github.com/nol13/fuzzball.js
https://www.npmjs.com/package/fuzzball
https://github.com/NaturalNode/natural/tree/master/lib/natural/tokenizers

My Question in StackOverflow:
https://stackoverflow.com/questions/47605377/semantic-search-retrieve-sentences-from-a-bunch-of-text-files-that-closely-mat
He solved using LCS (Longest common subsequence) and autocorrect library, but I feel the fuzzywuzzy library is better to try

ElasticSearch:
https://www.youtube.com/watch?v=uK_dFzg63MU
https://www.youtube.com/watch?v=9UEymp254kA

What is semantic search:
https://www.r-bloggers.com/fuzzy-string-matching-a-survival-skill-to-tackle-unstructured-information/
http://docs.ipstreet.com/docs/concept-search

Similar Library:
FuzzySet: https://stackoverflow.com/questions/10383044/fuzzy-string-comparison/38316398#38316398

NLTK and Wordnet Usage in Python:
https://likegeeks.com/nlp-tutorial-using-python-nltk/

Linux Utility:
https://github.com/laurikari/tre/
https://stackoverflow.com/questions/9439121/fuzzy-file-search-in-linux-console/19805303#19805303

### Convert to a executable

http://www.mxm.dk/2008/02/python-eggs-simple-introduction.html

### Split into sentences yourself

https://stackoverflow.com/questions/4576077/python-split-text-on-sentences/31505798#31505798

## finds - line with moby and sauce and tartar in ANY ORDER

- ag with PCRE (Perl Compatible Regular Expression)
ag '(?=.*?moby)(?=.*?sauce)(?=.*?tartar)^.*$' /Users/hrishikesh/H/HP/Dropbox/Kaizen/ng-rb/RB-files/attitude/rb/

- AWK
awk 'tolower($0) ~ /dick/ && tolower($0) ~ /moby/ && tolower($0) ~ /tartar/' /Users/hrishikesh/H/HP/Dropbox/Kaizen/ng-rb/RB-files/attitude/rb/**/*.*

using m.*y instead of moby
awk 'tolower($0) ~ /dick/ && tolower($0) ~ /m.*y/ && tolower($0) ~ /tartar/' /Users/hrishikesh/H/HP/Dropbox/Kaizen/ng-rb/RB-files/attitude/rb/**/*.*

- grep

(use ag for now)