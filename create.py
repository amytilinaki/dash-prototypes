import os
from random import randint

y=[range(1,101),range(101,201),range(201,301)]

parent=os.makedirs("rundata",exist_ok=True)

run_num=randint(1,3)

for i in range(1,run_num+1):
    for j in range(randint(1,2)):
        num=randint(0,2)
        f=open(os.path.join("rundata",(f"np04_run{i}_file_{num}.txt")),"w")
        for j in (y[num]):
            f.write(f"{str(j)}\n")