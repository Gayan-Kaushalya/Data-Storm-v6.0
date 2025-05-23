import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

train = pd.read_csv("train_storming_round.csv")  

train['year_month'] = pd.to_datetime(train['year_month'], format='%m/%d/%Y')
train.set_index('year_month', inplace=True)

st.title("Agent Performance Dashboard")

agent = st.text_input("Enter agent code:")

if agent:
    agent_data = train[train['agent_code'] == agent]

    if not agent_data.empty:
        plt.figure(figsize=(12, 6))
        plt.plot(agent_data.index, agent_data['new_policy_count'], marker='o')
        plt.title(f'New Policy Count Over Time for Agent {agent}')
        plt.xlabel('Month')
        plt.ylabel('New Policy Count')
        plt.xticks(rotation=45)
        plt.grid()
        plt.tight_layout()

        st.pyplot(plt)  
        plt.close()
    else:
        st.warning(f"No data found for agent code: {agent}")
