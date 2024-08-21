dic1 = {
    'x': 10,
    'y': 20,
}

dic2 = dic1 # Dic2 aponta no mesmo lugar que dic1
            # Se Dic2 recebe alteração, dic1 também recebe
            # Pois Dic2 aponta para Dic1

dic2 = dic1.copy() # Todos valores mutaveis são copiados do Dic1 para Dic2
                    # Dic2 se torna uma cópia de Dic1
                    # Caso Dic2 for alterado, Dic1 não será
