n = int(input())
a = n // 100
b = (n // 10) % 10
c = n % 10
match a:
    case 1 :
        print("сто")
    case 2:
        print("двести")
    case 3:
        print("триста")
    case 4:
        print("четыреста")
    case 5:
        print("пятьсот")
    case 6:
        print("шестьсот")
    case 7:
        print("семьсот")
    case 8:
        print("восемьсот")
    case 9:
        print("девятьсот")
    case _:
        print("")
match b,c:
    case 1,0:
        print("десять", "")
    case 1,1:
        print("одиннадцать", "")
    case 1,2:
        print("двенадцать", "")
    case 1,3:
        print("тринадцать", "")
    case 1,4:
        print("четырнадцать", "")
    case 1,5:
        print("пятнадцать", "")
    case 1,6:
        print("шестнадцать", "")
    case 1,7:
        print("семнадцать", "")
    case 1,8:
        print("восемьнадцать", "")
    case 1,9:
        print("девятнадцать", "")
    case 2,_:
        print("двадцать")
    case 3,_:
        print("тридцать")
    case 4,_:
        print("сорок")
    case 5,_:
        print("пятьдесят")
    case 6,_:
        print("шестьдесят")
    case 7,_:
        print("семьдесят")
    case 8,_:
        print("восемьдесят")
    case 9,_:
        print("девяносто")
    case _:
        print("")
if b != 1:
    match c:
         case 1:
            print("один")
         case 2:
             print("два")
         case 3:
             print("три")
         case 4:
            print("четыре")
         case 5:
            print("пять")
         case 6:
            print("шесть")
         case 7:
            print("семь")
         case 8:
            print("восемь")
         case 9:
            print("девять")
         case _:
            print("")
else:
    print("")
print(a,b,c)