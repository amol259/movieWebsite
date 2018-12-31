import media
import fresh_tomatoes
#Create several instances of the Movie class
""" 
    Create several instances of the Movie class imported from the media file. 
    The constructor arguments in order are : title, poster image url, youtube trailer url
"""

the_big_lebowski = media.Movie('The Big Lebowski',
                "http://goo.gl/2cxt3f",
                "https://www.youtube.com/watch?v=ngV0RBhGZmE"
                )

toy_story = media.Movie("Toy Story",
            "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
            "https://www.youtube.com/watch?v=KYz2wyBy3kc"
            )

fight_club = media.Movie("Fight Club", 
            "https://chicquero.files.wordpress.com/2011/11/minimal-movie-poster-chicquero-fight-club.jpg",
            "https://www.youtube.com/watch?v=SUXWAEX2jlg"
            )

howls_moving_castle = media.Movie("Howl's Moving Castle",
                     "http://upload.wikimedia.org/wikipedia/en/a/a0/Howls-moving-castleposter.jpg",
                     "https://youtu.be/iwROgK94zcM"
                     )

pulp_fiction = media.Movie("Pulp Fiction",
                "http://goo.gl/V5fb9n",
                "https://www.youtube.com/watch?v=s7EdQ4FqbhY"
                )
def main():
    """
    Store all instances of movie in a list.
    Then call the open movies function to open the browser and see our movie website
    """
    #Store all instances of movie in a list 
    movies_list = [the_big_lebowski,toy_story, fight_club, howls_moving_castle, pulp_fiction]
    #Call the open movie page method and pass in the list which has all instances of our movies
    fresh_tomatoes.open_movies_page(movies_list)

if __name__ == '__main__':
    main()