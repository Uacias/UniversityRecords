import sys

from src.database import Database
from src.student import Student


def main():
    db = Database("./database/database.json")
    db.load()

    while True:
        print("\n======== MENU ========")
        print("1. Show all the students")
        print("2. Add a new student")
        print("3. Search student by last name")
        print("4. Search student by PESEL")
        print("5. Sort students by last name")
        print("6. Sort students by PESEL")
        print("7. Remove student by index number")
        print("8. Edytuj dane studenta")
        print("0. Exit")
        choice = input("Wybierz opcję: ")

        if choice == "1":
            students = db.get_all_students()
            if students:
                print("\nLista wszystkich studentów:")
                for s in students:
                    print(
                        f"- {s.first_name} {s.last_name}, "
                        f"indeks: {s.index_number}, PESEL: {s.pesel}, "
                        f"płeć: {s.gender}, adres: {s.address}"
                    )
            else:
                print("\nBaza jest pusta.")

        elif choice == "2":
            first_name = input("Podaj imię: ")
            last_name = input("Podaj nazwisko: ")
            address = input("Podaj adres: ")
            index_number = input("Podaj numer indeksu: ")
            pesel = input("Podaj PESEL: ")
            gender = input("Podaj płeć (M/F): ")

            student = Student(
                first_name, last_name, address, index_number, pesel, gender
            )
            db.add_student(student)
            print("Dodano studenta.")

        elif choice == "3":
            ln = input("Podaj nazwisko: ")
            results = db.find_student_by_last_name(ln)
            if results:
                print(f"\nZnaleziono {len(results)} student(ów):")
                for s in results:
                    print(
                        f"- {s.first_name} {s.last_name}, "
                        f"indeks: {s.index_number}, PESEL: {s.pesel}"
                    )
            else:
                print("Brak studentów o takim nazwisku.")

        elif choice == "4":
            p = input("Podaj PESEL: ")
            found = db.find_student_by_pesel(p)
            if found:
                print(
                    f"Znaleziono studenta: {
                        found.first_name} {
                        found.last_name}, "
                    f"indeks: {
                        found.index_number}, płeć: {
                        found.gender}, adres: {
                        found.address}"
                )
            else:
                print("Brak studenta o podanym PESEL.")

        elif choice == "5":
            db.sort_students_by_last_name()
            print("Posortowano studentów rosnąco po nazwisku.")

        elif choice == "6":
            db.sort_students_by_pesel()
            print("Posortowano studentów rosnąco po PESEL.")

        elif choice == "7":
            index_number = input("Podaj numer indeksu studenta do usunięcia: ")
            db.remove_student(index_number)
            print("Operacja usuwania wykonana (jeśli istniał taki student).")

        elif choice == "8":
            index_number = input("Podaj numer indeksu studenta do aktualizacji: ")

            new_first_name = input("Nowe imię (pozostaw puste, aby nie zmieniać): ")
            new_last_name = input("Nowe nazwisko (pozostaw puste, aby nie zmieniać): ")
            new_address = input("Nowy adres (pozostaw puste, aby nie zmieniać): ")
            new_pesel = input("Nowy PESEL (pozostaw puste, aby nie zmieniać): ")
            new_gender = input("Nowa płeć (M/F) (pozostaw puste, aby nie zmieniać): ")

            success = db.update_student(
                index_number=index_number,
                new_first_name=new_first_name if new_first_name else None,
                new_last_name=new_last_name if new_last_name else None,
                new_address=new_address if new_address else None,
                new_pesel=new_pesel if new_pesel else None,
                new_gender=new_gender if new_gender else None,
            )

            if success:
                print("Dane studenta zostały zaktualizowane.")
            else:
                print("Nie znaleziono studenta o podanym numerze indeksu.")

        elif choice == "0":
            print("Zamykanie programu.")
            sys.exit(0)

        else:
            print("Niepoprawna opcja. Spróbuj ponownie.")


if __name__ == "__main__":
    main()
