# Study Companion - Complete System Overview

## 🎓 Project Summary

**Study Companion** is an intelligent multi-agent AI system that automatically generates comprehensive study materials for any educational topic. Built with CrewAI, it coordinates 4 specialized agents to create complete study packs including notes, solved examples, practice quizzes, and learning plans.

## 🏗️ Architecture Overview

### System Components

```
┌─────────────────────────────────────────────────────────────┐
│                    STUDY COMPANION SYSTEM                    │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────┐  ┌──────────────┐  ┌─────────────┐        │
│  │   main.py   │  │   crew.py    │  │  tasks.py   │        │
│  │  CLI Entry  │─▶│  Orchestr.   │─▶│  Task Def   │        │
│  └─────────────┘  └──────────────┘  └─────────────┘        │
│         │                │                    │              │
│         ▼                ▼                    ▼              │
│  ┌───────────────────────────────────────────────────┐      │
│  │              4 SPECIALIZED AGENTS                  │      │
│  ├───────────────────────────────────────────────────┤      │
│  │  📋 Study Manager    │  📝 Notes Generator        │      │
│  │  🔢 Example Solver   │  ✅ Quiz Maker             │      │
│  └───────────────────────────────────────────────────┘      │
│         │                                                    │
│         ▼                                                    │
│  ┌───────────────────────────────────────────────────┐      │
│  │                  SHARED TOOLS                      │      │
│  ├───────────────────────────────────────────────────┤      │
│  │  🔍 RAG (FAISS)  │  🌐 Web Search  │  🧮 Calc    │      │
│  └───────────────────────────────────────────────────┘      │
│         │                                                    │
│         ▼                                                    │
│  ┌───────────────────────────────────────────────────┐      │
│  │               COMPLETE STUDY PACK                  │      │
│  │  • Notes  • Examples  • Quiz  • Learning Plan      │      │
│  └───────────────────────────────────────────────────┘      │
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │          INTERFACES                                  │    │
│  │  • CLI (main.py)                                     │    │
│  │  • Web UI (frontend/app.py - Streamlit)             │    │
│  │  • Programmatic API (import run_pipeline)           │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## 📁 Complete File Structure

```
study-companion/
│
├── 📄 README_STUDY_COMPANION.md    # Full documentation
├── 📄 QUICK_START.md               # 5-minute setup guide
├── 📄 PROJECT_OVERVIEW.md          # This file
├── 📄 EDUCATIONAL_SYSTEM_OVERVIEW.md # Original system doc
│
├── ⚙️ Configuration Files
│   ├── .env.example                # Environment template
│   ├── requirements.txt            # Python dependencies
│   ├── main.py                     # CLI entry point
│   ├── crew.py                     # Agent orchestration
│   └── tasks.py                    # Task definitions
│
├── 📂 config/
│   ├── settings.py                 # Global configuration
│   └── logging_config.py           # Logging setup
│
├── 🤖 agents/                      # 4 Specialized Agents
│   ├── __init__.py                 # Exports all agents
│   ├── study_manager.py            # Workflow coordinator
│   ├── notes_generator.py          # Note creator
│   ├── example_solver.py           # Problem solver
│   └── quiz_maker.py               # Assessment creator
│
├── 🛠️ tools/                       # Shared Tools
│   ├── __init__.py                 # Tool factory
│   ├── rag_tool.py                 # RAG retrieval (FAISS)
│   ├── web_search.py               # DuckDuckGo search
│   └── calculator.py               # Math calculator
│
├── 📚 rag/                         # Knowledge Base
│   ├── build_vector_db.py          # Vector store builder
│   ├── documents/
│   │   └── sample_docs.txt         # Educational knowledge
│   └── vectorstore/                # FAISS index (generated)
│
└── 🌐 frontend/
    └── app.py                      # Streamlit web interface
```

## 🤖 Agent Details

### 1. Study Manager Agent
**File:** `agents/study_manager.py`
**Role:** Educational Workflow Coordinator
**Responsibilities:**
- Analyzes study topic and creates learning plan
- Defines learning objectives
- Coordinates all other agents
- Ensures coherent final output

**Output:**
- Study plan structure
- Learning objectives
- Topic organization
- Coordination guidelines

### 2. Notes Generator Agent
**File:** `agents/notes_generator.py`
**Role:** Educational Content Synthesizer
**Responsibilities:**
- Creates clear bullet-point notes
- Explains key concepts simply
- Organizes information logically
- Generates summaries

**Output:**
- Bullet-point notes
- Key definitions
- Concept explanations
- Section summaries

### 3. Example Solver Agent
**File:** `agents/example_solver.py`
**Role:** Problem-Solving Expert
**Responsibilities:**
- Creates relevant practice problems
- Provides step-by-step solutions
- Explains reasoning for each step
- Uses calculator tool for computations

**Output:**
- 3-5 practice problems
- Detailed solutions
- Step-by-step explanations
- Final answers with verification

### 4. Quiz Maker Agent
**File:** `agents/quiz_maker.py`
**Role:** Assessment Designer
**Responsibilities:**
- Designs comprehensive assessments
- Creates varied question types
- Tests multiple cognitive levels
- Provides detailed answer keys

**Output:**
- 10 Multiple Choice Questions
- 5 Short Answer Questions
- Complete answer key
- Explanation for each answer

## 🛠️ Tool System

### RAG Tool (rag_tool.py)
- **Purpose:** Retrieval-Augmented Generation
- **Technology:** FAISS vector store
- **Function:** Retrieves relevant educational content
- **Usage:** All agents for accurate information

### Web Search Tool (web_search.py)
- **Purpose:** Live information retrieval
- **Technology:** DuckDuckGo API
- **Function:** Current facts and examples
- **Usage:** When knowledge base is insufficient

### Calculator Tool (calculator.py)
- **Purpose:** Mathematical computations
- **Technology:** Python eval (safe)
- **Function:** Solves numerical problems
- **Usage:** Example Solver for math problems

## 🔄 Workflow Process

1. **User Input**
   - CLI: `python main.py --topic "Topic"`
   - Web: Enter topic in Streamlit interface
   - API: `run_pipeline("Topic")`

2. **Study Manager Task**
   - Analyzes topic
   - Creates learning plan
   - Defines objectives
   - Sets structure

3. **Notes Generator Task**
   - Researches topic (RAG + Web)
   - Creates bullet-point notes
   - Explains concepts
   - Generates summaries

4. **Example Solver Task**
   - Creates 3-5 problems
   - Solves step-by-step
   - Explains reasoning
   - Verifies answers

5. **Quiz Maker Task**
   - Designs 10 MCQs
   - Creates 5 short answers
   - Writes answer key
   - Adds explanations

6. **Final Output**
   - Complete study pack
   - All sections integrated
   - Formatted in Markdown
   - Ready for download

## ⚙️ Configuration

### Environment Variables (.env)
```env
OPENROUTER_API_KEY=your_key
MODEL_NAME=meta-llama/llama-3.3-70b-instruct:free
TEMPERATURE=0.2
MAX_TOKENS=800
```

### LLM Settings (config/settings.py)
- Model selection
- Temperature control
- Token limits
- Fallback models
- API configuration

### Task Configuration (tasks.py)
- Number of examples (default: 3-5)
- Quiz questions (default: 10 MCQs + 5 SA)
- Output format
- Quality criteria

## 📊 Use Cases & Applications

### Students 🎓
- Exam preparation materials
- Quick topic reviews
- Practice problems
- Self-assessment

### Teachers 👨‍🏫
- Lesson planning
- Practice material creation
- Assessment design
- Differentiated instruction

### Self-Learners 📖
- Structured learning paths
- Comprehensive resources
- Progress tracking
- Skill development

### Tutors 👥
- Customized materials
- Student-specific content
- Varied difficulty levels
- Quick preparation

### EdTech Companies 💼
- Automated content generation
- Scalable material creation
- Curriculum development
- Assessment systems

## 🚀 Deployment Options

### Local Development
```powershell
python main.py --topic "Topic"
python -m streamlit run frontend\app.py
```

### Streamlit Cloud
- Free hosting
- Easy deployment
- Automatic updates
- Built-in authentication

### Docker Container
```dockerfile
FROM python:3.11-slim
# ... see README for full Dockerfile
```

### Cloud Platforms
- **Azure App Service** - $0-100/month
- **AWS App Runner** - Pay per use
- **Google Cloud Run** - Serverless
- **Heroku** - Free tier available

## 🔧 Customization Guide

### Adding New Agents
1. Create agent file in `agents/`
2. Define system prompt and configuration
3. Export in `agents/__init__.py`
4. Add task in `tasks.py`
5. Update crew in `crew.py`

### Modifying Existing Agents
1. Edit agent file (e.g., `agents/notes_generator.py`)
2. Adjust system prompt
3. Change role/goal/backstory
4. Test with sample topic

### Adding New Tools
1. Create tool file in `tools/`
2. Implement tool class
3. Export in `tools/__init__.py`
4. Add to agent toolkit in tasks

### Customizing Knowledge Base
1. Edit `rag/documents/sample_docs.txt`
2. Add educational content
3. Rebuild: `python rag\build_vector_db.py`
4. Test with related topics

## 📈 Performance & Scaling

### Generation Time
- Simple topics: 1-2 minutes
- Complex topics: 3-5 minutes
- Factors: Model speed, topic complexity, web search needs

### Optimization Tips
- Use faster models for development
- Cache vector store in memory
- Implement request queuing
- Add result caching

### Scaling Strategies
- Load balancing across instances
- Queue-based processing
- Async agent execution
- Result caching system

## 🔒 Security & Privacy

### API Key Management
- Store in `.env` file (not committed)
- Use environment variables
- Rotate keys regularly
- Monitor usage

### Data Privacy
- No student data stored
- Generated content is ephemeral
- No tracking or analytics
- Local processing option

### Production Considerations
- Rate limiting
- Input validation
- Error handling
- Audit logging

## 🐛 Common Issues & Solutions

### Installation Issues
```powershell
# Fix: Upgrade pip
python -m pip install --upgrade pip

# Fix: Install dependencies
pip install -r requirements.txt
```

### Vector Store Issues
```powershell
# Fix: Rebuild vector store
python rag\build_vector_db.py
```

### API Key Issues
- Verify key in `.env`
- Check key is active
- Test at openrouter.ai/keys

### Slow Performance
- Check internet connection
- Try different model
- Reduce MAX_TOKENS
- Use caching

## 📚 Technical Stack

**Core Framework:**
- CrewAI - Multi-agent orchestration
- LangChain - LLM integration
- OpenRouter - LLM API

**AI/ML:**
- Meta Llama 3.3 70B - Primary model
- Sentence Transformers - Embeddings
- FAISS - Vector search

**Tools & Utilities:**
- Streamlit - Web interface
- Python-dotenv - Configuration
- DuckDuckGo - Web search

**Development:**
- Python 3.10+
- Virtual environment
- Git version control

## 🎯 Future Enhancements

### Planned Features
- [ ] Flashcard generation
- [ ] Mind map visualization
- [ ] PDF export
- [ ] Multi-language support
- [ ] Difficulty level selection
- [ ] Progress tracking
- [ ] Collaborative features

### Agent Improvements
- [ ] Video script generator
- [ ] Diagram creator
- [ ] Summary generator
- [ ] Concept mapper

### Tool Additions
- [ ] Image generation
- [ ] Code execution
- [ ] Database query
- [ ] API integration

### Platform Features
- [ ] User authentication
- [ ] Content library
- [ ] Sharing capabilities
- [ ] Analytics dashboard

## 📞 Support & Resources

**Documentation:**
- `README_STUDY_COMPANION.md` - Full documentation
- `QUICK_START.md` - Setup guide
- This file - System overview

**Code Resources:**
- `agents/` - Agent implementations
- `tasks.py` - Task definitions
- `crew.py` - Orchestration logic

**External Resources:**
- CrewAI Docs: https://docs.crewai.com
- OpenRouter: https://openrouter.ai
- Streamlit Docs: https://docs.streamlit.io

---

## 🎉 Quick Start Command

```powershell
python main.py --topic "Introduction to Machine Learning"
```

**Ready to create amazing study materials? Let's go! 🚀**
