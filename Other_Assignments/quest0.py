# Na dobry początek zajmiemy się czymś, co da Ci dobry pogląd na to z czym trzeba będzie się zmierzyć.
# Jedna osoba z naszej ekipy pracuje nad miejscem,
# które będzie dobre jako punkt obserwacyjny do kolejnego zlecenia.
# Spory ogród na dachu jednego z okolicznych biurowców wydaje się do tego idealny.
# Tom z naszej grupy zatrudnił się tam jako ogrodnik,
# aby mieć lepszy dostęp do miejsca i wtopić się w tłum.
#
# Jednym z obowiązków Toma jest odpowiednie dbanie o rośliny.
# Ma przynieść specjalny nawóz, którym nawilży każdą z nich.
# Na każdy metr kwadratowy przypada jedna paczka nawozu,
# a ogród ma C metrów kwadratowych. Tom ma plecak,
# ale jest słaby i udźwignie tylko K kilogramów, gdzie każda paczka waży W kg.
# Pomóż mu ogarnąć czy da radę przynieść wszystko jak należy tak,
# aby go nie wylali i nie spalił miejscówki.

# W pierwszej linii jedna dodatnia liczba całkowita t≤100 oznaczająca liczbę testów
# (Tom został poproszony o przyniesienie odżywek kilka razy).
# Następnie t linii, każda zawierająca trzy liczby: c, k, w, gdzie 1≤c,k,w≤100.
# t [liczba testów]
# c k w [liczba metrów, udźwig Toma oraz waga nawozu]


def quest_0():
    while True:
        try:
            t = int(input('Podaj liczbę testów dla Toma: '))
            if t < 1 or t > 100:
                raise ValueError
        except ValueError as e:
            print('Wprowadź poprawne dane!')
            continue
        else:
            break
    counter = 0
    result = []
    while counter < t:
        while True:
            try:
                c, k, w = [int(x) for x in input('Wprowadź 3 liczby oddzielone spacją: ').split()]
                counter += 1
                if c * w <= k:
                    out = 'yes'
                else:
                    out = 'no'
                result.append(out)
            except ValueError as e:
                print('Wprowadź liczby:')
                continue
            else:
                break
    return '\n'.join(result)


print(quest_0())
