with open("lower_to_upper1.txt","w+") as f:
    f.write("I am coding now\nI am doing it because I like it")
    f.seek(0)
    data=f.read().upper()

with open("lower_to_upper2.txt","w") as f:
    f.write(data)