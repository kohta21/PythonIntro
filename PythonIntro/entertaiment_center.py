# -*- coding: utf-8 -*-
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.eikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

#blank_movie = media.Movie()

print(toy_story.storyline)
toy_story.show_trailer()
#print(blank_movie.storyline)

