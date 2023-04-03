
def is_schrikkel_jaar(jaar):
    
        if jaar % 4 == 0:
            if jaar % 100 ==0:
                if jaar % 400 == 0:
                    print("Schrikkeljaar")
                else:
                    print("Geen schrikkeljaar")
            else:
                print(f"Schrikkeljaar: {jaar} ")
        else:
            print("Geen schrikkeljaar")
        
        


is_schrikkel_jaar(2000)
