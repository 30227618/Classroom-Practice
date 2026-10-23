def display_all_accounts(**accounts):
    for key, value in accounts.items():
        print(key,":", value)

def main():
    display_all_accounts(uid1="alice", uid2="bob", uid3="Charlie")

if __name__ == "__main__":
    main()