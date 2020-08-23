students = [
    {
        "name": "Jean-Luc Garza",
        "age": 24,
        "score": 80
    },
    {
        "name": "Teddy Munoz",
        "age": 79,
        "score": 93

    },
    {
        "name": "Georgia Ali",
        "age": 17,
        "score": 30
    },
    {
        "name": "Vicky Calhoun",
        "age": 8,
        "score": 69
    },
    {
        "name": "Awais Weaver",
        "age": 65,
        "score": 89
    },
    {
        "name": "Athena Kline",
        "age": 52,
        "score": 79
    },
    {
        "name": "Zacharia Whitaker",
        "age": 38,
        "score": 77
    },
        {
        "name": "Clarice Davenport",
        "age": 99,
        "score": 89
    },
    {
        "name": "Viktoria Flynn",
        "age": 84,
        "score": 68
    },
    {
        "name": "Ianis Crossley",
        "age": 20,
        "score": 89
    },
    {
        "name": "Johnnie Owens",
        "age": 74,
        "score": 68
    },
    {
        "name": "Emily-Rose Erickson",
        "age": 33,
        "score": 78
    },
    {
        "name": "Adeel Nieves",
        "age": 100,
        "score": 94
    },
    {
        "name": "Dustin Villegas",
        "age": 98,
        "score": 67
    },
    {
        "name": "Maxine Hughes",
        "age": 65,
        "score": 70
    },
    {
        "name": "Bilaal Harding",
        "age": 79,
        "score": 85
    },
    {
        "name": "Maddie Ventura",
        "age": 71,
        "score": 60
    },
    {
        "name": "Leroy Rees",
        "age": 44,
        "score": 70
    },
    {
        "name": "Wanda Frank",
        "age": 73,
        "score": 80
    },
    {
        "name": "Margaux Herbert",
        "age": 80,
        "score": 90
    },
    {
        "name": "Ali Rios",
        "age": 70,
        "score": 79
    },
    {
        "name": "Nigel Santiago",
        "age": 25,
        "score": 94
    },
    {
        "name": "Markus Greene",
        "age": 78,
        "score": 83
    },
    {
        "name": "Harlan Parrish",
        "age": 97,
        "score": 73
    },
    {
        "name": "Baran Davidson",
        "age": 43,
        "score": 92
    },
    {
        "name": "Seth Rodriguezh",
        "age": 67,
        "score": 30
    },
    {
        "name": "Diego Mayer",
        "age": 100,
        "score": 94
    },
]



class Hashtable:
    def __init__(self, class_size, array=None):
        self.class_size = class_size
        self.classes ={"A":[], "B":[],"C":[], "D":[]}


    def hash(self, score):
        if score >= 90:
            s_class = "A"
        elif 90 > score >= 80:
            s_class = "B"
        elif 80 > score >= 70:
            s_class = "C"
        elif 70 > score >= 60:
            s_class = "D"
        else:
            return None
        return s_class

    def insert(self, name, score):
        indx = self.hash(score)
        if indx:
            if len(self.classes[indx]) < self.class_size:
                self.classes[indx].append({"Name": name, "Score": score})
            else:
                print("Sorry class is full!")

    def print_table(self):
        print(self.classes)



class_size = int(input("What is the maximum number of students in class? "))

student_table = Hashtable(class_size)

for i in students:
    student_table.insert(i["name"], i["score"])

student_table.print_table()
