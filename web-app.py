import streamlit as st



# Define the URL of the backend chat API
backend_url = "http://127.0.0.1:8000"


st.markdown(
    """
    <style>
        .container{
            background: purple;
            color: white;
            padding: 10px, 25px;
            border-radius: 10px;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
            display: flex;
            align-items: center;
            justify-content: center;
        }
        h1{
            color: white;
        }
        
        @media (max-width: 768px) {
            
            .container{
            background: purple;
            color: white;
            padding: 10px, 10px;
            border-radius: 10px;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
            display: flex;
            align-items: center;
            justify-content: center;
        }
        h1{
            color: white;
        }
            
        }
    
    </style>
    
    """, 
    unsafe_allow_html=True
)


st.markdown("""
            <div class="container">
                <h1>Chat With Maxx</h1>
            </div>
        """, 
        unsafe_allow_html=True
    )


st.markdown("")

st.markdown("")

user_input = st.text_area(label="You:", value="", placeholder="Message", height=200)


if st.button("You Entered"):
    st.write(user_input)

