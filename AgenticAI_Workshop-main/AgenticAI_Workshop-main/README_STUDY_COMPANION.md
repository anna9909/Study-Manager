# Study Companion: AI-Powered Educational Material Generator

An intelligent multi-agent system that automatically creates comprehensive study materials for any topic. The Study Companion uses 4 specialized AI agents working together to generate complete study packs including notes, solved examples, practice quizzes, and learning plans.

## 🎯 What is Study Companion?

Study Companion is an educational AI system built with CrewAI that automates the creation of high-quality study materials. Simply provide a topic, and the system generates:

- 📝 **Clear Study Notes** - Bullet-point summaries and key concepts
- 🔢 **Solved Example Problems** - 3-5 problems with step-by-step solutions  
- ✅ **Practice Quizzes** - 10 MCQs + 5 short answer questions with answer keys
- 🎯 **Learning Plans** - Structured objectives and study recommendations

## 🏗️ System Architecture

### 4 Specialized AI Agents

1. **Study Manager** (`agents/study_manager.py`)
   - Orchestrates the entire workflow
   - Creates comprehensive learning plans
   - Ensures all materials are cohesive

2. **Notes Generator** (`agents/notes_generator.py`)
   - Produces easy-to-understand bullet-point notes
   - Explains complex concepts simply
   - Organizes information logically

3. **Example Solver** (`agents/example_solver.py`)
   - Creates relevant practice problems
   - Provides detailed step-by-step solutions
   - Explains reasoning behind each step

4. **Quiz Maker** (`agents/quiz_maker.py`)
   - Designs comprehensive assessments
   - Creates MCQs and short answer questions
   - Provides detailed answer keys with explanations

### 🛠️ Built-in Tools

Each agent has access to:
- **RAG (Retrieval-Augmented Generation)** - FAISS-backed knowledge base
- **Web Search** - Live DuckDuckGo lookups
- **Calculator** - Mathematical computations

## 📁 Project Structure

```
study-companion/
├── .env.example              # Environment variables template
├── requirements.txt          # Python dependencies
├── README.md                # Documentation
├── main.py                  # CLI entry point
├── crew.py                  # Agent orchestration
├── tasks.py                 # Task definitions
├── config/
│   ├── settings.py          # Configuration
│   └── logging_config.py    # Logging setup
├── agents/
│   ├── __init__.py
│   ├── study_manager.py     # Study Manager agent
│   ├── notes_generator.py   # Notes Generator agent
│   ├── example_solver.py    # Example Solver agent
│   └── quiz_maker.py        # Quiz Maker agent
├── tools/
│   ├── __init__.py
│   ├── rag_tool.py          # RAG retrieval
│   ├── web_search.py        # Web search
│   └── calculator.py        # Calculator
├── rag/
│   ├── build_vector_db.py   # Vector store builder
│   ├── documents/           # Knowledge base
│   │   └── sample_docs.txt
│   └── vectorstore/         # FAISS index
└── frontend/
    └── app.py               # Streamlit interface
```

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- OpenRouter API key ([get free tier](https://openrouter.ai/keys))
- 2GB free disk space

### Installation

```powershell
# 1. Navigate to project directory
cd c:\Users\amnab\Downloads\AgenticAI_Workshop-main\AgenticAI_Workshop-main

# 2. Create virtual environment
python -m venv .venv
.\. venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
copy .env.example .env
# Edit .env and add your OPENROUTER_API_KEY

# 5. Build knowledge base
python rag\build_vector_db.py
```

## 💻 Usage

### Command Line Interface

Generate study materials for any topic:

```powershell
python main.py --topic "Introduction to Machine Learning"
```

```powershell
python main.py --topic "Calculus Fundamentals"
```

```powershell
python main.py --topic "World History: Renaissance Period"
```

### Web Interface (Streamlit)

Launch the interactive interface:

```powershell
python -m streamlit run frontend\app.py
```

Then:
1. Open browser to `http://localhost:8501`
2. Enter your study topic
3. Click "Generate Study Pack"
4. View and download materials

### Programmatic Usage

```python
from main import run_pipeline

# Generate study materials
study_pack = run_pipeline("Biology: Cell Structure")
print(study_pack)
```

## 📚 Example Output

For "Introduction to Python Programming":

```markdown
# Study Pack: Introduction to Python Programming

## Learning Objectives
- Understand Python syntax and basic data types
- Write functions and control flow statements
- Work with lists, dictionaries, and loops

## Study Notes
### Variables and Data Types
- **Integer**: Whole numbers (e.g., 42, -10)
- **String**: Text in quotes (e.g., "Hello")
- **Float**: Decimal numbers (e.g., 3.14)
...

## Solved Example Problems
### Problem 1: Calculate Average
**Problem**: Write a function to calculate average of a list
**Solution**:
Step 1: Define function with parameter...
...

## Practice Quiz
### Multiple Choice Questions
1. What is the output of print(type(42))?
   A) <class 'str'>
   B) <class 'int'>  ✓
   C) <class 'float'>
...

### Answer Key
1. B - Correct. 42 is an integer...
```

## ⚙️ Customization

### Adding Custom Knowledge

1. Add content to `rag/documents/sample_docs.txt`
2. Rebuild vector store:
   ```powershell
   python rag\build_vector_db.py
   ```

### Modifying Agents

- **Study Manager** - Adjust planning style
- **Notes Generator** - Customize note format
- **Example Solver** - Change problem difficulty
- **Quiz Maker** - Modify question types

### Adjusting Tasks

Edit `tasks.py` to change:
- Number of example problems (default: 3-5)
- Quiz questions (default: 10 MCQs + 5 short answers)
- Output format
- Quality criteria

### LLM Configuration

Modify `config/settings.py`:
- Different models (`MODEL_NAME`)
- Temperature (creativity)
- Token limits (output length)
- Fallback models

## 🚢 Deployment

### Streamlit Community Cloud

1. Push to GitHub
2. Connect to Streamlit Cloud
3. Add `OPENROUTER_API_KEY` to secrets
4. Deploy

### Docker

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "frontend/app.py"]
```

### Cloud Platforms

- Azure App Service
- AWS App Runner
- Google Cloud Run
- Heroku

## 🔧 Troubleshooting

### Vector store not found
```powershell
python rag\build_vector_db.py
```

### API key errors
- Check `.env` file
- Verify key at https://openrouter.ai/keys

### Import errors
```powershell
pip install --upgrade -r requirements.txt
```

### Slow generation
- Check internet connection
- Try faster model in config
- Reduce MAX_TOKENS

## 📖 Use Cases

✅ **Students** - Exam prep materials
✅ **Teachers** - Practice materials for classes
✅ **Self-Learners** - Structured learning resources
✅ **Tutors** - Customized tutoring materials
✅ **EdTech** - Automated content generation

## 🤝 Contributing

We welcome contributions! Areas for improvement:

### New Agent Types
- Flashcard Generator
- Video Script Creator
- Diagram Generator
- Summary Generator

### Enhanced Tools
- Image generation
- PDF export
- Multi-language support
- Audio generation

### Features
- Difficulty level selection
- Subject-specific templates
- Progress tracking
- Collaboration features

## 📄 License

MIT License - see LICENSE file

## 🙏 Acknowledgments

- [CrewAI](https://www.crewai.com/) - Multi-agent framework
- [OpenRouter](https://openrouter.ai/) - LLM API
- [Streamlit](https://streamlit.io/) - Web interface
- [Sentence Transformers](https://www.sbert.net/) - Embeddings

---

**Ready to create study materials?**

```powershell
python main.py --topic "Your Topic Here"
```
