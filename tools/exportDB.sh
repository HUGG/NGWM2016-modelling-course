#!/bin/bash
PATH_TO_VISIT="/bulk/lkaislan/software/visit2_10_0.linux-x86_64/bin/visit"

export VISIT_EXPORT_INDIR=`pwd`
VISIT_EXPORT_MODELNAME=""

read -e -p "Enter model output directory: " VISIT_EXPORT_MODELNAME
while [ ! -d "$VISIT_EXPORT_MODELNAME" ]
do
    echo $VISIT_EXPORT_MODELNAME is not a directory.
    read -e -p "Enter model output directory: " VISIT_EXPORT_MODELNAME
done
export VISIT_EXPORT_MODELNAME

$PATH_TO_VISIT -cli -nowin -s ./exportDB.py
