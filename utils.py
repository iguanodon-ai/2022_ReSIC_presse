import os
from docx import Document
import shutil
import sys

medias_lang = { ## ordre de valériane
    "nl": [
        "DESTANDAARD", 
        "HETLAATSTENIEUWS",
        "VRT",
        "VTM"
    ],
    "fr": [
        "LESOIR",
        "LADH",
        "RTBF",
        "RTL"
    ]
}

genre = {
    "DESTANDAARD": "JOURNAL",
    "HETLAATSTENIEUWS": "JOURNAL",
    "VTM": "TV",
    "VRT": "TV",
    "LADH": "JOURNAL",
    "LESOIR": "JOURNAL",
    "RTBF": "TV",
    "RTL": "TV",
        }


#### DOCX TO TXT
def getText_docx(file):
    print(file)
    doc = Document(file)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def transform_files():
    files = [os.path.join("data/raw",file) for file in os.listdir("data/raw") if file.endswith(".docx")]
    for file in files:
        text = getText_docx(file)
        with open(file.replace("raw", "work").replace(".docx", ".txt"), "w") as f_out:
            f_out.write(text)

    files_txt = [os.path.join("data/raw",file) for file in os.listdir("data/raw") if file.endswith(".txt")]
    for file in files_txt:
        print(file)
        shutil.copy(file, file.replace("raw", "work"))

### DATE FINDER

def is_it_a_date(text, file):
    # Date is 10 characters, 8 ints and 2 separators
    # should have probably done a regex instead...
    # We return either FALSE or (True,reordered date)
    if file not in ["data/work/RTL.txt", "data/work/RTBF.txt"]:
        if len(text) == 10:
            if len(text.replace("/","").replace("-",'').replace(".","")) == 8: 
                try:
                    #print(text[-4:])
                    int(text[-4:])
                    #print(text.replace("-",'/').replace(".","/"))
                    
                    return True, text.replace("-",'/').replace(".","/")
                except ValueError:
                    try:
                        int(text[:4])
                        #print(text[:4])
                        
                        for sep in ["/", "-", "."]:
                            if sep in text:
                                tlist = text.split(sep)
                                tlist.reverse()
                                new_text = "/".join(tlist)
                                #print(text, new_text)
                                return True , new_text
                    except ValueError:
                        return False
        return False

    else: # special case where dates lack "20" in eg "2015"
        
        if len(text.replace(".","")) == 6:
            
            try:
                int(text[-2:])
                tlist = text.split(".")
                tlist[2] = "20"+tlist[2]  
                #print("/".join(tlist))
                return True, "/".join(tlist)
            except ValueError:
                #print(file, text)
                return False
        return False

def file_to_dates(file):
    """
    Gets a file, returns a {date:[text(s)]} dictionary
    NB: some dates have several texts
    """

    articles = {}
    with open(file, encoding="utf-8") as f:
        seen = False
        for line in f:
            line = line.rstrip()
            if is_it_a_date(line, file) == False:
                if seen == True:  # we ignore the first text without a date
                    articles[date].append(line)

            else: # this is a date
                seen = True
                date = is_it_a_date(line, file)[1]
                #print(date)
                if date not in articles.keys():
                    articles[date] = []
                else: ## This date already has an article
                     articles[date].append("NEW_ARTICLE")
    return articles

def split_at_values(liste, sep):
    """
    ## prend une liste et un séparateur
    ## retourne n sublistes basées sur le séparateur
    """
    indices = [i for i, x in enumerate(liste) if x == sep]
    returnlist = []
    for start, end in zip([0, *indices], [*indices, len(liste)]):
        returnlist.append(liste[start:end+1])
    return returnlist


def get_from_lang(lang):
    files = [os.path.join("data/work", media+".txt") for media in medias_lang[lang]]
    return files

def process_lang(lang):
    media_texts = {}
    for file in get_from_lang(lang):
        media = file.replace("data/work/", "").replace(".txt", "")
        media_texts[media] = file_to_dates(file)
    return media_texts


def process_files(lang):
    f = open(os.path.join("data/final", lang+".txt"), "w")
    media_texts = process_lang(lang)
    counter = 0
    for media_name, v in media_texts.items():
        print(f"### Dealing with {media_name}")
        for date in v:
            texts = v[date]
            jour = date[:2]
            mois = date[3:5]
            année = date[-4:]
            if "NEW_ARTICLE" in texts:
                texts = split_at_values(texts, 'NEW_ARTICLE')
                for article in texts:
                    for i, item in enumerate(article):
                        if item == "NEW_ARTICLE":
                            article.pop(i)
                    counter += 1
                    to_write = f'**** *texte_{counter}{media_name}{date[-2:]} *numero_{counter} *genre_{genre[media_name]} *media_{media_name} *date_{date} *jour_{jour} *mois_{mois} *année_{année}\n'
                    texts_string = "\n".join(article)
                    f.write(to_write+texts_string+"\n\n")

            else:
                counter += 1
                to_write = f'**** *texte_{counter}{media_name}{date[-2:]} *numero_{counter} *genre_{genre[media_name]} *media_{media_name} *date_{date} *jour_{jour} *mois_{mois} *année_{année}\n'
                texts_string = "\n".join(texts)
                f.write(to_write+texts_string+"\n\n")

    f.close()