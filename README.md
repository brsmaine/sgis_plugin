<hr><b>surveyorGIS (sGIS)<hr>
v3.40.1a <br>
2024.03.DEC</b><br><br>
sGIS is a set of Python plugins for manipulating vector map layers in Quantum GIS.  sGIS provides an alternative to the Processing toolbox, an intuitive user interface and customized capabilities tailored to the operations of professional Surveyors in the US State of Maine.<br>
Key Features:<br>
<ul>
  <li>QGIS Client Plugin</li>
  <li>PostgreSQL Database w/PostGIS extensions</li>
  <li>Parcel/Freehand/Line-based Job/Plan/Supplemental Management</li>
  <li>Job Document Generation</li>
  <li>CAD Output Generation</li>
  <li>Potree Webpage Generation</li>
</ul>
<br>
<img src="./images/sgisSnap.jpg">
updated to ensure compatibility with latest QGIS (v3.40.1)<br>
<hr>
latest updates:
<ul>
<li>sanitized* - all but two references to BRS/LA and all hardcoded paths/values removed</li>
<li>config.json - org specific configuration is now maintained in external file and read at plugin load/reload...</ul>
<b></b><a href=mailto:t.schmaltz@brsmaine.com>contact</a></b>
<hr>ALRRT/REMINDER: (sanitize before release)<br><br>

```python
# sgis_dialogs.7143 print("id BEFORE updating record: ")
# this will need to be updated when the db is sanitized
sql_select_query = """SELECT last_value from brs_jobs_id_seq"""
cursor.execute(sql_select_query)
```

```python
# sgis_dialogs.7265 print("id BEFORE updating record: ")
# this will need to be updated when the db is sanitized
sql_select_query = """SELECT last_value from brs_jobs_id_seq"""
cursor.execute(sql_select_query)
```
<hr>
