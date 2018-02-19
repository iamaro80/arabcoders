def read_text():
    quote = open(r'C:\GitHub\arabcoders\movie_quotes.txt')
    content_of_file = quote.read()
    print 'name of the file is:', quote.name
    print content_of_file
    quote.close()

read_text()



