import os
import pandas as pd

class DataProcessing:
    def __init__(self, file_path, expected_columns): 
        self.file_path = file_path
        self.expected_columns = expected_columns

    def processing_dataset(self):
        try:
            if not os.path.exists(self.file_path):
                raise FileNotFoundError(f"Файл '{self.file_path}' не найден.")
            try:
                df = pd.read_csv(self.file_path)
            except UnicodeDecodeError:
                df = pd.read_csv(self.file_path)

        
            missing_columns = [col for col in self.expected_columns if col not in df.columns]
            if missing_columns:
                raise ValueError(f"Отсутствуют столбцы: {', '.join(missing_columns)}")

            if df.empty:
                raise ValueError("Датафрейм пуст.")

            print("Чтение датафрейма завершено успешно.")
            return df

        except (FileNotFoundError, pd.errors.EmptyDataError, pd.errors.ParserError, ValueError) as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")

        return None

def main():
    expected_columns = [
        "Участники гражданского оборота", "Тип операции", "Сумма операции",
        "Вид расчета", "Место оплаты", "Терминал оплаты", "Дата оплаты",
        "Время оплаты", "Результат операции", "Cash-back", "Сумма cash-back"
    ]

    file_path = "var4.csv"
    processor = DataProcessing(file_path, expected_columns)
    df = processor.processing_dataset()

if __name__ == "__main__":
    main()
