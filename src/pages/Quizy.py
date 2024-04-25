import streamlit as st
from src import db


class Quizy:
    def __init__(self):
        self.page = None
        self.answers = None

    def print(self):
        st.title("Quizy")
        st.subheader("Wybierz zakres materiału:")

        pages_names = ['Część 1', 'Część 2']
        self.page = st.radio(
            label="Część 1. zawiera zakres materiału dr inż. Węsierskiej. Część 2. zawiera zakres dr inż. Polińskiego.",
            options=pages_names, index=0)

        if self.page == 'Część 1':
            self.get_questions(1)
        elif self.page == 'Część 2':
            self.get_questions(2)

    def get_questions(self, part):
        # funkcja łącząca z bazą w tym miejscu z argumentem = part
        if part == 1:
            result = ((1, "radio", "Czy kotek ma cztery łapki?", 2, 1, "Prawda", "Fałsz"),
                      (2, "select", "Które zwierzę jest ssakiem?", 4, 2, "Wróbelek", "Kotek", "Żabcia", "Ślimaczek"),
                      (3, "check", "Które elementy posiada kotek?", 5, 124, "Uszka", "Pazurki", "Kopyta", "Ogonek",
                       "Skrzydła"),
                      (4, "radio", "Czy kotki lubią drapać?", 2, 1, "Bardzo", "Niezbyt"))
        elif part == 2:
            result = ((1, "check", "Wybierz pory roku: ", 5, 1245, "Lato", "Wiosna", "Słońce", "Jesień", "Zima"),
                      (2, "check", "Które z elementów to zwierzęta?", 4, 234, "Fitoplankton", "Meduza", "Zebra",
                       "Koralowiec"),
                      (3, "check", "Które grzyby są jadalne?", 4, 134, "Enoki", "Muchomor", "Pieczarka", "Boczniak"))
        else:
            result = None

        length = len(result)
        self.answers = list(0 for x in range(int(len(result))))

        for index, r in enumerate(result):
            st.write(str(r[0]) + ". Pytanie:")
            cont = st.container(border=True)
            if r[1] == "radio":
                self.radio_add(r, cont, length)
            elif r[1] == "select":
                self.select_add(r, cont, length)
            elif r[1] == "check":
                self.check_add(r, cont, length)
        accept = st.button("Zatwierdź")
        if accept == True:
            self.show_results()



    def radio_add(self, q_tuple, c, l):
        options = list(x for x in range(int(q_tuple[3])))
        for o in options:
            options[o] = str(q_tuple[5 + o])
        r_question = c.radio(
            str(q_tuple[2]),
            options, index=None
        )
        for i in range(int(q_tuple[3])):
            if r_question == options[i]:
                self.answers[int(q_tuple[0])-1] = 1+i

        st.write(self.answers)

    def select_add(self, q_tuple, c, l):
        options = list(x for x in range(int(q_tuple[3])))
        for o in options:
            options[o] = str(q_tuple[5 + o])
        s_question = c.selectbox(
            str(q_tuple[2]),
            options, index=None, placeholder="Wybierz odpowiedź")

        for i in range(int(q_tuple[3])):
            if s_question == options[i]:
                self.answers[int(q_tuple[0])-1] = 1+i

        st.write(self.answers)

    def check_add(self, q_tuple, c, l):
        c_answers = list(x for x in range(int(q_tuple[3])))

        c.write(str(q_tuple[2])) #question
        options = list(x for x in range(int(q_tuple[3])))
        for o in options:
            options[o] = str(q_tuple[5 + o])
        for x in range(int(q_tuple[3])):
            check = c.checkbox(options[x])
            if check:
                c_answers[x] = "Checked"
            else:
                c_answers[x] = "N"

        compressed_answers = self.compress_check(c_answers)
        if compressed_answers > 0:
            self.answers[int(q_tuple[0]) - 1] = int(compressed_answers)
        else:
            self.answers[int(q_tuple[0]) - 1] = 0
        st.write(self.answers)


    def compress_check(self, ans):
        number = 0
        for index, a in enumerate(ans):
            if a == "Checked":
                number = number*10
                number += index+1
        return number

    def show_results(self):
        pass




quizy = Quizy()
quizy.print()
