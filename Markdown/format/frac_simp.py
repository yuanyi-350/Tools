import re
from brace_simp import escaped_greek, brace_pair_pos

def frac_pos(line: str) -> list[int]:
    return [m.start() for m in re.finditer(r"frac", line)]

pattern = r"\{(\d|" + escaped_greek + r")\}"

def frac_simp(line : str) -> str:
    brace_pair = brace_pair_pos(line)
    for index in frac_pos(line):
        start = index + 4
        if start not in brace_pair:
            continue
        start = brace_pair[start] + 1
        if start not in brace_pair:
            continue
        end = brace_pair[start]
        content = line[start+1: end]
        if re.match(r"^(\w|" + escaped_greek + r")$",content):
            content = "\1" + content + "\0"
            line = line[:start] + content + line[end + 1:]
    line = re.sub("\1", "", line)
    line = re.sub("\0" + r"(?!\w)", "", line)
    line = re.sub("\0", " ", line)
    line = re.sub(f"frac{pattern}{pattern}", r"frac\1\2", line)
    line = re.sub(f"frac{pattern}", r"frac\1", line)
    return line
