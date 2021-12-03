from main import disease


disease= input("Enter your disease: ")
low = disease.lower()
if "fever" in low :
    with open("fever.txt") as r:
        a = r.read()
        print(a)