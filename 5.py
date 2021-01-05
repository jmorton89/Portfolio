# start with a list
places = {
  "Pennsylvania": 20,
  "Tennessee": 1,
  "Hawaii": 4,
  "Japan": 2,
}
#create the file name and title
from reportlab.platypus import SimpleDocTemplate
report = SimpleDocTemplate("path.pdf")
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
styles = getSampleStyleSheet()  
report_title = Paragraph("Places I Have Lived", styles["h1"])
# import list data and format
table_data = []
for k, v in places.items():
    table_data.append([k, v])
report_table = Table(data=table_data)
report.build([report_title, report_table])
from reportlab.lib import colors
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
# sort items and then export to chart
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
report_pie = Pie(width=3, height=3)
report_pie.data = []
report_pie.labels = []
for place in sorted(places):
    report_pie.data.append(places[place])
    report_pie.labels.append(place)
report_chart = Drawing()
report_chart.add(report_pie)
# build out the new pdf
report.build([report_title, report_table, report_chart])