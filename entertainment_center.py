# media module consist of Movie class
# web_script module consist of code to render website
import media
import web_script

# Create instances of Class Movie
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",   # noqa
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

logan = media.Movie("Logan",
                    "American superhero film, produced by Marvel Entertainment, TSG Entertainment and The Donners' Company",  # noqa
                    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",  # noqa
                    "https://www.youtube.com/watch?v=Div0iP65aZo")

infinity_war = media.Movie("Infinity War",
                           "Marvel's Studios Avengers: Infinity War",
                           "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",  # noqa
                           "https://www.youtube.com/watch?v=QwievZ1Tx-8")

pacific_rim = media.Movie("Pacific Rim Uprising",
                          '''American science-fiction action film directed by
                          Steven S. DeKnight (in his feature-film
                          directorial debut) ''',
                          "https://upload.wikimedia.org/wikipedia/en/2/2e/Pacificrim2-poster.jpg",  # noqa
                          "https://www.youtube.com/watch?v=_EhiLLOhVis")

sherlock_gnomes = media.Movie("Sherlock Gnomes",
                              '''3D computer-animated comedy film
                              directed by John Stevenson''',
                              "https://upload.wikimedia.org/wikipedia/en/2/25/Sherlock_Gnomes.png",  # noqa
                              "https://www.youtube.com/watch?v=TR-sefx8ncI")  # noqa

tomb_raider = media.Movie("Tomb Raider",
                          '''Tomb Raider is a 2018 action adventure
                          film directed by Roar Uthaug''',
                          "https://upload.wikimedia.org/wikipedia/en/b/bd/Tomb_Raider_%282018_film%29.png",  # noqa
                          "https://www.youtube.com/watch?v=8ndhidEmUbI")  # noqa

social_network = media.Movie("Social Network",
                             ''''Mark Zuckerberg creates a social networking site, Facebook,
                             with the help of his friend Eduardo Saverin.
                             But soon, a string of lies tears their
                             relationship apart even as
                             Facebook connects people.''',
                             "http://t2.gstatic.com/images?q=tbn:ANd9GcTj268E01VcjLW3fNrO2z10WpXs7WMeciAB9wYSOA2DI-le_NQH",  # noqa
                             "https://www.youtube.com/watch?v=lB95KLmpLR4")  # noqa

theory_of_everything = media.Movie("Theory of Everything",
                                   '''Stephen Hawking, an excellent astrophysics
                                   student working on his research,
                                   learns that he suffers from motor neurone
                                   disease and has around two years to live''',
                                   "http://t0.gstatic.com/images?q=tbn:ANd9GcSgW7hpezP5xtikV7WqwwqFm37kqMeJeFEGpYcO30CDcchn9g8m",  # noqa
                                   "https://www.youtube.com/watch?v=Salz7uGp72c")  # noqa \


man_who_knew_infi = media.Movie("Man who knew infinity",
                                '''In 1913, brilliant South Indian mathematician
                                Srinivasa Ramanujan (Dev Patel) travels to
                                Trinity College in England to work with
                                professor G.H. Hardy (Jeremy Irons).''',
                                "http://t3.gstatic.com/images?q=tbn:ANd9GcRnrHiztFl1UMUDq1g8zajTENn9H9MsPA56Zh3aprKc3JEzQcIs",  # noqa
                                "https://www.youtube.com/watch?v=oXGm9Vlfx4w")  # noqa


movies = [avatar,
          logan, infinity_war,
          pacific_rim,
          sherlock_gnomes,
          tomb_raider,
          social_network,
          theory_of_everything,
          man_who_knew_infi]

# call open movies function with movie objects array
web_script.open_movies_page(movies)
