# Chatbot

This is a simple chatbot implementation using the ConversationalRetrievalChain from the LangChain library. It utilizes the OpenAI language model to provide conversational responses based on a given input.

![image](https://github.com/EMar42/my-Jabeta/assets/36295473/ca5b8957-45ad-4659-a99d-127c33c0a7bf)


## Prerequisites

Before running the chatbot, make sure you have the following requirements installed:

- Python (version 3.7 or higher)
- LangChain library (install via pip: `pip install langchain`)
- OpenAI API key (obtain from OpenAI platform)

## Project Structure

The project includes the following files and directories:

- `chatbot.py`: The main script that runs the chatbot.
- `data/`: A directory containing data files for the chatbot to utilize.
  - `data/file1.txt`: A text file with personal text-based data.
  - `data/file2.txt`: Another text file with personal text-based data.

Feel free to add or modify the data files in the `data/` directory according to your needs. The chatbot can utilize these files for more personalized responses or specific domain knowledge.

## Setup

1. Clone or download the repository.

2. Set up your OpenAI API key:
   - Open the file `chatbot.py` in a text editor.
   - Replace `"<ENTER YOUR KEY>"` in the `os.environ["OPENAI_API_KEY"]` line with your actual OpenAI API key.

3. Optional: Adjust the settings and customize the code as needed.

## Usage

1. Open a terminal or command prompt and navigate to the directory where `chatbot.py` is located.

2. Run the chatbot script:
python chatbot.py

3. Enter your queries or prompts in the terminal and press Enter.
- To exit the chatbot, type: `quit`, `q`, or `exit`.

## Customization

- You can modify the `initialize_chain()` function in `chatbot.py` to adjust the vectorstore and retriever configurations based on your requirements.
- The `chatgpt.py` script can be used to add additional functionality or customization to the chatbot. Feel free to modify it according to your needs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Make sure to update the README file with any specific instructions or details related to the "chatgpt.py" script and the contents of the "data" folder.
