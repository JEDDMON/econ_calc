import math

# Helper to get input safely
def get_num(prompt):
    print(prompt)
    while True:
        try:
            val_str = input("") 
            return float(val_str)
        except ValueError:
            print("Number required")

def main():
    view = 0
    while True:
        if(view == 1):
            print("6. CC")
            print("7. F/P")
            print("8. P/F")
            print("9. P/A")
            print("10. A/P")
            print("22. Next")
        elif(view == 2):
            print("11. F/A")
            print("12. A/F")
            print("13. A/G L")
            print("14. P/G L")
            print("15. P/g G")
            print("22. Next")
        elif(view == 3):
            print("16. CR")
            print("17. AW")
            print("0. Exit")
            print("22. Next")
        else:
            print("1. F=P(1+ni)")
            print("2. I=Pni")
            print("3. Eff Rate i=r/m")
            print("4. Eff Annual i_a")
            print("5. Eff Int (Any)")
            print("22. Next")
        
        sel = input("Select: ")

        if sel == '0':
            break

        # 1. Simple Interest F
        elif sel == '1': 
            P = get_num("P")
            n = get_num("n")
            i = get_num("i")
            print("F = {:.4f}".format(P * (1 + n * i)))
            input("EXE...")

        # 2. Simple Interest I
        elif sel == '2':
            P = get_num("P")
            n = get_num("n")
            i = get_num("i")
            print("I = {:.4f}".format(P * n * i))
            input("EXE...")

        # 3. Effective Rate i=r/m
        elif sel == '3':
            r = get_num("r")
            m = get_num("m")
            print("i = {:.6f}".format(r / m))
            input("EXE...")

        # 4. Effective Annual i_a
        elif sel == '4':
            i = get_num("i")
            m = get_num("m")
            print("i_a = {:.6f}".format(((1 + i) ** m) - 1))
            input("EXE...")

        # 5. Effective Int (Any)
        elif sel == '5':
            r = get_num("r")
            m = get_num("m")
            print("i = {:.6f}".format(((1 + (r / m)) ** m) - 1))
            input("EXE...")

        # 6. Continuous Interest
        elif sel == '6':
            r = get_num("r")
            print("i = {:.6f}".format(math.exp(r) - 1))
            input("EXE...")

        # 7. F/P
        elif sel == '7':
            P = get_num("P")
            i = get_num("i")
            n = get_num("n")
            fp = ((1 + i) ** n)
            print("fp = {:.4f}".format(fp))
            print("F = {:.4f}".format(P * fp))
            input("EXE...")

        # 8. P/F
        elif sel == '8':
            F = get_num("F")
            i = get_num("i")
            n = get_num("n")
            pf = 1 / ((1 + i) ** n)
            print("pf = {:.4f}".format(pf))
            print("P = {:.4f}".format(F * pf))
            input("EXE...")

        # 9. P/A
        elif sel == '9':
            A = get_num("A")
            i = get_num("i")
            n = get_num("n")
            if i == 0:
                 print("i cannot be 0")
            else:
                top = ((1 + i) ** n) - 1
                bot = i * ((1 + i) ** n)
                pa = top / bot
                print("pa = {:.4f}".format(pa))
                print("P = {:.4f}".format(A * pa))
                input("EXE...")

        # 10. A/P
        elif sel == '10':
            P = get_num("P")
            i = get_num("i")
            n = get_num("n")
            if i == 0:
                 print("i cannot be 0")
            else:
                top = i * ((1 + i) ** n)
                bot = ((1 + i) ** n) - 1
                ap = (top / bot)
                print("ap = {:.4f}".format(ap))
                print("A = {:.4f}".format(P * ap))
                input("EXE...")

        # 11. F/A
        elif sel == '11':
            A = get_num("A")
            i = get_num("i")
            n = get_num("n")
            if i == 0:
                 print("i cannot be 0")
            else:
                val = (((1 + i) ** n) - 1) / i
                print("fa = {:.4f}".format(val))
                print("F = {:.4f}".format(A * val))
                input("EXE...")

        # 12. A/F
        elif sel == '12':
            F = get_num("F:")
            i = get_num("i")
            n = get_num("n")
            if i == 0:
                 print("i cannot be 0")
            else:
                val = i / (((1 + i) ** n) - 1)
                print("af = {:.4f}".format(val))
                print("A = {:.4f}".format(F * val))
                input("EXE...")

        # 13. A/G
        elif sel == '13':
            G = get_num("G:")
            i = get_num("i (Rate):")
            n = get_num("n (Periods):")
            if i == 0:
                 print("i cannot be 0")
            else:
                top = ((1 + i) ** n) - (i * n) - 1
                bot = (i * ((1 + i) ** n)) - i
                ag = (top / bot)
                print("ag = {:.4f}".format())
                print("A = {:.4f}".format(G * ag))
                input("EXE...")

        # 14. P/G
        elif sel == '14':
            G = get_num("G")
            i = get_num("i")
            n = get_num("n")
            if i == 0:
                 print("i cannot be 0")
            else:
                top = ((1 + i) ** n) - (i * n) - 1
                bot = (i ** 2) * ((1 + i) ** n)
                pg = (top / bot)
                print("pg = {:.4f}".format(pg))
                print("P = {:.4f}".format(G * pg))
                input("EXE...")

        # 15. Geometric P/g
        elif sel == '15':
            A1 = get_num("A1")
            g = get_num("g")
            i = get_num("i")
            n = get_num("n")
            if i == g:
                print("Error: i cannot equal g")
            else:
                top = 1 - ((1 + g) ** n) * ((1 + i) ** -n)
                bot = i - g
                pg = (top / bot)
                print("pg = {:.4f}".format())
                print("P = {:.4f}".format(A1 * pg))
                input("EXE...")

        # 16. CR Cost
        elif sel == '16':
            print("CR = -P(A/P) - S(A/F)")
            P = get_num("P")
            S = get_num("S")
            i = get_num("i")
            n = get_num("n")
            if i == 0:
                print("i cannot be 0")
            else:
                ap = (i * ((1 + i) ** n)) / (((1 + i) ** n) - 1)
                af = i / (((1 + i) ** n) - 1)
                print("A/P = {:.4f}".format(ap))
                print("A/F = {:.4f}".format(af))
                
                # Assumes P and S are entered as raw cash flows
                cr = (-P * ap) - (S * af)
                print("CR = {:.4f}".format(cr))
                input("EXE...")

        # 17. Annual Worth (AW)
        elif sel == '17':
            print("Inputs: + for in, - for out")
            print("AW=P(A/P)+F(A/F)+A")
            P = get_num("P")
            F = get_num("F")
            A = get_num("A")
            i = get_num("i")
            n = get_num("n")
            
            if i == 0:
                print("i cannot be 0")
            else:
                # Calculate A/P factor
                ap_factor = (i * ((1 + i) ** n)) / (((1 + i) ** n) - 1)
                print("A/P = {:.4f}".format(ap_factor))
                # Calculate A/F factor
                af_factor = i / (((1 + i) ** n) - 1)
                print("A/F = {:.4f}".format(af_factor))
                
                aw = (P * ap_factor) + (F * af_factor) + A
                print("AW = {:.4f}".format(aw))
                input("EXE...")
        
        #view options 1 - 5
        elif sel == '18':
            view = 0
        elif sel == '19':
            view = 1
        elif sel == '20':
            view = 2
        elif sel == '21':
            view = 3
        elif sel == '22':
            view += 1
            if view > 3:
                view = 0
        else:
            print("Invalid Selection")



main()