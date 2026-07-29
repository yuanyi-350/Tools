from pathlib import Path
from openai import OpenAI

MODEL_NAME = "deepseek-v4-pro"

SYSTEM_PROMPT = """我将提供一个目录表。请你根据以下要求对目录进行重新整理和格式化：
1. 每一行的最后一项是页码, 页码只能是一个数字, 不要加括号
2. 相同级别的书签要采用相同的缩进量(即每章前面不加缩进, 每节前面加一个缩进, etc)
3. 对于所有的中文标点符号, 全部修改为相应的英文标点符号
4. 检查笔误并做最小修改
5. 只输出修改后的目录文本, 不要有任何总结和多余的文字

few-shot :
```text
第三章 数值微分与数值积分                            76
    §3.1 引言                            76
    §3.2 数值微分                            76
        3.2.1 Taylor 展开法                            76
        3.2.2 插值型求导公式                            80
    §3.3 数值积分                            82
        3.3.1 中点公式、梯形公式与 Simpson 公式                            82
        3.3.2 Newton-Cotes 求积公式                            85
        3.3.3 复合求积公式                            88
        3.3.4 加速收敛技术与 Romberg 求积方法                            91
        3.3.5 Gauss 求积公式                            97
        3.3.6 积分方程的数值解                            102
    习题三                            104
    上机习题三                            106
```
"""


def _parse_env(filepath):
    """Parse a .env file directly, without loading into environment variables."""
    config = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' in line:
                key, _, value = line.partition('=')
                config[key.strip()] = value.strip()
    return config


def main():
    _env = _parse_env(Path(__file__).parent / '.env')

    client = OpenAI(
        base_url=_env['URL'],
        api_key=_env['API_KEY'],
    )

    with open('TOC.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": text},
    ]

    resp = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
    )

    content = resp.choices[0].message.content
    print(content)

    with open('TOC-new.txt', 'w', encoding='utf-8') as file:
        file.write(content)


if __name__ == '__main__':
    main()
