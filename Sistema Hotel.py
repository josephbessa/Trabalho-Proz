#Nome: Joseph Bessa e Marcos Martins
#Algoritimo simulando um sistema para locação de quarto de hotel.
#Declaração de um valor incial para as variáveis e importanto bibliotecas.
import random
import os
menuB = 1
menuA = 0
days = 0
discount = 0
#Tela de carregamento inicial com uma arte para simular ela
for count in range(5):
    print("                       .|")
    print("                       | |")
    print("                       |'|            ._____")
    print("               ___    |  |            |.   |' .---|")
    print("       _    .-'   '-. |  |     .--'|  ||   | _|    |")
    print("    .-'|  _.|  |    ||   '-__  |   |  |    ||      |")
    print("    |' | |.    |    ||       | |   |  |    ||      |")
    print(" ___|  '-'     '    ""       '-'   '-.'    '`        |____")

    print("                _           _       _ ")
    print("               | |         | |     | |")
    print("               | |__   ___ | |_ ___| |")
    print("               | '_ \ / _ \| __/ _ \ |")
    print("               | | | | (_) | ||  __/ |")
    print("               |_| |_|\___/ \__\___|_|")
    os.system('cls')
name = str(input("Bem vindo!!\n Qual seu nome? "))
#Enquanto não for satisfeito o valor de pessoas,irá se repitir
while menuB == 1:
    person = int(input(" Sua Reserva é para quantas pessoas? Aceitamos até 15 pessoas em um quarto  "))
    if person > 15:
        print("Número de pessoas excedido!!")
        menuB = 1
        os.system('cls')
    else:
        menuB = 0            
print("Olá "+ name+", temos planos de descontos para sua estádia em nosso hotel:\n A partir de 10 você ganha um desconto de 5% na sua fatura, caso fique 20 dias ou mais você irá ter 15%")
days = int(input("Quantos dias deseja ficar no hotel?  "))
#Se o valor de dias atender os requisitos será feito um desconto do total
if days >= 10 and days < 20:
        discount = 0.05
elif days >= 20:
        discount = 0.1
        os.system('cls') 
 #Menu para escolha de quartos,caso o valor de pessoas seja maior do que o do quarto i´ra se repitor a escolha e falará que o quarto não suporta.
 #Criada listas para atribuir o valor de acordo com a opção escolhida pelo usuário.        
while menuA == 0:        
    menuA = int(input("Qual tipo de quarto deseja ficar?\n 1 - Solteiro (1 Pessoas)\n 2 - Casal (Até 2 Pessoas)\n 3 - Solteiro duplo(Até 2 Pessoas)\n 4 - Suite Master (Até 4 Pessoas)\n 5 - Cobertura (Até 15 Pessoas)\n Digite o número da sua opção:  "))
    os.system('cls')  
    match menuA:
        case 1:
            if person > 1:
                print("Quarto não recomendado para esse número de pessoas!")
                menuA = 0
                os.system('cls') 
            else: 
                valor = 200
                roomservice = {'Café': [100], 'Café e almoço': [200], 'Tudo incluso': [350], 'Nenhum': [0]} 
                option = input("Qual serviço você deseja?(Café, Café e almoço, Tudo incluso, Nenhum): ")
                os.system('cls') 
                turism = {'Sim': [200], 'Não': [0]}
                optionA = input("Deseja traslado durante a estádia?(Sim/Não): ")
                os.system('cls') 
                valor = person *(days * (valor + roomservice[option][0] + turism[optionA][0]))
                discount = valor * discount
                valor = valor - discount
                print("                       .|")
                print("                       | |")
                print("                       |'|            ._____")
                print("               ___    |  |            |.   |' .---|")
                print("       _    .-'   '-. |  |     .--'|  ||   | _|    |")
                print("    .-'|  _.|  |    ||   '-__  |   |  |    ||      |")
                print("    |' | |.    |    ||       | |   |  |    ||      |")
                print(" ___|  '-'     '    ""       '-'   '-.'    '`        |____")

                print("                _           _       _ ")
                print("               | |         | |     | |")
                print("               | |__   ___ | |_ ___| |")
                print("               | '_ \ / _ \| __/ _ \ |")
                print("               | | | | (_) | ||  __/ |")
                print("               |_| |_|\___/ \__\___|_|")
                print("Valor da sua estádia será: R$ %s" %valor)
                print("O número do seu quarto será: %d " % random.randint(1,12))
                
        case 2:
            if person > 2:
                print("Quarto não recomendado para esse número de pessoas!")
                menuA = 0
                os.system('cls') 
            else: 
                valor = 250
                roomservice = {'Café': [100], 'Café e almoço': [200], 'Tudo incluso': [350], 'Nenhum': [0]} 
                option = input("Qual serviço você deseja?(Café, Café e almoço, Tudo incluso, Nenhum): ")
                os.system('cls') 
                turism = {'Sim': [200], 'Não': [0]}
                optionA = input("Deseja traslado durante a estádia?(Sim/Não): ")
                os.system('cls') 
                valor = person *(days * (valor + roomservice[option][0] + turism[optionA][0]))
                discount = valor * discount
                valor = valor - discount
                print("                       .|")
                print("                       | |")
                print("                       |'|            ._____")
                print("               ___    |  |            |.   |' .---|")
                print("       _    .-'   '-. |  |     .--'|  ||   | _|    |")
                print("    .-'|  _.|  |    ||   '-__  |   |  |    ||      |")
                print("    |' | |.    |    ||       | |   |  |    ||      |")
                print(" ___|  '-'     '    ""       '-'   '-.'    '`        |____")

                print("                _           _       _ ")
                print("               | |         | |     | |")
                print("               | |__   ___ | |_ ___| |")
                print("               | '_ \ / _ \| __/ _ \ |")
                print("               | | | | (_) | ||  __/ |")
                print("               |_| |_|\___/ \__\___|_|")
                print("Valor da sua estádia será: R$ %s" %valor)
                print("O número do seu quarto será: %d " % random.randint(13,24))
        case 3:
            if person > 2:
                print("Quarto não recomendado para esse número de pessoas!")
                menuA = 0
                os.system('cls') 
            else: 
                valor = 250
                roomservice = {'Café': [100], 'Café e almoço': [200], 'Tudo incluso': [350], 'Nenhum': [0]} 
                option = input("Qual serviço você deseja?(Café, Café e almoço, Tudo incluso, Nenhum): ")
                os.system('cls') 
                turism = {'Sim': [200], 'Não': [0]}
                optionA = input("Deseja traslado durante a estádia?(Sim/Não): ")
                os.system('cls') 
                valor = person *(days * (valor + roomservice[option][0] + turism[optionA][0]))
                discount = valor * discount
                valor = valor - discount
                print("                       .|")
                print("                       | |")
                print("                       |'|            ._____")
                print("               ___    |  |            |.   |' .---|")
                print("       _    .-'   '-. |  |     .--'|  ||   | _|    |")
                print("    .-'|  _.|  |    ||   '-__  |   |  |    ||      |")
                print("    |' | |.    |    ||       | |   |  |    ||      |")
                print(" ___|  '-'     '    ""       '-'   '-.'    '`        |____")

                print("                _           _       _ ")
                print("               | |         | |     | |")
                print("               | |__   ___ | |_ ___| |")
                print("               | '_ \ / _ \| __/ _ \ |")
                print("               | | | | (_) | ||  __/ |")
                print("               |_| |_|\___/ \__\___|_|")
                print("Valor da sua estádia será: R$ %s" %valor) 
                print("O número do seu quarto será: %d " % random.randint(25,36))
        case 4:
            if person > 4:
                print("Quarto não recomendado para esse número de pessoas!")
                menuA = 0
                os.system('cls') 
            else: 
                valor = 700
                roomservice = {'Café': [100], 'Café e almoço': [200], 'Tudo incluso': [350], 'Nenhum': [0]} 
                option = input("Qual serviço você deseja?(Café, Café e almoço, Tudo incluso, Nenhum): ")
                os.system('cls') 
                turism = {'Sim': [200], 'Não': [0]}
                optionA = input("Deseja traslado durante a estádia?(Sim/Não): ")
                os.system('cls') 
                valor = person *(days * (valor + roomservice[option][0] + turism[optionA][0]))
                discount = valor * discount
                valor = valor - discount
                print("                       .|")
                print("                       | |")
                print("                       |'|            ._____")
                print("               ___    |  |            |.   |' .---|")
                print("       _    .-'   '-. |  |     .--'|  ||   | _|    |")
                print("    .-'|  _.|  |    ||   '-__  |   |  |    ||      |")
                print("    |' | |.    |    ||       | |   |  |    ||      |")
                print(" ___|  '-'     '    ""       '-'   '-.'    '`        |____")

                print("                _           _       _ ")
                print("               | |         | |     | |")
                print("               | |__   ___ | |_ ___| |")
                print("               | '_ \ / _ \| __/ _ \ |")
                print("               | | | | (_) | ||  __/ |")
                print("               |_| |_|\___/ \__\___|_|")
                print("Valor da sua estádia será: R$ %s" %valor)
                print("O número do seu quarto será: %d " % random.randint(37,50))
        case 5:
            if person > 15:
                print("Quarto não recomendado para esse número de pessoas!")
                menuA = 0
                os.system('cls') 
            else: 
                valor = 1500
                roomservice = {'Café': [100], 'Café e almoço': [200], 'Tudo incluso': [350], 'Nenhum': [0]} 
                option = input("Qual serviço você deseja?(Café, Café e almoço, Tudo incluso, Nenhum): ")
                os.system('cls') 
                turism = {'Sim': [200], 'Não': [0]}
                optionA = input("Deseja traslado durante a estádia?(Sim/Não): ")
                os.system('cls') 
                valor = person *(days * (valor + roomservice[option][0] + turism[optionA][0]))
                discount = valor * discount
                valor = valor - discount
                print("                       .|")
                print("                       | |")
                print("                       |'|            ._____")
                print("               ___    |  |            |.   |' .---|")
                print("       _    .-'   '-. |  |     .--'|  ||   | _|    |")
                print("    .-'|  _.|  |    ||   '-__  |   |  |    ||      |")
                print("    |' | |.    |    ||       | |   |  |    ||      |")
                print(" ___|  '-'     '    ""       '-'   '-.'    '`        |____")

                print("                _           _       _ ")
                print("               | |         | |     | |")
                print("               | |__   ___ | |_ ___| |")
                print("               | '_ \ / _ \| __/ _ \ |")
                print("               | | | | (_) | ||  __/ |")
                print("               |_| |_|\___/ \__\___|_|")
                print("Valor da sua estádia será: R$ %s" %valor) 
                print("O número do seu quarto será: 51 ")                           



