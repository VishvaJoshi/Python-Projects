import os

def bulk_rename(directory_path, prefix):
    
    os.chdir(directory_path)

 
    files = os.listdir()

    
    for index, file_name in enumerate(files):
       
        _, file_extension = os.path.splitext(file_name)

       
        new_name = f"{prefix}_{index + 1}{file_extension}"

        
        os.rename(file_name, new_name)
        print(f"Renamed: {file_name} -> {new_name}")


directory_path = "D:\Coding\python"
prefix = "activity"

bulk_rename(directory_path, prefix)
