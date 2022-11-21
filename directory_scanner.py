import glob
from settings2 import data_path
import numpy as np
from loading import data

class Run_Directory_Scanner:

    def create(run_value,tr_value):
        path1=(f"{data()}/*")
   
        run_dir=glob.glob(f"{data()}/*")

        run_list=[]
        run_info={}
        for num in range(len(run_dir)):
            
            path=f"{path1}run{num}*"
      
            if glob.glob(path):
                run_list.append(num)
           
        for i in(run_list):
            path=f'{path1}run{i}*'
           
            a={}
                    
            for filename in glob.glob(path):

                with open(filename, 'r') as f:
                        
                    for line in f:
                        a= a |{f"tr {int(line)}":filename}

            run_info=run_info | {f"run {i}":a}

        return run_info[f"run {run_value}"][f"tr {tr_value}"]


      #Include init function?

    # include safety net