import openai




openai.api_key= "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"

dialogue= []
while True:
    text= input()
    if text in ['','0']:
        break
    dialogue.append({"role": "user", "content": f"{text}"})
    response= openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= dialogue
    )
    
    try:
        print(response['choices'][0]['message']['content'])
    except Exception as e:
        print(e)
        print(response)
    print('\n\n\n')
