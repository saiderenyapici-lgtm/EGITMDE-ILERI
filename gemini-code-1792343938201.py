import os

def list_files(start_path):
    files_list = []
    for root, dirs, files in os.walk(start_path):
        for file in files:
            files_list.append(os.path.join(root, file))
    return files_list

print("Frontend files:", list_files('/app/frontend'))
print("Backend files:", list_files('/app/backend'))