import click

from pdf2AudioBook import convert as convertToMp3
from pdf2AudioBook import convertsToSiris, convertsToSirisEpub

@click.group()
def cli():
    pass

@cli.command()
@click.argument('pdf', type=click.Path(exists=True))
def convert(pdf):
    """ converts pdf file to mp3 """
    click.secho(f'converting {pdf}', fg='yellow')
    convertToMp3(pdf)

@cli.command()
@click.argument('pdf', type=click.Path(exists=True))
def convert2filesPageByPage(pdf):
    """ convert a pdf into a set of files (mp3), one file per page """
    click.secho(f'converting {pdf}', fg='yellow')
    file_extention = pdf.split('.')[-1]

    click.secho(f'detecting file exetetion ({file_extention})', fg='yellow')
    if file_extention == 'pdf':
        convertsToSiris(pdf)
        return True
    if file_extention == 'epub':
        convertsToSirisEpub(pdf)
        return True
    
    click.secho('You need to use .pdf or .epub')


if __name__ == '__main__':
    cli()
