import random
import datetime

class Movie ():
    def __init__(self, title, release, genre):
        self._title = title
        self.release = release
        self.genre = genre
        self._play_counter = 0

    def __str__(self):
        return f'{self._title} {self.release} {self.genre} {self._play_counter}'

    @property
    def title(self):
        return self._title

    @property
    def play_counter(self):
        return self._play_counter

    @play_counter.setter
    def play_counter (self, number):
        self._play_counter = number
    
    def play(self):
        self._play_counter += 1
        print(f'Obejrzałeś {self._title} ({self.release})')

class Series(Movie):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._season = season
        self._episode = episode

    def __str__(self):
        return f'{self._title} {self.release} {self.genre} {self.season}{self.episode} {self._play_counter}'

    @property
    def season(self):
        return self._season

    @property
    def episode(self):
        return self._episode

    def play(self):
        self._play_counter += 1
        print(f'Obejrzałeś {self._title} {self.season}{self.episode}')


class Library ():
    def __init__(self):
        self._lista = []
    
    @property
    def lista(self):
        return self._lista

    def add(self, object):
        if not (type(object) == Movie or type(object) == Series): 
            raise ValueError("neither a Movie nor Series")
        self._lista.append(object)

    def create_seasons (self, title, release, genre, season, how_many_episodes):
        new_season = []
        for i in range (1,how_many_episodes+1):
            new_season.append(Series(title = title, release = release, genre = genre, season = f'S{season:02}', episode = f'E{i:02}'))
        for i in new_season:
            self._lista.append(i)

    def get_movies(self):        
        return sorted([i for i in self._lista if type(i) == Movie], key = lambda pomidorowa: pomidorowa.title)

    def get_series(self):
        return sorted([i for i in self._lista if type(i) == Series], key = lambda pomidorowa: pomidorowa.title)

    def search(self, title):
        for item in self._lista:
            if item.title == title:
                print(f'Znaleziono {title}')
                return item
        
        raise Exception("Nie znaleziono")

    def generate_views(self):
        chosen_item = random.choice(self._lista)
        new_count = chosen_item.play_counter + random.randint(1, 100)
        chosen_item.play_counter=new_count
        return chosen_item.title, chosen_item.play_counter

    def generate_views_10x(self):
        for i in range (10):
            self.generate_views()

    def top_titles (self, content_type, number):
        
        top = sorted(self._lista, key = lambda ogorkowa: ogorkowa.play_counter, reverse=True)
        the_best = top[0:number]
        
        if content_type == "movie":
            top_m = []
            for movie in top:
                if type(movie) == Movie:
                    top_m.append(movie)
            the_best_m = top_m[0:number]
            return the_best, the_best_m

        elif content_type == "series":
            top_s = []
            for series in top:
                if type(series) == Series:
                    top_s.append(series)
            the_best_s = top_s[0:number]
            return the_best, the_best_s
            
        
        else:
            raise ValueError("neither a movie nor series")
        
    

if __name__ == "__main__":

    prawdziwe = [
    Movie(title = 'Tie Me Up! Tie Me Down!', release = 1990, genre = 'Comedy'),
    Movie(title = 'High Heels', release = 1991, genre = 'Comedy'),
    Movie(title = 'Dead Zone  The', release = 1983, genre = 'Horror'),
    Movie(title = 'Cuba', release = 1979, genre = 'Action'),
    Movie(title = 'Days of Heaven', release = 1978, genre = 'Drama' ),
    Movie(title = 'Octopussy', release = 1983, genre = 'Action' ),
    Movie(title = 'Target Eagle', release = 1984, genre = 'Action' ),
    Movie(title = 'American Angels: Baptism of Blood  The', release = 1989, genre = 'Drama' ),
    Movie(title = 'Subway', release = 1985, genre = 'Drama' ),
    Movie(title = 'Camille Claudel', release = 1990, genre = 'Drama' ),
    Movie(title = 'Fanny and Alexander', release = 1982, genre = 'Drama' ),
    Movie(title = 'Tragedy of a Ridiculous Man', release = 1982, genre = 'Drama' ),
    Movie(title = 'A Man & a Woman', release = 1966, genre = 'Drama' ),
    Movie(title = 'A Man & a Woman: Twenty releases Later', release = 1986, genre = 'Drama' ),
    Movie(title = 'Blackmail', release = 1929, genre = 'Mystery' ),
    Movie(title = 'Donovan s Reef', release = 1963, genre = 'Comedy' ),
    Movie(title = 'Tucker: The Man & His Dream', release = 1988, genre = 'Drama' ),
    Movie(title = 'Scrooged', release = 1988, genre = 'Comedy' ),
    Movie(title = 'Running Man  The', release = 1987, genre = 'Science Fiction' ),
    Movie(title = 'Raiders of the Lost Ark', release = 1981, genre = 'Action' ),
    Movie(title = 'Predator 2', release = 1991, genre = 'Action' ),
    Movie(title = 'Colors', release = 1988, genre = 'Drama' ),
    Movie(title = 'Un Hombre y una Mujer', release = 1966, genre = 'Drama' ),
    Movie(title = 'Official Story  The', release = 1985, genre = 'Drama' ),
    Series(title = 'Gra o Tron', release = 2012, genre = 'Fantasy',season = 'S01', episode = 'E02' ),
    Series(title = 'Gra o Tron', release = 2012, genre = 'Fantasy',season = 'S01', episode = 'E03' ),
    Series(title = 'Gra o Tron', release = 2012, genre = 'Fantasy',season = 'S02', episode = 'E01' ),
    Series(title = 'Gra o Tron', release = 2012, genre = 'Fantasy',season = 'S02', episode = 'E02' ),
    Series(title = 'Gra o Tron', release = 2012, genre = 'Fantasy',season = 'S02', episode = 'E03' ),
    Series(title = 'Gra o Tron', release = 2012, genre = 'Fantasy',season = 'S03', episode = 'E01' ),
    Series(title = 'Gra o Tron', release = 2012, genre = 'Fantasy',season = 'S03', episode = 'E02' ),
    Series(title = 'Gra o Tron', release = 2012, genre = 'Fantasy',season = 'S03', episode = 'E03' ),
    Series(title = 'Rodzina Soprano', release = 2000, genre = 'Drama',season = 'S01', episode = 'E01' ),
    Series(title = 'Rodzina Soprano', release = 2000, genre = 'Drama',season = 'S01', episode = 'E02' ),
    Series(title = 'Rodzina Soprano', release = 2000, genre = 'Drama',season = 'S01', episode = 'E03' ),
    Series(title = 'Rodzina Soprano', release = 2000, genre = 'Drama',season = 'S02', episode = 'E01' ),
    Series(title = 'Rodzina Soprano', release = 2000, genre = 'Drama',season = 'S02', episode = 'E02' ),
    Series(title = 'Rodzina Soprano', release = 2000, genre = 'Drama',season = 'S02', episode = 'E03' ),
    Series(title = 'Rodzina Soprano', release = 2000, genre = 'Drama',season = 'S03', episode = 'E01' ),
    Series(title = 'Rodzina Soprano', release = 2000, genre = 'Drama',season = 'S03', episode = 'E02' ),
    Series(title = 'Rodzina Soprano', release = 2000, genre = 'Drama',season = 'S03', episode = 'E03' ),
    Series(title = 'The Office', release = 2010, genre = 'Comedy',season = 'S01', episode = 'E01' ),
    Series(title = 'The Office', release = 2010, genre = 'Comedy',season = 'S01', episode = 'E02' ),
    Series(title = 'The Office', release = 2010, genre = 'Comedy',season = 'S01', episode = 'E03' ),
    Series(title = 'The Office', release = 2010, genre = 'Comedy',season = 'S02', episode = 'E01' ),
    Series(title = 'The Office', release = 2010, genre = 'Comedy',season = 'S02', episode = 'E02' ),
    Series(title = 'The Office', release = 2010, genre = 'Comedy',season = 'S02', episode = 'E03' ),
    Series(title = 'The Office', release = 2010, genre = 'Comedy',season = 'S03', episode = 'E01' ),
    Series(title = 'The Office', release = 2010, genre = 'Comedy',season = 'S03', episode = 'E02' ),
    Series(title = 'The Office', release = 2010, genre = 'Comedy',season = 'S03', episode = 'E03' ),
    ]

    def main():
        
        print("Biblioteka filmów")



        print("Sprawdzam")
        print(f"""
        1. Jest w stanie przechowywać informacje na temat filmów, które znajdują się w systemie. Każdy film powinien mieć następujące atrybuty: """)
        m = Movie(title = 'Tie Me Up! Tie Me Down!', release = 1990, genre = 'Comedy')
        print(m)

        print(f"""
        2. Umożliwia przechowywanie informacji na temat seriali. Każdy serial powinien mieć następujące atrybuty:""")
        s = Series(title = 'The Office', release = 2010, genre = 'Comedy',season = 'S01', episode = 'E01' )
        print (s)

        print(f"""
        3. Filmy i seriale mają metodę play, która zwiększa liczbę odtworzeń danego tytułu o 1.
        4. Po wyświetleniu serialu jako string pokazują się informacje o konkretnym odcinku, np.: “The Simpsons S01E05” (gdzie po S pokazany jest numer sezonu w notacji dwucyfrowej, natomiast po E - numer odcinka, również w zapisie dwucyfrowym).")
        5. Po wyświetleniu filmu jako string widoczne są tytuł i rok wydania np. “Pulp Fiction (1994)”.")
        """)
        
        Series.play (s)
        Movie.play(m)

        print(f"""
        6. Przechowuje filmy i seriale w jednej liście""")
        
        Hani = Library()
        for i in prawdziwe:
            Hani.add(i)
        
        print(Hani.lista)

        print(f"""
        7. Napisz funkcje get_movies oraz get_series, które będą filtrować listę i zwracać odpowiednio tylko filmy oraz tylko seriale. Posortuj listę wynikową alfabetycznie.""")

        tylko_filmy = Hani.get_movies()
        tylko_seriale = Hani.get_series()

        # for i in tylko_filmy:
        #     print (i)
        # for i in tylko_seriale:
        #     print (i)

        print(f"""
        8.Napisz funkcję search, która wyszukuje film lub serial po jego tytule.""")

        Hani.search("The Office")

        print(f"""
        9.Napisz funkcję generate_views, która losowo wybiera element z biblioteki, a następnie dodaje mu losową (z zakresu od 1 do 100) ilość odtworzeń.""")

        gv = Hani.generate_views()
        print(gv)

        print(f"""
        10. Napisz funkcję, która uruchomi generate_views 10 razy.""")

        Hani.generate_views_10x()

        print(f"""
        11.Napisz funkcję top_titles(), która zwróci wybraną ilość najpopularniejszych tytułów z biblioteki. Dla chętnych: dodaj do funkcji parametr content_type, którym wybierzesz czy mają zostać pokazane filmy, czy seriale.""")


        x = datetime.datetime.now().strftime("%d.%m.%Y")

        top3, top3m = Hani.top_titles("movie", 3)
        top3, top3s  = Hani.top_titles("series", 3)

        print(f'''
        Najpopularniejsze filmy i seriale dnia {x}
        ''')
        for i in top3:
            print(i)
        
        print(f'''
        Najpopularniejsze filmy dnia {x}
        ''')
        for i in top3m:
            print(i)
        
        print(f'''
        Najpopularniejsze seriale dnia {x}
        ''')
        for i in top3s:
            print(i)

        print(f"""Zadania dla chętnych
        1. Napisz funkcję, która za pomocą pętli dodaje pełne sezony seriali do biblioteki. Funkcja powinna przyjmować parametry takie jak: tytuł serialu, rok wydania, gatunek, numer sezonu, liczba odcinków do dodania.""")

        title = "Mentalista"
        release = 2008
        genre = "crime" 
        season = 1
        how_many_episodes = 25

        Hani.create_seasons (title, release, genre,season,how_many_episodes)

    main()    



