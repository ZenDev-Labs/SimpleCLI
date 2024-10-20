import ollama

def my_function(text_to_display):
    print('text from my_function :: {}'.format(text_to_display))


def ollama_module(text):
   ollama.chat(model=modelName, messages=[
  {
    'role': 'user',
    'content': text,
    
  },
]) 