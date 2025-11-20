# 🎓 Study Companion - AI-Powered Educational Material Generator

**An intelligent multi-agent system that automatically generates comprehensive study materials including notes, solved examples, and practice quizzes.**

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-00A67E?style=for-the-badge)](https://crewai.com)

---

## 🚀 Quick Start - Deploy in 5 Minutes!

### 1️⃣ Get API Key (FREE)
1. Go to [OpenRouter](https://openrouter.ai/keys)
2. Sign up and get your free API key

### 2️⃣ Deploy on Streamlit Cloud (FREE!)
1. Fork this repository to your GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Sign in with GitHub
4. Click **"New app"**
5. Select your forked repository
6. Set main file: `frontend/app.py`
7. Click **"Advanced settings"** → Add secret:
   ```
   OPENROUTER_API_KEY = "your-api-key-here"
   ```
8. Click **"Deploy"** ✨

**Your app will be live at:** `https://your-app-name.streamlit.app`

---

## 🎯 What It Does

Study Companion uses 4 specialized AI agents working together:

### 📋 Study Manager
Creates personalized learning plans and coordinates all agents

### 📝 Notes Generator  
Generates clear, bullet-point notes and summaries

### 🧮 Example Solver
Solves 3-5 practice problems with step-by-step solutions

### ❓ Quiz Maker
Creates 10 MCQs + 5 short-answer questions with answer keys

---

## 💡 Example Topics

- "Introduction to Machine Learning"
- "Photosynthesis in Plants"  
- "World War II History"
- "Python Programming Fundamentals"
- "Shakespeare's Hamlet Analysis"

---

## 🛠️ Technology Stack

- **CrewAI** - Multi-agent orchestration
- **LangChain** - LLM integration & RAG
- **OpenRouter** - LLM API (free tier)
- **FAISS** - Vector database
- **Streamlit** - Web interface
- **Sentence Transformers** - Embeddings

---

## 📚 Complete Documentation

- [Deployment Guide](DEPLOYMENT_GUIDE.md) - All deployment options (Streamlit, Docker, Azure, Heroku)
- [Quick Start Guide](QUICK_START.md) - Get started quickly
- [Project Overview](PROJECT_OVERVIEW.md) - Architecture details
- [Tools Documentation](TOOLS_UPDATE.md) - Educational tools
- [System Overview](EDUCATIONAL_SYSTEM_OVERVIEW.md) - Full details

---

## 🖥️ Local Development (Optional)

If you want to test locally before deploying:

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/study-companion.git
   cd study-companion
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   # Copy .env.example to .env and add your API key
   cp .env.example .env
   ```

4. **Build the knowledge base**
   ```bash
   python rag/build_vector_db.py
   ```

### Running Locally

**CLI Mode:**
```bash
python main.py --topic "Introduction to Python"
```

**Web Interface:**
```bash
streamlit run frontend/app.py
```
Then open: http://localhost:8501

---

## 🔧 Customization

- **Add Content**: Put educational documents in `rag/documents/` and rebuild vector store
- **Modify Agents**: Edit agent prompts in `agents/` folder
- **Adjust Tasks**: Update task definitions in `tasks.py`
- **Change Model**: Edit `config/settings.py` to use different LLM models

---

## 🔐 Security Best Practices

✅ **DO:**
- Use environment variables for API keys
- Add `.env` to `.gitignore`  
- Use Streamlit secrets for cloud deployment
- Rotate API keys regularly

❌ **DON'T:**
- Commit API keys to git
- Share API keys publicly
- Hard-code keys in code

---

## 📊 Cost

**100% FREE** when using:
- OpenRouter free tier (`llama-3.3-70b-instruct:free`)
- Streamlit Community Cloud
- Free GitHub account

---

## 🐛 Troubleshooting

**Issue:** "Vector store not found"  
**Solution:** Run `python rag/build_vector_db.py`

**Issue:** "Module not found"  
**Solution:** Run `pip install -r requirements.txt`

**Issue:** "API key error"  
**Solution:** Check your API key at [openrouter.ai/keys](https://openrouter.ai/keys)

**Issue:** "Port already in use"  
**Solution:** Use `streamlit run frontend/app.py --server.port 8502`

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for more troubleshooting.

---

## 🎉 Ready to Deploy?

**Fastest way (5 minutes):**
1. Fork this repo
2. Deploy on [streamlit.io/cloud](https://streamlit.io/cloud)  
3. Add your OpenRouter API key in secrets
4. Done! Your AI study assistant is live! 🚀

**Need help?** Check [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for step-by-step instructions.

---

Made with ❤️ using CrewAI Multi-Agent Framework
