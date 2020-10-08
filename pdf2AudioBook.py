import click

from pdf2AudioBook import convert as convertToMp3
from pdf2AudioBook import convertsToSiris

@click.group()
def cli():
    pass

@cli.command()
@click.argument('pdf', type=click.Path(exists=True))
def convert(pdf):
    """ converts pdf file to mp3 """
    click.secho(f'converting {pdf}', fg='yellow')
    s = convertToMp3(pdf)

@cli.command()
@click.argument('pdf', type=click.Path(exists=True))
def convert2filesPageByPage(pdf):
    """ convert a pdf into a set of files (mp3), one file per page """
    click.secho(f'converting {pdf}', fg='yellow')
    s = convertsToSiris(pdf)



if __name__ == '__main__':
    cli()
