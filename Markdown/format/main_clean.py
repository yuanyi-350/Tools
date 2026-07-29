from brace_simp import brace_simp
from frac_simp import frac_simp
import re

def replace_latex_symbols(input_str: str) -> str:
    correspond = {# 中文标点 -> 英文标点
                  "（": "(", "）": ")", "，": ", ", "．": ".",
                  "。": ". ", "；": "; ", "＂": "\"", "：": ": ", "－": "-",
                  # number fields
                  r"\mathbf{R}": r"\R", r"\mathbb{R}": r"\R", r"\boldsymbol{R}" : r"\R", r"\mathbb{Z}": r"\Z",
                  # functions
                  r"\operatorname{Ker}" : r"\ker", r"\operatorname{Im}" : r"\operatorname{im}",
                  r"\operatorname{dim}" : r"\dim", r"\operatorname{ker}" : r"\ker",
                  r"\operatorname{gcd}" : r"\gcd", r"\operatorname{det}" : r"\det",
                  r"\operatorname{deg}": r"\deg",
                  # others
                  r"\mid" : r"|", r"^{\prime}" : r"'", r"\leqslant": r"\le", r"\geqslant": r"\ge",
                  r"\ldots":r"\cdots", r"^{\prime \prime}" : r"''",
                  # arrows
                  r"\Longrightarrow" : r"\implies", r"\Rightarrow" : r"\implies",
                  r"\Longleftrightarrow": r"\iff", r"\rightarrow": r"\to", r"\Leftrightarrow" : r"\iff",
                  # \left< \right>
                  r"\left\langle": r"\left<", r"\right\rangle": r"\right>"}
    for old, new in correspond.items():
        input_str = input_str.replace(old, new)
    
    correspond_1 = {r"\langle": r"\left<", r"\rangle": r"\right>",
                    r"\leq": r"\le", r"\geq": r"\ge"}
    for old, new in correspond_1.items():
        input_str = input_str.replace(old, new)
    

    re_sub = {r"(?<!~)\sd\s*x": r"~dx"}
    for old, new in re_sub.items():
        input_str = re.sub(old, new, input_str)
    return input_str

def main_clean(filename):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    
    print(len(content), end = " -> ")
    content = replace_latex_symbols(content)
    
    lines = content.splitlines()
    length_cnt = 0

    for i, line in enumerate(lines):
        line = brace_simp(line)
        lines[i] = frac_simp(line).rstrip() + "\n"
        length_cnt += len(lines[i])

    print(length_cnt)

    with open(filename, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line)
