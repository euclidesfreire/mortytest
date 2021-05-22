#!/bin/bash

cls=clear


pause(){
 read -s -n 1 -p "Press any key to continue . . ."
 echo ""
}

create_folders_resultados(){
    
    folder=$1
    
    if [ ! -d $folder ]
    then
       sudo mkdir -m 777 -p $folder
    else
        echo "Diretorio ja exite!"
    fi
}

folders_resultados(){

    foldersArray[0]="resultados"
    foldersArray[1]="resultados/plots" 
    foldersArray[2]="resultados/plots/brasil.io"
    foldersArray[3]="resultados/plots/brasil.io/estados"
    foldersArray[4]="resultados/plots/brasil.io/estados/confirmados"
    foldersArray[5]="resultados/plots/brasil.io/estados/obitos"
    foldersArray[6]="resultados/plots/brasil.io/periodos"
    foldersArray[7]="resultados/plots/minsaude"
    foldersArray[8]="resultados/plots/minsaude/estados"
    foldersArray[9]="resultados/plots/minsaude/estados/confirmados"
    foldersArray[10]="resultados/plots/minsaude/estados/obitos"
    foldersArray[11]="resultados/plots/minsaude/periodos"
    foldersArray[11]="resultados/plots/minsaude/regiao"
    foldersArray[12]="resultados/plots/regcivil"
    foldersArray[13]="resultados/plots/regcivil/faixaetaria"
    foldersArray[13]="resultados/plots/regcivil/tipodedoenca"
    foldersArray[13]="resultados/plots/regcivil/estados"
    foldersArray[14]="resultados/plots/regcivil/estados/obitos"

    for i in "${foldersArray[@]}"; do 
       create_folders_resultados $i
    done
}



main()
{
    $cls

    #Creaye Folders Resultados
    folders_resultados
}

#Rum Main
main