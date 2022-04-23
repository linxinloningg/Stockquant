import os

from tqdm import tqdm

file_dir = r'C:\Users\Administrator\Desktop\\Stockquant\\pystock'

for root, dirs, files in tqdm(os.walk(file_dir)):
    for file_name in files:
        path = root+"\\"+file_name
        
        with open(path,"w") as f:
            f.write(" ")
            f.close()