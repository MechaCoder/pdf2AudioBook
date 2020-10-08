# pdf 2 AudioBook
this is a simple program that allows a user to turn `pdf` into mp3
useing tts tools.

## needed to run
for this program to work you are going to need `python 3.7` installed with a working `pipenv`

[link to pipenv](https://pipenv-fork.readthedocs.io/en/latest/)
[link to python 3.7](https://www.python.org/downloads/release/python-379/)

#it's a command line tool
this program dose not have a Grafical user interface and uses command line tools. to run the commands in tool you will need to runn it in pipenv. this is done by doing the following `pipenv run python pdf2AudioBook.py <command> <path to pdf>` e.g. `pipenv run python pdf2AudioBook.py convert memo.pdf`

`convert` - this command with complile a pdf file to a single .pdf file
`convert2filespagebypage` - this command will convert a pdf file in to many mp3 (one per page)
