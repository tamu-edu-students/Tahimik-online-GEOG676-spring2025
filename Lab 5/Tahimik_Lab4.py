# Create a gdb and garage feature
import arcpy

arcpy.env.workspace = r'D:\actual homework\TAMU GIST\GEO676 - GIS PROGRAMMING\Module 4 -Fun with ArcPy\codes_env'
folder_path = r'D:\actual homework\TAMU GIST\GEO676 - GIS PROGRAMMING\Module 4 -Fun with ArcPy'
gdb_name = 'Test.gdb'
gdb_path = folder_path + '\\' + gdb_name
arcpy.CreateFileGDB_management(folder_path, gdb_name)

csv_path = r'D:\actual homework\TAMU GIST\GEO676 - GIS PROGRAMMING\Module 4 -Fun with ArcPy\garages.csv'
garage_layer_name = 'Garage_Points'
garages = arcpy.MakeXYEventLayer_management(csv_path, 'X', 'Y', garage_layer_name)

input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)
garage_points = gdb_path + '\\' + garage_layer_name

# Open campus gdb, copy building feature to our GDB
campus = r'D:\actual homework\TAMU GIST\GEO676 - GIS PROGRAMMING\Module 4 -Fun with ArcPy\Campus.gdb'
buildings_campus = campus + '\Structures'
buildings = gdb_path + '\\' + 'Buildings'

arcpy.Copy_management(buildings_campus, buildings)

# Re-projection
spatial_ref = arcpy.Describe(buildings).spatialReference
arcpy.Project_management(garage_points, gdb_path + '\Garage_Points_reprojected', spatial_ref)

garageBuffered = arcpy.Buffer_analysis(gdb_path + '\Garage_Points_reprojected', gdb_path + '\Garage_Points_buffered', 150)

arcpy.Intersect_analysis([garageBuffered, buildings], gdb_path + '\Garage_Building_Intersection', 'ALL')

arcpy.TableToTable_conversion(gdb_path + '\Garage_Building_Intersection.dbf', 'D:\\actual homework\TAMU GIST\GEO676 - GIS PROGRAMMING\Module 4 -Fun with ArcPy', 'nearbyBuildings.csv')