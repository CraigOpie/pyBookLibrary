import sys
import sqlite3
import json
try:
    from PySide import QtWidgets, QtCore
    import PySide.QtWidgets as QtWidgets
except ImportError:
    from PySide2 import QtWidgets, QtCore, QtWidgets

class QuerySales(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.initMenu()
        self.dbname = ""
        self.cursor = None
        self.conn = None
        self.col_names = []
        self.results = None
        self.json = ""
        self.xml = ""
        self.sql = ""
        self.text = QtWidgets.QTextEdit()
        self.setCentralWidget(self.text)
        self.setGeometry(50,50,700,400)
        self.setWindowTitle("Query Sales Database")
        self.show()

    def initMenu(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("File")
        connect_db = QtWidgets.QAction("Connect to database",self)
        connect_db.triggered.connect(self.connectDB)
        self.save_json = QtWidgets.QAction("Save as JSON",self)
        self.save_json.triggered.connect(self.saveJSON)
        self.save_json.setEnabled(False)
        self.save_xml = QtWidgets.QAction("Save as XML",self)
        self.save_xml.triggered.connect(self.saveXML)
        self.save_xml.setEnabled(False)
        fileMenu.addAction(connect_db)
        fileMenu.addAction(self.save_json)
        fileMenu.addAction(self.save_xml)
        quit = QtWidgets.QAction("Quit",self)
        quit.triggered.connect(self.close)
        fileMenu.addAction(quit)
        self.queryMenu = menubar.addMenu("Query")
        run = QtWidgets.QAction("Run Query",self)
        run.triggered.connect(self.runQuery)
        show_json = QtWidgets.QAction("Show JSON",self)
        show_json.triggered.connect(self.showJSON)
        show_xml = QtWidgets.QAction("Show XML",self)
        show_xml.triggered.connect(self.showXML)
        self.queryMenu.addAction(run)
        self.queryMenu.addAction(show_json)
        self.queryMenu.addAction(show_xml)
        self.queryMenu.setEnabled(False)

    def connectToDB(self):
        self.conn = sqlite3.connect(self.dbname)
        self.conn.row_factory = sqlite3.Row
        self.cursor  = self.conn.cursor()

    def runQuery(self):
        dlg = QtWidgets.QInputDialog(self)
        dlg.setInputMode(QtWidgets.QInputDialog.TextInput)
        dlg.setWindowTitle('Get SQL')
        dlg.setLabelText("Enter sql: ")
        dlg.setTextValue("select * from sales_view")
        dlg.resize(400,200)
        ok = dlg.exec_()
        #text,ok = QtWidgets.QInputDialog.getText(self,'Get SQL','Enter sql: ')
        if (ok):
            self.sql = dlg.textValue()
            print("sql:",self.sql)
            self.getQueryResults(self.sql)
        #print(self.json)

    def getQueryResults(self,sql):
        self.cursor.execute(sql)
        r = self.cursor.fetchone()
        self.col_names = r.keys()
        self.cursor.execute(sql)
        self.results = self.cursor.fetchall()
        if (len(self.results) > 0):
            self.text.setText("Query returned " +
                str(len(self.results)) + " results")
            self.makeJSON()
            self.makeXML()
            self.save_json.setEnabled(True)
            self.save_xml.setEnabled(True)

    def makeJSON(self):
        results_d = {}
        results_d['sales'] = []
        for result in self.results:
            row_d = {}
            for i in range(0, len(self.col_names)):
                row_d[self.col_names[i]] = result[i]
            results_d['sales'].append(row_d)
        self.json = json.dumps(results_d,indent=2,sort_keys=True)

    def makeXML(self):
        temp = '<?xml version="1.0" ?>\n'
        temp += '<sales>\n'
        for result in self.results:
            temp += '  <sale>\n'
            for i in range(0, len(self.col_names)):
                temp += '    <' + self.col_names[i] + '>'
                temp += str(result[i]) + '</'
                temp += self.col_names[i] + '>\n'
            temp += '  </sale>\n'
        temp += '</sales>'
        self.xml = temp

    def saveJSON(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self,
            "Save as JSON",".")
        if (filename != ""):
            outfile = open(filename,"w")
            outfile.write(self.json)
            outfile.close()

    def saveXML(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self,
            "Save as XML",".")
        if (filename != ""):
            outfile = open(filename,"w")
            outfile.write(self.xml)
            outfile.close()

    def showJSON(self):
        self.text.setText(self.json)

    def showXML(self):
        self.text.setText(self.xml)

    def connectDB(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self,
            "Select database to use: ",".")
        if (filename != ""):
            self.dbname = filename
            self.conn = sqlite3.connect(self.dbname)
            self.conn.row_factory = sqlite3.Row
            self.cursor  = self.conn.cursor()
            if (self.cursor != None):
                self.queryMenu.setEnabled(True)

app = QtWidgets.QApplication(sys.argv)
mygui = QuerySales()
sys.exit(app.exec_())
