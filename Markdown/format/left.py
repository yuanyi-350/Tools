def left(filename, start, end):
    with open(filename, "r", encoding="utf-8") as file:
        lines = [line for line in file]

    start -= 1
    end -= 1

    for i in range(start, end + 1):
        lines[i] = lines[i].replace('\\left', "")
        lines[i] = lines[i].replace('\\right', "")

    with open(filename, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line)