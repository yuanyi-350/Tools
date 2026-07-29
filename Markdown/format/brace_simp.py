import re

greek_letters_with_slash : list[str] = [
    r"\alpha", r"\beta", r"\gamma", r"\delta", r"\varepsilon", r"\zeta", r"\eta", r"\theta",
    r"\iota", r"\kappa", r"\lambda", r"\mu", r"\nu", r"\xi", r"\omicron", r"\pi", r"\rho",
    r"\sigma", r"\tau", r"\upsilon", r"\phi", r"\chi", r"\psi", r"\omega",
    r"\Alpha", r"\Beta", r"\Gamma", r"\Delta", r"\Epsilon", r"\Zeta", r"\Eta", r"\Theta",
    r"\Iota", r"\Kappa", r"\Lambda", r"\Mu", r"\Nu", r"\Xi", r"\Omicron", r"\Pi", r"\Rho",
    r"\Sigma", r"\Tau", r"\Upsilon", r"\Phi", r"\Chi", r"\Psi", r"\Omega",
    r"\infty", r"\partial", r"\times"
]

escaped_greek = "|".join(re.escape(s) for s in greek_letters_with_slash)

def brace_simp(line : str):
    pattern = r"(_|\^)(?:\s*){(.|" + escaped_greek + r")}"
    return re.sub(pattern, r"\1\2", line)

def brace_pair_pos(line : str | list) -> dict:
    open_brace, brace_pair = [], {}
    for index, c in enumerate(line):
        if c == "{" and index > 0:
            open_brace.append(index)
        elif c == "}" and (index == 0 or line[index - 1] != "\\") and open_brace:
            brace_pair[open_brace.pop()] = index
    return brace_pair