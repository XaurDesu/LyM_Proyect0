import tokenize as tkn

def p0_landing():
    exp = input("Por favor, entre su expresion: \n")
    exp_list = exp.split("\n")

    for x in exp_list:
        print(x)