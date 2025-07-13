class MultipleFunctions():
    @staticmethod
    def triangle():
            Height = 32
            breadth = 34
            
            area = (Height * breadth) / 2
            Height1=2
            Height2=4
            Breadth=4
        
            perimeter = Height1 + Height2 + Breadth
            
            print(f"Height: {Height}")
            print(f"Breadth: {breadth}")
            print(f"Area formula: (Height*Breadth)/2")
            print(f"Area of Triangle: {area}")
            print(f"Height1: {Height1}")
            print(f"Height2: {Height2}")
            print(f"Breadth: {Breadth}")
            print("Perimeter formula: Height1+Height2+Breadth")
            print(f"Perimeter of Triangle: {perimeter}")

    @staticmethod
    def percentage():
        subjects = []
        for i in range(1, 6):
            mark = int(input(f"Subject{i}= "))
            subjects.append(mark)
        total = sum(subjects)
        percent = (total / 500) * 100
        print("Total : ", total)
        print("Percentage : ", percent)


    @staticmethod
    def Eligible(gender, age):
        if gender == "Male":
            if age >= 21:
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        elif gender == "Female":
            if age >= 18:
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
    print("Your Gender: Male")
    print("Your Age: 20")
    Eligible('Male', 20)


    @staticmethod
    def Subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")


    def OddEven():
        num = int(input('Enter a Number: '))
        if((num%2)==0):
            print(f'{num} is Even number')
        else:
            print(f'{num} is Odd number')