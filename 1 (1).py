# 心跳 / Heartbeat / 心跳
a = 60
b = 100
import random

random_int = random.randint(a, b)
print(f"心脏跳动数字为：{random_int}")  # 简体中文
print(f"心臟跳動數字為：{random_int}")  # 繁体中文
print(f"Heartbeat number: {random_int}")  # English

a = input("还要继续吗？请说是或否 / 還要繼續嗎？請說是或否 / Continue? Please say yes or no\n")
if a == '是' or a == 'yes' or a == 'Yes' or a == 'YES':
    a = 70
    b = 80
    random_int1 = random.randint(a, b)
    print(f"心脏一次泵血为：{random_int1} ml")  # 简体
    print(f"心臟一次泵血為：{random_int1} ml")  # 繁体
    print(f"Blood volume per heartbeat: {random_int1} ml")  # English

    b = input("还要继续吗？请说是或否 / 還要繼續嗎？請說是或否 / Continue? Please say yes or no\n")
    if b == '是' or b == 'yes' or b == 'Yes' or b == 'YES':
        cardiac_output = random_int * random_int1
        print(f"心出血量{cardiac_output} ml")  # 简体
        print(f"心輸出量{cardiac_output} ml")  # 繁体
        print(f"Cardiac output: {cardiac_output} ml")  # English

        c = input("还要继续吗？请说是或否 / 還要繼續嗎？請說是或否 / Continue? Please say yes or no\n")
        if c == '是' or c == 'yes' or c == 'Yes' or c == 'YES':
            o = input("炎症因子a与正常人相比差多少百万个（体积是1ml）\n 炎症因子a與正常人相比差多少百萬個（體積是1ml）\n How many million inflammatory factors a compared to normal (volume: 1ml)?\n ")
            o = float(o)
            total_inflammatory = cardiac_output * o
            print(f"炎症因子a与正常人相比差{o}百万个，所以是{total_inflammatory}百万个")  # 简体
            print(f"炎症因子a與正常人相比差{o}百萬個，所以是{total_inflammatory}百萬個")  # 繁体
            print(f"Inflammatory factor a differs by {o} million, total: {total_inflammatory} million")  # English

            d = input("还要继续吗？请说是或否 / 還要繼續嗎？請說是或否 / Continue? Please say yes or no\n")
            if d == '是' or d == 'yes' or d == 'Yes' or d == 'YES':
                fengzi = input("分子量为多少？/ 分子量為多少？/ What is the molecular weight?\n")
                wendu = input("绝对温度是多少？/ 絕對溫度是多少？/ What is the absolute temperature?\n")
                fengzi = float(fengzi)
                wendu = float(wendu)
              #因为前面是以百万为单位，所以相当于已经乘以10的-6次方
                osmotic_pressure = total_inflammatory * 0.001 / fengzi * 8.314 * wendu 
                print(f"炎症因子a渗透压{osmotic_pressure} Pa（1分钟以内）")  # 简体
                print(f"炎症因子a滲透壓{osmotic_pressure} Pa（一分鐘以內")  # 繁体
                print(f"Osmotic pressure of inflammatory factor a: {osmotic_pressure} Pa（Within a minute.）")  # English
            else:
                print("结束 / 結束 / End")
        else:
            print("结束 / 結束 / End")
    else:
        print("结束 / 結束 / End")
else:
    print("结束 / 結束 / End")
input("运行完毕，按回车键退出...")
