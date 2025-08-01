# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tuner_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

from .controller_parameters_widget import ControllerParametersWidget
from .plot_settings_widget import PlotSettingsWidget
from .system_values_widget import SystemValuesWidget

class Ui_TunerMainWindow(object):
    def setupUi(self, TunerMainWindow):
        if not TunerMainWindow.objectName():
            TunerMainWindow.setObjectName(u"TunerMainWindow")
        TunerMainWindow.resize(1073, 659)
        self.action_device_connection = QAction(TunerMainWindow)
        self.action_device_connection.setObjectName(u"action_device_connection")
        self.action_file_save_data = QAction(TunerMainWindow)
        self.action_file_save_data.setObjectName(u"action_file_save_data")
        self.action_device_information = QAction(TunerMainWindow)
        self.action_device_information.setObjectName(u"action_device_information")
        self.action_file_save_figure = QAction(TunerMainWindow)
        self.action_file_save_figure.setObjectName(u"action_file_save_figure")
        self.centralwidget = QWidget(TunerMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.parameters_widget = QWidget(self.centralwidget)
        self.parameters_widget.setObjectName(u"parameters_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.parameters_widget.sizePolicy().hasHeightForWidth())
        self.parameters_widget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.parameters_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.controller_parameters_groupbox = QGroupBox(self.parameters_widget)
        self.controller_parameters_groupbox.setObjectName(u"controller_parameters_groupbox")
        font = QFont()
        font.setBold(False)
        self.controller_parameters_groupbox.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.controller_parameters_groupbox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.controller_parameters_widget = ControllerParametersWidget(self.controller_parameters_groupbox)
        self.controller_parameters_widget.setObjectName(u"controller_parameters_widget")

        self.verticalLayout_2.addWidget(self.controller_parameters_widget)


        self.verticalLayout.addWidget(self.controller_parameters_groupbox)

        self.verticalSpacer_2 = QSpacerItem(10, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.system_values_groupbox = QGroupBox(self.parameters_widget)
        self.system_values_groupbox.setObjectName(u"system_values_groupbox")
        self.horizontalLayout_2 = QHBoxLayout(self.system_values_groupbox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.system_values_widget = SystemValuesWidget(self.system_values_groupbox)
        self.system_values_widget.setObjectName(u"system_values_widget")

        self.horizontalLayout_2.addWidget(self.system_values_widget)


        self.verticalLayout.addWidget(self.system_values_groupbox)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.plot_groupbox = QGroupBox(self.parameters_widget)
        self.plot_groupbox.setObjectName(u"plot_groupbox")
        self.horizontalLayout_3 = QHBoxLayout(self.plot_groupbox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.plot_settings_widget = PlotSettingsWidget(self.plot_groupbox)
        self.plot_settings_widget.setObjectName(u"plot_settings_widget")

        self.horizontalLayout_3.addWidget(self.plot_settings_widget)


        self.verticalLayout.addWidget(self.plot_groupbox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_4.addWidget(self.parameters_widget)

        self.plot_area_widget = QWidget(self.centralwidget)
        self.plot_area_widget.setObjectName(u"plot_area_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(15)
        sizePolicy1.setVerticalStretch(15)
        sizePolicy1.setHeightForWidth(self.plot_area_widget.sizePolicy().hasHeightForWidth())
        self.plot_area_widget.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.plot_area_widget)

        TunerMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TunerMainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1073, 19))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuDevice = QMenu(self.menubar)
        self.menuDevice.setObjectName(u"menuDevice")
        TunerMainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(TunerMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        TunerMainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDevice.menuAction())
        self.menuFile.addAction(self.action_file_save_data)
        self.menuFile.addAction(self.action_file_save_figure)
        self.menuDevice.addAction(self.action_device_connection)
        self.menuDevice.addAction(self.action_device_information)

        self.retranslateUi(TunerMainWindow)

        QMetaObject.connectSlotsByName(TunerMainWindow)
    # setupUi

    def retranslateUi(self, TunerMainWindow):
        TunerMainWindow.setWindowTitle(QCoreApplication.translate("TunerMainWindow", u"Pupae Thermal Device Tuner", None))
        self.action_device_connection.setText(QCoreApplication.translate("TunerMainWindow", u"Connection", None))
        self.action_file_save_data.setText(QCoreApplication.translate("TunerMainWindow", u"Save Data", None))
        self.action_device_information.setText(QCoreApplication.translate("TunerMainWindow", u"Information", None))
        self.action_file_save_figure.setText(QCoreApplication.translate("TunerMainWindow", u"Save Figure", None))
        self.controller_parameters_groupbox.setTitle(QCoreApplication.translate("TunerMainWindow", u"Controller Parameters", None))
        self.system_values_groupbox.setTitle(QCoreApplication.translate("TunerMainWindow", u"System Values", None))
        self.plot_groupbox.setTitle(QCoreApplication.translate("TunerMainWindow", u"Plot", None))
        self.menuFile.setTitle(QCoreApplication.translate("TunerMainWindow", u"File", None))
        self.menuDevice.setTitle(QCoreApplication.translate("TunerMainWindow", u"Device", None))
    # retranslateUi

