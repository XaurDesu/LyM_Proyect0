import tokenize as tkn


def input_taker():
    """
    este snippet de código permite ingresar varias lineas dentro de un mismo input, para luego
    utilizarlas una por una dentro de una estructura de datos 'List'.

    Input: None

    Output: list(str) -> exp
    """
    print("Por favor, entre su expresion (presione Ctrl+D (Windows) para guardarla.): \n")

    exp = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        exp.append(line)

    return exp


def blank_remover(lst):
    """
    Elimina las líneas vacías de una lista.

    Input: list 'lst'

    Output: None, las operaciones se hacen dentro de la list definida por input.
    """
    lst.remove("")
    for x in lst:

        if "\t" in x:
            x.replace("\t", "")
        print(x)


def token_maker(lst):
    ret = list(map(str.split, lst))

    return ret


def p0_landing():
    exp = input_taker()

    blank_remover(exp)

    tokenized_expression = token_maker(exp)
    print(tokenized_expression)
