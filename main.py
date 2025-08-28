digit_1 = int(input())
digit_2 = int(input())
digit_3 = int(input())
digit_4 = int(input())

def test_one(digit_1):
    if digit_1 == 8 or digit_1 == 9:
        return True
    else:
        return False

def test_two(digit_4):
    if digit_4 == 8 or digit_4 == 9:
        return True
    else:
        return False

def test_three(digit_2, digit_3):
    if digit_2 == digit_3:
        return True
    else:
        return False

if test_one(digit_1) and test_two(digit_4) and test_three(digit_2, digit_3):
    print("ignore")
else:
    print("answer")