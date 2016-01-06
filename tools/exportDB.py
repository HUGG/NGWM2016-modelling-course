import os

VER = "20160105_01"

pathToModels = os.environ['VISIT_EXPORT_INDIR']
modelname = os.environ['VISIT_EXPORT_MODELNAME']

fullPath = os.path.join(pathToModels, modelname)
pathToDatabase = os.path.join(fullPath, "XDMF.*.xmf")
pathToDatabase = pathToDatabase + " database"

OpenDatabase(pathToDatabase)
md = GetMetaData(pathToDatabase)

for istep in range(TimeSliderGetNStates()):
    print istep
    SetTimeSliderState(istep)

    for imesh in range(md.GetNumMeshes()):
        meshname = md.GetMeshes(imesh).name
        AddPlot("Mesh", meshname)
        DrawPlots()
        if md.GetMeshes(imesh).meshType == 2:
            # AVT_UNSTRUCTURED_MESH
            exportVariables = []
            for ivec in range(md.GetNumVectors()):
                if md.GetVectors(ivec).meshName == meshname:
                    exportVariables.append(md.GetVectors(ivec).name)
            for isca in range(md.GetNumScalars()):
                if md.GetScalars(isca).meshName == meshname:
                    exportVariables.append(md.GetScalars(isca).name)
        elif md.GetMeshes(imesh).meshType == 3:
            # AVT_POINT_MESH
            exportVariables = []
            for ivec in range(md.GetNumVectors()):
                if md.GetVectors(ivec).meshName == meshname:
                    exportVariables.append(md.GetVectors(ivec).name)
            for isca in range(md.GetNumScalars()):
                if md.GetScalars(isca).meshName == meshname:
                    exportVariables.append(md.GetScalars(isca).name)

        else:
            # unknown type 
            continue
        dbAtts = ExportDBAttributes()
        dbAtts.db_type = "VTK"
        dbAtts.filename = os.path.join(modelname, meshname + ".%04d" % istep)
        dbAtts.variables = tuple(exportVariables)
        ExportDatabase(dbAtts)
        DeleteAllPlots()

dummy = raw_input("Everything looks good. Press Enter to quit.")
quit()
