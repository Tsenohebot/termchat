from openai import OpenAI
import subprocess
import os

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"]
)

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4",  # Use "gpt-3.5-turbo" for cheaper option
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content

if __name__ == "__main__":
       print(r"""\
                    ___           ___           ___           ___           ___           ___                   
      ___          /  /\         /  /\         /  /\         /  /\         /  /\         /  /\          ___     
     /__/\        /  /::\       /  /::\       /  /::|       /  /::\       /  /:/        /  /::\        /__/\    
     \  \:\      /  /:/\:\     /  /:/\:\     /  /:|:|      /  /:/\:\     /  /:/        /  /:/\:\       \  \:\   
      \__\:\    /  /::\ \:\   /  /::\ \:\   /  /:/|:|__   /  /:/  \:\   /  /::\ ___   /  /::\ \:\       \__\:\  
      /  /::\  /__/:/\:\ \:\ /__/:/\:\_\:\ /__/:/_|::::\ /__/:/ \  \:\ /__/:/\:\  /\ /__/:/\:\_\:\      /  /::\ 
     /  /:/\:\ \  \:\ \:\_\/ \__\/~|::\/:/ \__\/  /~~/:/ \  \:\  \__\/ \__\/  \:\/:/ \__\/  \:\/:/     /  /:/\:\
    /  /:/__\/  \  \:\ \:\      |  |:|::/        /  /:/   \  \:\            \__\::/       \__\::/     /  /:/__\/
   /__/:/        \  \:\_\/      |  |:|\/        /  /:/     \  \:\           /  /:/        /  /:/     /__/:/     
   \__\/          \  \:\        |__|:|~        /__/:/       \  \:\         /__/:/        /__/:/      \__\/   
                   \__\/         \__\|         \__\/         \__\/         \__\/         \__\/                 
                                                                                                    Main V1.0
                                                                                                                """)
    print("GPTTerm. Type 'exit' to quit. - (c) Nabeel Akhtar 2024")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting...Have a nice day!")
            break
        try:
            response = chat_with_gpt(user_input)
            print(f"GPTTerm: {response}")
            subprocess.run(['say', response])
        except Exception as e:
            print(f"Error: {e}")