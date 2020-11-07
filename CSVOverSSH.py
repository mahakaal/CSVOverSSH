import shlex, subprocess, sys
import csv

import pandas as pd
import numpy as np

command_line = input("inserire comando: ")
print(command_line)
args = shlex.split(command_line)

ssh = subprocess.Popen(args,
                            shell=False,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            universal_newlines=True,
                            encoding="ISO-8859-1")

# result = ssh.stdout.readlines()
# if result == []:
#     error = ssh.stderr.readlines()
#     print (sys.stderr, "ERROR: %s" % error)
# else:
#     print(result)

reader = csv.reader(ssh.stdout, delimiter='|')
rows = [row for row in reader]

# read_csv = [dict(zip(rows[0], row)) for row in rows[1:]]

# print(read_csv)

df = pd.DataFrame(np.array(rows[1:]), columns=rows[0])
print(df)