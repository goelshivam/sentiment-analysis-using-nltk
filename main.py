import string
from collections import Counter
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
text=open('read.txt',encoding='utf-8').read()
lower_case=text.lower() #converting all words in lower case
#making text free of all punctuations.
cleaned_text=lower_case.translate(str.maketrans('','',string.punctuation))
#storing all words in a string- tokenization
tokenized_words=word_tokenize(cleaned_text,"english")
#stop words which does not add any meaning to our paragraphs
from nltk.corpus import stopwords
#finding words from cleaned_text and removing stop words from it
final_words=[]
for words in tokenized_words:
    if words  not in stopwords.words('english'):
        final_words.append(words)


#now coming to our emotions.txt
# NLP Emotion Algorithm
# 1) Check if the word in the final word list is also present in emotion.txt
#  - open the emotion file
#  - Loop through each line and clear it
#  - Extract the word and emotion using split

# 2) If word is present -> Add the emotion to emotion_list
# 3) Finally count each emotion in the emotion list
emotion_list=[]
with open('emotions.txt','r') as file:
    for line in file:
        clear_line=line.replace('\n','').replace(',','').replace("'",'').strip() #clearing all the mess in emotion.txt
        words,emotion=clear_line.split(':')
    
        if words in final_words:
            emotion_list.append(emotion)     


w=Counter(emotion_list)
print(w)
def sentiment_analyze(sentiment_text):
    score= SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg=score['neg']
    pos=score['pos']
    if neg>pos:
        print("negative sentiment")
    elif pos>neg:
        print("positive sentiment")
    else:
        print("neutral sewntiment")

sentiment_analyze(cleaned_text)

fig , ax1=plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()