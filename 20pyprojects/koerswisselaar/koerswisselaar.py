# de elke currency heeft zijn eigen value nodig
# multiply de currency met het aantal wat je wilt 

def main():
     print("Dit programma wisselt Dollars naar Pond")
     print()

     dollars = eval(input("Aantal dollars:  "))
    
     pond = wissel_ponds(dollars)

     print("Dat is {} Pond".format(pond))

     
     
wissel_ponds = lambda dollars: dollars * 0.81


main()