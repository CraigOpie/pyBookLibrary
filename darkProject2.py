#!/usr/bin/env python3
"""
Name:    Craig Opie
Class:   CENT110
File:    project2.py

Algorithm:
"""
from bs4 import BeautifulSoup #Parser for processing XML and HTML files
from json import dumps, loads #Parser for processing JSON files
import sqlite3 #Database architechture
import subprocess #Allows interaction with shell commands
import sys #Allows interaction with system files and locations
import qdarkstyle

# Ports PySide commands over to PySide2 if PySide2 is installed
try:
    from PySide import QtWidgets, QtCore
    import PySide.QtWidgets as QtWidgets
except ImportError:
    from PySide2 import QtWidgets, QtCore

# Main object for project 2
class Project2(QtWidgets.QMainWindow):
    """ This class creates a dialog box which displays a table for data.

    Public Attributes:
        self.activeDbTable (str): Used to specify the current table being
            accessed by the user.
        self.columnLabels (list): Used to store the main tables header text.
        self.db (str): Used to specify the database location using SQLite3.
        self.dbTables (list): Used to store a list of all available tables
            located in self.db.
        self.table (obj): Table object created from QtWidgets.
    """

    def __init__(self):
        """ Method is documented in the class level docstring """

        QtWidgets.QMainWindow.__init__(self)
        self.activeDbTable = ""
        self.columnLabels = []
        self.conn = ""
        self.db = ""
        self.dbTables = []
        self.table = QtWidgets.QTableWidget(1,3)
        self.table.setHorizontalHeaderLabels(self.columnLabels)
        self.initMenu()
        self.setCentralWidget(self.table)
        self.setGeometry(50,50,700,400)
        self.setWindowTitle("Project 2 QTableWidget")
        self.show()

    def initMenu(self):
        """ This method creates a dialog box menubar which allows users to
        navigate other methods of this class.
        """

        # Menubar is created with three selection options
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("File")
        editMenu = menubar.addMenu("Edit")
        dbMenu = menubar.addMenu("Database")

        # SubMenu of File - SQL Database Connection
        connSQL = QtWidgets.QAction("Conn SQL",self)
        connSQL.triggered.connect(self.connSQL)
        fileMenu.addAction(connSQL)

        # SubMenu of File - Opens XML, JSON, or CSV type files
        openItem = QtWidgets.QAction("Open",self)
        openItem.triggered.connect(self.openFile)
        fileMenu.addAction(openItem)

        # SubMenu of File - Saves XML, JSON, or CSV type files
        saveItem = QtWidgets.QAction("Save As",self)
        saveItem.triggered.connect(self.saveFile)
        fileMenu.addAction(saveItem)

        # SubMenu of File - Allows the user to exit the application
        quit = QtWidgets.QAction("Quit",self)
        quit.triggered.connect(self.close)
        fileMenu.addAction(quit)

        # SubMenu of Edit - Adds a row to the Table Widget
        addRow = QtWidgets.QAction("Add Row",self)
        addRow.triggered.connect(self.addRowDialog)
        editMenu.addAction(addRow)

        # SubMenu of Edit - Deletes the first row of Table Widget
        delFirstRow = QtWidgets.QAction("Delete First Row",self)
        delFirstRow.triggered.connect(self.delFirstRow)
        editMenu.addAction(delFirstRow)

        # SubMenu of Edit - Deletes the last row of Table Widget
        delLastRow = QtWidgets.QAction("Delete Last Row",self)
        delLastRow.triggered.connect(self.delLastRow)
        editMenu.addAction(delLastRow)

        # SubMenu of Edit - Deletes all selected rows of Table Widget
        delRows = QtWidgets.QAction("Delete Rows",self)
        delRows.triggered.connect(self.delRows)
        editMenu.addAction(delRows)

        # SubMenu of Database - Allows user to input new SQL Query Script
        querySQL = QtWidgets.QAction("New Query",self)
        querySQL.triggered.connect(self.querySQL)
        dbMenu.addAction(querySQL)

        # SubMenu of Database - Updates table data to open database table
        updateSQL = QtWidgets.QAction("Update",self)
        updateSQL.triggered.connect(self.updateSQL)
        dbMenu.addAction(updateSQL)

    def resetTable(self):
        """ This method resets the Table Widget properties to a known condition """

        self.table = QtWidgets.QTableWidget(1,3)
        self.columnLabels = []
        self.table.setHorizontalHeaderLabels(self.columnLabels)
        self.setCentralWidget(self.table)
        self.table.resizeColumnsToContents()

        # Sorting must be disabled prior to importing data into the table
        self.table.setSortingEnabled(False)

    def connSQL(self, filename):
        """ This method creates the initial SQLite3 database connection and
        returns the available tables and views for the user to navigate.

        Args:
            filename (str): Specifies the location of the database.
        Returns:
            self.DbTables (list): Specifies the available tables and views in
                the database.
        """

        def connect(database):
            """ This method creates a connection to the SQLite3 database.

            Args:
                database (str): Specifies location of database.
            Returns:
                conn (obj): Allows user to use connection for accessing database
                    if the database connection is successfully established.
            Raises:
                sqlite3.Error (Error): Displays error message for user when unable
                    to connect to database.
            """

            try:
                conn = sqlite3.connect(database)
                return conn
            except sqlite3.Error:
                print(sqlite3.Error)
            return None

        def query(conn):
            """ This method uses the database connection to perform querys.

            Args:
                conn (obj): Specifies valid connection path for database access.
            Returns:
                rows (list): Specifies result of database query.
            """

            cur = conn.cursor()
            cur.execute("SELECT name FROM sqlite_master")
            rows = cur.fetchall()
            return rows

        def supervisor(filename):
            """ This method uses the filename to execute the connection to database.

            Args:
                filename (str): Used for identifying the location of the database.
            Returns:
                query(conn) (list):
            """

            self.conn = connect(filename)
            with self.conn:
                return (query(self.conn))

        def main():
            """ This method allows the user to select the database location and executes
            the initial query for available tables in the database.  If the user tries
            to select a file that is not a *.db file, a popup message will be created
            informing the user that they selected the wrong file format.
            """

            filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File",".")
            if (filename != ""):
                if (filename.endswith("db")):
                    self.db = filename
                    self.dbTables = supervisor(self.db)
                    self.querySQL()
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setText("Incorrect format")
                    msg.exec_()
        main()

    def querySQL(self):
        """ This method uses the existing SQLite3 database connection information
        and returns the user specified query results to update the Table Widget.

        Returns:
            header (list): Used to populate table column names.
            data (list): Used to populate table data from query results.
        """

        def query(conn, queryString):
            """ This method uses the database connection to perform querys.

            Args:
                conn (obj): Specifies valid connection path for database access.
                queryString (str): Specifies the SQLite3 query command.
            Returns:
                rows (list): Specifies result of database query.
            """

            cur = conn.cursor()
            cur.execute(queryString)
            h = [description[0] for description in cur.description]
            rows = cur.fetchall()
            return h, rows

        def supervisor(queryString):
            """ This method uses the existing connection to conenect to the database and execute the statement.

            Args:
                queryString (str): Specifies the SQLite3 query command.
            Returns:
                query(conn, queryString) (list):
            """

            with self.conn:
                return(query(self.conn, queryString))

        def getStatement():
            """ This method generates a popup dialog box to allow the user to input a
            SQLite3 statement to query the database.

            Returns:
                popUp.textValue() (str): Contains user specified SQLite3 statement to pass
                    to the database for processing.
            """

            self.resetTable()

            # Convert tuple into a string and reformat to make the list easier to read
            tableString = ""
            for table in self.dbTables:
                table = str(table).replace(",", "").replace("(", "").replace(")", "").replace("'", "")
                tableString += table+", "

            # Create the popup allowing the user to input the SQLite3 statement
            popUp = QtWidgets.QInputDialog(self)
            popUp.setInputMode(QtWidgets.QInputDialog.TextInput)
            popUp.setWindowTitle('Enter Table Name')
            popUp.setLabelText("Please enter the tablename below:\n"+tableString.strip().strip(","))
            popUp.setTextValue("select * from sales_view")
            popUp.resize(400,200)
            ok = popUp.exec_()
            return(popUp.textValue())

        def updateTable(queryString):
            """ This method updates the Table Widget using the results of the SQLite3 query.

            Args:
                queryString (str): Specifies the SQLite3 query command.
            """

            queryList = queryString.split(" ")
            self.activeDbTable = queryList[len(queryList)-1]
            header, data = supervisor(queryString)
            self.table.setColumnCount(len(header))
            self.table.setRowCount(len(data))
            self.columnLabels = list(header)
            self.table.setHorizontalHeaderLabels(self.columnLabels)

            # Updates the table widget and ensures price value is a float for sorting
            for row in range(len(data)):
                for col in range(len(data[row])):
                    qitem = QtWidgets.QTableWidgetItem()
                    if data[row][col] == "price":
                        qitem.setData(QtCore.Qt.EditRole,float(data[row][col]))
                    else:
                        qitem.setData(QtCore.Qt.EditRole,data[row][col])
                    self.table.setItem(row,col,qitem)

        def main():
            """ This method allows the user to specify a SQLite3 statement, return the
            results, and populate and update the Table Widget.
            """

            queryString = getStatement()
            updateTable(queryString)
            self.table.resizeColumnsToContents()
            self.setCentralWidget(self.table)
            self.table.setSortingEnabled(True)

        main()

    def updateSQL(self):
        """ This method uses the existing SQLite3 database connection information
        and updates the SQLite3 database table to what is displayed in the
        Table Widget.
        """

        def updateAll(conn, query):
            """ This method updates the SQLite3 database table using the self
            generated update statement.

            Args:
                conn (str): Used for identifying the location of the database.
                query (str): Specifies the SQLite3 query command.
            """

            cur = conn.cursor()
            cur.execute(query)
            print("DataBase Updated: "+query)

        def supervisor(query):
            """ This method uses the existing connection to conenect to the database and execute the statement.

            Args:
                queryString (str): Specifies the SQLite3 update command.
            Returns:
                query(conn, queryString) (list):
            """

            with self.conn:
                updateAll(self.conn, query)

        def updateDb():
            """ This method generates the update statement that is used to update
            the SQLite3 database table and notifies the user when the update is
            complete.  NOTE: This does not append new information to the database.
            """

            for row in range(self.table.rowCount()):
                query = "UPDATE "+self.activeDbTable+" SET "
                id = 0
                for col in range(self.table.columnCount()):
                    header = self.columnLabels[col]
                    itemValue = self.table.item(row, col).text()
                    query += header+" = '"+itemValue+"', "
                    # ID must be an integer for the SQLite3 statement
                    if header == "id":
                        id = int(itemValue)
                query = query.strip().strip(",")
                query += " WHERE id = "+str(id)+";"
                supervisor(query)
            msg = QtWidgets.QMessageBox()
            msg.setText("Update Complete.")
            msg.exec_()

        def main():
            """ This method updates the SQLite3 database table to match the
            information displayed in the Table Widget and prevents the user
            from trying to update a view.
            """

            if self.activeDbTable.endswith("view"):
                msg = QtWidgets.QMessageBox()
                msg.setText("Cannot modify a view.")
                msg.exec_()
            else:
                updateDb()

        main()

    def openFile(self):
        """ Opens a dialog box and directs processing based on file extension.
        If the file extension is not recognized, a popup will display to inform
        the user.
        """

        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File",".")
        if (filename != ""):
            self.resetTable()
            if (filename.endswith("json")):
                self.openJson(filename)
            elif (filename.endswith("xml")):
                self.openXml(filename)
            elif (filename.endswith("csv")):
                self.openCsv(filename)
            else:
                msg = QtWidgets.QMessageBox()
                msg.setText("Incorrect format")
                msg.exec_()

    def openJson(self, filename):
        """ This method is used to process incoming JSON files, update
        the Table Widget, and refresh the Table Widget data.

        Args:
            filename (str): Used to identify the filename and location.
        """

        def updateTable(filename):
            """ This method is used to process incoming JSON files and update
            the Table Widget.

            Args:
                filename (str): Used to identify the filename and location.
            """

            with open(filename) as infile:
                contents_in = infile.read()
            sales_dict = loads(contents_in)
            sales_list = sales_dict["sales"]
            self.table.setRowCount(len(sales_list))
            keys = sales_list[0].keys()
            self.table.setColumnCount(len(keys))
            self.columnLabels = list(keys)
            self.table.setHorizontalHeaderLabels(self.columnLabels)

            # Populates the Table Widget
            row = 0
            for sale in sales_list:
                col=0
                for key in sale.keys():
                    qitem = QtWidgets.QTableWidgetItem()
                    if key == "price":
                        qitem.setData(QtCore.Qt.EditRole,float(sale[key]))
                    else:
                        qitem.setData(QtCore.Qt.EditRole,sale[key])
                    self.table.setItem(row,col,qitem)
                    col += 1
                row += 1

        def main(filename):
            """ This method is used to process incoming JSON files and refresh
            the Table Widget data.

            Args:
                filename (str): Used to identify the filename and location.
            """

            updateTable(filename)
            self.table.resizeColumnsToContents()
            self.setCentralWidget(self.table)
            self.table.setSortingEnabled(True)

        main(filename)

    def openXml(self, filename):
        """ This method is used to process incoming XML files, update
        the Table Widget, and refresh the Table Widget data.

        Args:
            filename (str): Used to identify the filename and location.
        """

        def updateTable(filename):
            """ This method is used to process incoming XML files, update
            the Table Widget.

            Args:
                filename (str): Used to identify the filename and location.
            """

            with open(filename) as infile:
                soup = BeautifulSoup(infile, "xml")
            priceCol = 0
            sale_tags = soup.find_all("sale")
            self.table.setRowCount(len(sale_tags))
            num_children = len(list(sale_tags[0].children))
            columnNames = []
            for child in sale_tags[0].children:
                if(child.name != None):
                    if child.name == "price":
                        priceCol = len(columnNames)
                    columnNames.append(child.name)
            self.table.setColumnCount(len(columnNames))
            self.columnLabels = columnNames
            self.table.setHorizontalHeaderLabels(self.columnLabels)

            # Populates the Table Widget
            for row in range(len(columnNames)):
                col=0
                for child in sale_tags[row].children:
                    if(child.name != None):
                        qitem = QtWidgets.QTableWidgetItem()
                        if col == priceCol:
                            qitem.setData(QtCore.Qt.EditRole,float(child.get_text()))
                        else:
                            qitem.setData(QtCore.Qt.EditRole,child.get_text())
                        self.table.setItem(row,col,qitem)
                        col += 1

        def main(filename):
            """ This method is used to process incoming XML files and refresh
            the Table Widget data.

            Args:
                filename (str): Used to identify the filename and location.
            """

            updateTable(filename)
            self.table.resizeColumnsToContents()
            self.setCentralWidget(self.table)
            self.table.setSortingEnabled(True)

        main(filename)

    def openCsv(self, filename):
        """ This method is used to process incoming CSV files, update
        the Table Widget, and refresh the Table Widget data.

        Args:
            filename (str): Used to identify the filename and location.
        """

        def updateTable(filename):
            """ This method is used to process incoming CSV files, update
            the Table Widget.

            Args:
                filename (str): Used to identify the filename and location.
            """

            with open(filename, "r") as infile:
                columnNames = infile.readline()
                lines = infile.readlines()
            columnNames = columnNames.strip().split("|")
            self.table.setColumnCount(len(columnNames))
            self.columnLabels = columnNames
            self.table.setHorizontalHeaderLabels(self.columnLabels)
            self.table.setRowCount(len(lines))

            # Populates the Table Widget
            for row in range(len(lines)):
                lines[row] = lines[row].strip().split("|")
                for col in range(len(lines[row])):
                    qitem = QtWidgets.QTableWidgetItem()
                    if columnNames[col] == "price":
                        qitem.setData(QtCore.Qt.EditRole,float(lines[row][col]))
                    else:
                        qitem.setData(QtCore.Qt.EditRole,lines[row][col])
                    self.table.setItem(row,col,qitem)

        def main(filename):
            """ This method is used to process incoming CSV files and refresh
            the Table Widget data.

            Args:
                filename (str): Used to identify the filename and location.
            """

            updateTable(filename)
            self.table.resizeColumnsToContents()
            self.setCentralWidget(self.table)
            self.table.setSortingEnabled(True)

        main(filename)

    def saveFile(self):
        """ Opens a dialog box and directs processing based on file extension.
        If the file extension is not recognized, a popup will display to inform
        the user.
        """

        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save File",".")
        if (filename != ""):
            if (filename.endswith("json")):
                self.saveJson(filename)
            elif (filename.endswith("xml")):
                self.saveXml(filename)
            elif (filename.endswith("csv")):
                self.saveCsv(filename)
            elif (filename.endswith("html")):
                self.saveHtml(filename)
            else:
                msg = QtWidgets.QMessageBox()
                msg.setText("Incorrect format")
                msg.exec_()

    def saveJson(self, filename):
        """ This method is used to process outgoing JSON files using data
        from the Table Widget.

        Args:
            filename (str): Used to identify the filename and location.
        """

        def processData():
            """ This method is used to process outgoing JSON files using data
            from the Table Widget.

            Args:
                filename (str): Used to identify the filename and location.
            Returns:
                output (dict): Used to store data in the proper JSON file
                format.
            """

            output = {}
            sales = []
            for row in range(self.table.rowCount()):
                sale = {}
                for col in range(self.table.columnCount()):
                    header = self.columnLabels[col]
                    itemValue = self.table.item(row, col).text()
                    # Saves id as integer for sorting
                    if header == "id":
                        sale[header] = int(itemValue)
                    # Saves price as float for sorting
                    elif header == "price":
                        sale[header] = float(itemValue)
                    else:
                        sale[header] = itemValue
                sales.append(sale)
            output["sales"] = sales
            return(output)

        def main(filename):
            """ This method is uses JSON dumps to process outgoing JSON files
            using data from the Table Widget.

            Args:
                filename (str): Used to identify the filename and location.
            """

            output = processData()
            with open(filename, "w") as outfile:
                outfile.write(dumps(output, indent=2, separators=(","," : "), sort_keys=False))

        main(filename)

    def saveXml(self, filename):
        """ This method is used to process outgoing XML files using data
        from the Table Widget.

        Args:
            filename (str): Used to identify the filename and location.
        """

        with open(filename, "w") as outfile:
            outfile.write('<?xml version="1.0" ?>')
            outfile.write('\n<sales>')
            for row in range(self.table.rowCount()):
                outfile.write('\n    <sale>')
                for col in range(self.table.columnCount()):
                    header = self.columnLabels[col]
                    itemValue = self.table.item(row, col).text()
                    outfile.write('\n        <'+header+'>'+str(itemValue)+'</'+header+'>')
                outfile.write('\n    </sale>')
            outfile.write('\n</sales>')

    def saveCsv(self, filename):
        """ This method is used to process outgoing CSV files using data
        from the Table Widget.  CSV files will use the '|' as delimiter.

        Args:
            filename (str): Used to identify the filename and location.
        """

        with open(filename, "w") as outfile:
            line = []
            for col in range(self.table.columnCount()):
                header = self.columnLabels[col]
                line.append(header)
            output = "|".join(line)
            outfile.write(output)
            for row in range(self.table.rowCount()):
                line = []
                for col in range(self.table.columnCount()):
                    itemValue = self.table.item(row, col).text()
                    line.append(str(itemValue))
                output = "|".join(line)
                outfile.write('\n'+output)

    def saveHtml(self, filename):
        """ This method is used to process outgoing HTML files using data
        from the Table Widget.  Data will be displayed in a standard HTML
        table with column headers, and the table is using a border='1'.

        Args:
            filename (str): Used to identify the filename and location.
        """

        with open(filename, "w") as outfile:
            outfile.write('<html>')
            outfile.write('\n    <head><title>'+filename+'</title></head>')
            outfile.write('\n    <body>')
            outfile.write('\n        <table border="1">')
            outfile.write('\n            <tr>')
            for col in range(self.table.columnCount()):
                header = self.columnLabels[col]
                outfile.write('\n                <th>'+header+'</th>')
            outfile.write('\n            </tr>')
            for row in range(self.table.rowCount()):
                outfile.write('\n            <tr>')
                for col in range(self.table.columnCount()):
                    itemValue = self.table.item(row, col).text()
                    outfile.write('\n                <td>'+itemValue+'</td>')
                outfile.write('\n            </tr>')
            outfile.write('\n        </table>')
            outfile.write('\n    </body>')
            outfile.write('\n</html>')

    def addRowDialog(self):
        """ Opens a dialog box and allows the user to input data for the next
        row that will be inserted at the bottom of the Table Widget.

        numRows = self.table.rowCount()
        self.table.insertRow(numRows)
        """

        self.myDialog = QtWidgets.QDialog(self)
        self.myDialog.setWindowTitle("Enter Data")
        layout = QtWidgets.QGridLayout()
        self.textBoxes = {}

        # Populates column names to understand which text box goes where
        row = 1
        for colname in self.columnLabels:
            label = QtWidgets.QLabel("Enter "+colname)
            layout.addWidget(label,row,0)
            self.textBoxes[colname] = QtWidgets.QLineEdit()
            layout.addWidget(self.textBoxes[colname],row,1)
            row += 1

        # Create buttons
        buttons = QtWidgets.QDialogButtonBox()
        buttons.setOrientation(QtCore.Qt.Vertical)
        buttons.addButton("Cancel",QtWidgets.QDialogButtonBox.RejectRole)
        buttons.addButton("Add",QtWidgets.QDialogButtonBox.AcceptRole)

        # Action associated with cancel
        self.myDialog.connect(buttons,QtCore.SIGNAL("rejected()"),self.myDialog.close)

        # Action associated with add
        self.myDialog.connect(buttons,QtCore.SIGNAL("accepted()"),self.addRowTable)

        # Add the layout to the dialog box
        layout.addWidget(buttons,0,2,3,1,QtCore.Qt.AlignCenter)
        self.myDialog.setLayout(layout)
        self.myDialog.exec_()

    def addRowTable(self):
        """ Inserts the next row at the bottom of the Table Widget.  Data is
        then imported into the Table Widget from addRowDialog.
        """

        # Close the dialogbox
        self.myDialog.done(0)
        self.table.sortItems(0, order=QtCore.Qt.AscendingOrder)
        self.table.insertRow(self.table.rowCount())
        lastRow = self.table.rowCount()-1
        col=0

        # Retrieve the content from the textboxes
        for colname in self.columnLabels:
            qitem = QtWidgets.QTableWidgetItem()
            qitem.setData(QtCore.Qt.EditRole,self.textBoxes[colname].text())
            self.table.setItem(lastRow,col,qitem)
            col += 1

    def delFirstRow(self):
        """ Deletes the top row of the Table Widget """

        self.table.removeRow(0)

    def delLastRow(self):
        """ Deletes the bottom row of the Table Widget """

        self.table.removeRow(self.table.rowCount()-1)

    def delRows(self):
        """ Deletes the selected row(s) of the Table Widget """

        selectedRows = []
        for row in self.table.selectionModel().selectedRows():
            selectedRow = QtCore.QPersistentModelIndex(row)
            selectedRows.append(selectedRow)
        for row in selectedRows:
            self.table.removeRow(row.row())

# Ensure the script is not being ran as a module for another script
if __name__ == "__main__":

    # Clear the screen
    subprocess.call('clear', shell=True)

    # Create an instance of the class and launch the dialog box
    dark_stylesheet = qdarkstyle.load_stylesheet_pyside2()
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(dark_stylesheet)
    mygui = Project2()
    sys.exit(app.exec_())
