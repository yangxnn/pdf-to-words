<!--
 * @Author       : yangxing(yangxnn@outlook.com)
 * @Date         : 2022-05-01 17:52:49
 * @LastEditors  : yangxing(yangxnn@outlook.com)
 * @LastEditTime : 2022-05-04 19:30:45
 * @FilePath     : /pdf-to-words/README.md
 * @Description  : 
 * 
 * Copyright (c) 2022 by yangxnn@outlook.com, All Rights Reserved. 
-->
# pdf-to-words

pdf-to-words是一个将pdf解析为单词的小脚本，解析的单词会按照出现次数排序，由高到低。

读英文论文时，常遇到不熟悉的单词，只能边查询边读，但查单词容易影响连贯性的理解与思考。

借助这个小脚本，可以在读论文前，先解析一边输出单词，提前记单词，省得边看边查影响阅读思路。

![GitHub](https://img.shields.io/github/license/yangxnn/pdf-to-words)

**关键词**: pdf, 解析, 单词

## 特点
- pdf解析为单词
- 单词按照出现次数降序排列

## 环境依赖
- pdfminer (version:20191125) [github](https://github.com/euske/pdfminer)
    - ```pip install pdfminer```
- python (3.x)


## 使用方法
```python
python main.py demo.pdf
```
demo.pdf是xgboost的论文


