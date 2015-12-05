''' Entertainment Center'''

import media
import fresh_tomatoes

macgruber = media.Movie("MacGruber",
                        "5.5",
                        "2010",
                        "A man saving the world, one throat rip at a time.",
                        "http://www.sobaditsgood.co.uk/wp-content/uploads/2015/06/MacGruber-UK-Poster.jpg",
                        "https://www.youtube.com/watch?v=Oyb6IQvAZt4")

dumb_and_dumber = media.Movie("Dumb and Dumber",
                              "7.3",
                              "1994",
                              "The cross-country adventures of two good-hearted but incredibly stupid friends.",
                              "http://cdn.fontmeme.com/images/dumb-dumber-poster.jpg",
                              "https://www.youtube.com/watch?v=l13yPhimE3o")

anchorman = media.Movie("Anchorman: The Legend of Ron Burgundy",
                        "7.2",
                        "2004",
                        "Ron Burgundy is San Diego's top rated newsman in the male-dominated broadcasting of the '70s.",
                        "https://upload.wikimedia.org/wikipedia/en/6/64/Movie_poster_Anchorman_The_Legend_of_Ron_Burgundy.jpg",
                        "https://www.youtube.com/watch?v=NJQ4qEWm9lU")

paul = media.Movie("Paul",
                   "7.0",
                   "2011",
                   "Two British comic-book geeks traveling across the U.S. encounter an alien outside Area 51.",
                   "https://www.movieposter.com/posters/archive/main/113/MPW-56550",
                   "https://www.youtube.com/watch?v=xZvsP3_t2Sk")

caddyshack = media.Movie("Caddyshack",
                         "7.4",
                         "1980",
                         "An exclusive golf course has to deal with a brash new member and a destructive dancing gopher.",
                         "https://www.movieposter.com/posters/archive/main/1/A70-713",
                         "https://www.youtube.com/watch?v=zrTqenN1SqQ")

donnie_darko = media.Movie("Donnie Darko",
                           "8.1",
                           "2001",
                           "A troubled teenager is plagued by visions of a large bunny rabbit that manipulates him.",
                           "https://www.movieposter.com/posters/archive/main/6/MPW-3129",
                           "https://www.youtube.com/watch?v=vijy4Oiawa8")

taken = media.Movie("Taken",
                    "7.9",
                    "2008",
                    "A retired CIA agent travels across Europe and relies on his old skills to save his estranged daughter.",
                    "https://www.movieposter.com/posters/archive/main/77/MPW-38536",
                    "https://www.youtube.com/watch?v=uPJVJBm9TPA")

animal_house = media.Movie("Animal House",
                           "7.6",
                           "1978",
                           "At a 1962 college, Dean Vernon Wormer is determined to expel the entire Delta Tau Chi Fraternity.",
                           "http://ia.media-imdb.com/images/M/MV5BMTU4OTEyNzY4NF5BMl5BanBnXkFtZTgwMzU5NTYxMTE@._V1_SX640_SY720_.jpg",
                           "https://www.youtube.com/watch?v=KWjtI6n5xWM")

the_godfather = media.Movie("The Godfather",
                            "9.2",
                            "1972",
                            "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
                            "http://cdn.fontmeme.com/images/The-Godfather-Poster.jpg",
                            "https://www.youtube.com/watch?v=sY1S34973zA")





movies = [macgruber, dumb_and_dumber, anchorman, paul, caddyshack, donnie_darko, taken, animal_house, the_godfather]

fresh_tomatoes.open_movies_page(movies)



                        


