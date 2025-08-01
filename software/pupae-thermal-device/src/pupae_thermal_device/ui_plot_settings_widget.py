# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plot_settings_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_PlotSettingsWidget(object):
    def setupUi(self, PlotSettingsWidget):
        if not PlotSettingsWidget.objectName():
            PlotSettingsWidget.setObjectName(u"PlotSettingsWidget")
        PlotSettingsWidget.resize(227, 98)
        self.horizontalLayout = QHBoxLayout(PlotSettingsWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(15)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.plot_reset_pushbutton = QPushButton(PlotSettingsWidget)
        self.plot_reset_pushbutton.setObjectName(u"plot_reset_pushbutton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_reset_pushbutton.sizePolicy().hasHeightForWidth())
        self.plot_reset_pushbutton.setSizePolicy(sizePolicy)
        self.plot_reset_pushbutton.setMinimumSize(QSize(100, 0))

        self.gridLayout_3.addWidget(self.plot_reset_pushbutton, 1, 1, 1, 1)

        self.plot_window_dblspinbox = QDoubleSpinBox(PlotSettingsWidget)
        self.plot_window_dblspinbox.setObjectName(u"plot_window_dblspinbox")
        sizePolicy.setHeightForWidth(self.plot_window_dblspinbox.sizePolicy().hasHeightForWidth())
        self.plot_window_dblspinbox.setSizePolicy(sizePolicy)
        self.plot_window_dblspinbox.setMinimumSize(QSize(100, 0))
        self.plot_window_dblspinbox.setMinimum(10.000000000000000)
        self.plot_window_dblspinbox.setMaximum(1000000.000000000000000)
        self.plot_window_dblspinbox.setSingleStep(10.000000000000000)
        self.plot_window_dblspinbox.setValue(180.000000000000000)

        self.gridLayout_3.addWidget(self.plot_window_dblspinbox, 0, 1, 1, 1)

        self.plot_window_units_label = QLabel(PlotSettingsWidget)
        self.plot_window_units_label.setObjectName(u"plot_window_units_label")

        self.gridLayout_3.addWidget(self.plot_window_units_label, 0, 2, 1, 1)

        self.plot_window_name_label = QLabel(PlotSettingsWidget)
        self.plot_window_name_label.setObjectName(u"plot_window_name_label")

        self.gridLayout_3.addWidget(self.plot_window_name_label, 0, 0, 1, 1)

        self.plot_reset_name_label = QLabel(PlotSettingsWidget)
        self.plot_reset_name_label.setObjectName(u"plot_reset_name_label")

        self.gridLayout_3.addWidget(self.plot_reset_name_label, 1, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_3)

        self.horizontalSpacer = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.retranslateUi(PlotSettingsWidget)

        QMetaObject.connectSlotsByName(PlotSettingsWidget)
    # setupUi

    def retranslateUi(self, PlotSettingsWidget):
        PlotSettingsWidget.setWindowTitle(QCoreApplication.translate("PlotSettingsWidget", u"Form", None))
        self.plot_reset_pushbutton.setText(QCoreApplication.translate("PlotSettingsWidget", u"Reset", None))
        self.plot_window_units_label.setText(QCoreApplication.translate("PlotSettingsWidget", u"s", None))
        self.plot_window_name_label.setText(QCoreApplication.translate("PlotSettingsWidget", u"Window ", None))
        self.plot_reset_name_label.setText(QCoreApplication.translate("PlotSettingsWidget", u"Plot", None))
    # retranslateUi

