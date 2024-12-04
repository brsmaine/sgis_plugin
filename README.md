<hr><b>surveyorGIS (sGIS)<hr>
v3.40.1a <br>
2024.03.DEC</b><br><br>
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
