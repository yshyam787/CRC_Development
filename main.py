#This is the main python file for loading the configuration file and create tables in the database based on the data types explained in the file_configuration.json file. 

import json #for loading JSON files
import os #for file traversal
import pandas as pd

from config import ROOT_DIRECTORY, CONFIGURATION_JSON #import root directory and configuraiton.json file. 

#Step1: Load the file_configuration.json
with open(CONFIGURATION_JSON, "r") as json_file:
    files_info = json.load(json_file) #Getting the files information based on file_configuration.json

#Step2: Function to print CSV file contents to test out the results. 
def print_file_contents(file_path):
    """Reada and prints the head of the CSV files."""
    df = pd.read_csv(file_path)
    print(df.head())

#Step3: Loop through folders and files in file_configuration.json
for folder in files_info["folders"]:
    folder_path = os.path.join(ROOT_DIRECTORY, folder["folder_name"])
    print(f"\n Folder: {folder["folder_name"]}") #Print folder name

    #Print all files in the folder
    for file in folder["files"]:
        file_path = os.path.join(folder_path, file["file_name"])
        print(f"Found file: {file["file_name"]}")

        #Print file contents
        print_file_contents(file_path) #Prints the contents if it is CSV. 
