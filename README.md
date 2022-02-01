# aria2TrackerUpdate

## English

### Requirement
[Python3](https://www.python.org/downloads/)

### Usage

```
python3 aria2TrackerUpdate.py <filePath>
```
or 
```
python3 aria2TrackerUpdate.py <filePath> <updateUrl>
```

### Default tracker URL
[ngosang/trackerslist](https://github.com/ngosang/trackerslist): trackers_best (20 trackers)

### Set with cron
Add the following text to /etc/crontab
```
18 0    * * 3   root    python3 aria2TrackerUpdate.py <filePath> <updateUrl> > /dev/null 2>&1
```
then
```
sudo service cron restart
```

### Set with task scheduler
[Click me](https://www.google.com/search?q=how+to+use+windows+task+scheduler)

### Other notice
This python script will only modify or add the trackers, "*bt-tracker=*". It will not change other aria2 configurations.

If the file path does not exist, the script will create a new configuration file.

The script cannot handle the SPACE character in the given path.

<br>

## 简体中文

### 要求
[Python3](https://www.python.org/downloads/)

### 用法

```
python3 aria2TrackerUpdate.py <filePath >
```
或 
```
python3 aria2TrackerUpdate.py <filePath> <updateUrl>
```

### 默认的跟踪器URL
[ngosang/trackerslist](https://github.com/ngosang/trackerslist): trackers_best (20 trackers)

### 使用cron设置
在 /etc/crontab 中添加以下文本
```
18 0 * * 3 root python3 aria2TrackerUpdate.py <filePath> <updateUrl> > /dev/null 2>&1
```
然后
```
sudo service cron restart
```

### 使用用任务计划程序设置
[点击我](https://www.baidu.com/s?wd=使用+windows+任务计划)

### 其他注意事项
这个python脚本只会修改或添加跟踪器，"*bt-tracker=*"。它不会改变其他的 aria2 配置。

如果文件路径不存在，该脚本将创建一个新的配置文件。

该脚本不能处理给定路径中的空格字符。
