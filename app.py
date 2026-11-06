import streamlit as st
from openai import OpenAI


# Initialize OpenAI client
client = OpenAI()

# ============================================
# PAGE CONFIGURATION
# ============================================

st.set_page_config(
    page_title="eCornell AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ============================================
# CORNELL HEADER
# ============================================

col1, col2 = st.columns([1, 4])
with col1:
    st.image(
        "cornell_seal.png",
        width=100,
    )
with col2:
    st.markdown(
        "<h3 style='color: #b31b1b; margin-bottom: 0;'>🤖 My First AI Chatbot</h3>",
        unsafe_allow_html=True,
    )
    st.caption("Powered by eCornell")

st.markdown("---")

# ============================================
# INITIALIZE MESSAGE HISTORY
# (You learned this pattern in the primer)
# ============================================

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! How can I help you today?"}
    ]

# ============================================
# DISPLAY CONVERSATION HISTORY
# (You learned this pattern in the primer)
# ============================================

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# ============================================
# CHAT INPUT & AI RESPONSE
# (This combines primer patterns with REAL AI from notebooks)
# ============================================

if prompt := st.chat_input("Type your message here..."):

    # Add user message to history and display it
    # (From the primer)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # ============================================
    # COMPLETE THIS API CALL
    # ============================================
    # This is the ONE NEW THING in this module

    # Call OpenAI API to get AI response
    response = client.chat.completions.create(
        model="gpt-4o",
        # BEGIN SOLUTION
         messages =st.session_state.messages
        # END SOLUTION
    )

    # Extract the AI's response text
    msg = response.choices[0].message.content

    # ============================================
    # SAVE AND DISPLAY AI RESPONSE
    # (From the primer)
    # ============================================

    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": msg})

    # Display assistant response
    st.chat_message("assistant").write(msg)

# ============================================
# FOOTER
# ============================================

st.markdown("---")

st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "© eCornell<br>"
    "For assistance, contact course staff"
    "</div>",
    unsafe_allow_html=True,
)
