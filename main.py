from utils import *


#transform_files()

files_txt = [os.path.join("data/work",file) for file in os.listdir("data/work") if file.endswith(".txt")]

### **** *texte_00001VRT15 *numero_00001 *genre_TV *media_VRT *date_050415 *jour_05 *mois_avril *annee_2015

for lang in ["nl", "fr"]:
    process_lang(lang)