import media
import fresh_tomatos


fury = media.Movie("Fury","War Never Ends Quietly",
                  "http://t2.gstatic.com/images?q=tbn:ANd9GcR_ppNO9FR1hT0mRhqD1lWovgQZMwxJRhYrEa7vYmTb-atN1Opu",
                  "https://www.youtube.com/watch?v=-OGvZoIrXpg")
midnight_in_paris = media.Movie("Midnight In Paris","A screenwriter travel back in time to 1920's Paris during his nightly strolls through the city.",
                                "http://t3.gstatic.com/images?q=tbn:ANd9GcTk3ssys2bKM5-U6XMgvoD8yVoS5Io2YKg_1xA6x6GA8mKuuqID",
                                "https://www.youtube.com/watch?v=wuOUdZjuCIA")
pitch_perfect = media.Movie("Pitch Perfect",
                            "Arriving at her new college, Beca (Anna Kendrick) finds herself not right for any clique but somehow is muscled into one that she never would have picked on her own: alongside mean girls, sweet girls and weird girls whose only thing in common is how good they sound when they sing",
                            "http://t3.gstatic.com/images?q=tbn:ANd9GcT1auKQEhoF6KOJ_wXKHtvGoOV91-6iv8Nu367yAZMWcyWpvZKY",
                            "https://www.youtube.com/watch?v=KaLa0VQYeY0")
dodgeball = media.Movie("Dodgeball: A True Underdog Story",
                        "A ragtag group bands together to save their gym by playing dodgeball.",
                        "http://www.gstatic.com/tv/thumb/dvdboxart/33984/p33984_d_v8_ac.jpg",
                        "https://www.youtube.com/watch?v=ztLcDpRJl9o")
groundhog_day = media.Movie("Groundhog Day",
                            "History repeats itself in this inventive, side-splitting comedy. Murray, a Pittsburgh weatherman on assignment in Punxsutawney, PA., gets stuck in a comic time-warp and must experience the same groundhog day over and over again...until he learns to appreciate the little things in life!",
                            "http://www.gstatic.com/tv/thumb/movieposters/14569/p14569_p_v8_ah.jpg",
                            "https://www.youtube.com/watch?v=2vmmTnDJnH0")
underworld = media.Movie("Underworld",
                         "Selene, a vampire warrior, is entrenched in a conflict between vampires and werewolves, while falling in love with Michael, a human who is sought by werewolves for unknown reasons.",
                         "http://www.gstatic.com/tv/thumb/movieposters/32955/p32955_p_v8_af.jpg",
                         "https://www.youtube.com/watch?v=MqT-e44kIM8")

movies=[fury,midnight_in_paris,pitch_perfect,dodgeball,groundhog_day,underworld]
#creates HTML doc for movie website
fresh_tomatos.open_movies_page(movies)
