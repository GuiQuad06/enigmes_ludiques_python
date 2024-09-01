from dijkstra_algo import dijkstra

dico = {
    'lille': {
        'caen': 293,
        'paris': 203,
        'strasbourg': 407},
    'caen': {
        'lille': 293,
        'paris': 199,
        'rennes': 157},
    'paris': {
        'lille': 203,
        'caen': 199,
        'strasbourg': 399,
        'rennes': 309,
        'clermont': 347,
        'dijon': 263},
    'strasbourg': {
        'lille': 407,
        'paris': 399,
        'dijon': 248,
        'lyon': 384},
    'rennes': {
        'caen': 157,
        'paris': 309,
        'bordeaux': 371},
    'dijon': {
        'paris': 263,
        'strasbourg': 248,
        'lyon': 175},
    'clermont': {
        'paris': 347,
        'bordeaux': 304,
        'toulouse': 276,
        'lyon': 137},
    'lyon': {
        'strasbourg': 384,
        'dijon': 175,
        'clermont': 137,
        'montpellier': 251,
        'nice': 296},
    'bordeaux': {
        'rennes': 371,
        'clermont': 304,
        'toulouse': 210},
    'toulouse': {
        'bordeaux': 210,
        'clermont': 276,
        'montpellier': 197},
    'montpellier': {
        'toulouse': 197,
        'lyon': 251,
        'marseille': 127},
    'marseille': {
        'montpellier': 127,
        'nice': 156},
    'nice': {
        'marseille': 156,
        'lyon': 296}
}


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    start = str(input('Veuillez rentrer une ville de depart:'))
    stop = str(input('Veuillez rentrer une ville de destination:'))

    shortest_way = dijkstra(dico, stop, start)
    print(f'Le chemin le + court de {start} a {stop} est {shortest_way} km')
