import subprocess

output = subprocess.run(["dir"], shell=True, capture_output=True)
print(output.stdout.decode("iso-8859-2")) # albo utf8

"""
podobnier jest w pliku ping.py

"""