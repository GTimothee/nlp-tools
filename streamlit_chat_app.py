import streamlit as st

if 'messages' not in st.session_state:
    st.session_state['messages'] = [{
        'role': 'assistant', 'content': "Do you have a question for me ?"
    }]


with st.container(height=500):

    for msg in st.session_state['messages']:

        with st.chat_message(msg['role']):
            st.write(msg['content'])

    prompt = st.chat_input("Ask a question")
    if prompt:
        print(f"prompt: {prompt}")
        st.session_state['messages'].append({
            'role': 'user', 'content': prompt
        })
        st.rerun()

    if st.session_state['messages'][-1]['role'] == 'user':
        st.session_state['messages'].append({
            'role': 'assistant', 'content': 'user said: ' + st.session_state['messages'][-1]['content']
        })
        st.rerun()
