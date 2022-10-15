import pandas as pd
import time
import numpy as np

starting = time.time()

#file reading
aux = pd.read_excel(r"planilha.xls")

#matrix
default_matrix = np.zeros((12 , 12), dtype = np.float64)

#first column 'DATA' remove
aux = aux.drop('DATA', axis=1)

#data searching
i = 0

cont = 0

while(i+12 < 31):

    default_matrix[0:12, 0] = round(aux["ITSA4"][i:i+12], 2 )
    default_matrix[0:12, 1] = round(aux["BBDC4"][i:i+12], 2 )
    default_matrix[0:12, 2] = round(aux["USIM5"][i:i+12], 2 )
    default_matrix[0:12, 3] = round(aux["BRFS3"][i:i+12], 2 )
    default_matrix[0:12, 4] = round(aux["BVMF3"][i:i+12], 2 )
    default_matrix[0:12, 5] = round(aux["CMIG4"][i:i+12], 2 )
    default_matrix[0:12, 6] = round(aux["GGBR4"][i:i+12], 2 )
    default_matrix[0:12, 7] = round(aux["BBAS3"][i:i+12], 2 )
    default_matrix[0:12, 8] = round(aux["ITUB4"][i:i+12], 2 )
    default_matrix[0:12, 9] = round(aux["PETR4"][i:i+12], 2 )
    default_matrix[0:12, 10] = round(aux["VALE5"][i:i+12], 2 )
    default_matrix[0:12, 11] = round(aux["ABEV3"][i:i+12], 2 )

    isaNaN = np.isnan(default_matrix)

    print(isaNaN)

    #NaN validation
    if(isaNaN.any() == 0):

        determinante = np.linalg.det(default_matrix)

        determinante = round(determinante, 15)

        #is possible to invert
        if(determinante != 0):

            #numpy library inverse operation
            matrix_inv = np.linalg.inv(default_matrix)

            #user output
            print(matrix_inv)
            print("\n")
        #is not possible to invert  
        else:
            print("This matrix cannot be inverted!")
            cont = cont + 1

        i = i + 1
    else:
        print("Some value in your file is not a number")

        i = i + 1


print(cont)

print("%s" % (time.time() - starting))
