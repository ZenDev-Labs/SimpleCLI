import ollama
import json
import sys


def my_function(text_to_display):
    print('text from my_function :: {}'.format(text_to_display))


def find_command(prompt):
    with open('commands_dataset.json', 'r') as f:
        commands_data = json.load(f)
    # Simple case-insensitive exact match
    for entry in commands_data:
        if entry['prompt'].lower() == prompt.lower():
            return entry['command']
    return "I'm sorry, I don't have a command for that prompt."

if __name__ == "__main__":
    user_prompt = ' '.join(sys.argv[1:])
    result = find_command(user_prompt)
    print(result)



def ollama_module(text):
   f = open("config.json", "r")
   config = json.load(f.read)
   model_name = config.service.model
   ollama.chat(model=model_name, messages=[
  {
    'role': 'user',
    'content': text,
    
  }],
  tools=[
      {
        'type': 'function',
        'function': {
          'name': 'find_command',
          'description': 'Search through all avalible project types',
          'parameters': {
            'type': 'object',
            'properties': {
              'prompt': {
                'type': 'string',
                'description': 'what app type you want to search for',
              }
            },
            'required': ['prompt'],
          },
        },
      },
    ],
) 