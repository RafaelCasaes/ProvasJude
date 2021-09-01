mamifero=input("O animal é mamífero? ")
if mamifero=='sim':
    quadrupede=input('O animal é quadrúpede? ')
    if quadrupede == 'sim':
        carnivoro=input('o animal é carnívoro? ')
        if carnivoro == 'sim':
            print('O animal escolhido é o Leão')
        else:
            print('O animal escolhido é o Cavalo')
    else:
        bipede=input('O animal é bípede? ')
        if bipede== 'sim':
            onivoro=input('O animal é onivoro? ')
            if onivoro=='sim':
                print('O animal escolhido é o Homem')
            else:
                print('O animal escolhido é o Macaco')
        else:
            voador=input('O animal é voador? ')
            if voador=='sim':
                print('O animal escolhido é o morcego')
            else:
                print('O animal escolhido é a Baleia')
else :
    aves=input('O animal é uma ave')
    if aves=='sim':
        voa=input('essa ave voa? ')
        if voa!='sim':
            trop=input('Essa ave é tropical? ')
            if trop=='sim':
                print('O animal escolhido é o Avestruz')
            else:
                print('O animal escolhido é o Pinguim')
        else:
            nad=input('Essa ave nada?')
            if nad=='sim':
                print('O animal escolhido é o Pato')
            else:
                print('O animal escolhido é a Águia')
    else:
        rep=input('O animal é um réptil?')
        if rep=='sim':
            casco=input('O animal tem casco? ')
            if casco=='sim':
                print('O animal escolhido foi a tartaruga')
            else:
                carn=input('O animal é carnívoro?')
                if carn=='sim':
                    print('O animal escolhido foi o Crocodílo')
                else:
                    print('O animal escolhido foi a Cobra')
print('fim de programa')
