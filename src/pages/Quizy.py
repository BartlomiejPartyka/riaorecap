import streamlit as st


class Quizy:
    def __init__(self):
        self.page = None
    def print(self):
        st.title("Quizy")
        st.subheader("  ")

        pages_names = ['Część 1', 'Część 2']
        self.page = st.radio('Wybierz zakres materiału', pages_names, index=None)

        if self.page == 'Część 1':
            st.write("Pierwszaa")
        elif self.page == 'Część 2':
            st.write("drugaaa")

    def get_questions(self):
        pass




quizy = Quizy()
quizy.print()
