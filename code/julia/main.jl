using LinearAlgebra

using XLSX

@time begin

    XLSX.openxlsx("planilha.xlsx", enable_cache = false) do f

        sheet = f["Plan1"]
        
        StartingLine = "B"
        i = 2
        FinalColumn = "M"
        j = 13

        for j in 13:6199
            
            Line = StartingLine * string(i) #gambiarra para pular a linha 1
            
            Column = FinalColumn * string(j) #gambiarra para limitar o tamanho da matriz
            
            myMatrix = sheet["$Line:$Column"]

            if det(Float64.(myMatrix)) != 0

                
                println(inv((Float64.(myMatrix))))
                println("###############################################################################################################################")
            
            else
                println("This matrix cannot be inverted!")
            
            end

            i = i+1

        end

    end

end