import arcpy 

arcpy.env.workspace = r"C:\arcgis\ArcTutor"

wslist= arcpy.ListWorkspaces()

for workspace in wslist :
    arcpy.env.workspace=workspace
    gdblist =arcpy.ListWorkspaces("", "FileGDB")
    print('{0} Contains {1}'.format(workspace , gdblist))
print(wslist)


class Find_GDB_In_Folders(arcpy):

    location = r"C:\arcgis\ArcTutor"
    arcpy.env.workspace = location
    wslist= arcpy.ListWorkspaces()






    def findgDB ():
        pass

