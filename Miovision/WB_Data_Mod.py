# Westbrook Miovision Data Transformation
# Sebago Technics Signal Operations 2023 VT

def Data_Mod():
    
    # Importing Libraries
    from datetime import timedelta
    import pandas as pd
    import time
    import glob
    import os
    
    #start = time.time() #Start time when execution begins
    count = 0
    
    print("2. Data Processing and Transformation.\n")
    
    path_initialfiles = r"A:\Data Analytics\ME Westbrook\Miovision\Raw Data\Intersection Name\*.csv"
    path_finalfiles = r"A:\Data Analytics\ME Westbrook\Miovision\Power BI Input\2023\Intersection Name/"
    
    folder_name = path_initialfiles.split("\\")[4]
    print('Intersection:',folder_name)
    
    for fname in glob.glob(path_initialfiles): # Loop for Reading all files in the folder
        date_name=os.path.basename(fname).split(".")[0]
        if not os.path.exists(path_finalfiles+date_name+".csv"): #If a file does not exist in the folder then proceed
            print("Calculating GSEvents on file:",date_name)
            count += 1
            
            # read csv file into a pandas dataframe
            df = pd.read_csv(fname) 
                  
            # Rename the header of the DataFrame
            df.rename(columns={'timestamp': 'Timestamp','class':'Class','entrance':'Entrance','exit':'Exit', 'qty': 'Value'}, inplace=True)
            
            # Split the Timestamp column into date and time columns
            df[['Date', 'GSTime']] = df['Timestamp'].str.split('T', expand=True)
            
            # Move the date and time columns to the second and third columns
            df.insert(1, 'Date', df.pop('Date'))
            df.insert(2, 'GSTime', df.pop('GSTime'))
            
            # create new columns based on conditions of Entrance and Exit columns
            df['Data Type'] = ''
            df['Phase'] = ''
            
            # Add a new column intersection at the beginning of the DataFrame
            df.insert(0, 'Intersection', 'Main St at Columbus Ave')
            
            # Move the class column to the last column
            cols = list(df.columns)
            cols.append(cols.pop(cols.index('Class')))
            df = df[cols]
            
            # create dictionary mapping entrance and exit values to data types
            data_type_dict = {
                ('E', 'N'): 'Right Volume',
                ('E', 'S'): 'Left Volume',
                ('E', 'W'): 'Thru Volume',
                ('W', 'N'): 'Left Volume',
                ('W', 'S'): 'Right Volume',
                ('W', 'E'): 'Thru Volume',
                ('S', 'N'): 'Thru Volume',
                ('S', 'E'): 'Right Volume',
                ('S', 'W'): 'Left Volume',
                ('N', 'S'): 'Thru Volume',
                ('N', 'E'): 'Left Volume',
                ('N', 'W'): 'Right Volume',
            }
            
            # apply dictionary to entrance and exit columns to create data type column
            df['Data Type'] = df.apply(lambda x: data_type_dict.get((x['Entrance'], x['Exit']), ''), axis=1)
    
            # create dictionary mapping entrance and exit values to data types
            phase_type_dict = {
                ('E', 'N'): 6,
                ('E', 'S'): 1,
                ('E', 'W'): 6,
                ('W', 'N'): 2,
                ('W', 'S'): 2,
                ('W', 'E'): 2,
                ('S', 'N'): 4,
                ('S', 'E'): 4,
                ('S', 'W'): 7,
                ('N', 'S'): 8,
                ('N', 'E'): 3,
                ('N', 'W'): 8,
            }
            
            # apply dictionary to entrance and exit columns to create data type column
            df['Phase'] = df.apply(lambda x: phase_type_dict.get((x['Entrance'], x['Exit']), ''), axis=1)
            
            # write the updated dataframe to a new csv file
            df.to_csv(path_finalfiles+date_name+".csv", index = False) 
    
    #end = time.time() #End time when the execution ends
    #total = end - start #Total time elapsed for executing a folder
    #total = str(timedelta(seconds=total))
    print("Total Numbers of Files Calculated:",count) 
    #print("Total time elapsed:",total,'\nDone.')
    print("Done.\n")
