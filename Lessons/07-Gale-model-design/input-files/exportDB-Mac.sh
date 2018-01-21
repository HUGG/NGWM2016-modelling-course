#!/bin/bash
#
# exportDB.sh - A script to convert Gale output to VTK using VisIt
#
# dwhipp 01.16

# Set variables
export VISIT_EXPORT_INDIR=`pwd`
echo "Enter the model output directory name and press Enter: "
read VISIT_EXPORT_MODELNAME
export VISIT_EXPORT_MODELNAME
/Applications/VisIt.app/Contents/MacOS/VisIt -cli -nowin -s ./exportDB.py
