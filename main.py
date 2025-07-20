import src.infoLists as infoLists
import src.mandandoEmails as mandandoEmails

if __name__ == "__main__":
    file_path = "src/Atualização cadastral.xlsx"
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
    clients1 = infoLists.extrair_clients(file_path, linhasPc, colunaInfo1)
    clients2 = infoLists.extrair_clients(file_path, linhasPc, colunaInfo2)
    clientes = clients1 + clients2
    infoLists.criar_db(clientes)
    mandandoEmails.rodar_envios()