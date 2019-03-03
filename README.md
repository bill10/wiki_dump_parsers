# Wikipedia Dump Parsers

A variety of parsers for extracting information from Wikipedia dump files. 

## Dependencies
* mwxml
* Each parser has its own dependencies

## Usage
    python main.py filename titles namespace
* filename: the 7z dump file, which is normally downloaded from Wikipedia's dump site (e.g., https://dumps.wikimedia.org/enwiki/20190301/enwiki-20190201-pages-meta-history1.xml-p10p2066.7z). The file should be unzipped but its name still has the .7z extension.
* titles: a text file containing the titles of the pages to be processed. One title per line. Words in a title are separated by space; case insensitive.
* namespace: namespace of the pages to be processed - TALK or MAIN (i.e., article).
* main.py is a template. The actual parsing is done by various parsers. The appropriate parser should be imported into the script first (line 7). Only one parser is allowed each time.
* Output: a TSV file. The content of the file will be different for different parsers.

### Parsers
* attack_parser.py: extract the page title, time, editor name, attack score, and aggressive score for each edit. It uses [wiki-detox](https://github.com/ewulczyn/wiki-detox) to assess the aggressive and attack scores. It relies on revision_differ.py from [wikihadoop](https://github.com/whym/wikihadoop) to extract the difference between two snapshots of a page.   
* edit_info_parser.py: extract the page title, time, editor name, and current page length for each edit.
* policy_parser.py: extract the page title, policy name, and number of counts of the policy for each page. It uses a pre-compiled list of Wikipedia policies and guidelines (wiki_policies.tsv). 


