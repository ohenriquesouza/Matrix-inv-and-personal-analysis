
|----------------|
|   using Pkg    |---> Essa parte deve ser adicionada no TERMINAL
|   Pkg.add("")  |
|----------------|

using XLSX

XLSX.openxlsx("planilha.xlsx", enable_cache = false) do f

    sheet = f["planilha"]
    
    StartingLine = "B"
    i = 2
    StartingColumn = "M"
    j = 13

    for r in XLSX.eachrow(planilha)
        
        Line = StartingLine * string(i)
        
        Column = StartingColumn * string(j)
        
        myMatrix = sheet["$Line:$Column"]
        
        println(inv((Float.(myMatrix))))
        
        i = i+1
        j = j+1

    end
end
