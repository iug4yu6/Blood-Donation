import pandas as pd

heading = """
╔═════════════════════════════════╗
║        BLOOD BANK SYSTEM        ║
╚═════════════════════════════════╝         ~ by Utkarsh Pandey
___________________________________
What's Your Choice ?
1. View Donors
2. Add Donor
3. Delete Donor
4. Check Stock
5. Issue Blood
6. To CSV
7. Open CSV
8. Exit
"""
print(heading)

donors = pd.DataFrame({"ID": [],
                       "Donor Name": [],
                       "Blood Group": [],
                       "Quantity(ML)": [],
                       "Contact": [],
                       "City": []})

stock = pd.DataFrame({"Blood Group": ["A+",
                                      "A-",
                                      "B+",
                                      "B-",
                                      "AB+",
                                      "AB-",
                                      "O+",
                                      "O-"],
                      "Quantity(ML)": [1000, 400, 8000, 200, 470, 660, 300, 220]})

issue = pd.DataFrame({"Blood Group": [],
                      "Quantity": [],
                      "Requester Name": []})


def view_donors():
    return donors


def add_donor(did, dname, dbg, Quantity, dcon, dcity):
    if len(str(dcon)) == 10:
        donors.loc[did] = [did, dname, dbg.upper(), Quantity, dcon, dcity]
    else:
        print("[*contact] length is invalid!")


def drop_donor(ID):
    donors.drop([ID], axis=0, inplace=True)


def stocks(bg):
    if not bg.isupper():
        bg = bg.upper()

    print(stock.loc[stock["Blood Group"] == bg, "Quantity(ML)"])


def issues(blood_group, quantity, requester):
    var = pd.Series(stock.loc[stock["Blood Group"] == blood_group, "Quantity(ML)"])
    if var.iloc[0] > quantity:
        stock.loc[stock["Blood Group"].str.lower() == blood_group.lower(), "Quantity(ML)"] -= quantity
        issue.loc[len(issue)] = [blood_group, quantity, requester]
    else:
        print("Insufficient Amount Captured!")

def to_csv(donorsP, stocksP, issuesP):
    donors.to_csv(donorsP, index=False)
    stock.to_csv(stocksP, index=False)
    issue.to_csv(issuesP, index=False)


def open_csv(donorO, stockO, insuueO):
    global donors, stock, issue
    donors = pd.read_csv(donorO)
    stock = pd.read_csv(stockO)
    issue = pd.read_csv(insuueO)


while True:
    choose = int(input("[?]> "))
    if choose == 1:
        print(view_donors())

    elif choose == 2:
        did = int(input("Donor ID: "))
        dname = input("Donor Name: ")
        dbg = input("Blood Group: ")
        Quantity = float(input("Quantity(ML): "))
        dcon = int(input("Contact: "))
        dcity = input("City: ")
        add_donor(did, dname, dbg, Quantity, dcon, dcity)
        stock.loc[stock["Blood Group"].str.lower() == dbg.lower(), "Quantity(ML)"] += Quantity
        print(f"{did} ID Donor Added Successfully !")

    elif choose == 3:
        ID = int(input('ID: '))
        drop_donor(ID)
        print(f"{ID} ID Donor deleted successfully !")

    elif choose == 4:
        bg = input("Blood Group: ")
        stocks(bg)

    elif choose == 5:
        bgs = input("Blood Group: ")
        qt = int(input("Quantity(ML): "))
        name = input("Requester Name: ")
        issues(bgs, qt, name)
        print(f"Requester {name} has been provided with {qt} mL of {bgs} blood.")

    elif choose == 6:
        ddd = input("[Save] Path for Donor: ")
        sss = input("[Save] Path for Stock: ")
        iii = input("[Save] Path for Issue: ")
        to_csv(ddd, sss, iii)

    elif choose == 7:
        ddd0 = input("[Open] Path for Donor: ")
        sss0 = input("[Open] Path for Stock: ")
        iii0 = input("[Open] Path for Issue: ")
        open_csv(ddd0, sss0, iii0)

    elif choose == 8:
        print("Thank You...")
        exit()
    else:
        print("Invalid Command\nTry Again!")