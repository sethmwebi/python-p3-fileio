with open("log_file.txt", mode="w", encoding="utf-8") as log_file:
    log_file.write("Log 1")

with open("log_file.txt", mode="a", encoding="utf-8") as log_file:
    log_file.write("Log 2")
