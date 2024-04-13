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


def get_structured_cashbacks_from_gpt_api(content):
    url = "https://us-central1-carbon-zone-417117.cloudfunctions.net/gpt-api"

    headers = {
        'Content-Type': 'application/json'
    }

    system_prompt = "You are a knowledgeable assistant tasked with creating a JSON array of cashback details. " \
                    "Each element in the array represents a different cashback object and includes 'percent', 'expired_date', and 'category'. " \
                    "For 'percent', provide the percent the buyer receives back interest on the amount spent on the purchase. " \
                    "For 'expired_date', how long is cashback valid - date object, if no information about date set null" \
                    "For 'category', which purchases are eligible for cashback, the category is can be number id or string. If cashback applies in this array category - 'category' will number of category id which applies" \
                    "[" \
                    "    {" \
                    "        \"id\": 1," \
                    "        \"name\": \"cinema\"" \
                    "    },{" \
                    "        \"id\": 2," \
                    "        \"name\": \"sport\"" \
                    "    }" \
                    "]" \
                    ", if cashback not applicable in this categories - 'category' will string, you use own knowledge and set the name for this category." \
                    "Here is an example of response\n" \
                    "{\n" \
                    "    \"cashbacks\": [\n" \
                    "        {\n" \
                    "        \"expired_date\": \"2024-11-03\",\n" \
                    "        \"percent\": 7.3\n," \
                    "        \"category\": 2\n" \
                    "        },\n" \
                    "        {\n" \
                    "            \"expired_date\": null,\n" \
                    "            \"percent\": 10,\n" \
                    "            \"category\": \"electronics\"\n" \
                    "        }\n" \
                    "    ]\n" \
                    "}\n"

    payload = {
        "content": {
            "system": system_prompt,
            "user": content
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()
