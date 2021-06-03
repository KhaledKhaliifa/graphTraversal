from PyQt5 import QtCore, QtGui, QtWidgets
import networkx as nx
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    #Declaring the directed and undirected graphs
    g = nx.DiGraph()
    ug = nx.Graph()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(472, 310)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Show Graph button
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        self.runButton.setGeometry(QtCore.QRect(200, 240, 75, 23))
        self.runButton.setObjectName("runButton")
        self.runButton.clicked.connect(self.run)

        #Clear graph button
        self.clearTreeButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearTreeButton.setGeometry(QtCore.QRect(10, 240, 75, 23))
        self.clearTreeButton.setFlat(False)
        self.clearTreeButton.setObjectName("clearTreeButton")
        self.clearTreeButton.clicked.connect(self.clearTree)

        #Add node button
        self.addNodeButt = QtWidgets.QPushButton(self.centralwidget)
        self.addNodeButt.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.addNodeButt.setObjectName("addNodeButt")
        self.addNodeButt.clicked.connect(self.addNode)

        #Remove node button
        self.removeNodeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeNodeButton.setGeometry(QtCore.QRect(10, 50, 75, 23))
        self.removeNodeButton.setObjectName("removeNodeButton")
        self.removeNodeButton.clicked.connect(self.removeNode)

        #Node name textbox
        self.nodeNameText = QtWidgets.QLineEdit(self.centralwidget)
        self.nodeNameText.setGeometry(QtCore.QRect(90, 30, 51, 20))
        self.nodeNameText.setToolTip("")
        self.nodeNameText.setText("")
        self.nodeNameText.setObjectName("nodeNameText")

        #Node name label
        self.nodeNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nodeNameLabel.setGeometry(QtCore.QRect(90, 50, 61, 21))
        self.nodeNameLabel.setObjectName("nodeNameLabel")

        #Add edge button
        self.addEdgeButt = QtWidgets.QPushButton(self.centralwidget)
        self.addEdgeButt.setGeometry(QtCore.QRect(10, 100, 75, 23))
        self.addEdgeButt.setObjectName("addEdgeButt")
        self.addEdgeButt.clicked.connect(self.addEdge)

        #Remove edge button
        self.removeEdgeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeEdgeButton.setGeometry(QtCore.QRect(10, 130, 75, 23))
        self.removeEdgeButton.setObjectName("removeEdgeButton")
        self.removeEdgeButton.clicked.connect(self.removeEdge)

        #"From" node textbox
        self.fromTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.fromTextbox.setGeometry(QtCore.QRect(90, 110, 51, 21))
        self.fromTextbox.setToolTip("")
        self.fromTextbox.setText("")
        self.fromTextbox.setObjectName("fromTextbox")

        #"To" node textbox
        self.toTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.toTextbox.setGeometry(QtCore.QRect(150, 110, 51, 21))
        self.toTextbox.setToolTip("")
        self.toTextbox.setText("")
        self.toTextbox.setObjectName("toTextbox")

        #Edge weight textbox
        self.weightTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.weightTextbox.setGeometry(QtCore.QRect(210, 110, 51, 21))
        self.weightTextbox.setToolTip("")
        self.weightTextbox.setText("")
        self.weightTextbox.setObjectName("weightTextbox")

        #Static labels
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 130, 101, 21))
        self.label_5.setObjectName("label_5")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 130, 31, 21))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 130, 31, 21))
        self.label_4.setObjectName("label_4")

        #Iterative deepening button
        self.itertaiveButton = QtWidgets.QPushButton(self.centralwidget)
        self.itertaiveButton.setGeometry(QtCore.QRect(370, 60, 75, 23))
        self.itertaiveButton.setObjectName("iterativeButton")
        self.itertaiveButton.clicked.connect(self.algoIterative)

        #Breadth first search button
        self.bfsButton = QtWidgets.QPushButton(self.centralwidget)
        self.bfsButton.setGeometry(QtCore.QRect(370, 100, 75, 23))
        self.bfsButton.setObjectName("bfsButton")
        self.bfsButton.clicked.connect(self.algoBFS)

        #A star search button
        self.astarButton = QtWidgets.QPushButton(self.centralwidget)
        self.astarButton.setGeometry(QtCore.QRect(370, 140, 75, 23))
        self.astarButton.setObjectName("astarButton")
        self.astarButton.clicked.connect(self.astarAlgo)

        #Uniform cost search button
        self.ucsButton = QtWidgets.QPushButton(self.centralwidget)
        self.ucsButton.setGeometry(QtCore.QRect(370, 180, 75, 23))
        self.ucsButton.setObjectName("ucsButton")
        self.ucsButton.clicked.connect(self.algoUCS)

        #Starting node textbox
        self.startTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.startTextbox.setGeometry(QtCore.QRect(350, 30, 51, 21))
        self.startTextbox.setToolTip("")
        self.startTextbox.setText("")
        self.startTextbox.setObjectName("startTextbox")

        #Goal node textbox
        self.goalTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.goalTextbox.setGeometry(QtCore.QRect(410, 30, 51, 21))
        self.goalTextbox.setToolTip("")
        self.goalTextbox.setText("")
        self.goalTextbox.setObjectName("goalTextbox")

        self.startLabel = QtWidgets.QLabel(self.centralwidget)
        self.startLabel.setGeometry(QtCore.QRect(360, 10, 31, 21))
        self.startLabel.setObjectName("startLabel")

        self.goalLabel = QtWidgets.QLabel(self.centralwidget)
        self.goalLabel.setGeometry(QtCore.QRect(420, 10, 31, 21))
        self.goalLabel.setObjectName("goalLabel")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(12, 200, 51, 21))
        self.label_6.setObjectName("label_6")

        self.nodesList = QtWidgets.QLabel(self.centralwidget)
        self.nodesList.setGeometry(QtCore.QRect(90, 201, 51, 21))
        self.nodesList.setObjectName("nodesList")

        #Directed radio button
        self.directedButton = QtWidgets.QRadioButton(self.centralwidget)
        self.directedButton.setGeometry(QtCore.QRect(370, 220, 82, 17))
        self.directedButton.setObjectName("directedButton")
        self.directedButton.clicked.connect(self.radioClicked)

        #Undirected radio button
        self.undirectedButton = QtWidgets.QRadioButton(self.centralwidget)
        self.undirectedButton.setGeometry(QtCore.QRect(370, 240, 82, 17))
        self.undirectedButton.setObjectName("undirectedButton")
        self.undirectedButton.clicked.connect(self.radioClicked)
        self.undirectedButton.setChecked(True)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 472, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #Show graph function
    def run(self):
        x = list(self.g.nodes())
        y = list(self.ug.nodes())

        if self.directedButton.isChecked():
            if not x:
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Directed graph is empty!")
                msg.setIcon(QMessageBox.Warning)
                x = msg.exec_()
                return

            else:
                pos = nx.spring_layout(self.g)

                nx.draw(self.g, pos, with_labels=True, node_size=1000, node_color='cyan', )
                labels = nx.get_edge_attributes(self.g, 'weight')
                nx.draw_networkx_edge_labels(self.g, pos, edge_labels=labels)
                nx.draw_networkx_edges(self.g, pos, width=3, arrowsize=30)

                plt.show()

        else:
            if not y:
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Undirected graph is empty!")
                msg.setIcon(QMessageBox.Warning)
                x = msg.exec_()
                return

            else:
                pos = nx.spring_layout(self.ug)

                nx.draw(self.ug, pos, with_labels=True, node_size=1000, node_color='cyan')
                labels = nx.get_edge_attributes(self.ug, 'weight')
                nx.draw_networkx_edge_labels(self.ug, pos, edge_labels=labels)
                nx.draw_networkx_edges(self.ug, pos, width=3, arrowsize=30)

                plt.show()

    #If a radio button is clicked function
    def radioClicked(self):
        x = list(self.g.nodes())
        y = list(self.ug.nodes())

        if self.directedButton.isChecked():
            if not x:
                self.nodesList.setText("Empty Graph!")
                self.nodesList.adjustSize()

            else:
                self.nodesList.setText(f"{self.g.nodes}")
                self.nodesList.adjustSize()

        else:
            if not y:
                self.nodesList.setText("Empty Graph!")
                self.nodesList.adjustSize()

            else:
                self.nodesList.setText(f"{self.ug.nodes}")
                self.nodesList.adjustSize()

    #Add node function
    def addNode(self):
        if self.nodeNameText.displayText() == "":
            msg = QMessageBox()
            msg.setWindowTitle("Error!")
            msg.setText("Please enter a node name!")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
            return

        else:
            if self.directedButton.isChecked():
                self.g.add_node(self.nodeNameText.displayText())
                self.nodesList.setText(f"{self.g.nodes}")
                self.nodesList.adjustSize()

            else:
                self.ug.add_node(self.nodeNameText.displayText())
                self.nodesList.setText(f"{self.ug.nodes}")
                self.nodesList.adjustSize()
            self.clearBoxes()

    #Add edge function
    def addEdge(self):
        if self.fromTextbox.displayText() == "" and self.toTextbox.displayText() == "":

            msg = QMessageBox()
            msg.setWindowTitle("Error!")
            msg.setText("Please enter a starting and ending node!")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()
            return

        elif self.toTextbox.displayText() == "":

            msg = QMessageBox()
            msg.setWindowTitle("Error!")
            msg.setText("Please enter an ending node!")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()
            return

        elif self.fromTextbox.displayText() == "":
            msg = QMessageBox()
            msg.setWindowTitle("Error!")
            msg.setText("Please enter a starting node!")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()
            return

        else:
            if self.directedButton.isChecked():
                if self.weightTextbox.displayText() == "":
                    self.g.add_edge(self.fromTextbox.displayText(), self.toTextbox.displayText())

                else:
                    self.g.add_edge(self.fromTextbox.displayText(), self.toTextbox.displayText(),weight=int(self.weightTextbox.displayText()))

                self.nodesList.setText(f"{self.g.nodes}")
                self.nodesList.adjustSize()
            else:
                if self.weightTextbox.displayText() == "":
                    self.ug.add_edge(self.fromTextbox.displayText(), self.toTextbox.displayText())

                else:
                    self.ug.add_edge(self.fromTextbox.displayText(), self.toTextbox.displayText(),weight=int(self.weightTextbox.displayText()))

                self.nodesList.setText(f"{self.ug.nodes}")
                self.nodesList.adjustSize()
            self.clearBoxes()

    #Remove edge function
    def removeEdge(self):
        if self.fromTextbox.displayText() == "" and self.toTextbox.displayText() == "":

            msg = QMessageBox()
            msg.setWindowTitle("Error!")
            msg.setText("Please enter a starting and ending node!")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()
            return

        elif self.toTextbox.displayText() == "":
            msg = QMessageBox()
            msg.setWindowTitle("Error!")
            msg.setText("Please enter an ending node!")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()
            return

        elif self.fromTextbox.displayText() == "":
            msg = QMessageBox()
            msg.setWindowTitle("Error!")
            msg.setText("Please enter a starting node!")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()
            return

        else:
            if self.directedButton.isChecked():
                if self.checkNode(self.fromTextbox.displayText()) and self.checkNode(self.toTextbox.displayText()):
                    self.g.remove_edge(self.fromTextbox.displayText(), self.toTextbox.displayText())

                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Error!")
                    msg.setText("Please make sure the from and to nodes are correct!")
                    msg.setIcon(QMessageBox.Warning)

                    x = msg.exec_()
                    return

            else:
                if self.checkNodeun(self.fromTextbox.displayText()) and self.checkNodeun(self.toTextbox.displayText()):
                    self.ug.remove_edge(self.fromTextbox.displayText(), self.toTextbox.displayText())

                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Error!")
                    msg.setText("Please make sure the from and to nodes are correct!")
                    msg.setIcon(QMessageBox.Warning)

                    x = msg.exec_()
                    return
            self.clearBoxes()

    #Remove node function
    def removeNode(self):
        if self.directedButton.isChecked():
            if self.nodeNameText.displayText() == "":
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Please enter a node!")
                msg.setIcon(QMessageBox.Warning)

                x = msg.exec_()
                return

            elif not self.checkNode(self.nodeNameText.displayText()):
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("The node you entered does not exist in the directed graph!")
                msg.setIcon(QMessageBox.Warning)

                x = msg.exec_()
                return

            else:
                self.g.remove_node(self.nodeNameText.displayText())
                x = list(self.g.nodes())

                if not x:
                    self.nodesList.setText("Empty Graph!")
                    self.nodesList.adjustSize()

                else:
                    self.nodesList.setText(f"{self.g.nodes}")
                    self.nodesList.adjustSize()
                self.clearBoxes()
        else:
            if self.nodeNameText.displayText() == "":
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Please enter a node!")
                msg.setIcon(QMessageBox.Warning)

                x = msg.exec_()
                return

            elif not self.checkNodeun(self.nodeNameText.displayText()):
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("The node you entered does not exist in the undirected graph!")
                msg.setIcon(QMessageBox.Warning)

                x = msg.exec_()
                return

            else:
                self.ug.remove_node(self.nodeNameText.displayText())
                y = list(self.ug.nodes())

                if not y:
                    self.nodesList.setText("Empty Graph!")
                    self.nodesList.adjustSize()

                else:
                    self.nodesList.setText(f"{self.ug.nodes}")
                    self.nodesList.adjustSize()
                self.clearBoxes()

    #Iterative deepening function
    def algoIterative(self):
        if self.startTextbox.displayText() == "" and self.goalTextbox.displayText() == "":
            msg = QMessageBox()
            msg.setWindowTitle("Error!")
            msg.setText("Please enter a start and goal nodes!")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()
            return

        elif self.startTextbox.displayText() == "":
            msg = QMessageBox()
            msg.setWindowTitle("Error!")
            msg.setText("Please enter a start node!")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()
            return

        elif self.goalTextbox.displayText() == "":
            msg = QMessageBox()
            msg.setWindowTitle("Error!")
            msg.setText("Please enter a valid goal node/s!")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()
            return

        else:
            finalList = []
            if self.directedButton.isChecked():
                myList = self.goalTextbox.displayText()
                listOfInputs = myList.split()

                if self.checkList(listOfInputs):
                    if not self.checkNode(self.startTextbox.displayText()) and not self.checkNode(self.goalTextbox.displayText()):
                        msg = QMessageBox()
                        msg.setWindowTitle("Error!")
                        msg.setText("Please enter valid start and goal nodes!")
                        msg.setIcon(QMessageBox.Warning)

                        x = msg.exec_()
                        return

                    elif not self.checkNode(self.startTextbox.displayText()):
                        msg = QMessageBox()
                        msg.setWindowTitle("Error!")
                        msg.setText("Please enter a valid starting node!")
                        msg.setIcon(QMessageBox.Warning)

                        x = msg.exec_()
                        return

                    elif self.isDiGraphEmpty():
                        msg = QMessageBox()
                        msg.setWindowTitle("Error!")
                        msg.setText("The directed graph has no edges!")
                        msg.setIcon(QMessageBox.Warning)

                        x = msg.exec_()
                        return

                    else:
                        oldGiven = self.goalTextbox.displayText()
                        given =  oldGiven.split()
                        myFlag = False
                        for i in given:
                            if nx.has_path(self.g, self.startTextbox.displayText(), i):
                                myFlag = True
                                break
                        if myFlag:
                            DFS = nx.depth_first_search.dfs_tree(self.g, self.startTextbox.displayText(),0)

                            flag = False
                            counter = 1

                            gEdges = list(self.g.edges())
                            dfsEdges = list(DFS.edges())

                            flag2 = False
                            y = self.goalTextbox.displayText()
                            splitList = y.split()

                            while ((not (gEdges == dfsEdges)) and flag == False):
                                if not flag2:
                                    DFS = nx.depth_first_search.dfs_tree(self.g, self.startTextbox.displayText(), counter)
                                    counter += 1
                                    dfsEdges = list(DFS.edges())

                                    for i in dfsEdges:
                                        for j in splitList:
                                            if i[1] == j:
                                                finalList = dfsEdges
                                                flag = True
                                                flag2 = True

                                                break
                                else:
                                    break

                            graph1 = nx.Graph()
                            graph1.add_edges_from(finalList)
                            nx.draw(graph1, with_labels=True, node_size=1000, node_color='cyan')

                            plt.show()

                        else:
                            msg = QMessageBox()
                            msg.setWindowTitle("Error!")
                            msg.setText(f"There doesn't exist a path from '{self.startTextbox.displayText()}' to one or more of the goal nodes")
                            msg.setIcon(QMessageBox.Warning)

                            x = msg.exec()
                            return
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Error!")
                    msg.setText("Please enter a valid goal node/s!")
                    msg.setIcon(QMessageBox.Warning)

                    x = msg.exec()
                    return

            else:
                if not self.checkNodeun(self.startTextbox.displayText()) and not self.checkNodeun(self.goalTextbox.displayText()):
                    msg = QMessageBox()
                    msg.setWindowTitle("Error!")
                    msg.setText("Please enter valid start and goal nodes!")
                    msg.setIcon(QMessageBox.Warning)

                    x = msg.exec_()
                    return

                elif not self.checkNodeun(self.startTextbox.displayText()):
                    msg = QMessageBox()
                    msg.setWindowTitle("Error!")
                    msg.setText("Please enter a valid starting node!")
                    msg.setIcon(QMessageBox.Warning)

                    x = msg.exec_()
                    return

                elif self.isGraphEmpty():
                    msg = QMessageBox()
                    msg.setWindowTitle("Error!")
                    msg.setText("The undirected graph has no edges!")
                    msg.setIcon(QMessageBox.Warning)

                    x = msg.exec_()
                    return

                else:
                    myList = self.goalTextbox.displayText()
                    listOfInputs = myList.split()
                    if self.checkListun(listOfInputs):
                        oldGiven = self.goalTextbox.displayText()
                        given = oldGiven.split()
                        myFlag = False
                        for i in given:
                            if nx.has_path(self.ug, self.startTextbox.displayText(), i):
                                myFlag = True
                                break
                        if myFlag:
                            DFS = nx.depth_first_search.dfs_tree(self.ug, self.startTextbox.displayText(), 0)

                            flag = False
                            counter = 1

                            gEdges = list(self.ug.edges())
                            dfsEdges = []

                            flag2 = False
                            y = self.goalTextbox.displayText()
                            splitList = y.split()

                            while ((not (gEdges == dfsEdges)) and flag == False):
                                dfsEdges=list(DFS.edges())
                                if not flag2:

                                    DFS = nx.depth_first_search.dfs_tree(self.ug, self.startTextbox.displayText(), counter)
                                    counter += 1
                                    dfsEdges = list(DFS.edges())
                                    for i in dfsEdges:
                                        for j in splitList:
                                            if i[1] == j:
                                                finalList = dfsEdges
                                                flag = True
                                                flag2 = True

                                                break
                                else:
                                    break

                            graph1 = nx.Graph()
                            graph1.add_edges_from(finalList)
                            nx.draw(graph1, with_labels=True, node_size=1000, node_color='cyan')

                            plt.show()

                        else:
                            msg = QMessageBox()
                            msg.setWindowTitle("Error!")
                            msg.setText(f"There doesn't exist a path from '{self.startTextbox.displayText()}' to one or more of the goal nodes")
                            msg.setIcon(QMessageBox.Warning)

                            x = msg.exec()
                            return

                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Error!")
                        msg.setText("Please enter a valid goal node/s!")
                        msg.setIcon(QMessageBox.Warning)

                        x = msg.exec()
                        return

    #Breadth first search function
    def algoBFS(self):

        if self.startTextbox.displayText() == "" and self.goalTextbox.displayText() == "":
            msg = QMessageBox()
            msg.setWindowTitle("Error!")
            msg.setText("Please enter a start and goal nodes!")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()
            return

        elif self.startTextbox.displayText() == "":
            msg = QMessageBox()
            msg.setWindowTitle("Error!")
            msg.setText("Please enter a starting node!")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()
            return

        elif self.goalTextbox.displayText() == "":
            msg = QMessageBox()
            msg.setWindowTitle("Error!")
            msg.setText("Please enter a valid goal node/s!")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec()
            return

        if self.directedButton.isChecked():
            if not self.checkNode(self.startTextbox.displayText()):
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Please enter a valid starting node!")
                msg.setIcon(QMessageBox.Warning)

                x = msg.exec_()
                return
            elif self.isDiGraphEmpty():
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("The directed graph has no edges!")
                msg.setIcon(QMessageBox.Warning)

                x = msg.exec_()
                return
            else:
                myList = self.goalTextbox.displayText()
                listOfInputs = myList.split()
                if self.checkList(listOfInputs):
                    oldGiven = self.goalTextbox.displayText()
                    given = oldGiven.split()
                    myFlag = False
                    for i in given:
                        if nx.has_path(self.g, self.startTextbox.displayText(), i):
                            myFlag = True
                            break
                    if myFlag:
                        self.BFS = nx.breadth_first_search.bfs_tree(self.g, self.startTextbox.displayText())

                        x = list(self.BFS.edges())
                        y = self.goalTextbox.displayText()

                        splitList = y.split()
                        counter1 = 0
                        y2 = []
                        flag = False
                        for i in x:
                            if not flag:
                                counter1 += 1
                                for j in splitList:
                                    if i[1] == j:
                                        y2 = x[0:counter1]
                                        flag = True

                                        break
                            else:
                                break

                        graph2 = nx.DiGraph()
                        graph2.add_edges_from(y2)
                        nx.draw(graph2, with_labels=True, node_size=1000, node_color='cyan')

                        plt.show()

                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Error!")
                        msg.setText(
                            f"There doesn't exist a path from '{self.startTextbox.displayText()}' to one or more of the goal nodes")
                        msg.setIcon(QMessageBox.Warning)

                        x = msg.exec()
                        return
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Error!")
                    msg.setText("Please enter a valid goal node/s!")
                    msg.setIcon(QMessageBox.Warning)

                    x = msg.exec()
                    return

        else:
            if not self.checkNodeun(self.startTextbox.displayText()):
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Please enter a valid starting node!")
                msg.setIcon(QMessageBox.Warning)

                x = msg.exec_()
                return
            elif self.isGraphEmpty():
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("The undirected graph has no edges!")
                msg.setIcon(QMessageBox.Warning)

                x = msg.exec_()
                return
            else:
                myList = self.goalTextbox.displayText()
                listOfInputs = myList.split()
                if self.checkListun(listOfInputs):
                    oldGiven = self.goalTextbox.displayText()
                    given = oldGiven.split()
                    myFlag = False
                    for i in given:
                        if nx.has_path(self.ug, self.startTextbox.displayText(), i):
                            myFlag = True
                            break
                    if myFlag:
                        self.BFS = nx.breadth_first_search.bfs_tree(self.ug, self.startTextbox.displayText())

                        x = list(self.BFS.edges())
                        y = self.goalTextbox.displayText()

                        splitList = y.split()
                        counter1 = 0
                        y2 = []
                        flag = False
                        for i in x:
                            if not flag:
                                counter1 += 1
                                for j in splitList:
                                    if i[1] == j:
                                        y2 = x[0:counter1]
                                        flag = True

                                        break
                            else:
                                break

                        graph2 = nx.Graph()
                        graph2.add_edges_from(y2)
                        nx.draw(graph2, with_labels=True, node_size=1000, node_color='cyan')

                        plt.show()
                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Error!")
                        msg.setText(f"There doesn't exist a path from '{self.startTextbox.displayText()}' to one or more of the goal nodes")
                        msg.setIcon(QMessageBox.Warning)

                        x = msg.exec()
                        return

                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Error!")
                    msg.setText("Please enter a valid goal node/s!")
                    msg.setIcon(QMessageBox.Warning)

                    x = msg.exec()
                    return

    #Heuristic function
    def heuristicFunction(self, a, b):
        path = nx.shortest_path_length(self.ug, a, b)
        return path

    #A star search function
    def astarAlgo(self):
        if self.directedButton.isChecked():

            G = nx.DiGraph()
            if self.startTextbox.displayText() == "" and self.goalTextbox.displayText() == "":
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Please enter a start and goal nodes!")
                msg.setIcon(QMessageBox.Warning)

                x = msg.exec_()
                return

            elif self.startTextbox.displayText() == "":
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Please enter a starting node!")
                msg.setIcon(QMessageBox.Warning)

                x = msg.exec()
                return

            elif not self.checkNode(self.startTextbox.displayText()):
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Please enter a valid start node!")
                msg.setIcon(QMessageBox.Warning)

                x = msg.exec()
                return

            elif self.goalTextbox.displayText()=="":
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Please enter a valid goal node/s!")
                msg.setIcon(QMessageBox.Warning)

                x = msg.exec()
                return
            elif self.isDiGraphEmpty():
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("The directed graph has no edges!")
                msg.setIcon(QMessageBox.Warning)

                x = msg.exec_()
                return
            else:

                newList = self.goalTextbox.displayText()
                listOfInputs = newList.split()

                if self.checkList(listOfInputs):
                    oldGiven = self.goalTextbox.displayText()
                    given = oldGiven.split()
                    myFlag = False
                    for i in given:
                        if nx.has_path(self.g, self.startTextbox.displayText(), i):
                            myFlag = True
                            break
                    if myFlag:
                        listOfLengths = []
                        listOfPaths = []
                        for i in listOfInputs:
                            #A star bugs when the graph is directed, and since we'll show the final path only,
                            # we used dijkstra which shows the same final path
                            listOfLengths.append(nx.dijkstra_path_length(self.g, self.startTextbox.displayText(), i, weight='weight'))
                            listOfPaths.append(nx.dijkstra_path(self.g, self.startTextbox.displayText(), i,weight='weight'))

                        minimum = min(listOfLengths)
                        min_index = listOfLengths.index(minimum)
                        newList = listOfPaths[min_index]
                        counter = 0

                        for i in range(len(newList) - 1):
                            G.add_edge(f'{newList[counter]}', f'{newList[counter + 1]}')
                            counter += 1

                        pos3 = nx.spring_layout(G)
                        labels = nx.get_edge_attributes(G, 'weight')

                        nx.draw_networkx_edge_labels(G, pos3, edge_labels=labels)
                        nx.draw(G, pos3, with_labels=True, node_size=550, node_color='cyan')
                        nx.draw_networkx_edges(G, pos3, width=3, arrowsize=30)

                        plt.show()

                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Error!")
                        msg.setText(f"There doesn't exist a path from '{self.startTextbox.displayText()}' to one or more of the goal nodes")
                        msg.setIcon(QMessageBox.Warning)

                        x = msg.exec()
                        return

                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Error!")
                    msg.setText("Please enter valid goal node/s!")
                    msg.setIcon(QMessageBox.Warning)
                    x = msg.exec()
                    self.goalTextbox.setText("")
                    return

        else:
            G= nx.Graph()

            if self.startTextbox.displayText() == "" and self.goalTextbox.displayText() == "":
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Please enter a start and goal nodes!")
                msg.setIcon(QMessageBox.Warning)

                x = msg.exec_()
                return
            elif self.startTextbox.displayText() == "":
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Please enter a starting node!")
                msg.setIcon(QMessageBox.Warning)
                x = msg.exec()
                return

            elif not self.checkNodeun(self.startTextbox.displayText()):
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Please enter a valid start node!")
                msg.setIcon(QMessageBox.Warning)
                x = msg.exec()
                return

            elif self.goalTextbox.displayText()=="":
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Please enter a valid goal node/s!")
                msg.setIcon(QMessageBox.Warning)
                x = msg.exec()
                return

            elif self.isGraphEmpty():
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("The undirected graph has no edges!")
                msg.setIcon(QMessageBox.Warning)

                x = msg.exec_()
                return

            else:
                newList = self.goalTextbox.displayText()
                listOfInputs = newList.split()

                if self.checkListun(listOfInputs):
                    oldGiven = self.goalTextbox.displayText()
                    given = oldGiven.split()
                    myFlag = False
                    for i in given:
                        if nx.has_path(self.ug, self.startTextbox.displayText(), i):
                            myFlag = True
                            break
                    if myFlag:
                        listOfLengths = []
                        listOfPaths = []

                        for i in listOfInputs:
                            listOfLengths.append(nx.astar_path_length(self.ug, self.startTextbox.displayText(), i,heuristic=self.heuristicFunction, weight='weight'))
                            listOfPaths.append(nx.astar_path(self.ug, self.startTextbox.displayText(), i, heuristic=self.heuristicFunction,weight='weight'))

                        minimum = min(listOfLengths)
                        min_index = listOfLengths.index(minimum)
                        newList = listOfPaths[min_index]
                        counter = 0

                        for i in range(len(newList) - 1):
                            G.add_edge(f'{newList[counter]}', f'{newList[counter + 1]}')
                            counter += 1

                        pos3 = nx.spring_layout(G)

                        labels = nx.get_edge_attributes(G, 'weight')
                        nx.draw_networkx_edge_labels(G, pos3, edge_labels=labels)
                        nx.draw(G, pos3, with_labels=True, node_size=550, node_color='cyan')
                        nx.draw_networkx_edges(G, pos3, width=3, arrowsize=30)

                        plt.show()

                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Error!")
                        msg.setText(
                            f"There doesn't exist a path from '{self.startTextbox.displayText()}' to one or more of the goal nodes")
                        msg.setIcon(QMessageBox.Warning)

                        x = msg.exec()
                        return
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Error!")
                    msg.setText("Please enter valid goal node/s!")
                    msg.setIcon(QMessageBox.Warning)

                    x = msg.exec()
                    self.goalTextbox.setText("")
                    return

    #Uniform cost search function
    def algoUCS(self):

        if self.startTextbox.displayText() == "" and self.goalTextbox.displayText() == "":
            msg = QMessageBox()
            msg.setWindowTitle("Error!")
            msg.setText("Please enter a start and goal nodes!")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()
            return

        elif self.startTextbox.displayText() == "":
            msg = QMessageBox()
            msg.setWindowTitle("Error!")
            msg.setText("Please enter a starting node!")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec()
            return

        if self.directedButton.isChecked():
            G2 = nx.DiGraph()

            if not self.checkNode(self.startTextbox.displayText()):
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Please enter a valid start node!")
                msg.setIcon(QMessageBox.Warning)

                x = msg.exec()
                return

            elif self.goalTextbox.displayText()=="":
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Please enter a valid goal node/s!")
                msg.setIcon(QMessageBox.Warning)

                x = msg.exec()
                return

            elif self.isDiGraphEmpty():
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("The directed graph has no edges!")
                msg.setIcon(QMessageBox.Warning)

                x = msg.exec_()
                return

            else:
                myList = self.goalTextbox.displayText()
                listOfInputs = myList.split()

                if self.checkList(listOfInputs):
                    oldGiven = self.goalTextbox.displayText()
                    given = oldGiven.split()
                    myFlag = False
                    for i in given:
                        if nx.has_path(self.g, self.startTextbox.displayText(), i):
                            myFlag = True
                            break
                    if myFlag:

                        listOfLengths = []
                        listOfPaths = []

                        for i in listOfInputs:
                            listOfLengths.append(nx.astar_path_length(self.g, self.startTextbox.displayText(), i, heuristic=None,weight='weight'))
                            listOfPaths.append(nx.astar_path(self.g, self.startTextbox.displayText(), i, heuristic=None, weight='weight'))

                        minimum = min(listOfLengths)
                        min_index = listOfLengths.index(minimum)
                        newList = listOfPaths[min_index]

                        counter = 0
                        for i in range(len(newList) - 1):
                            G2.add_edge(f'{newList[counter]}', f'{newList[counter + 1]}')
                            counter += 1

                        pos2 = nx.spring_layout(G2)

                        labels = nx.get_edge_attributes(G2, 'weight')
                        nx.draw_networkx_edge_labels(G2, pos2, edge_labels=labels)
                        nx.draw(G2, pos2, with_labels=True, node_size=500, node_color='cyan')
                        nx.draw_networkx_edges(G2, pos2, width=3, arrowsize=30)

                        plt.show()

                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Error!")
                        msg.setText(f"There doesn't exist a path from '{self.startTextbox.displayText()}' to one or more of the goal nodes")
                        msg.setIcon(QMessageBox.Warning)

                        x = msg.exec()
                        return

                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Error!")
                    msg.setText("Please enter valid goal node/s!")
                    msg.setIcon(QMessageBox.Warning)
                    x = msg.exec()

                    self.goalTextbox.setText("")
                    return
        else:

            G2 = nx.Graph()
            if not self.checkNodeun(self.startTextbox.displayText()):
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Please enter a valid start node!")
                msg.setIcon(QMessageBox.Warning)

                x = msg.exec()
                return

            elif self.goalTextbox.displayText()=="":
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Please enter a valid goal node/s!")
                msg.setIcon(QMessageBox.Warning)

                x = msg.exec()
                return

            elif self.isGraphEmpty():
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("The undirected graph has no edges!")
                msg.setIcon(QMessageBox.Warning)

                x = msg.exec_()
                return

            else:
                myList = self.goalTextbox.displayText()
                listOfInputs = myList.split()

                if self.checkListun(listOfInputs):
                    listOfLengths = []
                    listOfPaths = []
                    oldGiven = self.goalTextbox.displayText()
                    given = oldGiven.split()
                    myFlag = False
                    for i in given:
                        if nx.has_path(self.ug, self.startTextbox.displayText(), i):
                            myFlag = True
                            break
                    if myFlag:
                        for i in listOfInputs:
                            listOfLengths.append(nx.astar_path_length(self.ug, self.startTextbox.displayText(), i, heuristic=None,weight='weight'))
                            listOfPaths.append(nx.astar_path(self.ug, self.startTextbox.displayText(), i, heuristic=None, weight='weight'))

                        minimum = min(listOfLengths)
                        min_index = listOfLengths.index(minimum)
                        newList = listOfPaths[min_index]

                        counter = 0
                        for i in range(len(newList) - 1):
                            G2.add_edge(f'{newList[counter]}', f'{newList[counter + 1]}')
                            counter += 1

                        pos2 = nx.spring_layout(G2)

                        labels = nx.get_edge_attributes(G2, 'weight')
                        nx.draw_networkx_edge_labels(G2, pos2, edge_labels=labels)
                        nx.draw(G2, pos2, with_labels=True, node_size=500, node_color='cyan')
                        nx.draw_networkx_edges(G2, pos2, width=3, arrowsize=30)

                        plt.show()

                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Error!")
                        msg.setText(
                            f"There doesn't exist a path from '{self.startTextbox.displayText()}' to one or more of the goal nodes")
                        msg.setIcon(QMessageBox.Warning)

                        x = msg.exec()
                        return
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Error!")
                    msg.setText("Please enter valid goal node/s!")
                    msg.setIcon(QMessageBox.Warning)

                    x = msg.exec()
                    self.goalTextbox.setText("")
                    return

    #Helper function to check if a node is in the directed graph
    def checkNode(self, node):
        x = list(self.g.nodes())
        for i in x:
            if node in x:
                return True
            else:
                return False

    #Helper function to check if a node is in the undirected graph
    def checkNodeun(self, node):
        x = list(self.ug.nodes())
        for i in x:
            if node in x:
                return True
            else:
                return False

    #Helper function to check if at least one element in the list exists in the directed graph
    def checkList(self,myList):
        flag = True
        for i in myList:
            if not self.checkNode(i):
                flag = False
                break
        return flag

    #Helper function to check if at least one element in the list exists in the undirected graph
    def checkListun(self,myList):
        flag = True
        for i in myList:
            if not self.checkNodeun(i):
                flag = False
                break
        return flag

    #Function to clear the graph
    def clearTree(self):
        if self.directedButton.isChecked():
            x = list(self.g.nodes())

            if not x:
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Your directed graph is already empty!")
                msg.setIcon(QMessageBox.Warning)

                x = msg.exec_()
                return

            else:
                msg = QMessageBox()
                msg.setWindowTitle("Success!")
                msg.setText("Directed graph has been cleared successfully!")
                msg.setIcon(QMessageBox.Information)

                x = msg.exec_()

                self.g.clear()
                self.nodesList.setText("Empty Graph!")
                self.nodesList.adjustSize()

                return
        else:
            x = list(self.ug.nodes())

            if not x:
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Your undirected graph is already empty!")
                msg.setIcon(QMessageBox.Warning)

                x = msg.exec_()
                return

            else:
                msg = QMessageBox()
                msg.setWindowTitle("Success!")
                msg.setText("Undirected graph has been cleared successfully!")
                msg.setIcon(QMessageBox.Information)

                x = msg.exec_()

                self.ug.clear()
                self.nodesList.setText("Empty Graph!")
                self.nodesList.adjustSize()

                return

    #Helper function to check if the undirected graph is empty
    def isGraphEmpty(self):
        if not self.ug.edges():
            return True
        else:
            return False

    #Helper function to check if the directed graph is empty
    def isDiGraphEmpty(self):
        if not self.g.edges():
            return True
        else:
            return False

    #A function that is called after most button pushes to clear the textboxes
    def clearBoxes(self):
        self.startTextbox.setText("")
        self.goalTextbox.setText("")
        self.fromTextbox.setText("")
        self.toTextbox.setText("")
        self.nodeNameText.setText("")
        self.weightTextbox.setText("")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Graph Traversal"))

        self.runButton.setText(_translate("MainWindow", "Show Graph"))
        self.clearTreeButton.setText(_translate("MainWindow", "Clear Graph"))

        self.addNodeButt.setText(_translate("MainWindow", "Add Node"))
        self.nodeNameLabel.setText(_translate("MainWindow", "Node Name"))

        self.addEdgeButt.setText(_translate("MainWindow", "Add Edge"))
        self.label_3.setText(_translate("MainWindow", "From"))
        self.label_4.setText(_translate("MainWindow", "To"))
        self.label_5.setText(_translate("MainWindow", "Weight (optional)"))

        self.removeNodeButton.setText(_translate("MainWindow", "Remove Node"))
        self.removeEdgeButton.setText(_translate("MainWindow", "Remove Edge"))

        self.itertaiveButton.setText(_translate("MainWindow", "ITD"))
        self.bfsButton.setText(_translate("MainWindow", "BFS"))
        self.astarButton.setText(_translate("MainWindow", "A*"))
        self.ucsButton.setText(_translate("MainWindow", "UCS"))

        self.startLabel.setText(_translate("MainWindow", "Start"))
        self.goalLabel.setText(_translate("MainWindow", "Goal"))

        self.label_6.setText(_translate("MainWindow", "Nodes List:"))
        self.nodesList.setText(_translate("MainWindow", "Empty List!"))

        self.directedButton.setText(_translate("MainWindow", "Directed"))
        self.undirectedButton.setText(_translate("MainWindow", "Undirected"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())