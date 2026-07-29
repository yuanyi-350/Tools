from brace_simp import brace_pair_pos
import re

def match_pos(s, line_s: str) -> list:
    # 使用 re.escape() 来转义目标字符串中的反斜杠和其他特殊字符
    s = re.escape(s)
    return [match.start() for match in re.finditer(s, line_s)]

def style_simp(line_s : str, brace_pair : dict, target : str) -> str:
    # e.g. `target = "\\boldsymbol"` or `\\mathrm` or `\\mathbf`
    line = list(line_s)
    target += "{"
    for index in match_pos(target, line_s):
        start = index + len(target) - 1
        for i in range(index, start):
            line[i] = "\0"
        end = brace_pair[start]
        line[start], line[end] = "\0", "\0"
    return "".join(c for c in line if c != "\0")


def style(filename, start, end):
    with open(filename, "r", encoding="utf-8") as file:
        lines = [line for line in file]

    start -= 1
    end -= 1

    for i in range(start, end + 1):
        brace_pair = brace_pair_pos(lines[i])
        lines[i] = style_simp(lines[i], brace_pair, "\\mathrm")

        brace_pair = brace_pair_pos(lines[i])
        lines[i] = style_simp(lines[i], brace_pair, "\\mathbf")

        brace_pair = brace_pair_pos(lines[i])
        lines[i] = style_simp(lines[i], brace_pair, "\\boldsymbol")

    with open(filename, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line.rstrip()+"\n")
