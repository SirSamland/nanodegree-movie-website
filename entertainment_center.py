import media
import fresh_tomatoes

big_fish = media.Movie("Big Fish", "A frustrated son tries to determine the fact from fiction in his dying father's life.", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYyMzM3MzgyNV5BMl5BanBnXkFtZTcwMTI4MzUyMQ@@._V1_.jpg", "https://www.youtube.com/watch?v=M3YVTgTl-F0")

underworld = media.Movie("Underworld", "The story of a war between Vampires and Werewolves", "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNDExNDEyMV5BMl5BanBnXkFtZTcwODY1OTkxMw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg", "https://www.youtube.com/watch?v=MqT-e44kIM8")

troll_2 = media.Movie("Troll 2", "A family vacationing in a small town discovers the entire town is inhabited by goblins in disguise as humans, who plan to eat them.", "http://cdn.shopify.com/s/files/1/0558/2081/products/troll2posterff_thumb_6ba6329a-760d-4a2a-804c-d6f506c87529_grande.png?v=1410241630", "https://www.youtube.com/watch?v=CkNB0w1fYKk")

dynamite_warrior = media.Movie("Dynamite Warrior", "A Muay Thai warrior who seeks revenge and fights using fireworks.", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTI1MTkwMDEwOF5BMl5BanBnXkFtZTcwMDY5OTc0MQ@@._V1_.jpg", "https://www.youtube.com/watch?v=r01IVFEpQMg")

rush_hour = media.Movie("Rush Hour", "The fastest hands in the East meet the biggest mouth in the West!", "https://ddramatards.files.wordpress.com/2012/02/rush-hour-original.jpg", "https://www.youtube.com/watch?v=JMiFsFQcFLE")

the_illusionist = media.Movie("The Illusionist", "In turn-of-the-century Vienna, a magician uses his abilities to secure the love of a woman far above his social standing.", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTM1MjQyMDkzN15BMl5BanBnXkFtZTcwNzAyNTQzMQ@@._V1_SY1000_SX675_AL_.jpg", "https://www.youtube.com/watch?v=i0xO64icGSY")

movies = [big_fish, underworld, troll_2, rush_hour, dynamite_warrior, the_illusionist]

fresh_tomatoes.open_movies_page(movies)
