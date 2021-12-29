#!/usr/bin/env python3
"""
Name:    Craig Opie
Class:   CENT110
File:    project2.py

Algorithm:
1)  Import 'BeautifulSoup' as the XML and HTML parser.
2)  Import 'dumps' and 'loads' for processing JSON files.
3)  Import 'sqlite3' for interaction with the SQL database.
4)  Import 'subprocess' to use to clear the terminal window prior to running.
5)  Import 'sys' to interact with system files and directories.
6)  Utilize exception handling by Try:
    A)  Import 'QtWidgets' and 'QtCore' from PySide[version = 1.0].
    B)  Rename QtGui as QtWidgets for PySide[version = 1.0].
7)  Except, if an ImportError occurs:
    A)  Import 'QtWidgets' and 'QtCore' from PySide2.
8)  Create the GUI object, class 'Project2':
    A)  Initialize the instance:
        1.  Initialize the QMainWindow.
        2.  Create a class wide string variable 'activeDbTable'.
        3.  Create a class wide list variable 'columnLabels'.
        4.  Create a class wide string variable 'conn'.
        5.  Create a class wide string variable 'db'.
        6.  Create a class wide list variable 'dbTables'.
        7.  Create a Table Widget as 'table'.
        8.  Assign the 'table' column titles from columnLabels.
        9.  Initialize the GUI menu bar.
        10. Assign the table as the Central Widget in the GUI.
        11. Assign the window size.
        12. Assing the window title.
        13. Display the GUI.
    B)  Initialize the menu.
        1.  Assign the Menubar as a variable 'menubar'.
        2.  Create a menu item 'File'.
        3.  Create a menu item 'Edit'.
        4.  Create a menu item 'Database'.
        5.  Under the 'File' menu:
            a.  Assign 'Conn SQL' to connSQL.
            b.  If it is clicked, run the perform's connSQL method.
            c.  Link the button to the action that is available.
            d.  Assign 'Open' to openItem.
            e.  If it is clicked, run the perform's openFile method.
            f.  Link the button to the action that is available.
            g.  Assign 'Save As' to saveItem.
            h.  If it is clicked, run the perform's saveFile method.
            i.  Link the button to the action that is available.
            j.  Assign 'Quit' to quit.
            k.  If it is clicked, run the perform's close method.
            l.  Link the button to the action that is available.
        6.  Under the 'Edit' menu:
            a.  Assign 'Add Row' to addRow.
            b.  If it is clicked, run the perform's addRowDialog method.
            c.  Link the button to the action that is available.
            d.  Assign 'Delete First Row' to delFirstRow.
            e.  If it is clicked, run the perform's delFirstRow method.
            f.  Link the button to the action that is available.
            g.  Assign 'Delete Last Row' to delLastRow.
            h.  If it is clicked, run the perform's delLastRow method.
            i.  Link the button to the action that is available.
            j.  Assign 'Delete Rows' to delRows.
            k.  If it is clicked, run the perform's 'delRows' method.
            l.  Link the button to the action that is available.
        7.  Under the 'Database' menu:
            a.  Assign 'New Query' to querySQL.
            b.  If it is clicked, run the perform's querySQL method.
            c.  Link the button to the action that is available.
            d.  Assign 'Update' to 'updateSQL'.
            e.  If it is clicked, run the perform's updateSQL method.
            f.  Link the button to the action that is available.
    C)  Reset the table back to a known condition without sorting:
        1.  Assign the QTableWidget to 'table'.
        2.  Restore the columnLabels to hold a list type format.
        3.  Restore the class wide list variable 'columnLabels'.
        4.  Ensure the Table is the 'CentralWidget'.
        5.  Resize the Table to fit the contents.
        6.  Disable sorting to ensure the Table Widget enables correctly.
    D)  Perform the initial connection to the SQLite3 database and return the
        tables and views that are available for the user to browse.
        1.  Connect to the database:
            a.  Enter an exception handling sequence using try:
                i.  Assign the connection 'conn'.
                ii. Return the 'conn' if no errors took place.
            b.  Except if there are database errors:
                i.  Print the error for the user to see.
            c.  If the 'conn' didn't work, return none.
        2.  Query using the 'conn':
            a.  Assign the cursor to 'cur'.
            b.  Execture a 'select' statement to withdraw the names of all the
                tables and views contained in the database.
            c.  Create a list  containing the statement's results and assign
                to 'rows'.
            d.  Return 'rows'.
        3.  Open the SQLite3 connection and execute the statement:
            a.  Create the SQLite3 connection using the filename.
            b.  Open the SQLite3 connection:
                i.  Execute the query and return the results.
        4.  Allow the user to select the filename, create the connection,
            execute the table query, and call for an additional query.
            a.  Open the open file dialog box and set the PATH to 'filename'.
            b.  Verify the filename is not empty:
                i.  Verify the filename is a database type:
                    a)  Assign the filename to 'self.database'.
                    b)  Assign the result from above to a list of tables
                        'self.dbTables'.
                    c)  Call the 'querySQL' method to allow the user to input
                        a personalized query.
                ii. If the filename was not a database type:
                    a)  Create a popup box 'msg'.
                    b)  Set the text of the popup box to 'Incorrect Format'.
                    c)  Display the popup box.
        5.  Call the method 'main' (step 8.d.4 above).
    E)  Use the existing SQLite3 database connection to return a new user
        specified query results to update the Table Widget:
        1.  Query using the 'conn':
            a.  Assign the cursor to 'cur'.
            b.  Execture a 'select' statement to withdraw the information
                requested by the user.
            c.  Create a list of each field's title and assign to 'h'.
            d.  Create a list containing the statement's results and assign
                to 'rows'.
            e.  Return 'h' and 'rows'.
        2.  Open the SQLite3 connection and execute the statement:
            a.  Open the SQLite3 connection:
                i.  Execute the query and return the results.
        3.  Get the SQLite3 statement from the user using a popup dialog box:
            a.  Reset the Table Widget to a known condition.
            b.  Create a new string called 'tableString' for us to store the
                results of the initial SQLite3 query with all of the table
                names available.
            c.  For each table in 'self.dbTables':
                i.  Transform the tuple into a string, and format to look good.
                ii. Add the table to name to 'tableString'.
            d.  Create the popup dialog for the user.
            e.  Create a text type input method.
            f.  Set the title for the popup.
            g.  Create a label for the user to understand what to put in the
                text field.
            h.  Have a starting point already available for the user in the
                text field.
            i.  Make the popup a small dimension to not fill the screen.
            j.  Display the popup.
            k.  Return the value specified by the user.
        4.  Update the Table Widget with new data:
            a.  Split the user's query into a list 'queryList'.
            b.  Use the last value in the list as the active database table.
            c.  Assign 'header' and 'data' the results of the user's query.
            d.  Set the table to the correct column numbers.
            e.  Set the table to the correct row numbers.
            f.  Assign the column labels the field titles from the database.
            g.  Update the Table Widget to show the new labels.
            h.  For each row:
                i.  for each column:
                    a)  Assign the 'qitem' as an instance of WidgetItem.
                    b)  If the column label is 'price':
                        i)  Make the value in the Table a float type.
                    c)  Otherwise:
                        i)  Just populate the table with the information.
                    d)  Populate the table using the 'qitem'.
        5.  Wrap up all of the different methods into one convenient location
            to allow the user to specify the SQLite3 statement, return the
            results, and populate and update the Table Widget.
            a.  Assign the result of 'getStatement' to 'queryString'.
            b.  Call the 'updateTable' method passing 'queryString' as an
                argument.
            c.  Resize the table to the new specifications.
            d.  Set the Table Widget to have the focus.
            e.  Enable sorting by column names.
        6.  Call the 'main' method (8.E.5) above.
    F)  Update the existing SQLite3 table information with what is displayed
        in the Table Widget:
        1.  Update the table using a self generated update statement:
            a.  Assign the cursor to 'cur'.
            b.  Execture an 'update' statement to insert the information
                changed by the user.
            c.  Print 'Database updated: SQLite3 statement used'.
        2.  Open the SQLite3 connection and execute the statement:
            a.  Open the SQLite3 connection:
                i.  Execute the 'update' statement.
        3.  Generate the SQLite3 statement and update the database:
            a.  For each row in Table Widget:
                i.  Generate the prefix to the 'update' statement as 'query'.
                ii. Create a integer variable to store the 'id' of the entry.
                iii.For each column in Table Widget:
                    a)  Assign 'header' the value of column labels.
                    b)  Assign 'itemValue' the value of the current cell.
                    c)  Add 'header' and 'itemValue' to 'query'.
                    d)  If 'header' is "id":
                        i)  Turn the value into an integer from a string.
                iv. Strip 'query' and remove the final comma at the end.
                v.  Add the WHERE paramater to 'query' with 'id' as the search
                    parameter.
                vi. Run the 'update' query.
            b.  Create a popup box.
            c.  Specify the text to the popup box as "Update Complete".
            d.  Show the popup.
        4.  Wrap up all of the different methods into one convenient location
            to update the SQLite3 database table from Table Widget.  Prevent
            the user from trying to update a view:
            a.  If the 'activeDbTable' name ends with "view":
                i.  Create a popup box.
                ii. Specify the text to the popup box as "Cannot modify a
                    view".
                iii.Show the popup.
            b.  Call the 'updateTable' method passing 'queryString' as an
                argument.
        5.  Call the 'main' method (8.F.4) above.
    G)  Open a file:
        1.  Create an open file dialog box and assign to filename.
        2.  If filename is not blank:
            a.  Reset the Table Widget to a known condition.
            b.  If the file ends with JSON:
                i.  Process the file using the 'openJson' method.
            c.  If the file ends with XML:
                i.  Process the file using the 'openXml' method.
            d.  If the file ends with CSV:
                i.  Process the file using the 'openCsv' method.
            e.  Otherwise:
                i.  Create a popup box.
                ii. Specify the text to the popup box as "Incorrect Format".
                iii.Show the popup.
    H)  Process a JSON file input:
        1.  Update the Table Widget:
            a.  Open the JSON file:
                i.  Read the contents and assign to 'contents_in'.
            b.  Use the JSON.loads function to process 'contents_in' and
                assign to 'sales_dict'.
            c.  Assign the first list of 'sales_dict' to 'sales_list'.
            d.  Set the Table Widget to the number of rows as items in
                'sales_list'.
            e.  Set the entries for each item in 'sales_list' to 'keys'.
            f.  Set the Table Widget to the number of columns as entries in
                'keys'.
            g.  Set the Table Widget column labels to the values in 'keys'.
            h.  Update the Table Widget to show new column label information.
            i.  Assign 'row' to 0.
            j.  For each item in 'sales_list':
                i.  Assign 'col' to 0.
                ii. For each key in sale.keys():
                    a)  Assign the 'qitem' as an instance of WidgetItem.
                    b)  If the 'key' is 'price':
                        i)  Make the value in the Table a float type.
                    c)  Otherwise:
                        i)  Just populate the table with the information.
                    d)  Populate the table using the 'qitem'.
                    e)  Increment 'col' by 1.
                iii.Increment 'row' by 1.
        2.  Process the JSON file and refresh the Table Widget:
            a.  Call the method 'updateTable' using the filename.
            b.  Resize the Table Widget to new values.
            c.  Set the Table Widget to have the focus.
            d.  Enable sorting by column names.
        3.  Call the main method (8.H.2) above.
    I)  Process an XML file input:
        1.  Update the Table Widget:
            a.  Open the XML file:
                i.  Parse the contents using BeautifulSoup and assign to
                    'soup'.
            b.  Create 'priceCol' as 0.
            c.  Create 'sale_tags' and assign the results of searching the
                soup for 'sale'.
            d.  Set the row count to number of items in 'sale_tags'.
            e.  Create 'num_children' and set to the number of items in the
                first item of 'sale_tags'.
            f.  Create a list to store 'columnNames'.
            g.  For each child in the first element of sale_tags:
                i.  If the child is not blank:
                    a)  If child.name is "price":
                        i)  Set 'priceCol' to the length of columnNames.
                    b)  Append child.name to 'columnNames'.
            h.  Set the column count to the number of 'columnNames'.
            i.  Set the column labels to 'columnNames'.
            j.  Update the Table Widget column labels to new values.
            k.  For each row:
                i.  Assign 'col' to 0.
                ii. For each child in sale_tags[row].children:
                    a)  If child.name is not blank:
                        i)  Assign the 'qitem' as an instance of WidgetItem.
                        ii) If the col is 'priceCol':
                            [a]  Make the value in the Table a float type.
                        iii)Otherwise:
                            [a]  Just populate the table with the information.
                        iv) Populate the table using the 'qitem'.
                        v)  Increment 'col' by 1.
        2.  Process the XML file and refresh the Table Widget:
            a.  Call the method 'updateTable' using the filename.
            b.  Resize the Table Widget to new values.
            c.  Set the Table Widget to have the focus.
            d.  Enable sorting by column names.
        3.  Call the main method (8.I.2) above.
    J)  Process a CSV file input:
        1.  Update the Table Widget:
            a.  Open the CSV file:
                i.  Read the first line as 'columnNames'.
                ii. Read the remaining lines as 'lines'.
            b.  Strip and Split 'columnNames' by "|".
            c.  Set the column count to the number of 'columnNames'.
            d.  Set the column labels to 'columnNames'.
            e.  Update the Table Widget column labels to new values.
            f.  Set the row count to number of items in 'lines'.
            k.  For each row:
                i.  Strip and split the row using "|".
                ii. For each column:
                    a)  Assign the 'qitem' as an instance of WidgetItem.
                    b)  If the col is 'priceCol':
                        i)  Make the value in the Table a float type.
                    c)  Otherwise:
                        i)  Just populate the table with the information.
                    d)  Populate the table using the 'qitem'.
        2.  Process the CSV file and refresh the Table Widget:
            a.  Call the method 'updateTable' using the filename.
            b.  Resize the Table Widget to new values.
            c.  Set the Table Widget to have the focus.
            d.  Enable sorting by column names.
        3.  Call the main method (8.J.2) above.
    K)  Save a file:
        1.  Create an save file dialog box and assign to filename.
        2.  If filename is not blank:
            a.  If the file ends with JSON:
                i.  Process the file using the 'saveJson' method.
            b.  If the file ends with XML:
                i.  Process the file using the 'saveXml' method.
            c.  If the file ends with CSV:
                i.  Process the file using the 'saveCsv' method.
            c.  If the file ends with HTML:
                i.  Process the file using the 'saveHtml' method.
            d.  Otherwise:
                i.  Create a popup box.
                ii. Specify the text to the popup box as "Incorrect Format".
                iii.Show the popup.
    L)  Save a JSON file output:
        1.  Process Table Widget Data:
            a.  Create a dictionary called 'output'.
            b.  Create a list called 'sales'.
            c.  For each row:
                i.  Reset a dictionary called 'sale'.
                ii. For each column:
                    a)  Create a variable 'header' and assign the column
                        labels.
                    b)  Create a variable 'itemValue' and assign it to the
                        Table Widget item.
                    c)  If 'header' == "id":
                        i)  Add the 'header' as a key and itemValue as a value
                            but make it an integer and store in 'sale'.
                    d)  Else if 'header' == "price":
                        i)  Add the 'header' as a key and itemValue as a value
                            but make it a float and store in 'sale'.
                    e)  Else:
                        i)  Add the 'header' as a key and itemValue as a value
                            and store in 'sale'.
                iii.Append 'sale' to 'sales' list.
            d.  Add "sales" as the key and 'sales' as the value and store in
                'output'.
        2.  Process data and write file:
            a.  'Output' = method (8.L.1) above.
            b.  Open filename in write mode:
                i.  Use the JSON.dumps to write a JSON file using 'output'.
        3.  Call the main method (8.L.2) above.
    M)  Save a XML file output:
        1.  Open filename in write mode:
            a.  Write the XML version line to the file.
            b.  Write the open tag for 'sales'.
            c.  For each row:
                i.  Write the open tag for 'sale'.
                ii. For each column:
                    a)  Create a variable 'header' and assign the column
                        labels.
                    b)  Create a variable 'itemValue' and assign it to the
                        Table Widget item.
                    c)  Write the 'header' open and close tags and write
                        'itemValue' as the contents.
                iii.Write the closing tag for 'sale'.
            d.  Write the closing tag for 'sales'.
    N)  Save a CSV file output:
        1.  Open filename in write mode:
            a.  Create a new list 'line':
            b.  For each column:
                i.  Create a variable 'header' and assign the column
                    labels.
                ii. Append 'header' to 'line'.
            c.  Join 'line' using a "|" and store in 'output'.
            d.  Write 'output' to the file.
            e.  For each row:
                i.  reset the list 'line'.
                ii. For each column:
                    a)  Create a variable 'itemValue' and assign it to the
                        Table Widget item.
                    b)  Append 'itemValue' to 'line'.
                iii.Join 'line' using a "|" and store in 'output'.
                iv. Write 'output' to the file.
    O)  Save a HTML file output:
        1.  Open filename in write mode:
            a.  Write the opening tag for 'html'.
            b.  Write the 'head' and 'title' tag information.
            c.  Write the 'body' tag.
            d.  Write the 'table' tag with a border.
            e.  Write the table header row opening tag.
            f.  For each column:
                i.  Create a variable 'header' and assign the column
                    labels.
                ii. Write the column header values to the table.
            g.  Write the table header row closing tag.
            h.  For each row:
                i.  Write the table row opening tag.
                ii. For each column:
                    a)  Create a variable 'itemValue' and assign it the
                        Table Widget item.
                    b)  Write the 'itemValue' with table details tags.
                iii.Write the table row closing tag.
            i.  Write the closing tag for the table.
            j.  Write the closing tag for the body.
            k.  Write the closing tag for html.
    P)  Add a row to the Table Widget using dialog box:
        1.  Create a dialog box.
        2.  Set the window title to "Enter Data".
        3.  Utilize a grid layout for the dialog box contents.
        4.  Reset the class wide dictionary 'self.textBoxes'.
        5.  Create a variable 'row' and assign 1.
        6.  For each column:
            a.  Create a lable "Enter 'colname'".
            b.  Assign the lable widget to the layout.
            c.  Assign the class wide dictionary 'self.textBoxes[colname]'.
            d.  Assign the textbox widget to the layout.
            e.  Increment row.
        7.  Create 'buttons' using the QDialogButtonBox function.
        8.  Set the 'buttons' orientation as vertical.
        9.  Add the first button as cancel with a reject role.
        10. Add the second button as add with an accept role.
        11. Assign the reject role.
        12. Assign the accept role.
        13. Assign the 'buttons' a layout position.
        14. Set the layout into the dialog box.
        15. Show the dialog box.
    Q)  Use data from (8.P) to create and populate a new row for Table Widget.
        1.  Close the previous dialog box.
        2.  Sort the table in assending order by id.
        3.  Insert a new row.
        4.  Assign 'lastRow' as the number of rows - 1 for index purposes.
        5.  Create a variable 'col' and assign 0.
        6.  For each column:
            a.  Assign the 'qitem' as an instance of WidgetItem.
            b.  Populate the 'qitem' with the information from column.
            d.  Populate the table using the 'qitem'.
            e.  Increment 'col' by 1.
    R)  Delete the first row of the Table Widget:
        1.  Remove row with index 0.
    S)  Delete the last row of the Table Widget:
        1.  Remove row with the last index value.
    T)  Delete the selected row(s) of the Table Widget:
        1.  Create a new list 'selectedRows'.
        2.  For each row that is selected in the Table Widget.
            a.  Create a variable 'selectedRow' which contains the index of
                row.
            b.  Append 'selectedRow' to 'selectedRows'.
        3.  For each row in 'selectedRows':
            a.  Delete the row by index.
9)  If the file is being ran as a standalone file and not being called as a
    module:
    A)  Clear the terminal contents to make it easier for the user to identify
        new text related to this program.
    B)  Create a new instance of QApplication called 'app'.
    C)  Create a new instance of Project2 called 'mygui'.
    D)  Execute 'mygui' and exit 'app' when main dialog box is closed.
"""

from bs4 import BeautifulSoup #Parser for processing XML and HTML files
from json import dumps, loads #Parser for processing JSON files
import requests
import sqlite3 #Database architechture
import subprocess #Allows interaction with shell commands
import sys #Allows interaction with system files and locations

# Ports PySide commands over to PySide2 if PySide2 is installed
try:
    from PySide import QtGui, QtCore
    import PySide.QtGui as QtWidgets
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
        self.textBoxes = {}
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

    def connSQL(self):
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

            if self.activeDbTable == "sales_view":
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

    def addRowTable(self):
        """ Inserts the next row at the bottom of the Table Widget.  Data is
        then imported into the Table Widget from addRowDialog.
        """

        # Close the dialogbox
        self.myDialog.done(0)
        self.table.setSortingEnabled(False)
        self.table.sortItems(0, order=QtCore.Qt.AscendingOrder)
        self.table.insertRow(self.table.rowCount())
        lastRow = self.table.rowCount()-1

        # Reserve the next ID number
        id = self.table.rowCount()

        # Assign the user provided ISBN and URL to scrape
        isbn = self.isbn.text()
        link = "https://isbndb.com/book/"+isbn.replace("-", "")

        # Provide the URL to requests and parse the data using BS4
        page = requests.get(link, timeout=5)
        soup = BeautifulSoup(page.text, 'html.parser')

        # Get the books title information
        title = soup.title.text
        title = title.split(":")
        title = title[0].strip()

        # Parse through the tables to find the Author name and new book price
        author = ""
        price = ""
        for tr in soup.find_all('tr'):
            tr = tr.text.split("\n")
            for each in range(len(tr)):
                tr[each] = tr[each].strip()
                if tr[each] == "Authors":
                    author = tr[each+1]
                if tr[each] == "New":
                    price = tr[each+1]
                    break

        # Format price to be consistent with the table
        price = float(price.replace("$", ""))

        # Add all data scrapped from the web to a list
        data = []
        data.append(author)
        data.append(id)
        data.append(isbn)
        data.append(price)
        data.append(title)

        # Populate the textboxes
        for column in range(len(self.columnLabels)):
            self.textBoxes[self.columnLabels[column]] = data[column]

        # Retrieve the content from the textboxes
        col=0
        for colname in self.columnLabels:
            qitem = QtWidgets.QTableWidgetItem()
            qitem.setData(QtCore.Qt.EditRole,self.textBoxes[colname])
            self.table.setItem(lastRow,col,qitem)
            col += 1

        # Enable sorting now that table manipultation is complete
        self.table.setSortingEnabled(True)

    def addRowDialog(self):
        """ Opens a dialog box and allows the user to input data for the next
        row that will be inserted at the bottom of the Table Widget.

        numRows = self.table.rowCount()
        self.table.insertRow(numRows)
        """

        # Create a new dialog box
        self.myDialog = QtWidgets.QDialog(self)
        self.myDialog.setWindowTitle("Enter Data")
        layout = QtWidgets.QGridLayout()

        # Create the new text box and label
        label = QtWidgets.QLabel("Enter ISBN-13")
        layout.addWidget(label,0,0)
        self.isbn = QtWidgets.QLineEdit()
        layout.addWidget(self.isbn,0,1)

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
    app = QtWidgets.QApplication(sys.argv)
    mygui = Project2()
    sys.exit(app.exec_())
