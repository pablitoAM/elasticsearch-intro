#!/bin/bash
ELASTICSEARCH="https://search-es-pabloam-dev-mxxpwim667if6cpwf23yexsuey.eu-west-1.es.amazonaws.com"
INPUT="./data/AccidentesBicicletas_2017.cvs"
OLDIFS=$IFS
IFS=,
[ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
while read flname dob ssn tel status    #columns
do
    # curl -XPUT 
    echo "Fecha : $fecha"
    echo "DOB : $dob"
    echo "SSN : $ssn"
    echo "Telephone : $tel"
    echo "Status : $status"
    
done < $INPUT
IFS=$OLDIFS

clean_date(){

}

split_time(){

}

split_streets(){

}