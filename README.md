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
in one pic, the differences are
![image](https://github.com/user-attachments/assets/b85e4540-26bb-4f51-9d0d-94ae1d37c940)

- `2_chains_under_the_hood.py`

  if you are new to lambda functions, see below
![image](https://github.com/user-attachments/assets/28a0efa9-917f-42a2-9f46-7454715c854f)

this is just WORSE example of 3.1. In 3.1 we are doing int 1 line and here we are doing it in 3 lines
![image](https://github.com/user-attachments/assets/12ef0259-354a-4379-b29b-ba8d60491fd1)

- `3_chains_extended.py`
we are extending the chain(doing other functions) with the RunableLamda
![image](https://github.com/user-attachments/assets/5d363092-b232-47c4-8c4f-ebe7dffb9f9a)
![image](https://github.com/user-attachments/assets/469dc9c6-1065-488b-b3a0-f2828f133b4d)


- `4_chains_parallel.py`
### Workflow

1. **Ask the chat model to list all the main features of the product.**  
   Example: "List the main features of the product MacBook Pro."

2. **Take the result (list of features) and send it back to the chat model with two parallel questions:**
   - **Question A:** "Given these features(result), what are the pros of these features?"
   - **Question B:** "Given these features(result), what are the cons of these features?"

3. **Receive the responses for both questions (pros and cons) from the chat model.**

4. **Combine the pros and cons into a final structured review.**  
   Example:
   - Pros: (list of pros)
   - Cons: (list of cons)
![image](https://github.com/user-attachments/assets/847ca3b5-0f5c-4a9f-9b97-68a084492068)

---
### Example Execution and Explanation

Suppose we execute the chain with the product name "MacBook Pro." Here's how it would work step-by-step, followed by its practical use cases and reasoning.

---

### **1. Execution Example**
#### **Input:**
```python
result = chain.invoke({"product_name": "MacBook Pro"})
```

#### **Steps the Chain Follows:**

1. **Prompt Template:**
   The system prompt sets the model as an "expert product reviewer," and the human prompt asks:
   ```
   List the main features of the product MacBook Pro.
   ```

   **Model Output (Features):**
   ```
   - M1 Pro/M1 Max chips
   - Retina display
   - Long battery life
   - macOS ecosystem
   - Premium build quality
   ```

2. **Branching Analysis:**
   - **Pros Analysis Branch:**
     The `analyze_pros` function asks:
     ```
     Given these features: M1 Pro/M1 Max chips, Retina display, Long battery life, macOS ecosystem, Premium build quality, list the pros of these features.
     ```
     **Model Output (Pros):**
     ```
     - High-performance chips for demanding tasks.
     - Stunning visuals with the Retina display.
     - Extended battery life for all-day use.
     - Seamless integration within the Apple ecosystem.
     - Durable and elegant build quality.
     ```

   - **Cons Analysis Branch:**
     The `analyze_cons` function asks:
     ```
     Given these features: M1 Pro/M1 Max chips, Retina display, Long battery life, macOS ecosystem, Premium build quality, list the cons of these features.
     ```
     **Model Output (Cons):**
     ```
     - Expensive compared to competitors.
     - Limited compatibility with non-Apple devices.
     - Lack of upgradability (e.g., RAM and storage).
     ```

3. **Combine Outputs:**
   The `combine_pros_cons` function formats the pros and cons into a structured review:
   ```
   Pros:
   - High-performance chips for demanding tasks.
   - Stunning visuals with the Retina display.
   - Extended battery life for all-day use.
   - Seamless integration within the Apple ecosystem.
   - Durable and elegant build quality.

   Cons:
   - Expensive compared to competitors.
   - Limited compatibility with non-Apple devices.
   - Lack of upgradability (e.g., RAM and storage).
   ```

#### **Output:**
```plaintext
Pros:
- High-performance chips for demanding tasks.
- Stunning visuals with the Retina display.
- Extended battery life for all-day use.
- Seamless integration within the Apple ecosystem.
- Durable and elegant build quality.

Cons:
- Expensive compared to competitors.
- Limited compatibility with non-Apple devices.
- Lack of upgradability (e.g., RAM and storage).
```

---


### **3. Practical Use Cases**
This approach can be applied in various domains:

#### **a. E-commerce:**
   - Automatically generate product reviews for online stores.
   - Help customers compare products by listing detailed pros and cons.

#### **b. Content Creation:**
   - Assist bloggers and tech reviewers by automating part of the review-writing process.
   - Generate structured content for marketing or promotional purposes.

#### **c. Decision Support:**
   - Aid consumers or businesses in making informed decisions by providing a balanced overview of products.

#### **d. Customer Support:**
   - Summarize feedback for products based on features and provide tailored advice to users.

#### **e. Market Analysis:**
   - Use similar workflows to analyze competitor products and identify strengths/weaknesses in a structured manner.
---

- `5_chains_branching.py`
![image](https://github.com/user-attachments/assets/73ab7da8-9bf7-40a7-b8de-b77a4725941a)

Learn how to create chains using Chat Models and Prompts to automate tasks.

**4. RAG (Retrieval-Augmented Generation)**  
**For speed and efficiency**: Use `sentence-transformers/all-MiniLM-L6-v2`.  
**For better accuracy and results**: Upgrade to `sentence-transformers/all-mpnet-base-v2`.  
- `1a_rag_basics.py`
![image](https://github.com/user-attachments/assets/6296be07-c222-4658-a035-c4c6af7a291e)
---
![image](https://github.com/user-attachments/assets/cedd2474-c882-42de-b58a-5170a1187eb5)
![image](https://github.com/user-attachments/assets/6c2907f0-d20b-4ec8-8711-461e2b7bf6d6)

```
pip install chromadb
```
if we use the code, it fails during the embedding creation step. so lets find a Different Embedding Model
```
pip install sentence-transformers

```

---
if you are getting this
```
Vector store already exists. No need to initialize.
```
ad want to delete the vector you can do it by clicking on the `db` and delete it

![image](https://github.com/user-attachments/assets/b69d1155-ce48-4d7b-a69c-d27eecb38a33)

- `1b_rag_basics.py`
---
what does vector store look like
![image](https://github.com/user-attachments/assets/507b4734-bb9a-424d-a477-051472657853)
Here’s a simple table explaining `k` and `score_threshold` in easy words:

| **Parameter**       | **What It Does**                                                        | **Example Value** | **What It Means**                                                                                           |
|----------------------|-------------------------------------------------------------------------|-------------------|-------------------------------------------------------------------------------------------------------------|
| **`k`**             | Limits the maximum number of results (documents) to retrieve.          | `k=3`            | Retrieve only the top 3 most relevant documents.                                                           |
| **`score_threshold`** | Sets the minimum relevance score required for a document to be included. | `score_threshold=0.9` | Only include documents with a similarity score of 90% (0.9) or higher.                                      |

---

### **How They Work Together**
- **`k=3, score_threshold=0.9`**:
  - Get up to 3 documents that are very closely related to the query (90% relevance or higher).
  
- **What Happens If No Document Meets the Threshold?**
  - If no document has a similarity score above 0.9, the result will be empty.

---

### **Example:**
- If there are 5 documents with scores: `0.95, 0.92, 0.85, 0.80, 0.78`:
  - With `k=3` and `score_threshold=0.9`, only the first 2 documents (`0.95` and `0.92`) will be retrieved.
  - The rest (`0.85, 0.80, 0.78`) are excluded due to the threshold.

- `2a_rag_basics_metadata.py`  
adding the source(from where the AI found that info)
- `2b_rag_basics_metadata.py`  
no comments
- `3_rag_text_splitting_deep_dive.py`  
`chunk_size=1000`: Each chunk will have up to 1000 characters.  
`chunk_overlap=100`: Each chunk overlaps with the next one by 100 characters. This overlap ensures that important context isn't lost between chunks.


| **Splitting Method**          | **What It Does**                                                                                  | **When to Use It**                                                                             |
|--------------------------------|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| **Character-based Splitting** | Cuts text into chunks of a fixed number of characters.                                             | Use when you want chunks of the same size, no matter where the sentences or paragraphs end.   |
| **Sentence-based Splitting**  | Breaks text into chunks, making sure each chunk ends at a complete sentence.(we are gonna look for full stops)                    | Use when you want each chunk to make sense as a full idea or sentence.                        |
| **Token-based Splitting**     | Splits text into chunks based on words or smaller parts (tokens), using a tokenizer.              | Use when working with AI models that limit how many tokens (words) you can use at one time.   |
| **Recursive Character-based Splitting** (most used) | Tries to break text at natural places (like sentences or paragraphs) but stays within a size limit.               | Use when you want to balance between keeping chunks meaningful and keeping them small.         |
| **Custom Splitting**          | Lets you make your own rules for splitting text, like splitting by paragraphs or custom markers.   | Use when your text has a special format that other methods don’t handle well.                 |


- `4_rag_embedding_deep_dive.py`  
here, we showed the implementations of other text embeddings and models  
(so NO CHANGES IN THE CODE)  
    - OpenAIEmbeddings(model="text-embedding-ada-002")  
    - HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
---
```query_vector_store("chroma_db_with_metadata",    query,         embedding_function,     "similarity",       {"k": 3})```  
```                    name of the vector store,    our question,  embedding models,        search type,       search type's parameter```
- `5_rag_retriever_deep_dive.py`  
This example focuses on exploring how to fine-tune and customize search methods in **retrievers** for retrieving documents from **vector stores**. By the end, you'll learn:

1. How to adjust search parameters in retrievers.
2. How different types of search queries work.
3. How fine-tuning these parameters impacts search results.

The goal is to understand and compare the results of various search approaches.

| Name                          | What                                                                                           | Code                                                                                                                                       | Code Parameters Description                                                                                       |
|-------------------------------|------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Similarity Search             | Retrieves documents based on vector similarity, finding the most similar ones to the query.    | `query_vector_store("chroma_db_with_metadata", query, embedding_function, "similarity", {"k": 3})`                                        | `"k": Number of top similar documents to retrieve.`                                                             |
| Max Marginal Relevance (MMR)  | Balances relevance to the query with diversity among retrieved documents to avoid redundancy.  | `query_vector_store("chroma_db_with_metadata", query, embedding_function, "mmr", {"k": 3, "fetch_k": 20, "lambda_mult": 0.5})`           | `"k": Number of documents to retrieve.`<br>`"fetch_k": Number of documents fetched initially for diversity.`<br>`"lambda_mult": Diversity control (1 for minimum diversity, 0 for maximum).` |
| Similarity Score Threshold    | Retrieves only documents that exceed a specified similarity score threshold.                  | `query_vector_store("chroma_db_with_metadata", query, embedding_function, "similarity_score_threshold", {"k": 3, "score_threshold": 0.1})` | `"k": Number of documents to retrieve.`<br>`"score_threshold": Minimum similarity score for relevance.`          |

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
