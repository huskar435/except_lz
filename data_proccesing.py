import pandas as pd
from pandas.errors import EmptyDataError
import os

class Data_Processing:
    def __init__(self, file_path): 
        self.file_path = file_path
     
    def existence_check(self):
        if not os.path.exists(self.file_path):
            print(f"Возникла следующая ошибка: [Errno2] No such file or directory: '{self.file_path}'")
            return False
        return True

    def content_check(self):
        try:
            df = pd.read_csv(self.file_path)
            if df.empty:
                print(f"")
                return False
        except EmptyDataError:
            print("Возникла следующая ошибка: Датафрейм '{self.file_path}' пуст.")
            return False
        except FileNotFoundError:
            print(f"Возникла следующая ошибка: [Errno2] No such file or directory: '{self.file_path}'")
            return False
        return True

    def analyze_dataframe(self):
        try:
            pd.read_csv(self.file_path)
            print("Чтение датафрейма завершено успешно")
        except FileNotFoundError:
            print(f"Возникла следующая ошибка: [Errno2] No such file or directory: '{self.file_path}'")
        except Exception as e:
            print(f"Структура датафрейма НЕ соответствует ожидаемой: {e}")

def main():
    processor = Data_Processing("var4.csv")
    if processor.existence_check():
        processor.content_check()
        processor.analyze_dataframe()

if __name__ == "__main__":
    main()
