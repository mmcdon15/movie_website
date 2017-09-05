import media
import fresh_tomatos

# Fury movie: title, poster image, trailer url
fury = media.Movie("Fury",
                   "https://goo.gl/vuErwy",
                   "https://www.youtube.com/watch?v=-OGvZoIrXpg")
# Midnight in paris movie: title, poster image, trailer url
m_i_p = media.Movie("Midnight In Paris",
                    "https://goo.gl/rM8vXU",
                    "https://www.youtube.com/watch?v=wuOUdZjuCIA")
# Pitch Perfect movie: title, poster image, trailer url
pitch_perfect = media.Movie("Pitch Perfect",
                            "https://goo.gl/7hzbxM",
                            "https://www.youtube.com/watch?v=KaLa0VQYeY0")
# Dodgeball movie: title, poster image, trailer url
dodgeball = media.Movie("Dodgeball: A True Underdog Story",
                        "https://goo.gl/EXYTpL",
                        "https://www.youtube.com/watch?v=ztLcDpRJl9o")
# Groundhog day: title, poster image, trailer url
groundhog_day = media.Movie("Groundhog Day",
                            "https://goo.gl/yrHBfV",
                            "https://www.youtube.com/watch?v=2vmmTnDJnH0")
# Underworld movie = title, poster image, trailer url
underworld = media.Movie("Underworld",
                         "https://goo.gl/a5XnWC",
                         "https://www.youtube.com/watch?v=MqT-e44kIM8")

# creates a list of movies
movies = [fury, m_i_p, pitch_perfect, dodgeball, groundhog_day, underworld]

# creates HTML doc for movie website
fresh_tomatos.open_movies_page(movies)
