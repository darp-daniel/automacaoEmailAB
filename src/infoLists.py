from pprint import pprint
import openpyxl

def extrair_clients(file_path, linhasPc, colunaInfo):
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active

    clientes = []

    max_linhas = ws.max_row
    blocos =   max_linhas // linhasPc

    for bloco in range(blocos):

        inicio = (bloco * linhasPc) + 1

        info_cliente = {}

        for info, (col, linha) in colunaInfo.items():
            cell = ws[f"{col}{inicio + linha - 1}"]
            info_cliente[info] = cell.value
        
        clientes.append(info_cliente)
    return clientes

if __name__ == "__main__":
    file_path = "/home/daniel/Desktop/WorkSpace/automacaoEmails/src/Atualização cadastral.xlsx"
    linhasPc = 12
    colunaInfo1 = {
        "nomeEmpresa": ("D", 1),
        "email": ("B", 8),
        "representante": ("C", 6),
        "cargo": ("J", 6)
    }
    colunaInfo2 = {
        "nomeEmpresa": ("P", 1),
        "email": ("N", 8),
        "representante": ("O", 6),
        "cargo": ("V", 6)
    }
    clients1 = extrair_clients(file_path, linhasPc, colunaInfo1)
    clients2 = extrair_clients(file_path, linhasPc, colunaInfo2)

    pprint(clients1)
    pprint(clients2)