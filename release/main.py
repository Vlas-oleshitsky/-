import os
import sqlite3
from PyQt6 import QtWidgets
from UI.main_ui import Ui_CoffeeApp
from UI.addEditCoffeeForm_ui import Ui_AddEditCoffeeForm

# Путь к базе данных
database_path = os.path.join(os.path.dirname(__file__), "data", "coffee.sqlite")


class CoffeeApp(QtWidgets.QMainWindow, Ui_CoffeeApp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_data()
        self.pushButtonAdd.clicked.connect(self.add_record)
        self.pushButtonEdit.clicked.connect(self.edit_record)

    def load_data(self):
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM coffee")
        records = cursor.fetchall()

        self.tableWidget.setRowCount(len(records))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(
            ["ID", "Название сорта", "Степень обжарки", "Молотый/в зернах", "Описание вкуса", "Цена", "Объем упаковки"])

        for row_idx, row_data in enumerate(records):
            for col_idx, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(col_data)))

        cursor.close()
        connection.close()

    def add_record(self):
        self.add_edit_form = AddEditCoffeeForm(self)
        self.add_edit_form.show()

    def edit_record(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            record_id = self.tableWidget.item(selected_row, 0).text()
            self.add_edit_form = AddEditCoffeeForm(self, record_id)
            self.add_edit_form.show()


class AddEditCoffeeForm(QtWidgets.QDialog, Ui_AddEditCoffeeForm):
    def __init__(self, parent, record_id=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.record_id = record_id
        if record_id:
            self.load_record()
        self.buttonBox.accepted.connect(self.save_record)
        self.buttonBox.rejected.connect(self.close)

    def load_record(self):
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM coffee WHERE id=?", (self.record_id,))
        record = cursor.fetchone()
        if record:
            self.lineEditID.setText(str(record[0]))
            self.lineEditName.setText(record[1])
            self.lineEditRoast.setText(record[2])
            self.lineEditType.setText(record[3])
            self.lineEditDescription.setText(record[4])
            self.lineEditPrice.setText(str(record[5]))
            self.lineEditVolume.setText(str(record[6]))
        cursor.close()
        connection.close()

    def save_record(self):
        try:
            id = int(self.lineEditID.text())
            name = self.lineEditName.text()
            roast = self.lineEditRoast.text()
            type = self.lineEditType.text()
            description = self.lineEditDescription.text()
            price = float(self.lineEditPrice.text())
            volume = float(self.lineEditVolume.text())

            print(
                f"id: {id}, name: {name}, roast: {roast}, type: {type}, description: {description}, price: {price}, volume: {volume}")

            connection = sqlite3.connect(database_path)
            cursor = connection.cursor()

            if self.record_id:
                cursor.execute("""UPDATE coffee SET 
                                name=?, 
                                roast=?, 
                                type=?, 
                                description=?, 
                                price=?, 
                                volume=? 
                                WHERE id=?""",
                               (name, roast, type, description, price, volume, id))
                print(
                    f"UPDATE coffee SET name={name}, roast={roast}, type={type}, description={description}, price={price}, volume={volume} WHERE id={id}")
            else:
                cursor.execute("""INSERT INTO coffee (name, roast, type, description, price, volume) 
                                VALUES (?, ?, ?, ?, ?, ?)""",
                               (name, roast, type, description, price, volume))
                print(
                    f"INSERT INTO coffee (name, roast, type, description, price, volume) VALUES ({name}, {roast}, {type}, {description}, {price}, {volume})")

            connection.commit()
            cursor.close()
            connection.close()

            # Перезагрузка данных в таблице
            self.parent.load_data()
            self.close()
        except ValueError as e:
            QtWidgets.QMessageBox.critical(self, "Ошибка", f"Неверный тип данных: {e}")
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(self, "Ошибка базы данных", f"Ошибка базы данных: {e}")


def main():
    app = QtWidgets.QApplication([])
    window = CoffeeApp()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
