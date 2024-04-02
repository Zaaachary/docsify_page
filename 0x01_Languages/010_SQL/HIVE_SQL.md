# Hive SQL

## 学习资料

CSDN: [Link](https://blog.csdn.net/helloHbulie/article/details/115376657)






## Explode
关键点：一行拆成多行，例如 "A,B,C,D" → "A" | "B" | "C" | "D" 。`explode(split(alphabeta,','))`

[Ref1](https://zhuanlan.zhihu.com/p/115918587), [Ref2](https://blog.csdn.net/qq_42374697/article/details/115273726)



## regexp_extract(string ***subject***,  string ***pattern***,  int ***index***)

**返回值:** string。功能就是从一个字符串里面找到需要的那部分字符内容，比如想要从'#@#$$$$#1***%'中找到数字1。该函数输入参数只对string字符串、json string等适用，map或者array用不了

**说明：**  将字符串subject按照pattern正则表达式的规则拆分，返回index指定匹配出的字符内容。

第一参数：  要处理的字段

第二参数:   需要匹配的正则表达式

第三个参数:

- 0是显示与之匹配的整个字符串
- 1 是显示第一个括号里面的
- 2 是显示第二个括号里面的字段...
