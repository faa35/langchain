link: https://github.com/bhancockio/langchain-crash-course

***python version***

![Screenshot 2024-12-25 151555](https://github.com/user-attachments/assets/d0efcdd0-9410-43d2-bd6d-4bcab1d228ee)


```powershell
C:\Users\User\AppData\Local\Programs\Python\Python312\Scripts\
```

```powershell
C:\Users\User\AppData\Local\Programs\Python\Python312\
```

cloned with github desktop

**LangChain Crash Course**

Welcome to the LangChain Crash Course repository! This repo contains all the code examples you'll need to follow along with the LangChain Master Class for Beginners video. By the end of this course, you'll know how to use LangChain to create your own AI agents, build RAG chatbots, and automate tasks with AI.

**Course Outline**

1. **Setup Environment**
2. **Chat Models**
3. **Prompt Templates**
4. **Chains**
5. **RAG (Retrieval-Augmented Generation)**
6. **Agents & Tools**

**Getting Started**

**Prerequisites**

- Python 3.10 or 3.11
- watch **pyproject.toml** to see all the dependencies
- Poetry (Follow this [Poetry installation tutorial](https://python-poetry.org/docs/#installation) to install Poetry on your system)(dependency management tool for python)
- install poetry(with pipx)
1. first install pipx

```powershell
# If you installed python using Microsoft Store, replace `py` with `python3` in the next line.
py -m pip install --user pipx
```

1. 


![Screenshot 2024-12-25 154539](https://github.com/user-attachments/assets/4aa52962-d819-41be-b5e2-76d574746baa)

1. This command ensures that the `pipx` executable and other scripts are added to your system's PATH. Without it, the `pipx` command won't be recognized.

```powershell
python -m pipx ensurepath
```

1. Close the current terminal(also the VS Code and open a new one and run: ) 

```powershell
pipx --version
```

NOW LETS INSTALL POETRY

```powershell
pipx install poetry
```

Run the following command to confirm that `poetry` is installed and accessible:

```powershell
poetry --version

```

- NOw run

```powershell
poetry
```

**Installation**

1. ~~Clone the repository:~~ (already did that)
    
    ```
    ~~<!-- TODO: UPDATE TO MY  -->
    git clone https://github.com/bhancockio/langchain-crash-course
    cd langchain-crash-course~~
    ```
    
2. Install dependencies using Poetry:
    
    ```
    poetry install --no-root
    ```
    

**PROBLEM**

```powershell
Installing google-crc32c (1.5.0): Failed
```

1. Set up your environment variables:
    - Rename the `.env.example` file to `.env` and update the variables inside with your own values. Example:
    
    ```
    mv .env.example .env
    ```
    
2. Activate the Poetry shell to run the examples:
    
    ```
    poetry shell
    ```
    
3. Run the code examples:
    
    ```
     python 1_chat_models/1_chat_model_basic.py
    ```
    
4. ModuleNotFoundError: No module named 'dotenv’

```powershell
pip install python-dotenv

```

1. try to ru it again and find *ModuleNotFoundError: No module named 'langchain_openai’* **PROBLEM**

```powershell
pip install langchain
```





 

**We are gonna do it with env and GoggleGenAI instead of Chatgpt**

Before using env, we are gonna read the https://python.langchain.com/v0.2/docs/integrations/chat/ to know about the ChatGoogleGenerativeAI. We are gonna click on that and gonna know about the installation and the setups

```
pip install langchain langchain-google-genai python-dotenv
```
here we are just installing google gen ai and dotenv as its required for .\1_chat_models\1_chat_model_basic.py 



```powershell
PS D:\Fall 24\lang chain crash course\langchain-crash-course> python -v venv venvshawon

```


![Screenshot 2024-12-25 211116](https://github.com/user-attachments/assets/a3e23765-edfd-457b-a7eb-97b3a6b43696)

```powershell
pip install langchain langchain-google-genai python-dotenv
```




![Screenshot 2024-12-25 211527](https://github.com/user-attachments/assets/01153559-b8fb-4379-8cd8-aa7d0881bd56)







**Repository Structure**

Here's a breakdown of the folders and what you'll find in each:

**1. Chat Models**

- `1_chat_model_basic.py`
- `2_chat_model_basic_conversation.py`
- `3_chat_model_alternatives.py`
- `4_chat_model_conversation_with_user.py`
- `5_chat_model_save_message_history_firestore.py`

Learn how to interact with models like ChatGPT, Claude, and Gemini.

**2. Prompt Templates**

- `1_prompt_template_basic.py`
- `2_prompt_template_with_chat_model.py`

Understand the basics of prompt templates and how to use them effectively.

**3. Chains**

- `1_chains_basics.py`
- `2_chains_under_the_hood.py`
- `3_chains_extended.py`
- `4_chains_parallel.py`
- `5_chains_branching.py`

Learn how to create chains using Chat Models and Prompts to automate tasks.

**4. RAG (Retrieval-Augmented Generation)**

- `1a_rag_basics.py`
- `1b_rag_basics.py`
- `2a_rag_basics_metadata.py`
- `2b_rag_basics_metadata.py`
- `3_rag_text_splitting_deep_dive.py`
- `4_rag_embedding_deep_dive.py`
- `5_rag_retriever_deep_dive.py`
- `6_rag_one_off_question.py`
- `7_rag_conversational.py`
- `8_rag_web_scrape_firecrawl.py`
- `8_rag_web_scrape.py`

Explore the technologies like documents, embeddings, and vector stores that enable RAG queries.

**5. Agents & Tools**

- `1_agent_and_tools_basics.py`
- `agent_deep_dive/`
    - `1_agent_react_chat.py`
    - `2_react_docstore.py`
- `tools_deep_dive/`
    - `1_tool_constructor.py`
    - `2_tool_decorator.py`
    - `3_tool_base_tool.py`

Learn about agents, how they work, and how to build custom tools to enhance their capabilities.




**Repository Structure(NOTES)**

Here's a breakdown of the folders and what you'll find in each:
one thing to note is we are using .invoke method so that the chat model responds to us(1) and using it to create prompts(2)
```
model.invoke(messages)
```

```
model.invoke(prompt)
```
**1. Chat Models**

- `1_chat_model_basic.py`
  just we are getting a response from the gogglegenAI
- `2_chat_model_basic_conversation.py`
having a conversation
- `3_chat_model_alternatives.py`
   ```
   pip install langchain-anthropic langchain-openai
   ```
   couldn't figure out how to solve chat anthropic problem.
   so we are gonna skip it
- `4_chat_model_conversation_with_user.py`
  everytime we are putting the whole chat_history to Ai for a response
```
You: hi
AI: Hi there! How can I help you today?

You: who is newton (answer me in a single line)?
AI: Sir Isaac Newton was a renowned physicist, mathematician, astronomer, alchemist, theologian, and author.

You: exit



---- Message History ----
[
    SystemMessage(content='You are a helpful AI assistant.'),
    HumanMessage(content='hi'),
    AIMessage(content='Hi there! How can I help you today?\n'),
    HumanMessage(content='who is newton (answer me in a single line)?'),
    AIMessage(content='Sir Isaac Newton was a renowned physicist, mathematician, astronomer, alchemist, theologian, and author.\n')
]

```
- `5_chat_model_save_message_history_firestore.py`
![image](https://github.com/user-attachments/assets/d9258aef-6f67-47a1-86f7-7ee844ddbdb6)
starting from  pip install google-cloud-firestore 
```
 pip install google-cloud-firestore 
```
```
 pip install langchain-google-firestore
```

Steps to replicate this example:
1. Create a Firebase account
2. Create a new Firebase project
    - Copy the project ID
3. Create a Firestore database in the Firebase project
4. Install the Google Cloud CLI on your computer
    - https://cloud.google.com/sdk/docs/install
    - Authenticate the Google Cloud CLI with your Google account
        - https://cloud.google.com/docs/authentication/provide-credentials-adc#local-dev
    - Set your default project to the new Firebase project you created
5. Enable the Firestore API in the Google Cloud Console:
    - https://console.cloud.google.com/flows/enableapi?apiid=firestore.googleapis.com


![image](https://github.com/user-attachments/assets/08340caa-a1b8-4b6d-a973-49aaf9b4740c)
![image](https://github.com/user-attachments/assets/e7ef5155-a6ce-45af-8c71-fcc154bdaa39)
maybe unnecessary idk
![image](https://github.com/user-attachments/assets/98afb723-f5ae-4149-9d08-c08330af86b5)
.
.
before running the file, do
![image](https://github.com/user-attachments/assets/605e8daa-62c1-4e99-aaa7-3530d451c124)
and then do,
![image](https://github.com/user-attachments/assets/637fc4e8-3e78-40b4-8816-3592c57ab25f)

and the dashboard
![image](https://github.com/user-attachments/assets/a2b0d7ef-ba3f-42d6-a260-e8e1cf81f0df)
running it again
![image](https://github.com/user-attachments/assets/b831582c-3619-48d0-ae83-cbcb2113d178)
.
.
Learn how to interact with models like ChatGPT, Claude, and Gemini.

**2. Prompt Templates**

- `1_prompt_template_basic.py`
- `2_prompt_template_with_chat_model.py`

Understand the basics of prompt templates and how to use them effectively.

**3. Chains**

- `1_chains_basics.py`
  ![image](https://github.com/user-attachments/assets/71f1cb6a-ab70-4f4f-b9c3-8bb2bfeb9410)
![image](https://github.com/user-attachments/assets/8ee8c718-7cc8-4e8c-a8b0-07b07d74a1fb)
this is mainly a better alternative for 2.2
in one pic the differences are
![image](https://github.com/user-attachments/assets/b85e4540-26bb-4f51-9d0d-94ae1d37c940)

- `2_chains_under_the_hood.py`
- `3_chains_extended.py`
- `4_chains_parallel.py`
- `5_chains_branching.py`

Learn how to create chains using Chat Models and Prompts to automate tasks.

**4. RAG (Retrieval-Augmented Generation)**

- `1a_rag_basics.py`
- `1b_rag_basics.py`
- `2a_rag_basics_metadata.py`
- `2b_rag_basics_metadata.py`
- `3_rag_text_splitting_deep_dive.py`
- `4_rag_embedding_deep_dive.py`
- `5_rag_retriever_deep_dive.py`
- `6_rag_one_off_question.py`
- `7_rag_conversational.py`
- `8_rag_web_scrape_firecrawl.py`
- `8_rag_web_scrape.py`

Explore the technologies like documents, embeddings, and vector stores that enable RAG queries.

**5. Agents & Tools**

- `1_agent_and_tools_basics.py`
- `agent_deep_dive/`
    - `1_agent_react_chat.py`
    - `2_react_docstore.py`
- `tools_deep_dive/`
    - `1_tool_constructor.py`
    - `2_tool_decorator.py`
    - `3_tool_base_tool.py`

Learn about agents, how they work, and how to build custom tools to enhance their capabilities.






































**How to Use This Repository**

1. **Watch the Video:** Start by watching the LangChain Master Class for Beginners video on YouTube at 2X speed for a high-level overview.
2. **Run the Code Examples:** Follow along with the code examples provided in this repository. Each section in the video corresponds to a folder in this repo.
3. **Join the Community:** If you get stuck or want to connect with other AI developers, join the FREE Skool community [here](https://www.skool.com/ai-developer-accelerator/about).

**Comprehensive Documentation**

Each script in this repository contains detailed comments explaining the purpose and functionality of the code. This will help you understand the flow and logic behind each example.

**FAQ**

**Q: What is LangChain?**

A: LangChain is a framework designed to simplify the process of building applications that utilize language models.

**Q: How do I set up my environment?**

A: Follow the instructions in the "Getting Started" section above. Ensure you have Python 3.10 or 3.11 installed, install Poetry, clone the repository, install dependencies, rename the `.env.example` file to `.env`, and activate the Poetry shell.

**Q: I am getting an error when running the examples. What should I do?**

A: Ensure all dependencies are installed correctly and your environment variables are set up properly. If the issue persists, seek help in the Skool community or open an issue on GitHub.

**Q: Can I contribute to this repository?**

A: Yes! Contributions are welcome. Please open an issue or submit a pull request with your changes.

**Q: Where can I find more information about LangChain?**

A: Check out the official LangChain documentation and join the Skool community for additional resources and support.

**Support**

If you encounter any issues or have questions, feel free to open an issue on GitHub or ask for help in the Skool community.

**License**

This project is licensed under the MIT License.
