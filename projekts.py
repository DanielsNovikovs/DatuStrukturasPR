import csv
import os

PVN = 0.21
FAILS = 'preces (4).csv'

def paradit_preces():
    if not os.path.exists(FAILS):
        print("Nav pievienotu preču!")
        return
    
    with open(FAILS, mode='r', newline='', encoding='utf-8') as fails:
        lasitajs = csv.DictReader(fails, delimiter=';')
        print("\n{:20} {:>10} {:>10} {:>10}".format("Prece", "Cena bez PVN", "PVN", "Kopā"))
        print("-"*55)
        for rinda in lasitajs:
            print("{:20} {:>10}€ {:>10}€ {:>10}€".format(
                rinda['Prece'],
                rinda['Bez PVN'],
                rinda['PVN'],
                rinda['Kopa']  
            ))

def pievienot_preci(preces_nosaukums):
    try:
        cena = float(input(f"Ievadiet cenu EUR priekš '{preces_nosaukums}': "))
    except ValueError:
        print("Nepareiza cena! Lūdzu ievadiet skaitli.")
        return

    pvn_summa = round(cena * PVN, 2)
    kopa = round(cena + pvn_summa, 2)

    lauki = ['Prece', 'Bez PVN', 'PVN', 'Kopa']  
    fails_eksiste = os.path.exists(FAILS)

    with open(FAILS, mode='a', newline='', encoding='utf-8') as fails:
        rakstitajs = csv.DictWriter(fails, fieldnames=lauki, delimiter=';')
        
        if not fails_eksiste:
            rakstitajs.writeheader()
        
        rakstitajs.writerow({
            'Prece': preces_nosaukums,
            'Bez PVN': f"{cena:.2f}",
            'PVN': f"{pvn_summa:.2f}",
            'Kopa': f"{kopa:.2f}"  
        })
    
    print(f"Prece '{preces_nosaukums}' veiksmīgi pievienota!")

def dzest_preci(preces_nosaukums):
    if not os.path.exists(FAILS):
        print("Nav ko dzēst!")
        return

    preces = []
    atrasta = False

    with open(FAILS, mode='r', newline='', encoding='utf-8') as fails:
        lasitajs = csv.DictReader(fails, delimiter=';')
        for rinda in lasitajs:
            if rinda['Prece'].lower() == preces_nosaukums.lower():
                atrasta = True
            else:
                preces.append(rinda)

    if not atrasta:
        print(f"Prece '{preces_nosaukums}' nav atrasta!")
        return

    with open(FAILS, mode='w', newline='', encoding='utf-8') as fails:
        rakstitajs = csv.DictWriter(fails, fieldnames=lasitajs.fieldnames, delimiter=';')
        rakstitajs.writeheader()
        rakstitajs.writerows(preces)
    
    print(f"Prece '{preces_nosaukums}' veiksmīgi dzēsta!")

def main():
    print("PVN kalkulators - 21%")
    print("Pieejamās komandas:")
    print("  add <preces_nosaukums> - Pievienot preci")
    print("  delete <preces_nosaukums> - Dzēst preci")
    print("  list - Parādīt visus produktus")
    print("  exit - Iziet no programmas")

    while True:
        komanda = input("\nIevadiet komandu: ").strip().split()
        
        if not komanda:
            continue
        
        if komanda[0].lower() == 'exit':
            print("Bye Bye My Dear Friend ;(")
            break
        
        if komanda[0].lower() == 'list':
            paradit_preces()
        
        elif komanda[0].lower() == 'add' and len(komanda) > 1:
            preces_nosaukums = ' '.join(komanda[1:])
            pievienot_preci(preces_nosaukums)
        
        elif komanda[0].lower() == 'delete' and len(komanda) > 1:
            preces_nosaukums = ' '.join(komanda[1:])
            dzest_preci(preces_nosaukums)
        
        else:
            print("Nepareiza komanda! Mēģiniet vēlreiz.")

if __name__ == "__main__":
    main()