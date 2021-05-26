import io
import xlsxwriter


def write_excel():
    excel_stream = './test.xlsx'
    workbook = xlsxwriter.Workbook(excel_stream)
    worksheet = workbook.add_worksheet("sheet1")
    for i in range(1048577):  # 最多可放数据
        worksheet.write(i, 0, i + 1)
    workbook.close()


if __name__ == '__main__':
    write_excel()
