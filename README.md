<a href="https://iguanodon.ai"><img src="img/iguanodon.ai.png" width="125" height="125" align="right" /></a>

# Nettoyage et mise en forme de corpus 

## Description

Ce repository contient le code créé dans le cadre d'une mission de nettoyage et formattage d'un corpus de retranscriptions de presse (TV et presse écrite) en Belgique francophone et néerlandophone. 


## But

Transformer plusieurs fichiers (`.txt`, `.docx`) de médias différents (VRT, RTBF, RTL-TVI, VTM, De Standaard, Het Laatste Nieuws, Le Soir, La Dernière Heure) contenant des retranscriptions d'articles en deux fichiers distincts : l'un pour le français, l'autre pour le néerlandais. 

Ces fichiers doivent contenir différentes métadonnées par article : le genre (TV ou journal), la date (en différentes granularités), le média, et un identifiant unique. Ces métadonnées doivent pouvoir être lues par les logiciels [Hyperbase](http://hyperbase.unice.fr/hyperbase/) et [TXM](https://txm.gitpages.huma-num.fr/textometrie/Pr%C3%A9sentation/). 

## Étapes d'utilisation du code dans ce repository

1. La fonction `transform_files()` va transformer tous les fichiers `docx` se trouvant dans `data/raw` en format texte et va les déplacer dans `data/work`, les fichiers textes existants seront également copiés dans ce nouveau dossier
2. La fonction `process_lang(lang)` va créer `data/final/{lang}.txt` qui contiendra tous les articles de presse pour tous les médias de langue `lang`


## Licence et contact

Ce code a été écrit par Simon Hengchen ([https://iguanodon.ai](https://iguanodon.ai)) à la commande de Valériane Mistiaen ([Université libre de Bruxelles](https://www.ulb.be/fr/valeriane-mistiaen), [Vrije Universiteit Brussel](https://researchportal.vub.be/en/persons/val%C3%A9riane-mistiaen)). Ce code est mis à disposition du public <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">sous licence permissive CC BY-SA 4.0</a>. 


 <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a>
