import os
import re


def timeStepExists(istep, outpath):
    for file in os.listdir(outpath):
        if file.endswith(".%05d.vtk" % istep):
            return True
    return False

def listTimeSteps(path):
    files = []
    tsteps = []
    for file in os.listdir(path):
        ret = re.search('XDMF\.([0-9]{1,})\.xmf$', file)
        if ret is not None:
            files.append(file)
            tsteps.append(int(ret.group(1)))
    return files, tsteps


VER = "20160110_01"

reprocessExistingModels = False

pathToModels = os.environ['VISIT_EXPORT_INDIR']
modelname = os.environ['VISIT_EXPORT_MODELNAME']

fullPath = os.path.join(pathToModels, modelname)

outfiles, outtsteps = listTimeSteps(fullPath)

nsteps = len(outtsteps)
print " *** Processing %d timesteps ..." % nsteps

outtsteps_sorted = [val for val in outtsteps]
outtsteps_sorted.sort()

rets = 0

for istep in outtsteps_sorted:
    i = outtsteps.index(istep)
    ifile = os.path.join(fullPath, outfiles[i])
    if (not reprocessExistingModels) and timeStepExists(istep, fullPath):
        print " *** Skipping! " + str(istep)
        continue
    print " *** Processing timestep %05d ..." % istep
    OpenComputeEngine()
    OpenDatabase(ifile)
    SetPipelineCachingMode(0)
    md = GetMetaData(ifile)

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
        dbAtts.filename = os.path.join(modelname, meshname + ".%05d" % istep)
        dbAtts.variables = tuple(exportVariables)
        ret = ExportDatabase(dbAtts)
        if ret == 0:
            rets = rets + 1
        DeleteAllPlots()
    CloseDatabase(ifile)
    CloseComputeEngine()

Close()
if rets > 0:
    print " *** Some errors occurred: " + str(rets)
dummy = raw_input("Press Enter to quit.")
quit()
