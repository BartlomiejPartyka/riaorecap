import streamlit as st


class Quizy:
    def __init__(self):
        self.page = None

    def print(self):
        st.title("Quizy")
        st.subheader("  ")

        pages_names = ['Część 1', 'Część 2']
        self.page = st.radio('Wybierz zakres materiału', pages_names, index=0)

        if self.page == 'Część 1':
            self.get_questions1()
        elif self.page == 'Część 2':
            st.write("drugaaa")

    def get_questions1(self):
        # funkcja łącząca z bazą w tym miejscu
        result = ((1, "radio", "Czy kotek ma cztery łapki?", 2, 1, "Prawda", "Fałsz"),
                  (2, "select", "Które zwierzę jest ssakiem?", 4, 2, "Wróbelek", "Kotek", "Żabcia", "Ślimaczek"),
                  (3, "check", "Które elementy posiada kotek?", 5, 124, "Uszka", "Pazurki", "Kopyta", "Ogonek",
                   "Skrzydła"),
                  (4, "radio", "Czy kotki lubią drapać?", 2, 1, "Bardzo", "Niezbyt"))

        for r in result:
            st.write(str(r[0]) + ". Pytanie:")
            cont = st.container(border=True)
            if r[1] == "radio":
                self.radio_add(r, cont)
            elif r[1] == "select":
                self.select_add(r, cont)
            elif r[1] == "check":
                self.check_add(r, cont)

    def radio_add(self, q_tuple, c):
        answers = list(x for x in range(int(q_tuple[3])))
        for a in answers:
            answers[a] = str(q_tuple[5 + a])
        r_question = c.radio(
            str(q_tuple[2]),
            answers, index=None)

    def select_add(self, q_tuple, c):
        answers = list(x for x in range(int(q_tuple[3])))
        for a in answers:
            answers[a] = str(q_tuple[5 + a])
        s_question = c.selectbox(
            str(q_tuple[2]),
            answers, index=None)

    def check_add(self, q_tuple, c):
        c.write(str(q_tuple[2]))
        answers = list(x for x in range(int(q_tuple[3])))
        for a in answers:
            answers[a] = str(q_tuple[5 + a])
        for x in range(int(q_tuple[3])):
            check = c.checkbox(answers[x])


quizy = Quizy()
quizy.print()
