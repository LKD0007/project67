import time
f = []
m = []
s = []
o = []

a = input('Enter a book type: ')

while True:
    asking = input('\nDo you want to (add), (acceses), (delete) or (exit): ').lower()

    if asking == 'add':
        b = input('Enter the book name: ')
        if a == 'fictional':
            f.append(b)
        elif a == 'mithological':
            m.append(b)
        elif a == 'scientific':
            s.append(b)
        else:
            o.append(b)
        print('Book entered successfully')

    elif asking == 'acceses':
        acceses1 = input('Which book type do you want to acceses: ')
        if acceses1 == 'mithological':
            print(f"Mithological books: {list(set(m))}")
        elif acceses1 == 'fictional':
            print(f"Fictional books: {list(set(f))}")
        elif acceses1 == 'scientific':
            print(f"Scientific books: {list(set(s))}")

    elif asking == 'delete':
        dele = input('Which book do you want to delete: ')
        sec = input('From which type (scientific, fictional, mithological): ')
        try:
            if sec == 'scientific':
                s.remove(dele)
                print("Updated Scientific list:", s)
            elif sec == 'fictional':
                f.remove(dele)
                print("Updated Fictional list:", f)
            elif sec == 'mithological':
                m.remove(dele)
                print("Updated Mithological list:", m)
            else:
                o.remove(dele)
                print("Updated Other list:", o)
        except ValueError:
            print("Error: That book title was not found in the list.")

    elif asking == 'exit':
        print("Goodbye!")
        break