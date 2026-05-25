from utils import is_valid_number
def main():
    grades=[]
    n=None

    while not isinstance(n,int):
        value=input("Введите количество предметов")
        if is_valid_number(value):
            n=int(float(value))
        else:
            print("Некорректный ввод, повторите попытку")
