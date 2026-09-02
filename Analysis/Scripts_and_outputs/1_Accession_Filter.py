# This script will use a list of names to collect the files
# of interest from a directory and copy them to a new location

import os
import shutil
import argparse

############
## SCRIPT ##
def Accession_creator(file_name, list_name, extension):
    """
    Takes a .txt file containing a list of Accessions/IDs and returns a list 
    that can then be used to search through a directory of files
    
    file_name: the file that contains the accessions, each one seperated by a new line (\n)
    list_name: the name of the list that will have the accessions appended to
    extension: the extension that the files searching for may contain. Can put "NA" if this 
               is not needed
    """

    with open(file_name, "r") as accessions:
            for a in accessions:

                if extension == "NA":
                    formatted_a = a.strip("\n")
                    list_name.append(formatted_a)
                else:
                    formatted_a = a.strip("\n") + extension
                    list_name.append(formatted_a)
    print(f"Number of accessions found: {len(list_name)}")
def Collect_files(source_location, final_destination, file_name):
    """
    Using a file_name as a string, locate the file in a specified directory, then
    copy this file to a different directory

    source_location: The pwd of where the files of interest are located
    final_destination: The pwd of where you want the files to end up
    file_name: The file name that you are searching for in the source
               directory
    """
    for file in os.listdir(source_location):
        if file == file_name:
            source_file = os.path.join(source_location, file)
            destination_file = os.path.join(final_destination, file)
            shutil.copy(source_file, destination_file)
            print(f"[ {file} has been copied ]")
def script(name_of_accession_text_file, source_pwd, destination_pwd, file_extension_type):
     # Creating the list of files to search for from the accessions list
    print("====> Collecting IDs <====")
    accessions = []
    Accession_creator(name_of_accession_text_file, accessions, file_extension_type)

    # Using the generated list, collect the files and move them to a specified directory
    print("\n","====> Moving files <====")
    for a in accessions:
        Collect_files(source_pwd, destination_pwd, a)

    # Print out any files that were not found in the source directory
    print("\n","====> Checking for unfound files <====")
    found_files =[]
    found_files = os.listdir(destination_pwd)
    print(f"{len(found_files)}/{len(accessions)} found: Could not locate {len(accessions)-len(found_files)} file(s)")
    print(len(accessions)-len(found_files))

    # Show the files not found
    unique_files = set(found_files).symmetric_difference(set(accessions))
    print(f"====> These files were not found:\n")
    for f in unique_files:
        print("***",f, "***\n")

### ARG PARSER SETUP ###
def main():
    parser = argparse.ArgumentParser(description="Copies protein files to a new specified location based on a list of names")
    
    # Step 2: Define the expected arguments
    parser.add_argument('-names', type=str, required=True, 
                        help="A file.txt containing a list of names. They should not have an extension (e.g. .pdb)")
    parser.add_argument('-source', type=str, required=True, 
                        help="Source pathway directory where the collection of files are located")
    parser.add_argument('-destin', type=str, required=True, 
                        help="Destination pathway directory where the files will be copied to")
    parser.add_argument('-ext', type=str, required=True, 
                        help="File extension type: expected to be '.pdb' for this script")

    # Parse the arguments
    args = parser.parse_args()
    
    # Use the arguments in your script
    accessions = args.names
    destination_pwd_variable = args.destin
    source_pwd_variable = args.source
    file_extension = args.ext
    print("Collecting the files")
    
    # Your code logic here, e.g., reading from input_file and writing to output_file
    script(accessions, source_pwd=source_pwd_variable, destination_pwd=destination_pwd_variable, file_extension_type=file_extension)

if __name__ == "__main__":
    main()