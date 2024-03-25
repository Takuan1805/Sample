import random
import string


    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choices(characters, k = length))
    return random_string

def main():
    is_looping = True

    while is_looping:
        try:
            length = int(input("文字数"))
            check = length_check(length)

            if check == 0:
                is_looping = False
                break
            elif check == 1:
                print("無効")
            else:
                process_value(length)
        except ValueError:
            print("無効")
            continue
    print("完了")

def length_check(num):
    if num == 0:
        print("check: 0")
        return 0 #終了
    elif num < 0 or num < 4 or num > 64:
        print("check :1")
        return 1 #無効
    else:
        print("check: 2")
        return 2

def process_value(value):

    print(generate_random_string(value))

if __name__ == "__main__":
    main()