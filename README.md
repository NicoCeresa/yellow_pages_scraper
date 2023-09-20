# Yellow Pages Restaurant Scraper

**https://www.yellowpages.com/oakland-ca/restaurants**

## How to run
- Download files
- Locate `scraper_v2.py`
- Run that file

## Outputs
- The script will output 2 files: `pre_cleaned_output.csv` and `cleaned.csv`
- Pretty clear what means what
- The ones I have here are simply samples and yours will be much longer as I only went through the first 3 pages here out of 100 total

## Description of each file

**scraper_v1.py**
- My first attempt at a scraper
- Very unorganized but I keep it in to show alternate ideas to do something like this

**scraper_v2.py**
- My working scraper
- Prettier and more functional than scraper_v1 probably will ever be

**test1.py**
- I am going to connect the output to a relational database and query the data so this will connect to one
- Currently working with DBeaver

**transform.ipynb**
- Made sure I knew exactly how to transform to my liking before making it into an actual script
- Able to view step by step easily

**transform.py**
- Just the notebook in script form
- outputs the cleaned csv
