#!/bin/bash

cls=clear


pause(){
 read -s -n 1 -p "Press any key to continue . . ."
 echo ""
}

create_folders_resultados(){
    
    folder = $1

    if [ ! -d $folders ]
    then
        mkdir -m 777 -p $folder
    else
        echo "Diretorio ja exite!"
    fi
}

folders_resultados(){

    foldersArray = (
        "resultados"
        "resultados/plots" 
        "resultados/plots/brasil.io"
        "resultados/plots/brasil.io/estados"
        "resultados/plots/brasil.io/estados/confirmados"
        "resultados/plots/brasil.io/estados/obitos"
        "resultados/plots/brasil.io/periodos"
        "resultados/plots/minsaude"
        "resultados/plots/minsaude/estados"
        "resultados/plots/minsaude/estados/confirmados"
        "resultados/plots/minsaude/estados/obitos"
        "resultados/plots/minsaude/periodos"
        "resultados/plots/regcivil"
        "resultados/plots/regcivil/estados"
        "resultados/plots/regcivil/estados/confirmados"
        "resultados/plots/regcivil/estados/obitos"
        "resultados/plots/regcivil/periodos")

    for i in "${foldersArray[@]}"; do 
        create_folders_resultados $i
    done
}



main()
{
    #Creaye Folders Resultados
    folders_resultados
}

#Rum Main
main