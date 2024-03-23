import random
import string

def generate_random_string(length) -> str:
    int(length)
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choices(characters, k = length))
    return random_string

def main():
    is_looping = True
    length = None
    while is_looping:
        length = input("文字数(4以上64以下の整数、0で終了)")
        try:
            length = int(length)
            if length == 0: #終了条件の設定
                is_looping = False
                break
            elif length < 4:
                print("無効")
                continue
            elif length > 64:
                print("無効")
                continue
        except ValueError:
            print("無効")
            continue
        process_value(length) #PW生成
        continue
    print("完了")

def process_value(value: int):
    print(generate_random_string(value))

if __name__ == "__main__":
    main()