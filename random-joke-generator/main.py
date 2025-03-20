
import streamlit as st
import requests
def get_random_joke():
    """ fatch a random joke from the API"""#-#-
    try:
        response =requests.get("https://official-joke-api.appspot.com/random_joke")

        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data ['setup']} \n\n {joke_data ['punchline']}"
        else:
            return "Something went wrong with the API request."
    except :
        return "why did programmer quit his jo ? \n because he didn't get array"
    
def main():
    st.title("Random Joke Generator")
    st.write("click the button below to generate a random joke")
    
    if st.button("Get Joke"):
        joke = get_random_joke()
        st.success(joke)
        
    st.divider()
    
    st.markdown(
    """
    <div style-'text-align:center'>
    <p> joke from official joke API</p>
    <P> build  by MEER MANAV <a href='https://github.com/Meermanav'> </a>
    </p>
    </div>
    """, 
    unsafe_allow_html=True,
    )   
    
if __name__ == "__main__":
    main()
            
        
         