import streamlit as st
import functions

todos = functions.get_todos()

def add_todos():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My To-Do App")
st.subheader("This is my first Python web app.")
st.write("This app is was created to boost productivity.")


for index, todo in enumerate(todos[:]):
    key_checkbox = f"{index}_{todo}"
    checkbox = st.checkbox(label=todo, key=key_checkbox)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[key_checkbox]
        st.rerun()


st.text_input(label="Enter a todo", placeholder="Enter a new to-do...",
              on_change=add_todos, key="new_todo")
