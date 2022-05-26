#!/usr/bin/bash

# scrapy crawl etymologies -a words_file=words.txt -o etymologies.csv
scrapy crawl etymologies -a words_file=words.txt -o etymologies.json
