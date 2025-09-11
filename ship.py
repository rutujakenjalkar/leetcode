def ship(cap,no):

    round=0
    extra=1
    x=no//cap
    round=x
    if no%cap!=0:
        round+=1
    
    return round

print(ship(1,999))

        

    





    
    