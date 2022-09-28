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
while(i+12 < 6199):

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

    #NaN validation
    if(isaNaN.any() != 1):

        #is possible to invert
        if(np.linalg.det(default_matrix) != 0):

            #numpy library inverse operation
            matrix_inv = np.linalg.inv(default_matrix)

            #user output
            print("\n-----------------------------------------------------------------------------\n")
            print(default_matrix)
            print("\n#############################################################################\n")
            print(matrix_inv)
            print("\n-----------------------------------------------------------------------------\n")
        #is not possible to invert  
        else:
            print("This matrix cannot be inverted!")

        i = i + 1
    else:
        print("Some value in your file is not a number")
    
print("%s" % (time.time() - starting))