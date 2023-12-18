# 查看分支里文件

你可以使用以下命令来查看特定分支内的文件：

```bash
git ls-tree -r <branch-name>
```

将`<branch-name>`替换为你想要查看的分支的名称。执行这个命令后，会列出该分支内的所有文件和目录。



# 删除特定文件

看起来你想要删除Test1/1.txt这个文件，你可以使用以下命令来删除该文件并提交更改：

```bash
git rm Test1/1.txt
git commit -m "Remove Test1/1.txt"
git push origin <branch-name>
```

请将`<branch-name>`替换为你要推送到的分支名称。执行这些命令后，Test1/1.txt文件将被删除并且更改会被推送到远程仓库。



# 同步改动到分支

要将main分支的内容同步到教程分支，你需要执行以下步骤：

首先，确保你在本地main分支上，并且拉取了最新的更改：

```bash
git checkout main
git pull origin main
```

然后，切换到教程分支并合并main分支的内容：

```bash
git checkout 教程
git merge main
```

如果有冲突，需要解决冲突后再进行提交。

最后，将教程分支的更改推送到远程仓库：

```bash
git push origin 教程
```

这样就可以将main分支的内容同步到教程分支了。



