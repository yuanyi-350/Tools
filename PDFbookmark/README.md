https://www.zhihu.com/question/344805337/answer/1116258929



② 添加书签/目录

准备一个 txt 文本文件（假设命名为 `toc.txt`），在其中手动录入需要添加的目录，或者从文本型 PDF 中直接复制出目录，采用类似下面格式即可：

```text
Introduction                            14
I. Interview Questions                            99
    Data Structures                            100
    Chapter 1 | Arrays and Strings                            100
        Hash Tables                            100
        StringBuilder                            101
    Chapter 2 | Linked Lists                            104
        Creating a Linked List                            104
        The "Runner" Technique                            105
    Additional Review Problems                            193
```

唯一的要求是每一行的最后一项是页码（前面的空白符个数不限），并且相同级别的书签要采用相同的缩进量（空格或 tab 都可以）。

> 【注意】如果是在 Windows 上创建 txt 文档的话，需要注意将文件保存为 **UTF-8** 编码格式，不然的话其中的汉字用第 ① 步的脚本读取出来就是乱码了。（Windows 上直接创建的 txt 文档一般默认都是 **ANSI** 编码格式）

---

然后在第 ① 步中创建的 `PDFbookmark.py` 所在目录下打开终端/命令提示符，运行以下代码即可：

> 其中最后一个参数 `9` 表示将 `toc.txt` 文件中的页码全部偏移 +9（即全部加上 9） 

```bash
python ./PDFbookmark.py '/Users/Emrys/Desktop/demo 2015.pdf' '/Users/Emrys/Desktop/toc.txt' 9
```

运行之后，会在要添加目录的 PDF 文件同目录下面生成一个新的 PDF 文件，名字为 `[原 PDF 文件名]-new.pdf`。 

演示效果如下：