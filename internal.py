from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from itemDetailClass import ItemDetails
from invoiceGenerate import Ui_InvoiceGenerated
from firebase import firebase
import datetime, json, threading
from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
from InvoiceGenerator.pdf import SimpleInvoice
from google.cloud import storage
import matplotlib.pyplot as plt
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "json.json"
os.environ["INVOICE_LANG"] = "en"
client = Client("House No 607,\nSaini Vihar, Phase - 2,\nBaltana, Zirakpur")
provider = Provider('Python Project', bank_account='2600420569', bank_code='2018')
creator = Creator('Himanshu Mittal')
list1 = []


class Internal_Ui(object):
    def __init__(self, email):
        self.connection = sqlite3.connect("D:\\Python-Project\\item-info.db")
        self.firebase = firebase.FirebaseApplication('https://pyhton-project-6071.firebaseio.com', None)
        self.email = email
        self.total = 0
        self.flag = 0
        self.date = datetime.datetime.now().strftime("%d-%m-%Y")
        thread1 = threading.Thread(target=self.run, args=())
        thread1.daemon = True
        thread1.start()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(657, 437)
        Dialog.setStyleSheet("QPushButton, QLineEdit\n"
                                "{\n"
                                "    border-radius:10px;\n"
                                "}\n"
                                "\n"
                                "QListWidget\n"
                                "{\n"
                                "    padding: 10px;\n"
                                "    box-shadow: 5px 10px red;\n"
                                "}\n"
                                "\n"
                                "QVBoxLayout\n"
                                "{\n"   
                                "    background-color:green;\n"
                                "}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 70, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.itemNotext = QtWidgets.QLineEdit(Dialog)
        self.itemNotext.setGeometry(QtCore.QRect(150, 90, 113, 20))
        self.itemNotext.setObjectName("itemNotext")
        self.quantityText = QtWidgets.QLineEdit(Dialog)
        self.quantityText.setGeometry(QtCore.QRect(420, 90, 113, 20))
        self.quantityText.setText("")
        self.quantityText.setObjectName("quantityText")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(450, 70, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.addButton = QtWidgets.QPushButton(Dialog)
        self.addButton.setGeometry(QtCore.QRect(170, 130, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.addButton.setFont(font)
        self.addButton.setStyleSheet("    background-color:#4CAF50;\n"
                                        "    border:none;\n"
                                        "    color: white;\n"
                                        "    padding: 20px;\n"
                                        "    text-align: center;\n"
                                        "    text-decoration: none;\n"
                                        "    display: inline-block;\n"
                                        "    font-size:12px;\n"
                                        "    margin: 4px 2px;\n"
                                        "    cursor: pointer;\n"
                                        "  \n"
                                        "")
        self.addButton.setObjectName("addButton")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 190, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(330, 190, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(230, 190, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.itemNameListWidget = QtWidgets.QListWidget(Dialog)
        self.itemNameListWidget.setGeometry(QtCore.QRect(30, 210, 141, 192))
        self.itemNameListWidget.setObjectName("itemNameListWidget")
        self.priceListWidget = QtWidgets.QListWidget(Dialog)
        self.priceListWidget.setGeometry(QtCore.QRect(210, 210, 81, 192))
        self.priceListWidget.setObjectName("priceListWidget")
        self.quantityListWidget = QtWidgets.QListWidget(Dialog)
        self.quantityListWidget.setGeometry(QtCore.QRect(320, 210, 81, 192))
        self.quantityListWidget.setObjectName("quantityListWidget")
        self.generateButton = QtWidgets.QPushButton(Dialog)
        self.generateButton.setGeometry(QtCore.QRect(390, 130, 141, 31))
        self.generateButton.setStyleSheet("background-color: #4CAF50; \n"
                                            "border: none;\n"
                                            "color: white;\n"
                                            "padding: 20px;\n"
                                            "text-align: center;\n"
                                            "text-decoration: none;\n"  
                                            "display: inline-block;\n"
                                            "font-size:12px;\n"
                                            "margin: 4px 2px;\n"
                                            "cursor: pointer;")
        self.generateButton.setObjectName("generateButton")
        self.removeButton = QtWidgets.QPushButton(Dialog)
        self.removeButton.setGeometry(QtCore.QRect(270, 130, 91, 31))
        self.removeButton.setStyleSheet("background-color:#4CAF50;\n"
                                            "border: none;\n"
                                            "color: white;\n"
                                            "padding: 20px;\n"
                                            "text-align: center;\n"
                                            "text-decoration: none;\n"
                                            "display: inline-block;\n"
                                            "font-size:12px;\n"
                                            "margin: 4px 2px;\n"
                                            "cursor: pointer;\n"
                                            "")
        self.removeButton.setObjectName("removeButton")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(430, 230, 221, 181))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.shopping_bill_grid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.shopping_bill_grid.setContentsMargins(0, 0, 0, 0)
        self.shopping_bill_grid.setObjectName("shopping_bill_grid")
        self.tax_value = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tax_value.setFont(font)
        self.tax_value.setAlignment(QtCore.Qt.AlignCenter)
        self.tax_value.setObjectName("tax_value")
        self.shopping_bill_grid.addWidget(self.tax_value, 1, 1, 1, 1)
        self.tax_box = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tax_box.setFont(font)
        self.tax_box.setAlignment(QtCore.Qt.AlignCenter)
        self.tax_box.setObjectName("tax_box")
        self.shopping_bill_grid.addWidget(self.tax_box, 1, 0, 1, 1)
        self.discount_box = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.discount_box.setFont(font)
        self.discount_box.setAlignment(QtCore.Qt.AlignCenter)
        self.discount_box.setObjectName("discount_box")
        self.shopping_bill_grid.addWidget(self.discount_box, 2, 0, 1, 1)
        self.discount_value = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.discount_value.setFont(font)
        self.discount_value.setAlignment(QtCore.Qt.AlignCenter)
        self.discount_value.setObjectName("discount_value")
        self.shopping_bill_grid.addWidget(self.discount_value, 2, 1, 1, 1)
        self.sub_total_value = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sub_total_value.setFont(font)
        self.sub_total_value.setAlignment(QtCore.Qt.AlignCenter)
        self.sub_total_value.setObjectName("sub_total_value")
        self.shopping_bill_grid.addWidget(self.sub_total_value, 0, 1, 1, 1)
        self.sub_total_box = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sub_total_box.setFont(font)
        self.sub_total_box.setAlignment(QtCore.Qt.AlignCenter)
        self.sub_total_box.setObjectName("sub_total_box")
        self.shopping_bill_grid.addWidget(self.sub_total_box, 0, 0, 1, 1)
        self.total_box = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.total_box.setFont(font)
        self.total_box.setAlignment(QtCore.Qt.AlignCenter)
        self.total_box.setObjectName("total_box")
        self.shopping_bill_grid.addWidget(self.total_box, 3, 0, 1, 1)
        self.total_value = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.total_value.setFont(font)
        self.total_value.setAlignment(QtCore.Qt.AlignCenter)
        self.total_value.setObjectName("total_value")
        self.shopping_bill_grid.addWidget(self.total_value, 3, 1, 1, 1)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(430, 170, 221, 51))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.shopping_bill_box = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.shopping_bill_box.setContentsMargins(0, 0, 0, 0)
        self.shopping_bill_box.setObjectName("shopping_bill_box")
        self.shopping_bill_text = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.shopping_bill_text.setFont(font)
        self.shopping_bill_text.setAlignment(QtCore.Qt.AlignCenter)
        self.shopping_bill_text.setObjectName("shopping_bill_text")
        self.shopping_bill_box.addWidget(self.shopping_bill_text)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(210, 0, 283, 59))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.sale_button = QtWidgets.QPushButton(Dialog)
        self.sale_button.setGeometry(QtCore.QRect(550, 50, 101, 31))
        self.sale_button.setStyleSheet("background-color:#4CAF50;\n"
                                            "border:none;\n"
                                            "color: white;\n"
                                            "padding: 20px;\n"
                                            "text-align: center;\n"
                                            "text-decoration: none;\n"
                                            "display: inline-block;\n"
                                            "font-size:12px;\n"
                                            "margin: 4px 2px;\n"
                                            "cursor: pointer;\n"
                                            "\n"
                                            "")
        self.sale_button.setObjectName("sale_button")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 90, 101, 31))
        self.pushButton_2.setStyleSheet("background-color:#4CAF50;\n"
                                            "border:none;\n"
                                            "color: white;\n"
                                            "padding: 20px;\n"
                                            "text-align: center;\n"
                                            "text-decoration: none;\n"
                                            "display: inline-block;\n"
                                            "font-size:12px;\n"
                                            "margin: 4px 2px;\n"
                                            "cursor: pointer;\n"
                                            "\n"
                                            "")
        self.pushButton_2.setObjectName("pushButton_2")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.addButton.clicked.connect(self.item_added)
        self.removeButton.clicked.connect(self.update_item)
        self.generateButton.clicked.connect(self.pdf_data)
        self.itemNameListWidget.itemClicked.connect(self.show_names)
        self.itemNameListWidget.itemDoubleClicked.connect(self.remove_item)
        self.sale_button.clicked.connect(self.sale_graph)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Item No."))
        self.label_2.setText(_translate("Dialog", "Quantity"))
        self.addButton.setText(_translate("Dialog", "Add"))
        self.label_3.setText(_translate("Dialog", "Item Name"))
        self.label_4.setText(_translate("Dialog", "Quantity"))
        self.label_5.setText(_translate("Dialog", "Price"))
        self.generateButton.setText(_translate("Dialog", "Generate Invoice"))
        self.removeButton.setText(_translate("Dialog", "Remove"))
        self.tax_value.setText(_translate("Dialog", "0.00"))
        self.tax_box.setText(_translate("Dialog", "Tax"))
        self.discount_box.setText(_translate("Dialog", "Discount"))
        self.discount_value.setText(_translate("Dialog", "0.00"))
        self.sub_total_value.setText(_translate("Dialog", "0.00"))
        self.sub_total_box.setText(_translate("Dialog", "Sub Total"))
        self.total_box.setText(_translate("Dialog", "Totals"))
        self.total_value.setText(_translate("Dialog", "0.00"))
        self.shopping_bill_text.setText(_translate("Dialog", "Shopping Bill"))
        self.label_6.setText(_translate("Dialog", "Bill Management System"))
        self.sale_button.setText(_translate("Dialog", "Sale Graph"))
        self.pushButton_2.setText(_translate("Dialog", "Clear"))

    def item_added(self):
        result = self.firebase.get('/' + self.email + '/' + self.date, None)
        if result is not None:
            index = int(list(result.keys())[-1][-1]) + 1
        else:
            index = 1
        itemNo = self.itemNotext.text()
        quan = self.quantityText.text()
        query = "SELECT itemName, price, url FROM itemInfo WHERE itemCode = " + str(itemNo)
        results = self.connection.execute(query)
        for data in results:
            obj = ItemDetails()
            obj.setName(data[0])
            obj.setPrice(data[1])
            obj.setQuantity(self.quantityText.text())
            obj.setUrl(data[2])
            if result is not None:
                for x, y in result.items():
                    if y['name'] == data[0]:
                        new_quantity = int(quan)+int(y['quantity'])
                        self.firebase.put('/'+self.email+'/'+self.date+'/'+x, 'quantity', new_quantity)
                        self.flag = 1
                        break
                    else:
                        self.flag = 0
            if self.flag == 0:
                self.firebase.put('/' + self.email + '/' + self.date, 'item' + str(index),
                                  json.loads(json.dumps(obj.__dict__)))
                conn = sqlite3.connect('item-Info.db')
                cur = conn.cursor()
                cur.execute("INSERT INTO sold_item (date_added,item_name,Quantity,Price) VALUES (?,?,?,?)",
                            (str(self.date), str(data[0]),self.quantityText.text(), data[1]))
                conn.commit()

    def run(self):
        while True:
            prev = self.firebase.get('/'+self.email+'/'+self.date, None)
            self.itemNameListWidget.clear()
            self.priceListWidget.clear()
            self.quantityListWidget.clear()
            if prev is not None:
                total = 0
                for item in prev.items():
                    self.itemNameListWidget.addItem(item[1]['name'])
                    self.priceListWidget.addItem(item[1]['price'])
                    total = total+int(item[1]['quantity'])*int(item[1]['price'])
                    self.quantityListWidget.addItem(str(item[1]['quantity']))
                tax = 0.08*total
                self.sub_total_value.setText(str(total)+'.00')
                self.total_value.setText(str(tax+total))

    def update_item(self):
        item_no = self.itemNotext.text()
        new_quantity = self.quantityText.text()
        sql1 = "SELECT itemName, price from itemInfo WHERE itemCode = "+str(item_no)
        sql11 = self.connection.execute(sql1)
        for items in sql11:
            data = list(items)
        fire_data = self.firebase.get('/'+self.email+'/'+self.date,None)
        for x, y in fire_data.items():
            if(y['name'] == data[0]):
                self.firebase.put('/'+self.email+'/'+self.date+'/'+x, 'quantity', new_quantity)

    def remove_item(self):
        item_name = self.itemNameListWidget.currentItem().text()
        fire_data = self.firebase.get('/'+self.email+'/'+self.date, None)
        for x,y in fire_data.items():
            if(y['name'] == item_name):
                self.firebase.delete('/'+self.email+'/'+self.date+'/'+x, None)

    def show_names(self):
        item1 = self.itemNameListWidget.currentItem().text()
        conn = sqlite3.connect('item-Info.db')
        cur = conn.cursor()
        sql1 = "SELECT itemCode fROM itemInfo WHERE itemName = '" + item1 + "';"
        cur.execute(sql1)
        sql11 = cur.fetchall()
        for items in sql11:
            item = items
        self.itemNotext.setText(str(item[0]))

    def pdf_store(self, filename):
        prefix = filename.split('.pdf')[0]+'/'+str(self.date)
        storage_client = storage.Client()
        bucket = storage_client.get_bucket('pyhton-project-6071.appspot.com')
        blobs = bucket.list_blobs(prefix = prefix)
        for blob in blobs:
            b = str(blob.name).split(prefix + '/')[1]
            list1.append(b)
        if len(list1) is not 0:
            index = len(list1)+1
        else:
            index = 1
        path = 'PDF/'+filename
        PDFblob = bucket.blob(self.email+'/'+self.date+'/'+str(index)+' '+filename)
        PDFblob.upload_from_filename(path)

    def pdf_data(self):
        invoice = Invoice(client, provider, creator)
        invoice.currency_locale = 'en_IN.UTF-8'
        fire_data = self.firebase.get('/'+self.email+'/'+self.date, None)
        for x, y in fire_data.items():
            invoice.add_item(Item(y['quantity'], y['price'], description=y['name']))
        pdf = SimpleInvoice(invoice)
        pdf.gen("invoice.pdf", generate_qr_code=True)
        #self.pdf_store(file_name)
        # self.welcomeWindow = QtWidgets.QDialog()
        # self.ui = Ui_InvoiceGenerated()
        # self.ui.setupUi(self.welcomeWindow)
        # self.welcomeWindow.show()

    def sale_graph(self):
        conn = sqlite3.connect('item-info.db')
        cur = conn.cursor()
        cur.execute("SELECT * from sold_item")
        data = cur.fetchall()
        cost_dict = {}
        x_axis = []
        y_axis = []
        for items in data:
            a = items[0]
            total = 0
            for item in data:
                if a == item[0]:
                    total = total + item[3] * item[2]
            cost_dict[a] = total
        cost_dict = dict(sorted(cost_dict.items(), key=lambda x: datetime.datetime.strptime(x[0], '%d-%m-%Y'),
                                reverse=False))
        for key in cost_dict.keys():
            x_axis.append(key)
        for value in cost_dict.values():
            y_axis.append(value)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.bar(x_axis, y_axis, label='Bars1', color='orange')
        ax.set_xlabel('Date')
        ax.set_ylabel('Total Sale')
        plt.title('Total Sale Graph')
        ax.xaxis.label.set_color('red')
        ax.yaxis.label.set_color('red')
        plt.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Internal_Ui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

