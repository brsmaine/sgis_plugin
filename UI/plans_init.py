from PyQt5.QtWidgets import QLineEdit, QToolButton, QStackedWidget, QPushButton, QDateTimeEdit, QComboBox
from qgis.core import *

# nameField = None
from qgis.utils import iface

myDialog = None
stackedWidget = None

def formOpen(dialog, layerid, featureid):

    if 1 == 1:

        global myDialog
        myDialog = dialog

        #dialog.parent().setFixedWidth(1080)
        #dialog.parent().setFixedHeight(950)
        dialog.parent().setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
            
        name = dialog.findChild(QLineEdit, "name")
        address = dialog.findChild(QLineEdit, "address")
        town = dialog.findChild(QLineEdit, "town")
        townP = dialog.findChild(QLineEdit, "town_parcels")
        cd_no = dialog.findChild(QLineEdit, "cd_no")
        job = dialog.findChild(QLineEdit, "job")
        initials = dialog.findChild(QLineEdit, "initials")
        map = dialog.findChild(QLineEdit, "map")
        lot = dialog.findChild(QLineEdit, "lot")
        surveyor = dialog.findChild(QLineEdit, "surveyor")
        notes = dialog.findChild(QLineEdit, "notes")

        rev_no = dialog.findChild(QLineEdit, "rev_no")
        planbook = dialog.findChild(QLineEdit, "planbook")
        planpage = dialog.findChild(QLineEdit, "planpage")
        size_no = dialog.findChild(QLineEdit, "size_no")

        plan_no = dialog.findChild(QLineEdit, "plan_no")
        plan_type = dialog.findChild(QComboBox, "plan_type")

        idValue = dialog.findChild(QLineEdit, "idValue")
        file_no = dialog.findChild(QLineEdit, "file_no")

        if name.text() == 'NULL':
            name.setText('')
        else:
            pass
        if address.text() == 'NULL':
            address.setText('')
        else:
            pass
        if town.text() == 'NULL':
            town.setText('')
        else:
            pass
        try:
            if townP.text() == 'NULL':
                townP.setText('')
        except Exception as e:
            pass
        else:
            pass
        try:
          if cd_no.text() == 'NULL':
              cd_no.setText('')
          else:
              pass
        except Exception as e:
            pass
        if job.text() == 'NULL':
            job.setText('')
        else:
            pass
    else:
        pass
