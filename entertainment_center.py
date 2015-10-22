import fresh_tomatoes
import media


# Create selected instances of class Movie with the following data
empire = media.Movie("The Empire Strikes Back",
                      "The saga continues as our heroes enter their darkest period",
                      "http://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",
                      "https://www.youtube.com/watch?v=JNwNXF9Y6kY",
                      "As dads go, yours was better.")


pineapple = media.Movie("Pineapple Express",
                         "A pothead and his dealer are on the run when he sees the supplier execute a competitor",
                         "http://upload.wikimedia.org/wikipedia/en/c/ca/Pineapple_Express_Poster.jpg",
                         "https://www.youtube.com/watch?v=_GnV2u30oOU",
                         "There are no drug lords looking for you.")


mystery_men = media.Movie("Mystery Men",
                           "A group of not-quite-super heroes stumble into heroism",
                           "http://ia.media-imdb.com/images/M/MV5BMTM2NjM0NTIzN15BMl5BanBnXkFtZTcwNTg4MjEyMQ@@._V1_SX640_SY720_.jpg",
                           "https://www.youtube.com/watch?v=PKmHBFgIoX0",
                           "Jock loses. Losers win. 'Nuff said.")


the_burbs = media.Movie("The Burbs",
                         "A group of suburbanites team up to take on their new neihgbors from hell.",
                         "http://upload.wikimedia.org/wikipedia/en/0/07/Burbsposter.jpg",
                         "https://www.youtube.com/watch?v=Z3lfkZTwN00",
                         "Even in mediocrity, you can undermine evil freaks by breaking a few laws.")


illusionist = media.Movie("The Illusionist",
                           "A talented magician fools powerful men and saves the girl he loved since childhood",
                           "http://upload.wikimedia.org/wikipedia/en/6/6a/The_Illusionist_Poster.jpg",
                           "https://www.youtube.com/watch?v=hoElooKJBMg",
                           "You can do a way better vaguely European accent than Edward Norton.")

the_golden_child = media.Movie("The Golden Child",
                                "A private investigator who searches for missing kids is hired to find...the Golden Child.",
                                "http://upload.wikimedia.org/wikipedia/en/1/1a/Golden_child_movie.jpg",
                                "https://www.youtube.com/watch?v=_Pd0-Je3XDQ",
                                "Classic Eddie. It warms the soul.")

# Store all of the instances of Class into one variable 
movies = [empire, pineapple, mystery_men, the_burbs, illusionist, the_golden_child]

# Run the function from fresh_tomatoes.py that assembles all the pieces using the movie variable above
fresh_tomatoes.open_movies_page(movies)

