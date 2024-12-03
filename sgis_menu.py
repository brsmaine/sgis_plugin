# -------------------------------------------------------------
#    sgis_menu - QGIS plugins menu class
#
#    begin                : 17 January 2018
#    copyright            : (c) 2018 by AViTAS Concepts, LLC.
#    email                : tim.schmaltz@gmail.com
#
#   BRSGIS is proprietary software. You may not copy, sell,
#   redistribute and/or modify it without the express
#   written authorization of both AViTAS Concepts, LLC and
#   Boothbay Regional Surveyors, LLC.
# -------------------------------------------------------------
from builtins import object

from PyQt5.QtCore import *

from .sgis_dialogs import *


# ---------------------------------------------

class sgis_menu(object):
    def __init__(self, iface):
        self.iface = iface
        self.sgis_menu = None

    def sgis_add_submenu(self, submenu):
        if self.sgis_menu != None:
            self.sgis_menu.addMenu(submenu)
        else:
            self.iface.addPluginToMenu("&sgis", submenu.menuAction())

    def initGui(self):

        self.sToolBar = self.iface.mainWindow().findChild(QToolBar, u'surveyorGIS')
        if not self.sToolBar:
            self.sToolBar = self.iface.addToolBar(u'SGIS')
            self.sToolBar.setObjectName(u'SGIS')

        icon = QIcon(os.path.dirname(__file__) + "/icons/create.svg")
        self.prep_action = QAction(icon, "&Set formConfig", self.iface.mainWindow())
        self.prep_action.triggered.connect(self.setFormsConfig)
        self.prep_action.trigger()
      
        self.sgis_menu = QMenu(QCoreApplication.translate("sgis", "&surveyorGIS"))
        self.iface.mainWindow().menuBar().insertMenu(self.iface.firstRightStandardMenu().menuAction(), self.sgis_menu)

        icon = QIcon(os.path.dirname(__file__) + "/icons/create.svg")
        self.new_menu = QMenu(QCoreApplication.translate("sgis", "&New"))
        self.new_menu.setIcon(icon)
        self.sgis_add_submenu(self.new_menu)

        # JOBS Submenu
        icon = QIcon(os.path.dirname(__file__) + "/icons/create.svg")
        self.job_menu = QMenu(QCoreApplication.translate("&New", "&Job"))
        self.job_menu.setIcon(icon)
        self.new_menu.addMenu(self.job_menu)

        # PLANS Submenu
        icon = QIcon(os.path.dirname(__file__) + "/icons/create.svg")
        self.plan_menu = QMenu(QCoreApplication.translate("&New", "&Plan"))
        self.plan_menu.setIcon(icon)
        self.new_menu.addMenu(self.plan_menu)

        icon = QIcon(os.path.dirname(__file__) + "/icons/create.svg")
        self.newJob_action = QAction(icon, "&Parcel-based", self.iface.mainWindow())
        self.newJob_action.triggered.connect(self.newJob)
        self.job_menu.addAction(self.newJob_action)

        icon = QIcon(os.path.dirname(__file__) + "/icons/create.svg")
        self.newLPJob_action = QAction(icon, "&Line/Freehand-based", self.iface.mainWindow())
        self.newLPJob_action.triggered.connect(self.newLPJob)
        self.job_menu.addAction(self.newLPJob_action)

        # SUPPLEMENTALS Submenu
        icon = QIcon(os.path.dirname(__file__) + "/icons/create.svg")
        self.supp_menu = QMenu(QCoreApplication.translate("&New", "&Supplemental"))
        self.supp_menu.setIcon(icon)
        self.new_menu.addMenu(self.supp_menu)

        icon = QIcon(os.path.dirname(__file__) + "/icons/create.svg")
        self.newParcelSupp_action = QAction(icon, "&Parcel-based", self.iface.mainWindow())
        self.newParcelSupp_action.triggered.connect(self.setSuppTypeP)
        self.supp_menu.addAction(self.newParcelSupp_action)

        icon = QIcon(os.path.dirname(__file__) + "/icons/create.svg")
        self.newLPSupp_action = QAction(icon, "&Line/Freehand-based", self.iface.mainWindow())
        self.newLPSupp_action.triggered.connect(self.setSuppType)
        self.supp_menu.addAction(self.newLPSupp_action)

        icon = QIcon(os.path.dirname(__file__) + "/icons/create.svg")
        self.newPlan_action = QAction(icon, "&Parcel-based", self.iface.mainWindow())
        self.newPlan_action.triggered.connect(self.newPlan)
        self.plan_menu.addAction(self.newPlan_action)
        
        icon = QIcon(os.path.dirname(__file__) + "/icons/create.svg")
        self.newFreehandPlan_action = QAction(icon, "&Freehand", self.iface.mainWindow())
        self.newFreehandPlan_action.triggered.connect(self.newFreehandPlan)
        self.plan_menu.addAction(self.newFreehandPlan_action)

        # Output / PrintOuts Submenu
        icon = QIcon(os.path.dirname(__file__) + "/icons/print.svg")
        self.output_entry_menu = QMenu(QCoreApplication.translate("&New", "&Outputs / PrintOuts"))
        self.output_entry_menu.setIcon(icon)
        self.job_menu.addMenu(self.output_entry_menu)

        icon = QIcon(os.path.dirname(__file__) + "/icons/face.svg")
        self.printFolderLabel_action = QAction(icon, "Print &Folder Face Label", self.iface.mainWindow())
        self.printFolderLabel_action.triggered.connect(self.printFolderLabel)
        self.output_entry_menu.addAction(self.printFolderLabel_action)

        icon = QIcon(os.path.dirname(__file__) + "/icons/yellow.svg")
        self.printYellowSheet_action = QAction(icon, "Print &YellowSheet", self.iface.mainWindow())
        self.printYellowSheet_action.triggered.connect(self.printYellowSheet)
        self.output_entry_menu.addAction(self.printYellowSheet_action)

        icon = QIcon(os.path.dirname(__file__) + "/icons/label.svg")
        self.printFolderLabel2_action = QAction(icon, "Print Folder &Label", self.iface.mainWindow())
        self.printFolderLabel2_action.triggered.connect(self.printFolderLabel2)
        self.output_entry_menu.addAction(self.printFolderLabel2_action)

        icon = QIcon(os.path.dirname(__file__) + "/icons/maptable.svg")
        self.printMapTable_action = QAction(icon, "Print &MapTable", self.iface.mainWindow())
        self.printMapTable_action.triggered.connect(self.printMapTable)
        self.output_entry_menu.addAction(self.printMapTable_action)

        icon = QIcon(os.path.dirname(__file__) + "/icons/user.svg")
        self.printContacts_action = QAction(icon, "Print &Contacts", self.iface.mainWindow())
        self.printContacts_action.triggered.connect(self.printContacts)
        self.output_entry_menu.addAction(self.printContacts_action)

        icon = QIcon(os.path.dirname(__file__) + "/icons/mv.svg")
        self.printMapView_action = QAction(icon, "Print &MapView", self.iface.mainWindow())
        self.printMapView_action.triggered.connect(self.printMapView)
        self.output_entry_menu.addAction(self.printMapView_action)

        icon = QIcon(os.path.dirname(__file__) + "/icons/mv.svg")
        self.printSiteMap_action = QAction(icon, "Print &SiteMap", self.iface.mainWindow())
        self.printSiteMap_action.triggered.connect(self.printSiteMap)
        self.output_entry_menu.addAction(self.printSiteMap_action)

        icon = QIcon(os.path.dirname(__file__) + "/icons/yellow.svg")
        self.CADexportOrig_action = QAction(icon, "&Generate CAD Outputs", self.iface.mainWindow())
        self.CADexportOrig_action.triggered.connect(self.CADexportOrig)
        self.output_entry_menu.addAction(self.CADexportOrig_action)

        icon = QIcon(os.path.dirname(__file__) + "/icons/util.svg")
        self.potreeExport_action = QAction(icon, "&Generate Potree Webpage", self.iface.mainWindow())
        self.potreeExport_action.triggered.connect(self.potreeExport)
        self.output_entry_menu.addAction(self.potreeExport_action)

        icon = QIcon(os.path.dirname(__file__) + "/icons/face.svg")
        self.allOutputs_action = QAction(icon, "&NEW - Generate ALL Outputs", self.iface.mainWindow())
        self.allOutputs_action.triggered.connect(self.printAllOutputs)
        self.output_entry_menu.addAction(self.allOutputs_action)

        icon = QIcon(os.path.dirname(__file__) + "/icons/edit.svg")
        self.edit_menu = QMenu(QCoreApplication.translate("sgis", "&Edit"))
        self.edit_menu.setIcon(icon)
        self.sgis_add_submenu(self.edit_menu)

        icon = QIcon(os.path.dirname(__file__) + "/icons/edit.svg")
        self.delete_menu = QMenu(QCoreApplication.translate("sgis", "&Delete"))
        self.delete_menu.setIcon(icon)
        self.sgis_add_submenu(self.delete_menu)

        icon = QIcon(os.path.dirname(__file__) + "/icons/edit.svg")
        self.deleteFeature_action = QAction(icon, "&Delete Feature (Job/Plan/Supp)", self.iface.mainWindow())
        self.deleteFeature_action.triggered.connect(self.deleteFeature)
        self.delete_menu.addAction(self.deleteFeature_action)

        icon = QIcon(os.path.dirname(__file__) + "/icons/edit.svg")
        self.editJob_action = QAction(icon, "&Edit Job", self.iface.mainWindow())
        self.editJob_action.triggered.connect(self.editJob)
        self.edit_menu.addAction(self.editJob_action)

        icon = QIcon(os.path.dirname(__file__) + "/icons/edit.svg")
        self.editSupp_action = QAction(icon, "&Edit Supplemental", self.iface.mainWindow())
        self.editSupp_action.triggered.connect(self.editSupp)
        self.edit_menu.addAction(self.editSupp_action)

        icon = QIcon(os.path.dirname(__file__) + "/icons/edit.svg")
        self.editPlan_action = QAction(icon, "&Edit Plan", self.iface.mainWindow())
        self.editPlan_action.triggered.connect(self.editPlan)
        self.edit_menu.addAction(self.editPlan_action)

        icon = QIcon(os.path.dirname(__file__) + "/icons/search.svg")
        self.search_menu = QMenu(QCoreApplication.translate("sgis", "&Search"))
        self.search_menu.setIcon(icon)
        self.sgis_add_submenu(self.search_menu)

        # search menu
        icon = QIcon(os.path.dirname(__file__) + "/icons/search.svg")
        self.search_action = QAction(icon, "&Search by Value", self.iface.mainWindow())
        self.search_action.triggered.connect(self.search)
        self.search_menu.addAction(self.search_action)
        self.sToolBar.addAction(self.search_action)

        # Utilities Submenu
        icon = QIcon(os.path.dirname(__file__) + "/icons/util.svg")
        self.util_menu = QMenu(QCoreApplication.translate("sgis", "&Utilities"))
        self.util_menu.setIcon(icon)
        self.sgis_add_submenu(self.util_menu)

        icon = QIcon(os.path.dirname(__file__) + "/icons/util.svg")
        self.printEstimates_action = QAction(icon, "Print &Estimates List", self.iface.mainWindow())
        self.printEstimates_action.triggered.connect(self.printEstimates)
        self.util_menu.addAction(self.printEstimates_action)

        icon = QIcon(os.path.dirname(__file__) + "/icons/util.svg")
        self.moveJob_action = QAction(icon, "&MOVE Job", self.iface.mainWindow())
        self.moveJob_action.triggered.connect(self.moveJob)
        self.util_menu.addAction(self.moveJob_action)

        icon = QIcon(os.path.dirname(__file__) + "/icons/util.svg")
        self.movePlan_action = QAction(icon, "&MOVE Plan", self.iface.mainWindow())
        self.movePlan_action.triggered.connect(self.movePlan)
        self.util_menu.addAction(self.movePlan_action)

        icon = QIcon(os.path.dirname(__file__) + "/icons/util.svg")
        self.moveSupp_action = QAction(icon, "M&OVE Supplemental", self.iface.mainWindow())
        self.moveSupp_action.triggered.connect(self.moveSupp)
        self.util_menu.addAction(self.moveSupp_action)
        
        icon = QIcon(os.path.dirname(__file__) + "/icons/freehand.svg")
        self.export_action = QAction(icon, "&Freehand Select/map_bk_lots to Clipboard", self.iface.mainWindow())
        self.export_action.triggered.connect(self.bulkExport)
        self.util_menu.addAction(self.export_action)

        icon = QIcon(os.path.dirname(__file__) + "/icons/buffers.svg")
        self.abutters_action = QAction(icon, "&Generate Buffer/Abutters", self.iface.mainWindow())
        self.abutters_action.triggered.connect(self.abutters)
        self.util_menu.addAction(self.abutters_action)
        
        icon = QIcon(os.path.dirname(__file__) + "/icons/yellow.svg")
        self.CADexportNEW_action = QAction(icon, "&Generate CAD Outputs (NEW)", self.iface.mainWindow())
        self.CADexportNEW_action.triggered.connect(self.cadExportNEW)
        self.util_menu.addAction(self.CADexportNEW_action)

    def setFormsConfig(self):
        self.prep_dialog = sgis_prep(self.iface)
        self.prep_dialog.initGui()

    def unload(self):
        if self.sgis_menu != None:
            self.iface.mainWindow().menuBar().removeAction(self.sgis_menu.menuAction())
        else:
            self.iface.removePluginMenu("&sgis", self.animate_menu.menuAction())

    def newPlan(self):
        QgsMessageLog.logMessage('Launching new plan...', 'sGIS', level=Qgis.Info)
        self.newPlan_dialog = sgis_newPlan(self.iface)
        self.newPlan_dialog.initGui()

    def newFreehandPlan(self):
        QgsMessageLog.logMessage('Launching new freehand plan...', 'sGIS', level=Qgis.Info)
        self.newFreehandPlan_dialog = sgis_newFreehandPlan(self.iface)
        self.newFreehandPlan_dialog.initGui()

    def moveJob(self):
        QgsMessageLog.logMessage('Launching moveJob utility...', 'sGIS', level=Qgis.Info)
        self.moveJob_dialog = sgis_moveJob(self.iface)
        self.moveJob_dialog.initGui()

    def movePlan(self):
        QgsMessageLog.logMessage('Launching movePlan utility...', 'sGIS', level=Qgis.Info)
        self.movePlan_dialog = sgis_movePlan(self.iface)
        self.movePlan_dialog.initGui()

    def moveSupp(self):
        QgsMessageLog.logMessage('Launching moveSupplemental utility...', 'sGIS', level=Qgis.Info)
        self.moveSupp_dialog = sgis_moveSupp(self.iface)
        self.moveSupp_dialog.initGui()

    def newJob(self):
        self.newJob_dialog = sgis_newJob_ORIGINAL(self.iface)
        self.newJob_dialog.initGui()

    def newLPJob(self):
        sType = 'X'
        pType = 'LP'
        QgsMessageLog.logMessage('Launching new LP job...', 'sGIS', level=Qgis.Info)
        self.newLPJob_dialog = sgis_newLPJob(self.iface, sType, pType)
        self.newLPJob_dialog.initGui(sType, pType)

    def deleteFeature(self):
        self.deleteFeature_dialog = sgis_deleteFeature(self.iface)
        self.deleteFeature_dialog.initGui()

    def editJob(self):
        QgsMessageLog.logMessage('Editing Existing Job...', 'sGIS', level=Qgis.Info)
        self.editJob_dialog = sgis_editJob(self.iface)
        self.editJob_dialog.initGui()

    def editSupp(self):
        QgsMessageLog.logMessage('Editing Existing Supplemental...', 'sGIS', level=Qgis.Info)
        self.editSupp_dialog = sgis_editSupp(self.iface)
        self.editSupp_dialog.initGui()

    def editPlan(self):
        QgsMessageLog.logMessage('Editing Existing Plan...', 'sGIS', level=Qgis.Info)
        self.editPlan_dialog = sgis_editPlan(self.iface)
        self.editPlan_dialog.initGui()

    def search(self):
        QgsMessageLog.logMessage('Launching search...', 'sGIS', level=Qgis.Info)
        self.search_dialog = sgis_search(self.iface)
        self.search_dialog.run()

    def printFolderLabel(self):
        QgsMessageLog.logMessage('Generating Folder Face Label...', 'sGIS', level=Qgis.Info)
        self.printFolderLabel_dialog = sgis_printFolderLabel(self.iface)
        self.printFolderLabel_dialog.initGui()

    def printYellowSheet(self):
        QgsMessageLog.logMessage('Generating YellowSheet...', 'sGIS', level=Qgis.Info)
        self.printYellowSheet_dialog = sgis_printYellowSheet(self.iface)
        self.printYellowSheet_dialog.initGui()

    def printFolderLabel2(self):
        QgsMessageLog.logMessage('Generating Folder Label...', 'sGIS', level=Qgis.Info)
        self.label_dialog = sgis_label_dialog(self.iface)
        self.label_dialog.show()

    def printAllOutputs(self):
        QgsMessageLog.logMessage('ALL Outputs (Except Folder Label) will be generated...', 'sGIS', level=Qgis.Info)
        self.allOutputs_dialog = sgis_allOutputs(self.iface)
        self.allOutputs_dialog.run()
        
    def CADexportOrig(self):
        QgsMessageLog.logMessage('Launching (Orig) CAD Export Form...', 'sGIS', level=Qgis.Info)
        self.CADexportOrig_dialog = sgis_CADexportOrig_dialog(self.iface)
        self.CADexportOrig_dialog.show()

    def cadExportNEW(self):
        QgsMessageLog.logMessage('Launching (NEW) CAD Export Form...', 'sGIS', level=Qgis.Info)
        self.CADexportNEW_dialog = sgis_CADexportNEW_dialog(self.iface)
        self.CADexportNEW_dialog.show()

    def potreeExport(self):
        QgsMessageLog.logMessage('Launching Potree Export Form...', 'sGIS', level=Qgis.Info)
        self.potreeExport_dialog = sgis_potreeExport_dialog(self.iface)
        self.potreeExport_dialog.show()

    def setSuppType(self):
        QgsMessageLog.logMessage('Launching Supplmental Form...', 'sGIS', level=Qgis.Info)
        pType = 'LP'
        self.supp_dialog = sgis_supp_dialog(self.iface, pType)
        self.supp_dialog.show()

    def setSuppTypeP(self):
        QgsMessageLog.logMessage('Launching Supplmental Form...', 'sGIS', level=Qgis.Info)
        pType = 'P'
        self.supp_dialog = sgis_supp_dialog(self.iface, pType)
        self.supp_dialog.show()

    def printMapTable(self):
        QgsMessageLog.logMessage('Generating Map Table...', 'sGIS', level=Qgis.Info)
        self.mt_dialog = sgis_printMapTable(self.iface)
        self.mt_dialog.initGui()

    def printMapView(self):
        QgsMessageLog.logMessage('Generating Map View...', 'sGIS', level=Qgis.Info)
        self.mv_dialog = sgis_printMapView(self.iface)
        self.mv_dialog.initGui()

    def printEstimates(self):
        QgsMessageLog.logMessage('Generating Estimates...', 'sGIS', level=Qgis.Info)
        self.e_dialog = sgis_printEstimates(self.iface)
        self.e_dialog.initGui()

    def printContacts(self):
        QgsMessageLog.logMessage('Generating Contacts...', 'sGIS', level=Qgis.Info)
        self.c_dialog = sgis_printContacts(self.iface)
        self.c_dialog.initGui()

    def printSiteMap(self):
        QgsMessageLog.logMessage('Generating Site Map...', 'sGIS', level=Qgis.Info)
        self.mv_dialog = sgis_printSiteMap(self.iface)
        self.mv_dialog.initGui()

    def addNewParcel(self):
        QgsMessageLog.logMessage('Adding NEW parcel...', 'sGIS', level=Qgis.Info)
        self.parcel_dialog = sgis_parcel(self.iface)
        self.parcel_dialog.initGui()
        
    def abutters(self):
        # Must be saved in self, otherwise garbage collector destroys dialog
        QgsMessageLog.logMessage('Launching Abutters...', 'sGIS', level=Qgis.Info)
        self.abutters_dialog = sgis_abutters(self.iface)
        self.abutters_dialog.run()
    
    def bulkExport(self):
        QgsMessageLog.logMessage('Launching Export...', 'sGIS', level=Qgis.Info)
        self.export_dialog = sgis_bulkMapExport(self.iface)
        self.export_dialog.initGui()
