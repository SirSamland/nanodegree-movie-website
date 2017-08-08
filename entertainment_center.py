"""Stores data from movies and displays them on a website."""
import media
import fresh_tomatoes

big_fish = media.Movie("Big Fish",
                       "A story of telling fact from fiction.",
                       "https://goo.gl/WWmyH9",
                       "https://www.youtube.com/watch?v=M3YVTgTl-F0")

underworld = media.Movie("Underworld",
                         "The story of a war between Vampires and Werewolves",
                         "https://goo.gl/QizKzu",
                         "https://www.youtube.com/watch?v=MqT-e44kIM8")

troll_2 = media.Movie("Troll 2",
                      "Quite possibly the worst movie ever.",
                      "https://goo.gl/QqKKTv",
                      "https://www.youtube.com/watch?v=CkNB0w1fYKk")

dynamite_warrior = media.Movie("Dynamite Warrior",
                               "Muay Thai action with fireworks thrown in.",
                               "https://goo.gl/T28Yst",
                               "https://www.youtube.com/watch?v=r01IVFEpQMg")

rush_hour = media.Movie("Rush Hour",
                        "Jackie Chan & Chris Tucker VS the crime world.",
                        "https://goo.gl/pEobR1",
                        "https://www.youtube.com/watch?v=JMiFsFQcFLE")

the_illusionist = media.Movie("The Illusionist",
                              "A magician in love.",
                              "https://goo.gl/Xql6je",
                              "https://www.youtube.com/watch?v=i0xO64icGSY")

movies = [big_fish, underworld, troll_2,
          rush_hour, dynamite_warrior, the_illusionist]

fresh_tomatoes.open_movies_page(movies)
