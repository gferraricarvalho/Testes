import doctest
from datetime import datetime 

def get_date(date_input):
    """
    Calcula a diferença entre duas datas.

    Parameters
    ----------
    date_input : Data passada no formato conforme o exemplo: 28 de Agosto de 2023 - 18 de setembro de 2023
        
    Returns
    Retorna a diferença entre as datas!
    ----------
    
    >>> get_date("28 de Agosto de 2023 - 29 de Agosto de 2023")
    1
    
    >>> get_date("20 de Agosto de 2022 - 29 de Agosto de 2023")
    374
    
    """
    nlist_1 = [int(i) for i in date_input.split() if i.isdigit()]
    if len(nlist_1) != 4:
       raise(ValueError)
    
    months = {"Janeiro": 1, "Fevereiro":2, "Março":3, "Abril":4, "Maio":5, "Junho":6, "Julho":7, "Agosto":8, "Setembro":9, "Outubro":10, "Novembro":11, "Dezembro":12}
    nlist_2 = [str(j) for j in date_input.split() if j in months]
    if len(nlist_2) != 2:
       raise(ValueError)
    
    data_1 = datetime(nlist_1[1], months[nlist_2[0]], nlist_1[0])
    data_2 = datetime(nlist_1[3], months[nlist_2[1]], nlist_1[2])
    return(abs((data_1 - data_2).days))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
