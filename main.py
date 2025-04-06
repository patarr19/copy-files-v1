from random import choice


def copyFileImgVid(fromFile, toFile):
    try:
        with open(fromFile, "rb") as from_file:
            with open(toFile, "wb") as to_file:
                to_file.write(from_file.read())
            print(f"Содержимое из {fromFile} файла успешно скопировано в {toFile}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def copyTxt(fromFile, toFile):
    try:
        with open(fromFile, "r", encoding = "utf-8") as from_file:
            with open(toFile, "w", encoding = "utf-8") as to_file:
                for line in from_file:
                    to_file.write(line)
        print(f"Содержимое из {fromFile} файла скопировано в {toFile} файл")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    choice = input("1: Скопировать видео/изображение; 2: Скопировать текст. ")
    if choice == "1":
        copyFileImgVid("D:\\YURKA-CODER\\python-prog\\copyFileContent\\testpng1\\pen.png",
                       "D:\\YURKA-CODER\\python-prog\\copyFileContent\\testpng2\\pen_copy.png")
    elif choice == "2":
        copyTxt("D:\\YURKA-CODER\пароли\\passwords.txt", "copied.txt")
    else:
        print("Не найдена команда")
