Summarizer & Quiz Generator Agent
Using Streamlit + OpenAgents SDK + Gemini + PyPDF + Context7 MCP
________________________________________
1. Project Overview
This project builds a PDF Summarizer & Quiz Generator Agent using:
•	UI: Streamlit
•	Model: Google Gemini (gemini-2.0-flash) accessed through the OpenAgents SDK
•	File Handling: PyPDF for PDF text extraction
•	Tools: Context7 MCP functions + SDK tool-calling
•	Agent Logic:
o	Summarizes uploaded PDFs
o	Generates quizzes (MCQs or mixed format) from the full PDF text
The agent uses function-calling tools to read files, summarize text, and generate quiz content.
No custom protocols or formats allowed — follow official SDK syntax only.
________________________________________
2. Critical Configuration Rules (Zero-Bloat Protocol)
These rules ensure your project stays clean and correct:
✅ 1. No Extra Code
•	No unnecessary classes or files
•	No custom parsing logic
•	Only minimal working integration
•	No invented tool formats
✅ 2. Correct API Setup
•	Use OpenAgents SDK, not the normal openai library
•	Base URL:
https://generativelanguage.googleapis.com/v1beta/openai/
•	Model: gemini-2.0-flash
•	API key: GEMINI_API_KEY from .env
✅ 3. SDK Specific Syntax
Follow the official documentation for:
•	Tool definitions
•	Agent initialization
•	Model binding
•	Message calling
If any error occurs → re-check docs using MCP get-library-docs.
✅ 4. Error Recovery Protocol
If you encounter:
•	ImportError
•	SyntaxError
•	AttributeError
→ Stop, re-read docs, fix code exactly as per official syntax.
✅ 5. Dependency Management (uv)
Install only:
•	openai-agents
•	streamlit
•	pypdf
•	python-dotenv
Do NOT reinstall existing packages.
________________________________________
3. Architecture & Required Files
Your project folder must look like:
.
├── .env
├── tools.py              # PDF extraction + utility tools
├── agent.py              # Agent + model + tool registration
├── app.py                # Streamlit UI
├── pyproject.toml        # uv config
└── uploads/              # Temporary PDF uploads
Do NOT create extra folders unless necessary.
________________________________________
4. Implementation Steps
🔵 Step 1 — Read SDK Documentation (Mandatory)
Before coding, use MCP tool:
get-library-docs openai-agents
Review:
•	How tools are defined
•	How to create an Agent
•	How to attach OpenaiChatCompletionModel
•	Tool call syntax
If not 100% certain → check docs again.
________________________________________
🔵 Step 2 — Tools Implementation (tools.py)
You must create two primary tools:
Tool 1: extract_pdf_text(file_path)
•	Opens the uploaded PDF
•	Extracts full text using PyPDF
•	Returns plain text
•	No formatting, no splitting
Tool 2: return_summary(text)
•	Receives PDF text
•	Sends it to model for summarization
•	Returns structured summary
Tool 3: generate_quiz(text, questions=5)
•	Creates MCQs OR mixed quiz from full original PDF text
•	Returns JSON or clean text (your choice)
All tools must be defined using official SDK decorators or tool classes.
No extra parameters or metadata.
________________________________________
🔵 Step 3 — Agent Configuration (agent.py)
Agent responsibilities:
1.	Load GEMINI API key
2.	Configure model using:
OpenaiChatCompletionMode
3. Set base URL
https://generativelanguage.googleapis.com/v1beta/openai/
4Import tools from tools.py
5.Register tools with the Agent
6. Add system prompt:
System Prompt Text (copy exactly):
You are a Summarizer & Quiz Generator Agent. 
When a PDF is uploaded, extract its text using the PDF tool. 
When asked to summarize, generate a clean, structured summary. 
When asked to create a quiz, use the full original PDF text, not the summary. 
Call tools whenever required. 
Never guess—always use file content.
No other instructions allowed.
________________________________________
🔵 Step 4 — Streamlit Front-End (app.py)
UI must support:
A. PDF Upload
•	User selects a PDF
•	Save file to ./uploads
•	Pass the file path to agent function
B. Summarizer Button
•	After upload → displays "Generate Summary"
•	Sends a message to agent
•	Shows structured summary in UI (card/block format)
C. Quiz Generator Button
•	After summary → displays "Create Quiz"
•	Requests quiz from the agent
•	Shows MCQs or mixed questions
Streamlit Guidelines
@cl.on_chat_start is not used here — this is Streamlit, not Chainlit.
Use:
•	st.file_uploader
•	st.button
•	st.session_state to store extracted PDF text
Summary and quiz must be shown only after the user triggers the event.
________________________________________
🔵 Step 5 — Environment & Dependencies
.env
GEMINI_API_KEY=your_key_here
pyproject.toml dependencies
Only include:
openai-agents
streamlit
pypdf
python-dotenv
context7
Nothing else unless required.
________________________________________
5. Testing Scenarios
✅ Test 1 — PDF Upload
User uploads PDF →
extract_pdf_text tool extracts text →
Agent prints confirmation
✅ Test 2 — Summarization
User clicks "Generate Summary" →
Agent returns clean summary
✅ Test 3 — Quiz Generation
User clicks "Create Quiz" →
Agent reads full PDF text →
Generates MCQs or mixed quiz questions
(5–10 questions recommended)
✅ Test 4 — Wrong File
Non-PDF file → App must show "Only PDF allowed"


