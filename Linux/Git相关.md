# Git 相关



关闭 fast-forward 进行合并 `git merge --no-ff master `





删除分支`git branch -d rc_merge`

强制删除分支 `git branch -D rc_merge`



##### 检出远程分支到本地

1. **获取最新的远程分支列表**

   ```
   git fetch
   ```

   这将更新你的本地远程跟踪分支列表。

2. **检出远程分支**

   ```
   git checkout <branch_name>
   ```

   如果分支不存在于本地，Git 会自动创建一个新的本地分支，名为 `<branch_name>`，并将其设置为跟踪远程分支。