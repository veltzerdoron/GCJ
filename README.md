# GCJ

Automation scratching and riddle solutions for Google's Code Jam contests from 2010-2018 (where they moved to the online interactive session)

### Prerequisites

python 3 (not using anything (non standard that is))

## Running the old automated go.py tool

running 

python go.py

will give you the following message:

usage: go.py [-h] [-i {Y,N,S}] [-v] ID contest stage problems

this is a standard parsing implementation, running the -h (help) option gives:

positional arguments:
  ID                    Googles URL parameter defining the stage
  contest               Master folder for the stage (usually year)
  stage                 Name of the stage to be run
  problems              List of problems to be solved, defaults to ABC

optional arguments:
  -h, --help            show this help message and exit
  -i {Y,N,S}, --interact {Y,N,S}
                        fully interact ('Y') just submit ('S') or have no
                        interaction ('N') with the site
  -v, --version         show program's version number and exit



it uses faylixes java GCJ automation under the hood which in turn opens firefox for account login

note: this whole process has been deprecated since 2017 and is now only usable for legacy contests

### file conventions

Folders are kept under the format

download/year/stage - other contestants code I learned from

src/year/stage - my code per year (2010-2018) and stage name (qual, firsta, firstb, seconda, etc...)

under each of these folders (say the contest contains an A riddle) there will be files dubbed:

 A.py - code for solving A accepting std input output, etc...
 A-definition-0.in - input defintion
 A-definition-0.example - expected output
 A-input-0.out - A.py's generated output
 A-large/small-0...9-in/out - input and output files for the attempts

 An additional legend file is generated by my scraping GCJ JavaScript which contains the riddle names

Apart from the special go folder which contains the above described automation tool

The go folder under src, also includes a template X.py program that was used as a starting point for all the actual solutions I wrote as well as some other tidbits I maintained including a contest preplist a TODO list and a scraper JavaScript to be used under tampermonkey.

### tamper monkey script

Installation is quite easy but once installed a button will appear once you open the contest page, pressing seth button will download all input/output files 

### codin

PEP 8 bug knock yourself out

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used (Faylixe, that means you)
* Inspiration
* etc

