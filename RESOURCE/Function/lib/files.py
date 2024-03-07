

MarkdownFilePath = ""


def ReadFileContent(filepath : str) -> list:
    global MarkdownFilePath
    MarkdownFilePath = filepath
    file = open(filepath, "r", encoding="utf-8")
    lines = file.readlines()
    file.close()
    return lines

def SaveFileContent( lines : list) -> None:
    file = open(MarkdownFilePath, "w", encoding="utf-8")
    file.writelines(lines)
    file.close()
