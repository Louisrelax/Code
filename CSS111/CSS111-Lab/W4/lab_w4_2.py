money = int(input("net money="))
if 150000 >= money >= 0:
    print("Hurray,tax exempted")
else:
    if 300000 >= money > 150000:
        tax = (money-150000) * 0.05
    elif 500000 >= money > 300000:
        tax = (money-300000) * 0.10 + 150000*0.05
    elif 750000 >= money > 500000:
        tax = (money-500000) * 0.15 + (200000*0.10) + (150000*0.05)
    elif 1000000 >= money > 750000:
        tax = (money-750000) * 0.20 + (250000*0.15) + (200000*0.10) + (150000*0.05)
    elif 2000000 >= money > 1000000:
        tax = (money-1000000) * 0.25 + (250000*0.20) + (250000*0.15) + (200000*0.10) + (150000*0.05)
    elif 5000000 >= money > 2000000:
        tax = (money-2000000) * 0.30 + (1000000*0.25) + (250000*0.20) + (250000*0.15) + (200000*0.10) + (150000*0.05)
    else:
        tax = (money-5000000) * 0.35 + (3000000*0.30) + (1000000*0.25) + (250000*0.20) + (250000*0.15) + (200000*0.10) + (150000*0.05)
    print("pay tax=","{:,}".format(tax))