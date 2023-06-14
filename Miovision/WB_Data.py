# Westbrook Miovision Data Pull and Processing
# Sebago Technics Signal Operations 2023 @Vraj Thakkar

# Import Library
from datetime import timedelta
import time

start = time.time()

# Importing Modules
from WB_Latest_File import get_latest_file
from WB_API_CSV_Data import Get_Data
from WB_Data_Mod import Data_Mod

print("Westbrook Miovision Signal Operations Data Process:")

folder_path = r"A:\Data Analytics\ME Westbrook\Miovision\Raw Data\Intersection Name"

# Call Methods

#0 Get Last File Pulled Info
get_latest_file(folder_path)

#1 Get Data through API Request to Miovision
Get_Data()

#2 Process and Transform Data for Power BI Report.
Data_Mod()

end = time.time() #End time when the execution ends
total = end - start #Total time elapsed for executing a folder
total = str(timedelta(seconds=total))
print("Total time elapsed:",total,'\nDone.')
