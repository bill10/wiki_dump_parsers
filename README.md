# Wikipedia Dump Parsers

A variety of parsers for extracting information from Wikipedia dump files. The parsers are used in the my paper 

Citation to be added.

## Dependencies
* mwxml
* Each parser has its own dependencies (See details below).

## Usage
    python main.py dump_file title_file namespace
* dump_file: the 7z dump file, which is normally downloaded from Wikipedia's dump site (e.g., https://dumps.wikimedia.org/enwiki/20190301/enwiki-20190201-pages-meta-history1.xml-p10p2066.7z). The file should be unzipped but the input 7z should still has the .7z extension.
* title_file: a text file containing the titles of the pages to be processed. One title per line. Words in a title are separated by space; case insensitive. An example file (all_titles.txt) is included.
* namespace: namespace of the pages to be processed - TALK or MAIN (i.e., article).
* main.py is a template. The actual parsing is done by various parsers. The appropriate parser should be imported into the script first (line 7). Only one parser is allowed each time.
* Output: a TSV file. The content of the file will be different for different parsers.

### Parsers
* attack_parser.py: extract page title, time, editor name, attack score, and aggressive score for each edit. It uses [wiki-detox](https://github.com/ewulczyn/wiki-detox) to assess the aggressive and attack scores. It relies on revision_differ.py and diff_match_patch.py (both are included) from [wikihadoop](https://github.com/whym/wikihadoop) to extract the difference between two snapshots of a page. Each line of the output corresponds to an edit. 
* edit_info_parser.py: extract page title, time, editor name, and current page length for each edit. Each line of the output  corresponds to an edit.
* policy_parser.py: extract page title, policy name, and number of mentions of the policy for each page. It uses a pre-compiled list of Wikipedia policies and guidelines (wiki_policies.tsv). Each line of the output corresponds to a (title, policy) combination.
* quality_parser.py: assess the quality of each page. It uses [wikiclass](https://github.com/wikimedia/articlequality) and [revscoring](https://github.com/wikimedia/revscoring) to calculate the quality of each page. Each line of the output corresponds to page. 
* tf_parser.py: calculate word frequncies for each page. It relies on the stopword dictionary from NLTK to remove stopwords. Each line of the output corresponds to a (page, word) combination.
* word_radius_parser: extract page title, number of words, and radius of each page. It relies on the stopword dictionary from NLTK to remove stopwords. It uses the word embeddings from [fastText](https://fasttext.cc/docs/en/pretrained-vectors.html) to represent words as  numeric vectors; the radius of a page is then defined as the median distance from the words on the page to their centroid. Each line of the output corresponds to a page.  

## Parallel Processing
A complete snapshot of Wikipedia normally consists of hundreds of dumps, which can be processed in parallel to speed up the computation. A few scripts are included for computing clusters with SLURM.
* download.sh: download all the 7z dump files listed in a text file, unzip them, and remove the compressed files. An example is shown below where dumps_20161201.txt is a file contaning the names for all the 7z dumps for the snapshot on 20180401. One filen per line.

    ```
    ./download.sh dumps_20161201.txt
    ```
* run_me.sh: submit the dump files and the parser to SLURM for parsing in parallel. It will submit the SLURM submission script (submit.sh) for each dump file in parallel. One can modify the submit.sh script for appropriate submission parameters. The output of this script (if ran successfully on the SLURM cluster) will be a lot of TSV files with each file corresponding to the parsing result of a dump file. Usage:

    ```
    ./run_me.sh dumps_file title_file namespace 
    ```
** dumps_file: a text file containing the names of all the 7z dump file to be parsed. One file per line. A example file is included (dumps_20161201.txt). The 7z dumps should be unzipped. One can run the download.sh script on this list first to download and unzip and data.
** title_file: a text file containing the titles of the pages to be processed. One title per line. Words in a title are separated by space; case insensitive. An example file (all_titles.txt) is included.
** namespace: namespace of the pages to be processed - TALK or MAIN (i.e., article).


