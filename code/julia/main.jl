using LinearAlgebra

using XLSX

@time begin

    XLSX.openxlsx("planilha.xlsx", enable_cache = false) do f

        sheet = f["Plan1"]
        
        StartingLine = "B"
        i = 2
        FinalColumn = "M"
        j = 13

        Line = StartingLine * string(i) #gambiarra para pular a linha 1
            
        Column = FinalColumn * string(j) #gambiarra para limitar o tamanho da matriz

        contador = 0

        for j in 13:31

            contador = contador + 1

            println(contador)
            
            myMatrix = sheet["$Line:$Column"]

            determinante = det(Float32.(myMatrix))

            if determinante != 0

                inversa = inv(Float32.(myMatrix))
                
                println(inversa)
                
                println("\n")
            
            else
                println("This matrix cannot be inverted!")

                i = i+1
            
            end

            i = i+1

        end

    end

end
