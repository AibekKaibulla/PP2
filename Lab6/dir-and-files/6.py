# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

start_ch = 'A'
end_ch = 'Z'

start = ord(start_ch)
stop = ord(end_ch) + 1

for ch in range(start, stop):
    file_name = f"{chr(ch)}.txt"  
    with open(file_name, "w") as f:
        pass  
