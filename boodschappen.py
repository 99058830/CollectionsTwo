groceryList = {}

def dictCreation():
    print('STOP om je boodschappenlijstje te tonen.')
    print('OPSCHONEN om je boodschappenlijstje op te schonen.')
    print('VERWIJDER om een toegevoegd item te verwijderen.')
    while True:
        items = input('Wat wil je toevoegen aan je boodschappen lijstje? ').lower()
        if items == 'stop':
            print(groceryList)
        elif items == 'opschonen':
            groceryList.clear()
            print('Uw boodschappenlijstje is nu opgeschoond!')
            print(groceryList)
        elif items == 'verwijder':
            print(groceryList)
            delete = str(input('Wat wilt u verwijderen uit uw boodschappen lijstje? ')).lower()
            if delete in groceryList:
                groceryList.pop(delete)
                print(groceryList)
        else:
            if items in groceryList:
                groceryList[items] += 1
            else:
                groceryList[items] = 1
dictCreation()