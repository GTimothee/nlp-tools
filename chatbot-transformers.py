from transformers import pipeline
from transformers import AutoModelForCausalLM, AutoTokenizer

if __name__ == "__main__":
  model_name = "TheBloke/Mistral-7B-Instruct-v0.2-AWQ"
  model = AutoModelForCausalLM.from_pretrained(model_name, device_map="cuda:0")
  tokenizer = AutoTokenizer.from_pretrained(model_name)
  chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=100)
  chat_history = []
  while True:
    # user input
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    chat_history.append({"role": "user", "content": user_input})
  
    # llm response
    output = chatbot(chat_history)
    chat_history = output[0]['generated_text']
    print(f"Assistant: {chat_history[-1]['content']}")
