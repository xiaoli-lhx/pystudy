# BMI = 体重 / (身高 ** 2)
user_weight = float(input("请输入您的体重(单位：kg): "))
user_height = float(input("请输入您的身高(单位：m): "))
user_gender = input("请输入您的性别：")
user_BMI = user_weight / user_height ** 2
print("您的BMI值为: "+str(user_BMI))

# 偏瘦：user_BMI <= 18.5
# 正常：18.5 < user_BMI<= 25
# 偏胖：25< user_BMI <=30
# 肥胖：user_BMI > 30
if user_gender == "男":
    if user_BMI <= 18.5:
        print("先生您好，此BMI值属于偏瘦范围。")
    elif 18.5 < user_BMI <= 25:
        print("先生您好，此BMI值属于正常范围。")
    elif 25 < user_BMI <= 30:
        print("先生您好，此BMI值属于偏胖范围。")
    else:
        print("先生您好，此BMI值属于肥胖范围。")
else:
    if user_BMI <= 18.5:
        print("女士您好，此BMI值属于偏瘦范围。")
    elif 18.5 < user_BMI <= 25:
        print("女士您好，此BMI值属于正常范围。")
    elif 25 < user_BMI <= 30:
        print("女士您好，此BMI值属于偏胖范围。")
    else:
        print("女士您好，此BMI值属于肥胖范围。")
