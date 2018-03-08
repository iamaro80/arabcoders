import media
import fresh_tomatoes

terminal = media.Movie('Terminal',
                       'A man stuck in airport',
                       'https://goo.gl/X386JQ',
                       'https://youtu.be/GZjC9dAvWuU?t=11')

the_man_who_knew_infinity = media.Movie('The Man Who Knew Infinity',
                                        'The story of Srinivasa Ramanujan',
                                        'https://goo.gl/1WyLNe',
                                        'https://youtu.be/NP0lUqNAw3k')
fault_in_our_stars = media.Movie('Fault in our stars',
                                 'A story of teenagers fighting the cancer',
                                 'https://goo.gl/KGganw',
                                 'https://youtu.be/9ItBvH5J6ss')

movies = [terminal, the_man_who_knew_infinity, fault_in_our_stars]

fresh_tomatoes.open_movies_page(movies)
