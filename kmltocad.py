import arcpy
import os


with arcpy.EnvManager(scratchWorkspace=r"C:\Users\hanye\Desktop\kml",workspace=r"C:\Users\hanye\Desktop\kml"):
    arcpy.env.overwriteOutput=True
    kmls=arcpy.ListFiles("*.kml")
    for file in kmls:
        arcpy.conversion.KMLToLayer(r"C:\Users\hanye\Desktop\kml\{}".format(file),r"C:\Users\hanye\Desktop\kml\geodb","{}".format(file[0:8]), "NO_GROUNDOVERLAY")


arcpy.env.workspace= (r"C:\Users\hanye\Desktop\kml\geodb")
workspaces= arcpy.ListWorkspaces("*","FileGDB")


for ws in workspaces:
    gdb=arcpy.Compact_management(ws)

    arcpy.env.workspace = ws

    fds= arcpy.ListDatasets()
    listFC = []
    for fd in fds :
        arcpy.env.workspace = os.path.join( ws , fd)
        fcs= arcpy.ListFeatureClasses()
        listFC += fcs
        for fc in listFC:
            arcpy.ExportCAD_conversion(fcs,"DWG version 2007" , r"C:\Users\hanye\Desktop\kml\cad\{}.dwg".format(ws[-12:-4]),"USE_FILENAMES_IN_TABLES","OVERWRITE_EXISTING_FILES")




print("ALL DON GEOCODER")




    
