def main():
    due=50
    accepted_coins=[1,5,10,25]

    while due>0:
        print(f"Amount Due: {due}")
        coin=int(input("Inset coin:"))
        if coin in accepted_coins:
            due -= coin

    change = abs(due)
    print(f"Change Owed: {change}")

if __name__ == "__main__":
    main()
