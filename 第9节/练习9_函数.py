# 第9节：函数
# 复习要点：函数定义、参数（位置/关键字/默认/可变）、返回值、lambda、作用域
# 基础题1：函数基础
# 需求：编写以下函数
#   1. is_prime(n) - 判断是否为质数，返回True/False
#   2. factorial(n) - 计算阶乘 n!，返回整数
#   3. fibonacci(n) - 返回包含n个斐波那契数列的列表

# 基础题2：参数类型练习
# 需求：编写一个计算器函数 calc(a, b, operation="add")
# operation可选："add"加、"sub"减、"mul"乘、"div"除
# 要求：
#   1. 用关键字参数调用 calc(b=5, a=3)
#   2. 用 *args 处理多个数相加
#   3. 用 **kwargs 处理带名字的计算

# 项目题：文本处理工具箱
# 需求：实现一个文本处理函数库
# 要求：
#   1. count_words(text) - 统计单词数量
#   2. count_chars(text) - 统计字符数量（不含空格）
#   3. reverse_text(text) - 反转字符串
#   4. is_palindrome(text) - 判断是否为回文（正反读一样，如"上海自来水来自海上"）
#   5. top_n_words(text, n) - 返回出现频率最高的n个单词及次数
#   6. 编写一个主函数 menu() 整合所有功能，提供交互菜单
# 附加挑战：用 lambda 和 map 实现文本加密（凯撒密码：每个字母向后移动3位）