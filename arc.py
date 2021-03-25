
import arcpy
import os


with arcpy.EnvManager(scratchWorkspace=r"C:\\Users\\hanye\\Desktop\\kml", workspace=r"C:\\Users\\hanye\\Desktop\\kml" ):
    arcpy.env.overwriteOutput = True
    kmls=arcpy.ListFiles("*.kml")
    print("h")
    for file in kmls:
        arcpy.conversion.KMLToLayer(r"C:\\Users\\hanye\\Desktop\\kml\\{}".format(file), r"C:\Users\hanye\Desktop\kml\geodb", "{}".format(file[0:8]), "NO_GROUNDOVERLAY") 

print("--------------------------------------------------------------------------------------------------------------------")






arcpy.env.workspace = (r"C:\Users\hanye\Desktop\kml\geodb")

# List all file geodatabases in the current workspace
workspaces = arcpy.ListWorkspaces("*", "FileGDB")

for workspace in workspaces:
    # Compact each geodatabase
    gdb=arcpy.Compact_management(workspace)


    print(workspace)
    print(gdb)


    print("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
    arcpy.env.workspace = workspace

    # Use the ListFeatureClasses function to return a list of
    #  shapefiles.

    # Get list of polygon feature classes in FGDB
    
    fds = arcpy.ListDatasets()
    listFC = []
    for fd in fds:
        arcpy.env.workspace = os.path.join(workspace, fd)
        fcs = arcpy.ListFeatureClasses()
        listFC += fcs
        print (fcs)
        for fc in fcs:
            arcpy.ExportCAD_conversion(fcs, "DWG version 2007", r"C:\Users\hanye\Desktop\kml\cad\{}.dwg".format(workspace[-12:-4]), 
                           "USE_FILENAMES_IN_TABLES", "OVERWRITE_EXISTING_FILES")



print("ALL Don GEOCODER")








