# 第1节：变量与数据类型
# 复习要点：变量命名规则、int/float/str/bool类型、类型转换、print输入输出
# 基础题1：温度转换器
# 需求：用户输入一个华氏温度，程序输出对应的摄氏温度
# 公式：C = (F - 32) * 5 / 9
# 要求：保留2位小数，输出格式："华氏{输入}°F = 摄氏{结果}°C"
# 提示：用 input() 获取输入，用 float() 转换，用 f-string 格式化输出

# fahrenheit = float(input("请输入华氏温度："))
# celsius = (fahrenheit - 32) * 5 / 9
# print(f"华氏{fahrenheit}°F = 摄氏{celsius:.2f}°C")


# 基础题2：自我介绍
# 需求：用户依次输入姓名、年龄、身高，程序输出自我介绍
# 输出格式：
# "大家好，我叫{name}，今年{age}岁，身高{height}cm。
#  希望和大家成为朋友！"
# 提示：年龄要转成整数，身高保留1位小数
# name = input("请输入你的姓名：")
# age = int(input("请输入你的年龄："))
# height = float(input("请输入你的身高（cm）："))
# print(f"大家好，我叫{name}，今年{age}岁，身高{height:.1f}cm。希望和大家成为朋友！")

# 项目题：BMI计算器
# 需求：输入体重(kg)和身高(m)，计算BMI值
# BMI = 体重 / 身高²
# 根据BMI判断体型：
#   < 18.5 → "偏瘦"
#   18.5~23.9 → "正常"
#   24~27.9 → "偏胖"
#   >= 28 → "肥胖"
# 输出格式："你的BMI为{结果}，体型属于：{判断}"
# 附加挑战：添加异常处理（身高不能为0或负数）

# try:
#     weight = float(input("体重(kg)："))
#     height = float(input("身高(m)："))
#     if height <= 0:
#         print("身高不能为0或负数！")
#     else:
#         bmi = weight / (height ** 2)
#         if bmi < 18.5:
#             category = "偏瘦"
#         elif 18.5 <= bmi < 24:
#             category = "正常"
#         elif 24 <= bmi < 28:
#             category = "偏胖"
#         else:
#             category = "肥胖"
#         print(f"你的BMI为{bmi:.2f}，体型属于：{category}")
# except ValueError:
#     print("请输入有效的数字！")


    #写一个函数，计算在一定的身高下，达到不同体型所需的体重范围，并输出结果
# def bmi_weight_range(height):
#     if height <= 0:
#         print("身高不能为0或负数！")
#         return
#     weight_underweight = 18.5 * (height ** 2)
#     weight_normal_min = 18.5 * (height ** 2)
#     weight_normal_max = 23.9 * (height ** 2)
#     weight_overweight_min = 24 * (height ** 2)
#     weight_overweight_max = 27.9 * (height ** 2)
#     weight_obese = 28 * (height ** 2)

#     print(f"对于身高{height}m：")
#     print(f"偏瘦：体重 < {weight_underweight:.2f} kg")
#     print(f"正常：体重在 {weight_normal_min:.2f} kg ~ {weight_normal_max:.2f} kg")
#     print(f"偏胖：体重在 {weight_overweight_min:.2f} kg ~ {weight_overweight_max:.2f} kg")
#     print(f"肥胖：体重 >= {weight_obese:.2f} kg")


# bmi_weight_range(float(input("请输入身高(m)：")))