import media
import fresh_tomatos


fury = media.Movie("Fury",
                   "https://goo.gl/vuErwy",
                   "https://www.youtube.com/watch?v=-OGvZoIrXpg")
m_i_p = media.Movie("Midnight In Paris",
                    "https://goo.gl/rM8vXU",
                    "https://www.youtube.com/watch?v=wuOUdZjuCIA")
pitch_perfect = media.Movie("Pitch Perfect",
                            "https://goo.gl/7hzbxM",
                            "https://www.youtube.com/watch?v=KaLa0VQYeY0")
dodgeball = media.Movie("Dodgeball: A True Underdog Story",
                        "https://goo.gl/EXYTpL",
                        "https://www.youtube.com/watch?v=ztLcDpRJl9o")
groundhog_day = media.Movie("Groundhog Day",
                            "https://goo.gl/yrHBfV",
                            "https://www.youtube.com/watch?v=2vmmTnDJnH0")
underworld = media.Movie("Underworld",
                         "https://goo.gl/a5XnWC",
                         "https://www.youtube.com/watch?v=MqT-e44kIM8")

movies = [fury, m_i_p, pitch_perfect, dodgeball, groundhog_day, underworld]
# creates HTML doc for movie website
fresh_tomatos.open_movies_page(movies)
