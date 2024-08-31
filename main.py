cartes = [
    [1, 4, 6, 9, 12, 14, 17, 19, 22, 25, 27, 30, 33],
    [2, 7, 10, 15, 20, 23, 28, 31],
    [3, 4, 11, 12, 16, 17, 24, 25, 32, 33],
    [5, 6, 7, 18, 19, 20, 26, 27, 28],
    [8, 9, 10, 11, 12, 29, 30, 31, 32, 33],
    [13, 14, 15, 16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]]

value_carte = 0

def fibo(n):
    if n <= 2:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    choosen_num = int(input('veuillez rentrer un numero entre 0 et 33'))

    for index, carte in enumerate(cartes):
        print(f'Voici les nombres de la carte {index}')
        for num in carte:
            print(num)
        isCartePresente = input('la carte choisie figure t elle dans la collection ? O/n')
        if isCartePresente.lower() == 'o':
            value_carte += fibo(index + 1)

    print('ok') if value_carte == choosen_num else print('nok')

