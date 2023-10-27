import random
randnum = random.randint(1,1000)
while True:
    guess = input("请猜一个1到1000的整数:")
    if not guess.isdigit():
        print("请输入整数")
    elif int(guess)<1 or int(guess)>1000:
        print("请输入(1,1000)的整数")
    else:
        if int(guess)>randnum:
          print("猜大了")
        elif int(guess)<randnum:
          print("猜小了")
        else:
          print("猜对了！ 牛逼牛逼")
          break
