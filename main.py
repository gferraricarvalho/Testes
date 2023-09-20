import SourceDate as sd

var = "null"

while(var != "3"):
    var = input("Opções:\n 1 - Input \n 2 - from file\n 3 - Sair\n")
    
    if var == "1":
        date_input = input()
        print("A diferença em dias entre as datas é: ",sd.get_date(date_input))
    elif var == "2":
        date_file = input()
        f = open(date_file)   
        print("A diferença em dias entre as datas é:", sd.get_date(f.read()))
    elif var == "3":
        break
    else:
        print("Entrada inválida\n")
        continue