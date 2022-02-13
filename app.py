import streamlit as st
from gpt3_prompt import generate_prompt
from image_preproc import generate_card

st.set_page_config(
    page_title="Valentine's Message Generator",
    page_icon="🐾",
    layout="centered")

st.sidebar.image("logo.png", use_column_width=True)

api_key = st.sidebar.text_input("OpenAI API Key:", type="password")

st.sidebar.write("Made with ❤️ by [@Saboo_Shubham_](https://twitter.com/Saboo_Shubham_)")

st.sidebar.write("Powered by [OpenAI](https://openai.com/) & [Streamlit](https://streamlit.io/)")
if api_key:
            
        inp = st.selectbox('💕 Message for', ['Her 💃', 'Him 🕺'])
        
        if st.button('Spread the love ✨'):
            # Generate the caption
            caption = generate_prompt(inp, api_key)
            # Generate the card
            image = generate_card(caption)
            # Show the image    
            st.image(image)
else:
    st.error("🔑 API Key Not Found!")
    st.write("💡 No OpenAI API key? Get yours [here](https://openai.com/blog/api-no-waitlist/)")
