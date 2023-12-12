# Git的使用

[TOC]

## **零、github导入/gitee导入RSA密钥**

**生成rsa密钥**

![image-20231212090458618](C:\Users\Asus\AppData\Roaming\Typora\typora-user-images\image-20231212090458618.png)

```
生成SSH密钥是连接你的本地计算机与远程存储库（如GitHub）的一种常见方式。以下是在命令行中生成SSH密钥的步骤：

打开命令行工具（如Git Bash、PowerShell或终端）。
输入以下命令来生成新的SSH密钥：
bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
在这个命令中，"your_email@example.com" 应该替换为你在GitHub上注册的电子邮件地址。你也可以选择不输入邮箱地址，直接按Enter键跳过。
系统会提示你选择SSH密钥的保存位置，默认情况下是在/home/username/.ssh/目录中。你可以选择使用默认位置，也可以选择自定义的位置。
在提示下，输入一个安全密码来保护你的SSH密钥。这个密码会在你使用SSH密钥时需要输入。
生成密钥后，你会收到一条消息，其中包含你的新的SSH密钥的指纹和密钥的位置。默认情况下，公钥保存在/home/username/.ssh/id_rsa.pub，私钥保存在/home/username/.ssh/id_rsa。
最后，将公钥内容复制到你的GitHub账户中。你可以使用以下命令来打印公钥内容：
bash
cat ~/.ssh/id_rsa.pub
复制输出的内容，然后在GitHub的设置中添加SSH密钥。
完成以上步骤后，你的新的SSH密钥就已经生成并且添加到你的GitHub账户中了。希望这些步骤能够帮助你成功地生成SSH密钥。如果你有其他问题或需要进一步的帮助，请随时告诉我。我会尽力协助你。
```

**打开gitee**

![image-20231212090255285](C:\Users\Asus\AppData\Roaming\Typora\typora-user-images\image-20231212090255285.png)

![image-20231212090319721](C:\Users\Asus\AppData\Roaming\Typora\typora-user-images\image-20231212090319721.png)

![image-20231212090357803](C:\Users\Asus\AppData\Roaming\Typora\typora-user-images\image-20231212090357803.png)



## **一、克隆库**

**在任意地方新建文件夹**



**在文件夹内，也就是文件栏框，输入cmd**

![image-20231212085430209](C:\Users\Asus\AppData\Roaming\Typora\typora-user-images\image-20231212085430209.png)

**命令里输入**

**没有vpn就用第一行命令**

```
git clone https://gitee.com/qq1249050094/soft-work-assignments.git

git config --global user.name "自己gitee用户名"

git config --global user.email "自己gitee绑定邮箱号"

git init
```



## **二、上传自己分支**

### ***1、首先***

```
git remote add origin https://gitee.com/qq1249050094/soft-work-assignments.git
```

表示添加远程仓库并将其命名为 "origin"



***2、在目录下新建文件夹***

```
mkdir [自己名字分支]
cd [自己名字分支]
```



***3、在此目录下编写自己的代码***



**编写完成后**



***4、上交代码***



**在上交之前，列举当前远程仓库中有哪些分支**

```
git ls-remote --heads origin
```

**然后逐一**

```
git branch --set-upstream-to=origin/main main
git branch --set-upstream-to=origin/分支名字 分支名字
```

**然后拉取所有分支**

```
git pull --all
```

**最后提交自己代码**

```
git checkout -b [自己名字分支]
git push origin [自己名字分支]
git add .
git commit -m "提交说明"
git push origin [自己名字分支]
```



**最后可以前往[软工作业: 作业库 (gitee.com)](https://gitee.com/qq1249050094/soft-work-assignments)查看是否上交成功**

