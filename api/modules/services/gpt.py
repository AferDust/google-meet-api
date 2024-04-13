import json

import requests


def get_structured_program_from_gpt_api(content):
    url = "https://us-central1-carbon-zone-417117.cloudfunctions.net/gpt-api"

    headers = {
        'Content-Type': 'application/json'
    }

    system_prompt = (
        "You are a knowledgeable assistant tasked with creating a JSON array of program details. "
        "Each element in the array represents a different program and includes 'name', 'description', and 'faqs'. "
        "For 'name', provide the title of the program. For 'description', give a brief explanation of what the program offers. "
        "you create based on what people might typically ask about such a program, with each 'faqs' entry containing 'question', 'answer', "
        "and optionally"
        "Your FAQs should be generated from your knowledge base and be relevant to the program details provided. "
        "Here is an example of how each program's JSON object should be structured in the array: \n"
        "{\n"
        "\"programs\": [\n"
        "    {\n"
        "        \"name\": \"Наименование Проаграммы\",\n"
        "        \"description\": \"Описание программы и ее целей.\",\n"
        "        \"faqs\": [\n"
        "            {\n"
        "                \"question\": \"Кто имеет право на участие в этой программе?\",\n"
        "                \"answer\": \"Программа предназначена для людей, которые...\",\n"
        "            },\n"
        "            {\n"
        "                \"question\": \"Как я могу подать заявку?\",\n"
        "                \"answer\": \"Заявки можно подать онлайн на сайте...\",\n"
        "            }\n"
        "            // More FAQ entries here\n"
        "        ]\n"
        "    }\n"
        "    // More program entries here\n"
        "]\n"
        "}\n\n"
        "Given this information, please generate a JSON array with program data and FAQs as described. And all "
    )

    # Now, you would send the system_prompt as the 'content' field of a message object to the GPT API.

    payload = {
        "content": {
            "system": system_prompt,
            "user": content
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()


def get_structured_cashbacks_from_gpt_api(content, categories):
    url = "https://us-central1-carbon-zone-417117.cloudfunctions.net/gpt-api"

    headers = {
        'Content-Type': 'application/json'
    }

    system_prompt = "Вы опытный помощник, которому поручено создать массив данных о кэшбэке в формате JSON.Каждый элемент массива представляет собой отдельный объект кэшбэка и включает в себя 'percent', 'expired_date' и 'category'. В качестве 'percent' укажите процент, который покупатель получает в виде процентов от суммы, потраченной на покупку. Для 'expired_date' как долго действителен кэшбэк — объект даты, если информация о дате отсутствует, установите null. Для 'category', дается кэшбэк если оплачивает товары в этой категорий, категорией может быть числовой идентификатор или строка. Если тема кэшбэка соответствует категории в этой массиве,  " + json.dumps(categories) + ", 'category' будет integer id категории, в этой массиве., если тема кэшбэка не применим в этих категориях — 'category' будет строка, вы используете свои знания и задаете имя для этой категории. Вот пример ответа {\"cashbacks\": [{\"expired_date\": \"2024-11-03\", \"percent\": 7.3, \"category\": 1},{ \"expired_date\": ноль \"percent\": 10, \"category\": \"электроника\"}]}"
    print(system_prompt)
    payload = {
        "content": {
            "system": system_prompt,
            "user": content
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()
