'''Media File'''

class Movie():

    def __init__(self, movie_title, movie_imdb_rating, movie_release_year, movie_storyline, poster_image, trailer_youtube):
        '''Initializes an instance of the class Movie'''
        self.title = movie_title
        self.imdb_rating = movie_imdb_rating
        self.release_year = movie_release_year
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
