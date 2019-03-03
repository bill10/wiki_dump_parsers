# Wikipedia Dump Parsers

A variety of parsers for extracting information from Wikipedia dump files. 

## Dependencies
* mwxml

## Usage
    python main.py filename titles namespace
* filename: the 7z dump file, which is normally downloaded from Wikipedia's dump site (e.g., https://dumps.wikimedia.org/enwiki/20190301/enwiki-20190201-pages-meta-history1.xml-p10p2066.7z). The file should be unzipped but its name still has .7z extension.
* titles: a text file containing the titles of the pages to be processed. One title per line. Words in a title are separated by space; case insensitive.
* namespace: namespace of the pages to be processed - TALK or MAIN (i.e., article)
