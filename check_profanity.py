import urllib

def read_text():
    quote = open(r'C:\GitHub\arabcoders\movie_quotes.txt')
    content_of_file = quote.read()
    quote.close()
    check_profanity(content_of_file)


def check_profanity(text_to_check):
    aut = urllib
    connection = urllib.urlopen('http://www.wdylike.appspot.com/?q='+text_to_check)
    output = connection.read()
    if 'false' in output:
        print 'Profanity Alert!!'
    elif 'true' in output:
        print 'This document has no curse word!'
    else:
        print 'Could not scan the document probably.'
    connection.close()


read_text()




