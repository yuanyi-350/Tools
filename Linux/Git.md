1. 各种权限很头疼, 建议采用 gh 工具

   ```bash
   $ gh auth login
   $ gh auth status # 查看状态
   ```
   
3. `git clone`

   To use this project, first clone it to your local:

   ```bash
   $ git clone https://github.com/leanprover-community/mathlib4
   ```

3. 这里的 `mathlib` 是官方库 (`upstream`), 我并没有修改权限. 但是我可以 fork 一个自己的仓库 `yuanyi_mathlib` (`origin`)
   ```bash
   $ git remote rename origin upstream # upstream 指向 mathlib
   $ git remote add origin git@github.com:yuanyi-350/yuanyi_mathlib4.git
   # origin 指向 yuanyi_mathlib
   $ git remote -v
   origin  git@github.com:yuanyi-350/yuanyi_mathlib4.git (fetch)
   origin  git@github.com:yuanyi-350/yuanyi_mathlib4.git (push)
   upstream  https://github.com/leanprover-community/mathlib4 (fetch)
   upstream  https://github.com/leanprover-community/mathlib4 (push)
   ```

   例如出现这种问题时
   
   ```bash
   $ git remote -v
   origin  https://github.com/yuanyi-350/llm-from-scratch-assignment5-alignment (fetch)
   origin  https://github.com/yuanyi-350/llm-from-scratch-assignment5-alignment (push)
   upstream        https://github.com/stanford-cs336/assignment5-alignment (fetch)
   upstream        https://github.com/stanford-cs336/assignment5-alignment (push)
   $ git push
   remote: Permission to stanford-cs336/assignment5-alignment.git denied to yuanyi-350.
   fatal: unable to access 'https://github.com/stanford-cs336/assignment5-alignment/': The requested URL returned error: 403
   ```
   
   解决方案
   
   ```bash
   $ git push origin
   ```
   
4. `git branch` 查看本地已经存在的branch

   ```bash
   $ git branch
   * master
   ```

   查看远程的 branch
   ```bash
   $ git remote show origin
   Remote branches:
     Rudin_3.7
     close-range
     fourier
     master
   ```
   或者
   ```bash
   $ git branch -r
   ```

5. 切换branch (`git switch -c` 的用法)
  
   ```bash
   $ git switch -c new-feature # 基于**当前分支**创建 new-feature 分支, 并切换过去.
   ```
   
   ```bash
   $ git switch -c Rudin_3.7 origin/Rudin_3.7
   # 基于远程分支 origin/Rudin_3.7 创建本地分支 Rudin_3.7, 并设置上游跟踪关系 (用于第一次在本地创建 branch)
   $ git switch fourier # 需要本地已存在 fourier branch 
   ```
   
6. 创建branch

   ```bash
   $ git switch -c my-feature # 创建一个新的本地 branch my-feature, 并切换过去
   $ git push -u origin my-feature # 把本地的 branch 推到 origin
   # 如果当前在 my-feature branch, 则 git push -u origin HEAD 和上面作用完全一样, HEAD = 当前 branch
   ```
   
6. 删除branch

   ```bash
   $ git branch -d my-feature
   $ git branch -D my-feature # 强制删除
   ```
   
6. 同步官方仓库

   ```bash
   $ git switch master
   $ git pull upstream master # 等价于 git fetch upstream && git merge upstream/master
   ```
   
6. **提交代码**

   ```bash
   $ git status # 查看修改了哪些文件, 绿色的在暂存区(Staging Area), 红色的在工作区(Working Directory)
   On branch main
   Your branch is up to date with 'origin/main'.
   
   Changes to be committed:
   (use "git restore --staged <file>..." to unstage)
         new file:   cs336_basics/train_bpe.py
   
   Changes not staged for commit:
   (use "git add <file>..." to update what will be committed)
   (use "git restore <file>..." to discard changes in working directory)
         modified:   cs336_basics/train_bpe.py
   $ git add . # 把一些工作区的文件放入暂存区
   $ git commit -m "message" # 把暂存区的东西存档
   $ git push # 把暂存区的东西放入仓库(Repository)
   ```

   如果直接 `git commit` , 则会涉及 **vim 使用**: 先按 `Esc` (确保退出插入模式), 输入 `:wq` 然后回车 (一定要输入 `:` )

10. 撤销修改

   ```bash
   # 例如我把工作区的 file 一通魔改
   $ git restore file # 文件会变回最后一次 commit 时的状态
   # 例如有一个 commit 错了,
   $ git log # 查阅历史,找到你想回去的 commit hash, 例如 935d239
   $ git reset --hard 935d239 # 本地代码连同历史记录,彻底穿越回这个节点
   $ git push -f # 覆盖 origin
   ```

12. `git worktree` 

    为同一个仓库创建多个工作区

    传统做法 A: 在一个目录里频繁切换分支 + `stash` 

    - 痛点: 上下文切换重、容易漏 `stash` 或冲突、临时文件污染. 

    传统做法 B: 为每个并行任务再 `git clone` 一个仓库

    - 痛点: 占用更多磁盘/网络, 重复索引, 初次安装依赖/编译开销大. 

    worktree: 为每条工作流给一个目录, 互不影响, 无需频繁 `stash`. 共享对象库和索引, 创建/切换更快, 磁盘占用更低. 

    ```bash
    # 比如 master 上正在跑某个 code agent, 然后要去 feature-branch 修错误.
    $ git worktree add ../feature-branch-folder feature-branch
    $ git worktree list
    $ git worktree remove ../feature-branch-folder # 删除分身目录, 
    ```

     `git worktree prune` 清理非正常死亡的 worktree, 比如不小心用 `rm -rf ../feature-branch-folder` 把目录暴力删除, 用此办法清理而非 `remove`.
    
13. `git apply` 魔法

    ```bash
    $ git diff file > changes.diff # .diff 文件记录修改
    $ git apply changes.diff
    ```

2. 查看提交了哪些 PR

   ```bash
   $ gh pr list --author "@me" # 还开着的 PR
   $ gh pr list --author "@me" --state "all" # 所有的 PR
   $ gh pr list --author "@me" --limit 50 # 默认 30 条 PR
   ```
   
3. 切换到 PR 对应的 branch

   ```bash
   $ gh pr checkout 12345
   ```
