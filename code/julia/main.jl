using Pkg

Pkg.add("XLSX")

using XLSX

XLSX.openxlsx("planilha.xlsx", enable_cache = false) do f

    sheet = f["Sheet1"]

    for r in XLSX.eachrow(sheet)

        rn = XLSX.row_number(r)

        v1 = r[1]

        v2 = r[2]

        v3 = r["B"]

        v4 = r[4]

        println("v1=$v1, v2=$v2, v3=$v3, v4=$v4 ")

    end
end