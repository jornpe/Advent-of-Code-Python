with open("output.txt", "w") as file:
    for line in ["Hey there!", "LearnPython.com is awesome!"]:
        file.write(line + '\n')
