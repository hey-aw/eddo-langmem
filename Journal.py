import streamlit as st
import pandas as pd

mock_student_data = {
    "student_id": "emily_123",
    "journal_summaries": [
        {
            "id": "thread_1",
            "date": "2024-04-07",
            "summary": "Today's video of the concrete beam was crazy! I never thought something so strong could bend. 🤔",
        },
        {
            "id": "thread_2",
            "date": "2024-04-05",
            "summary": "We learned about different types of forces.  I wonder if the kind of force matters for how things change shape...",
        },
        # ...more thread summaries
    ],
    "aha_moments": [
        {
            "event": "Realized even strong materials bend a little under force.",
            "timestamp": "2024-04-07T14:25:00",
            "tags": ["strength", "flexibility", "force"],
        },
        # ...more aha moments
    ],
}

st.set_page_config(page_title="Eddo Journal", page_icon="📔")
st.title("Student Learning Dashboard")
student_id = mock_student_data['student_id']

col1, col2 = st.columns(2) 

with col1:
    st.header("Journal Reflections")
    for thread in mock_student_data['journal_summaries']:
        st.subheader(thread['date']) 
        st.write(thread['summary'])  # Using an expander

with col2:
    st.header("Aha! Moments")
    aha_df = pd.DataFrame(mock_student_data['aha_moments'])  

    for index, row in aha_df.iterrows():
        st.write("💡 " + row["event"])
        if row['tags']:
            st.caption(', '.join(row['tags'])) 

