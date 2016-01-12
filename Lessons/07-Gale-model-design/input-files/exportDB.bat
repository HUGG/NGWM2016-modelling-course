@echo off

set VERSION="20160106_01"
set PATH_TO_VISIT="C:\Program Files\LLNL\VisIt 2.10.0\visit.exe"

set TMP_STORE_VAL=%VISIT_EXPORT_MODELNAME%

if not exist exportDB.py (
  echo exportDB.py not found!
  echo Copy exportDB.py to the same directory with %0 and re-run
  set /p DUMMY="Press enter to quit"
  exit
)

set VISIT_EXPORT_INDIR=%cd%
if exist "%1" set VISIT_EXPORT_MODELNAME="%1"
:WHILE_MODEL
if not exist "%VISIT_EXPORT_MODELNAME%" (
  set /p VISIT_EXPORT_MODELNAME="Give model name: "
  goto WHILE_MODEL
)
echo Running conversion ...
%PATH_TO_VISIT% -cli -nowin -s ./exportDB.py
set VISIT_EXPORT_MODELNAME=%TMP_STORE_VAL%
