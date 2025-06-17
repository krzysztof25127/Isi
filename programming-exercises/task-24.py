# Napisać funkcję tworzącą plik pc.csv. Pierwszy wiersz ma zawierać nazwy kolumn: pc_name, ip. 
# Nazwy komputerów mają zaczynać się literą P oraz 4 oktetem adresu ip. 
# Adresy zaczynają się od 172.30.2.1 do 172.30.2.100. Plik csv ma być rozdzielany przecinkami.

import csv
def create_pc_csv(file_path):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(['pc_name', 'ip'])
        
        for i in range(1, 101):
            pc_name = f'P{i}'
            ip_address = f'172.30.2.{i}'
            writer.writerow([pc_name, ip_address])

if __name__ == "__main__":
    file_path = 'pc.csv'
    create_pc_csv(file_path)