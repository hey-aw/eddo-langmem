with col1:
    st.header("Journal Reflections")
    recent_threads = fetch_journal_summaries(student_id) # Hypothetical function

    for thread in recent_threads:
        st.subheader(thread['date']) 
        st.write(thread['summary'])
        st.button("Continue", key=f"thread_{thread['id']}") # Unique key for each button
