import json

command = input('Digite o comando para a IA: ')
details = input('Digite os detalhes: ')
example = input('Digite algum exemplo: ')

prompt = {
    'command':command,
    'detail':details,
    'example':example
}

json_format = json.dumps(prompt, indent=4, ensure_ascii=False)

print('\nPrompt enviado:')
print(json_format)