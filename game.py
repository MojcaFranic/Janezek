print ("Uganka")
guess = 0
while guess != 1:
    g = raw_input("Janezek je imel 5 bonbonov. Poje 2. Koliko mu jih ostane?")
    guess = int(g)
    if guess == 1:
        print ("Tako je, ker so mu 2 ukradli mu ostane 1.")
    else:
        if guess > 3:
            print("Imel jih je 5, 2 je pojedel...")
        else:
            if guess > 1:
                print ("Ko ni bil pozoren so mu 2 ukradli.")
print ("Janezek is scared 4 life")





