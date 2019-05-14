import xlrd

ExcelFileName= 'deptos.xlsx'
workbook = xlrd.open_workbook(ExcelFileName)
worksheet = workbook.sheet_by_name("Hoja1") # We need to read the data
#from the Excel sheet named "Sheet1"

num_rows = worksheet.nrows #Number of Rows
num_cols = worksheet.ncols #Number of Columns

first = True

html = """<table class="table table-striped">""" + "\n"
html += """<thead>""" + "\n"
html += """<tr>""" + "\n"

def is_float(input):
  try:
    num = float(input)
  except ValueError:
    return False
  return True

result_data =[]
for curr_row in range(0, num_rows, 1):
    row_data = []
    if first:
        first = False
        for curr_col in range(0, num_cols, 1):
            data = worksheet.cell_value(curr_row, curr_col)  # Read the data in the current cell
            html += """<th scope="col">""" + str(data) + "</th>\n"
        html += """</tr>""" + "\n"
        html += """</thead>""" + "\n"
        html += """<tbody>""" + "\n"
    else:
        html += """<tr>""" + "\n"
        for curr_col in range(0, num_cols, 1):
            data = worksheet.cell_value(curr_row, curr_col)  # Read the data in the current cell
            if curr_col != num_cols-1:
                if is_float(data):
                    data = int(data)
                html += """<td>""" + str(data) + "</td>\n"
            else:
                html += """<td><a href=" """+str(data)+""" "> """
                html +="""<div style="height:100%;width:100%">Ver Propiedad</div></a></td>"""

        html += """</tr>""" + "\n"

html += """</tbody>""" + "\n"
html += """</table>""" + "\n"

print(html)

