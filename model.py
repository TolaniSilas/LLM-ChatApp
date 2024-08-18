# Import the necessary libraries.
import os 
from groq import Groq
from dotenv import load_dotenv

# Load the environment variables from the .env file.
load_dotenv()


# Create a ChatBot class.
class ChatBot():
    
    # Load the GROQ API KEY from the env file.
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
    
    client = Groq(api_key=GROQ_API_KEY)
    
    query:str
    # output:str = ""
    
    models = [
    # "llama-3.1-405b-reasoning",
    "llama-3.1-70b-versatile",
    "llama-3.1-8b-instant",
    "mixtral-8x7b-32768"
    ]
    
    output_type= ["Batch", "Stream"]
    toekn_class = {"short": 150, "Moderate": 700, "Long": 1536}
    
    system_prompt = """You are an intelligent generative chatbox designed to assist users by providing relevant and accurate responses to any queries. \
        As a knowledge-rich system, you have been trained on a vast dataset, equipping you with extensive knowledge across a wide range of topics. Your \
        responses are based on the latest information available, ensuring users receive up-to-date and pertinent answers. Your primary goal is to \
        understand user queries effectively and deliver insightful and helpful responses. Your name is Maxx."""
        
    
    def generate_batch_response(self, user_message, token, model=models[0], temperature=0):
        
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_message}
                ],
                temperature=temperature,
                response_format={"type": "text"},
                max_tokens=token,
                stream=False
            )  
            
            return response
            
        
        except Exception as e:
            return {"Error": str(e)}
        
        
    
    def generate_stream_response(self, user_message, token, model=models[0], temperature=0):
          
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_message}
                ],
                temperature=temperature,
                response_format={"type": "text"},
                max_tokens=token,
                stream=True 
            )  
               
            return response
         
             
        except Exception as e:
            return {"Error": str(e)}
        
    

if __name__ == "__main__":
    
    user_input = input("Message:\n")
     
    Chat_Bot = ChatBot()
    
    # print(Chat_Bot.generate_batch_response(user_input, temperature=0.7))
    
    
    # output = Chat_Bot.generate_stream_response(user_input, temperature=0.7)
    # print()
    # print("Chatbot: ", end="")
    # for chunk in output:
       
    #     print(chunk.choices[0].delta.content, end="")
        
    
    
    

    



 
