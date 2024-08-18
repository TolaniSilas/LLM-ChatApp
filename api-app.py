# Import the necessary libraries.
import os, time, traceback
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import PlainTextResponse, StreamingResponse 
from model import ChatBot



# Instantiate the FastAPI Class.
app = FastAPI()

# Instantiate the ChatBot Class.
chatbot = ChatBot()

# Load the GROQ API KEY from the env file.
# GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# client = Groq(api_key=GROQ_API_KEY)


@app.get("/health")
async def health():
    return {
        "application": "LLM Application",
        "message": "Running Successfully"
    }


@app.post("/chat_stream")
async def chat_stream(request: Request):
    
    try: 
        # Get all the user queries.
        user_query = await request.json()
        
        # Get the user message.
        user_message = user_query["message"]
        if not user_message:
            raise HTTPException(status_code=400, detail="Message field cannot be empty!")
        
        try: 
            # Get the user's temperature configuration. 
            temperature = float(user_query["temperature"])
            
        except:
            return {
                "Error": "Invalid temperature input, pass a number between 0 and 2."
            }
            
        try: 
            selected_max_token = int(user_query["max_tokens"])
        
        except Exception as e:
            print("Error with selecting maximum number of tokens:\n", str(e)) 
            

        try:
            # Get the user's selected model.
            selected_model = user_query["model"]
    
            if selected_model not in chatbot.models:
                return {
                    "Error": "You did not pass a correct model code!/ model not available!"
                    }
            
            else: 
                model = selected_model
            
        except Exception as e:
            print("Invalid model input", e)
            
            
        # Generate a response.
        response = chatbot.generate_stream_response(user_message=user_message, model=model, token=selected_max_token, temperature=temperature)
        
        # Stream the Response.
        def stream_response():
            output = ""
            for chunk in response:
                token = chunk.choices[0].delta.content
                if token:
                    output += token
                    yield f"""{token}"""
                    # Add a delay between chunks to reduce stream speed.
                    time.sleep(0.05)
                               
        return StreamingResponse(stream_response(), media_type="text/plain", status_code=200)
                            
    except Exception as e:
        return {
            "Error": str(e)
        }
        
            

@app.post("/chat_batch")
async def chat_batch(request: Request):
    
    try:
        # Get all the user queries.
        user_query = await request.json()
        
        # Get the user message.
        user_message = user_query["message"]
        if not user_message:
            raise HTTPException(status_code=400, detail="Message field cannot be empty!")
        
        try: 
            # Get the user's temperature configuration. 
            temperature = float(user_query["temperature"])
            
        except:
            return {
                "Error": "Invalid temperature input, pass a number between 0 and 2."
            }
            
        try: 
            selected_max_token = int(user_query["max_tokens"])
        
        except Exception as e:
            print("Error with selecting maximum number of tokens:\n", str(e)) 
            

        try:
            # Get the user's selected model.
            selected_model = user_query["model"]
    
            if selected_model not in chatbot.models:
                return {
                    "Error": "You did not pass a correct model code!/ model not available!"
                    }
            
            else: 
                model = selected_model
            
        except Exception as e:
            print("Invalid model input", e)
            
            
        # Generate a response.
        response = chatbot.generate_batch_response(user_message=user_message, model=model, token=selected_max_token, temperature=temperature)
            
        # Get the model batch output.
        output = response.choices[0].message.content
            
        return PlainTextResponse(content=output, status_code=200)

    except Exception as e:
        return {
            "Error": str(e)
        }
        
    
    
if __name__ == "__main__":
    
    # Import the Uvicorn module for Asynchronous running.
    import uvicorn
    
    print("Starting the ChatBot Api Endpoint...")
    
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)