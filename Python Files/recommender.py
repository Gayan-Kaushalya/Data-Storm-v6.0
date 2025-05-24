import streamlit as st
import pandas as pd


df = pd.read_csv("../agent_performance.csv") 

st.title("Intervention Recommendation Assistant")

agent_code = st.text_input("Enter Agent Code:")

if agent_code:
    agent_row = df[df['agent_code'] == agent_code]

    if not agent_row.empty:
        performance_level = agent_row.iloc[0]['performance'].strip().lower()

        st.success(f"Agent {agent_code} is a **{performance_level.capitalize()}** performing agent.")

        if performance_level == 'high':
            st.subheader("Intervention Strategies for High Performers")
            st.markdown("""
            - Celebrate performance through **incentives** and **leaderboard features**  
            - Pair them with **medium or new agents as mentors**
            """)
        elif performance_level == 'medium':
            st.subheader("Intervention Strategies for Medium Performers")
            st.markdown("""
            - Group sessions with **high performers to share techniques**  
            - Analyse if **lead quality** is affecting performance  
            - Run **short-term performance challenges** to boost motivation
            """)
        elif performance_level == 'low':
            st.subheader("Intervention Strategies for Low Performers")
            st.markdown("""
            - Provide **personalised help**  
            - Share **structured call scripts and pitch frameworks**  
            - **Review results monthly** and adjust interventions accordingly
            """)
        else:
            st.warning(f"Unknown performance level: {performance_level}")
    else:
        st.error(f"No agent found with code: {agent_code}")
