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

    for i in range(n):
        grade=None
        while not isinstance(grade,float):
            value=input(f"Введите оценку по предмету {i+1}: ")
            if is_valid_number(value):
                grade=float(value)
            else:
                print("Некорректный ввод, повторите попытку")
            grades.append(grade)
