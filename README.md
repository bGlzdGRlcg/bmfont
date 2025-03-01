# bmfont

一个用来快速生成telegram字体emoji的工具

生成完之后可以直接发送给官方机器人，无需裁剪转换格式

# 快速开始

```shell
python -m venv venv
venv/bin/python -m pip install --upgrade pip
venv/bin/pip install pillow
venv/bin/python bmfont.py
```

# 使用方法

- 修改`bmfont.py`第34行`chars`为你需要生成的文字
- 替换`font.ttf`文件为你需要的字体
- 根据字体修改`bmfont.py`第45行的字体大小

```shell
python -m venv venv
venv/bin/python -m pip install --upgrade pip
venv/bin/pip install pillow
venv/bin/python bmfont.py
```