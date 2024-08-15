import streamlit as st
import functionsforweb as func

todos = func.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    func.write_todos(todos)


st.title("My To-Do App")
st.subheader("This is my to-do app")
st.write("Increase your productivity! Make a list!")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        func.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new to-do",
              on_change=add_todo, key="new_todo")
