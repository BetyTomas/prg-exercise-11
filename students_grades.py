from sorting import random_numbers

class StudentsGrades:
    def __init__(self, seznam_znamek):
        self.seznam_znamek = seznam_znamek #vlevo pod jakym nazvem si to ulozim a vpravo vstup #

    def get_by_index(self, index):
        return self.seznam_znamek[index] #

    def count(self):
        return len(self.seznam_znamek)


    def get_grade(self, index):
        pocet_bodu = self.get_by_index(index)

        if pocet_bodu >= 90:
            return "A"
        elif pocet_bodu >= 80 and pocet_bodu < 90:
            return "B"
        elif pocet_bodu >= 70 and pocet_bodu < 80:
            return "C"
        elif pocet_bodu >= 60 and pocet_bodu < 70:
            return "D"
        elif pocet_bodu >= 50 and pocet_bodu < 60:
            return "E"
        else:
            return "F"

    def find(self, hledany_pocet_bodu):
        seznam = []

        for i in range(len(self.seznam_znamek)):
            if self.seznam_znamek[i] == hledany_pocet_bodu:
                seznam.append(i)

        return seznam

    def get_sorted(self):
        scores = list(self.seznam_znamek) #udelali jsme si kopii
        for i in range(len(scores)):
            for j in range(0, len(scores) -1):
                if scores[j] > scores[j + 1]:
                    scores[j], scores[j + 1] = scores[j + 1], scores[j]
        return scores

def main(): #main neni soucasti tridz, neni to metoda
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    pocet_studentu_psalo_test = results.count()
    print(pocet_studentu_psalo_test)

    for i in range(pocet_studentu_psalo_test):
        print(f"Student {i}: {results.get_by_index(i)} points – {results.get_grade(i)}")

    indexy_stovek = results.find(100)
    print(f"Studenti s plným počtem: {indexy_stovek}")

    print(f"Seřazené výsledky: {results.get_sorted()}")

    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(random_results.count())
    print(random_results.get_sorted())

if __name__ == "__main__":
    main()






    # musime vytvorit objekt
#print(results.seznam_znamek) # necham si vypsat znamky, UZ NEPSAT SELF
#print(results.get_by_index(2)) #vyuzije results jako self, pracuje s nim
#print(results.get_grade(2))
#print(results.find(100))  # [6]
#print(results.find(50))   # [4]
#print(results.find(77))   # []
#print(results.get_sorted())   # [38, 42, 50, 58, 67, 73, 85, 91, 100]


