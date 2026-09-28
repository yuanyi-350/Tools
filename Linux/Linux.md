### 基础

```bash
$ sudo reboot # 重启
$ sudo shutdown # 1 min 后关机
$ sudo shutdown -c # 取消关机
```

##### 命令行

`Ctrl + Alt + T` 启动 , `Ctrl + D` 关闭 , `clear` 清空命令行.

`Ctrl+R` 搜索 `bash_history` , 自动补全.

##### 查看文档

```bash
$ ls --help | more
$ man rg | more # man 的 docstring 会非常长, more 用来翻页
$ man rg | less # less 比 more 更强, 可以上下翻页, 搜索, 跳转
```

示例

```
SYNOPSIS
       mawk [-W option] [-F value] [-v var=value] [--] 'program text' [file ...]
       mawk [-W option] [-F value] [-v var=value] [-f program-file] [--] [file ...]
```

| 写法         | 含义                                                         |
| ------------ | ------------------------------------------------------------ |
| `[xxx]`      | 可选，可以写也可以不写                                       |
| `...`        | 可以有多个                                                   |
| `[file ...]` | 可以跟一个或多个输入文件                                     |
| `--`         | 表示选项结束，后面的内容不再当作选项解析, 见下面 `rg` 的案例 |

##### 软件安装与卸载

```bash
$ sudo apt install ./package.deb # 安装
$ sudo apt purge <name> # 卸载
```

### 文件系统

```bash
$ touch ~/file # 新建文件
$ cmp file1 file2 # 比较两个文件, 无输出表示二者完全相同
$ head -n 5 filename.txt # 显示前5行
```

`Ctrl + O` 保存文本, `Enter` 确认, `Ctrl + X` 回退到terminal

`cd` , `mv` , `cp` , `mvdir` , `cat` , `rm my_file` 删除文件 ,  `rmdir` 只能删除空目录 ,  `rm -rf my_dir ` 删除目录

`ls /data` 可以直接查看 `/data` 的结构, 而不用 `cd` 更换目录.

`df -h` 查看磁盘空间

```bash
yuanyi@kubuntu:~$ du -sh ~/.elan # 仅显示总计大小, 不列出每个子目录
5.1G    /home/yuanyi/.elan
yuanyi@kubuntu:~$ du -h ~/.elan -d 1 # 限制显示的目录深度最多递归 1层
13M     /home/yuanyi/.elan/bin
5.1G    /home/yuanyi/.elan/toolchains
4.0K    /home/yuanyi/.elan/tmp
5.1G    /home/yuanyi/.elan
yuanyi@kubuntu:~$ du -ah ~/.elan -d 1 # 显示所有文件的大小, 而不仅仅是目录
4.0K    /home/yuanyi/.elan/settings.toml
13M     /home/yuanyi/.elan/bin
5.1G    /home/yuanyi/.elan/toolchains
4.0K    /home/yuanyi/.elan/known-projects
4.0K    /home/yuanyi/.elan/tmp
4.0K    /home/yuanyi/.elan/env
5.1G    /home/yuanyi/.elan
```

`/` 开头的地址表示绝对地址, 其他开头的为相对地址,  `.` 表示当前目录, `..` 表示 parents 目录, `~` 表示家目录(见下面的例子)

```bash
stu2400010766@lfs-dev:/home$ ls
sifer          stu2400010766  stu2400014903    ubuntu # 一台机器可能会有多个用户
# 在其他地方 cd ~ 会回到 /home/stu2400010766 , 也就是我的家
```

##### vim and nano

```bash
$ nano ~/file # 编辑文件, 如果没有则会创建文件
# Ctrl + W 搜索 PAT, 然后 Alt + W 跳转到下一个 PAT
$ code -g ~/file:123 # 跳转到文件的 123 行
$ vim ~/file # 编辑文件规则和 nano 一样
# 最初是指令模式, 按 `i` 进入编辑模式, 底部出现-INSERT-字样, 可输入除[Esc]以外的任意字符 
# 编辑完毕后, 按 [Esc] 进入指令模式, 此时底部-INSERT-字样消失
# 输入 `:wq` (一定不要忘记 `:`) 存盘(write) 并退出(quit)
# `:q` 即代表直接离开

# /PAT 搜索关键词
# 指令模式中 `h`, `j`, `k`, `l` 表示光标分别向左, 下, 上, 右移动
# `5j` 或者 `5[Down]`即表示向下移动5行
# 指令模式中 `x` 表示向后删除一个字符, `X` 表示向前删除一个字符
# 指令模式中 `dd` 删除光标所在行, `3dd` 表示删除后面的 3 行
# `d$` 表示删除光标到结尾
# 指令模式中 `yy` 表示复制光标所在行, `3yy` 表示复制后面的 3 行
# 指令模式中 `p` 表示将已复制的数据在光标下一列贴上, P 则为贴在光标上一列
```

##### 文件权限

User, Group, Others 三种身份

read, write, execute 三种权限

`ls -al` 查看文件属性

文件属性为一个10位字符, 第一位表示文件类型; 后面分成三段, 分别是三种身份的三种权限

例如, `[-][rwx][r-x][r--]` 表示User 全部权限, Group可读可执行, Others 可读

改变权限 : `chmod`  , `[r:4] > [w:2] > [x:1]`

例如 `chmod 777 file` 就表示把 `file` 的权限变成所有人均可读, 可写, 可执行.

##### 搜索内容

```bash
$ grep -ir "error" /path/to/directory/ # 搜索文件内容, -i表示忽略大小写, -r表示递归的搜索目录
$ vim regular_express.txt
"Open Source" is a good mechanism to develop programs.
My god!
google is the best tools for search keyword.
goooooogle yes!
go! go! Let's go
$ grep -nP "[^g]oo" regular_express.txt # -P 兼容 Perl 兼容正则表达式（PCRE）, -n 输出行号
3:google is the best tools for search keyword.
4:goooooogle yes!
```

##### `ripgrep` (`rg`)

推荐用 `ripgrep` (`rg`) 更快的搜索. 自动忽略 `.gitignore`

```bash
$ rg "TODO" Mathlib/
$ rg --files Mathlib/ # 输出所有 Mathlib 目录下的文件名
$ rg --files Mathlib/ | wc -l # 统计 Mathlib 目录下有多少个文件, 其中 wc 是 word count 的简写, -l 表示多少行
$ rg -C 5 "PAT" # 把匹配到的那一行上面 5 行和下面 5 行都打印出来, --context
$ rg -B 5 "PAT" # 只打印上面 5 行, --before-context
$ rg -A 5 "PAT" # 只打印下面 5 行, --after-context
```

`rg` 默认把搜索内容当作正则表达式。`-F` (`--fixed-strings`) 表示按普通字符串匹配，不解释其中的 `"`, `.`, `[`, `*` 等字符。

```bash
$ rg -F '.lean' data.log # 搜索字面量 ".lean", 而非 regex 匹配
$ rg "-t" data.log # 出现报错 "rg: ripgrep requires at least one pattern to execute a search"
$ rg -- "-t" data.log # -- 表示后面的内容都不要再当成选项.
```

##### `fd`

```bash
$ fd "nginx"
$ fd -e py
```

##### `sed`

```bash
$ sed -n '1000p;1000q' data.jsonl # 只输出文件的第 1000 行，然后立刻退出。
```

##### `jq`

JSONL 每行是一条独立的 JSON 记录。用 `sed` 抽取指定行进行质检

```bash
$ sed -n '1000p;1000q' data.jsonl | jq '.' # 查看第 1000 条记录
$ head -n 5 data.jsonl | jq '.,"========="' # 将条目与条目直接分割
```

`-n` 关闭默认输出，`1000p` 打印第 1000 行，`1000q` 随即退出，不会继续扫描文件的剩余部分。

### SSH的使用

```bash
$ ls ~/.ssh
$ cat ~/.ssh/id_rsa.pub # 查看密钥
$ cat ~/.shh/id_ed25519.pub # 查看密钥
```

##### 登陆

```bash
$ ssh -i /path/to/your_specific_private_key username@server_ip
$ vi ~/.ssh/config
Host my_borrowed_server
    HostName 192.168.1.100       # 服务器的 IP
    User target_user
    IdentityFile /path/to/your_specific_private_key
```

##### 传输文件

```bash
$ scp file.txt user@remote_host:/path/to/destination/
$ scp -r mydir user@remote_host:/path/to/destination/ # 建议先压缩文件再传zip
# 例如我登陆服务器用 ssh -p 31084 stu2400010766@connect.westd.seetacloud.com 
$ scp -P 31084 file.zip stu2400010766@connect.westd.seetacloud.com:/home/stu2400010766/
```

##### 压缩与解压

```bash
$ tar -czvf archive.tar.gz file1 file2 file3
$ tar -czvf backup.tar.gz /path/to/directory/ # 压缩包名称为 backup.tar.gz, 只有一个 directory 目录
```

其中 `c` 表示打包, `z` 表示使用 gzip 压缩, `v` 表示显示详细过程(可选), `f` 表示导出文件(否则会在terminal中输出二进制编码)

```bash
$ tar -xzvf archive.tar.gz # 解压到指定目录
$ tar -xzvf archive.tar.gz -C /path/to/target/directory
```

`-f` 的后一个参数必须是文件名, 即 `tar -czvf backup.tar.gz /path/to/directory/` 合法, 

但是 `tar -cfzv backup.tar.gz /path/to/directory/` 却会出错(会产生一个名为 `zv` 的文件)

对于zip文件, 直接

```bash
$ zip -r archive.zip my_dir/
$ zip -r package.zip path/to/project/ -x "*/.venv/*" "*/__pycache__/*" 
$ unzip archive.zip # 解压缩
```

##### 使用 `curl` 下载文件

```bash
$ curl -L "https://example.com/report.pdf" -o report.pdf # 跟随重定向，并将文件保存为 report.pdf
$ curl -L -O "https://example.com/report.pdf" # 跟随重定向，并使用 URL 中的原文件名 report.pdf
```

- `-L` (`--location`)：自动跟随 HTTP 301、302 等重定向，下载链接会跳转时需要使用。
- `-o` (`--output`)：使用自己指定的文件名保存；后面必须跟文件名，例如 `-o report.pdf`。
- `-O` (`--remote-name`)：使用 URL 末尾的原文件名保存，例如 URL 以 `report.pdf` 结尾时保存为 `report.pdf`。

`-o` 和 `-O` 通常二选一。若 URL 末尾没有明确的文件名，例如 `https://example.com/download?id=123`，建议使用 `-o report.pdf`。

##### 硬链接与软连接

| 特性         | 软链接 `ln -s`                             | 硬链接 `ln`              |
| ------------ | ------------------------------------------ | ------------------------ |
| 本质         | 类似 Windows “快捷方式” , 可指向不存在目标 | 同一文件数据的另一个名称 |
| 原文件被删除 | 失效                                       | 仍可正常访问数据         |
| 跨文件系统   | 可以                                       | 不可以                   |
| 链接目录     | 可以                                       | 通常不允许               |

### 进程

##### 终端复用器 `tmux`

需要先用 codex 设置可以用鼠标滚动翻页.

```bash
$ python script.py    # 程序正常执行, 终端会被这个程序占用, 直到程序结束你才能继续输入别的命令.
$ tmux new -d -s train "python train.py" # 也可以用 tmux -d 达成同样效果
```

```bash
$ tmux new -s yuanyi_train # 创建 yuanyi_train 会话, 进入一个新的窗口, 在里面输入命令 uv run ...
# 按住键盘上的 Ctrl + B (告诉 tmux , 下一个要按的键是给 tmux 的命令, 不是给里面运行的程序的)
# 松开所有键, 按一下 D 键 (代表 Detach), 这样退出 Tmux 界面回到普通 terminal
[detached (from session yuanyi_train)] #说明任务已在后台安全运行, 可以去睡觉了
$ tmux ls # 睡醒后查看后台所有任务
yuanyi_train: 1 windows (created Fri Jan 30 01:01:15 2026)
$ tmux attach -t yuanyi_train # 回到 tmux 界面
$ tmux att -t yuanyi_train # 同上
# 在 session 内部输入 exit 即可清除这个 session, 或者
$ tmux kill-session -t <session_name>
```

##### 进程查询

```bash
$ ps aux | rg 'lake'
yuanyi	1234	....
....
$ kill 1234
```

##### 终止进程

```bash
$ pkill -TERM -x lean # -x 表示进程名必须完全匹配，不会匹配 clean
```

### Shell 脚本

##### 变量赋值与取用

变量的赋值

```bash
$ export file="data.txt" # 子进程中会继承环境变量
$ file="data.txt" # 局部变量, 仅当前 Shell 进程生效
# 错误写法, 等号两侧不要有空白 ===>
$ file = "data.txt"
```

变量的取用

```bash
$ echo "$file"
```

##### 循环遍历目录

```bash
$ directory="/path/to/your/directory"
$ for file in "$directory"/*; do
>   # 等同于 test -e "$file" || continue
>   [ -e "$file" ] || continue
>   
>   # 等同于 if test -f "$file"; then
>   if [ -f "$file" ]; then # 条件判断符, -e 表示判断是否存在, -f 表示判断是否是文件
>       echo "$file"
>       git apply "$file" || continue
>   fi
> done
```

##### 管道与重定向 (Pipes & Redirections)

Linux 中每个程序默认有三个数据流: stdin(0, 键盘), stdout(1, 屏幕), stderr(2, 屏幕)。

```bash
$ python script.py &  # & 表示后台运行, 可以继续输入别的命令, 但运行日志依然会满屏幕乱跳.
$ python script.py > script.log 2>&1 & # stdout(1)写进log, stderr(2)也重定向到(1)
# &1 表示这里的 1 指的是 1 号管道, 而不是一个名字叫 '1' 的文件. 
$ python script.py > /dev/null 2>&1 & # 定向到 /dev/null 的内容会被系统直接丢弃, 不留痕迹, 相当于完全舍弃日志.
$ nohup cmd > service.log 2>&1 & # 类似tmux, 忽略 SIGHUP 信号, 终端关闭程序继续运行.
# 注意: 用 nohup 后台运行的程序, 要停止只能通过 ps aux 查 PID, 然后 kill <PID>
```

`>`  / `>>`：控制往哪写 。`>` 是覆盖, `>>` 是追加。

 `<` / `<<`：控制从哪读。`<` 是读文件, `<<` 是读多行文本块。

 `<< EOF`：heredoc, 把多行文本喂给命令

```bash
$ cat >> /home/user/myconfig.txt << 'EOF'
PATH="$PATH:/usr/local/bin"
export MY_VAR="hello world"
EOF
```

```bash
# 完全等价的写法, 更好看
$ cat << 'EOF' >> /home/user/myconfig.txt
PATH="$PATH:/usr/local/bin"
export MY_VAR="hello world"
EOF
```

这里面 `'EOF'` 可以保证写入是 `PATH="$PATH:/usr/local/bin"`

如果用 `EOF` 则可能写入是 `PATH="/usr/bin:...:/usr/local/bin"` 

```bash
$ python - << EOF
print("x")
EOF
x
```

`<<- EOF`: 允许 heredoc 内容缩进

```bash
$ python - <<- 'EOF'
def add(a, b):
    return a + b
print(add(1, 2))
EOF
3
```

**管道符 `|` (连接多个命令)** 将前一个命令的stdout直接连到后一个命令的stdin.

```bash
$ ps aux | grep python # 找出所有进程, 并把结果喂给 grep 去过滤出含有 python 的行
$ ls -al | head -n 5 # 查看当前目录详细列表, 过滤后只显示前 5 行
$ cat my.log | grep "error" | wc -l # 统计日志文件里 "error" 出现了多少行
```

**`xargs`**

``` bash
$ rg -l sorry ArxivSolutions -0 | xargs -0 rm # -0 = --null：给打印出来的路径后面加一个 NUL 字节, 
# 用于避免文件名中有空格造成错误
$ rg --files -z -g '*.lean' ArxivSolutions | xargs -0 wc -l | sort -n | tail -20   # 找最大的文件
```

### 桌面端

##### 图形化界面

`Alt+Space` 将窗口Always On Top

##### 双系统安装

参考 : [从零开始：Ubuntu 24.04 LTS + Win11双系统安装教程 - 知乎](https://zhuanlan.zhihu.com/p/1975303563619098675)

建议150G以上磁盘空间

- 然后安装完后Linux时间会是UTC+0, 需要

    ```bash
    $ timedatectl set-local-rtc 1 --adjust-system-clock
    $ timedatectl # 输出结果中有 RTC in local TZ: yes 则设置成功
    ```

    重启电脑, 选择进入 Windows, 此时 Windows 的时间可能还是错的, 右键点击右下角的时间 -> "调整日期/时间" -> 点击 "立即同步"

**安全使用双系统共享文件夹**

必须关机切换系统, 而不要休眠模式, 以免一个系统可能还有数据在缓存中未写入磁盘.

**设置开机自启动**

```bash
$ nano ~/.config/autostart/ggdd.desktop
[Desktop Entry]
Type=Application
Exec=/home/yuanyi/data/Mathpix_Snipping.AppImage # 每次开机自动在bash中执行这条命令
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=Mathpix
```

设置 VPN 代理

```bash
export https_proxy=http://127.0.0.1:9674 http_proxy=http://127.0.0.1:9674 all_proxy=socks5://127.0.0.1:9674
```

##### VMware安装虚拟机

- 安装desktop版本(不要安装server版本)

- 留够40G硬盘, 并且存储在D盘

- password输入后并不会在terminal里显示出来

**图形界面**

```bash
$ sudo apt update
$ sudo apt install ubuntu-desktop
$ sudo apt install open-vm-tools-desktop
```

共享文件夹

```bash
$ sudo apt install open-vm-tools open-vm-tools-desktop
```

在 `/mnt/hgfs` 目录下

`Ctrl + Alt` 返回本机

##### ThinkPad T14p 硬件

`Fn + Space` 调节键盘亮度

然后建议安装 `TLP` 保护电池, 

```bash
$ sudo tlp fullcharge # 出门前充满电
$ sudo nano /etc/tlp.conf # 调节性能模式还是节能模式

PLATFORM_PROFILE_ON_AC=performance
CPU_ENERGY_PERF_POLICY_ON_AC=balance_performance

PLATFORM_PROFILE_ON_BAT=low-power
CPU_ENERGY_PERF_POLICY_ON_BAT=power

$ sudo tlp start # 让配置生效
$ sudo tlp-stat -p # 查看配置
```
