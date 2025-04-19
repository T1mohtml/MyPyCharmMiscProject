pelmeni = input("Did you cook the pelmeni? ").strip().lower()  # Приведення до нижнього регістра
if pelmeni == "yes":
    print("OK")
    eat = input("Did you eat all of the pelmeni? ").strip().lower()
    if eat == "yes":
        print("Well, OK, then buy kebab for dinner")
    else:
        print("ok then fry em' for dinner")
else:
    print("Well, you should have cooked the pelmeni")