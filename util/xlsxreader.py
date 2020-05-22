import openpyxl as pyxl


class XlsxReader(object):
    """
    Classe responsavel pela leitura dos arquivos de entrada do excel.
    """
    @staticmethod
    def useSheet(xlsx_file):
        """
        Efetua a leitura de um arquivo xlsx cujo caminho e nome consta na variavel xlsx_file e retorna um dicionario equivalente.
        :param xlsx_file: Caminho e nome do arquivo de entrada
        :type xlsx_file: basestring
        :return: Dicionario equivalente ao arquivo xlsx
        :rtype: dict
        """
        workbook = pyxl.load_workbook(xlsx_file)
        sheets = {}
        for sheet in workbook.worksheets:
            sheets[sheet.title] = []
            for (key, row) in enumerate(sheet.iter_rows()):
                if key == 0:
                    header = [cell.value for cell in row]
                else:
                    row_dict = {}
                    row_values = [cell.value for cell in row]
                    for (index, value) in enumerate(row_values):
                        row_dict[str(header[index])] = value
                    sheets[sheet.title].append(row_dict)
        return sheets