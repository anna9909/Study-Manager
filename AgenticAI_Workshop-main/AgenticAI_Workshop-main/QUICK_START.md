# Study Companion - Quick Setup Guide

## 🚀 Getting Started in 5 Minutes

### Step 1: Verify Python Installation
```powershell
python --version
# Should show Python 3.10 or higher
```

### Step 2: Navigate to Project
```powershell
cd c:\Users\amnab\Downloads\AgenticAI_Workshop-main\AgenticAI_Workshop-main
```

### Step 3: Create Virtual Environment
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Step 4: Install Dependencies
```powershell
pip install -r requirements.txt
```

### Step 5: Configure API Key
```powershell
# Copy the example env file
copy .env.example .env

# Edit .env file and add your OpenRouter API key:
# OPENROUTER_API_KEY=your_actual_key_here
```

**Get your free API key:** https://openrouter.ai/keys

### Step 6: Build Knowledge Base
```powershell
python rag\build_vector_db.py
```

### Step 7: Test the System
```powershell
# Generate your first study pack!
python main.py --topic "Introduction to Python"
```

## 🌐 Launch Web Interface
```powershell
python -m streamlit run frontend\app.py
```

Then open: http://localhost:8501

## 📝 Example Commands

```powershell
# Mathematics
python main.py --topic "Algebra: Quadratic Equations"

# Science
python main.py --topic "Physics: Newton's Laws of Motion"

# Programming
python main.py --topic "JavaScript: Async/Await and Promises"

# History
python main.py --topic "American Revolution: Causes and Effects"
```

## ❓ Troubleshooting

### Issue: "ModuleNotFoundError"
**Solution:**
```powershell
pip install --upgrade -r requirements.txt
```

### Issue: "Vector store not found"
**Solution:**
```powershell
python rag\build_vector_db.py
```

### Issue: "API key error"
**Solution:**
- Check `.env` file exists
- Verify `OPENROUTER_API_KEY` is set correctly
- Test key at https://openrouter.ai/keys

### Issue: "Slow generation"
**Solution:**
- Check internet connection
- Try during off-peak hours
- Consider upgrading to a paid model

## 🎯 Next Steps

1. **Customize Agents**
   - Edit files in `agents/` directory
   - Adjust prompts and behaviors

2. **Add Custom Knowledge**
   - Add content to `rag/documents/sample_docs.txt`
   - Run `python rag\build_vector_db.py`

3. **Modify Tasks**
   - Edit `tasks.py` to change outputs
   - Adjust number of problems/questions

4. **Deploy**
   - Share on Streamlit Cloud
   - Deploy to cloud platforms
   - Containerize with Docker

## 💡 Tips for Best Results

✅ **Be Specific** - "Python: List Comprehensions and Lambda Functions" vs "Python"
✅ **Right Level** - Specify "Introduction to..." or "Advanced..." for difficulty
✅ **Clear Scope** - Break large topics into smaller, focused topics
✅ **Check Output** - Review and customize generated materials

## 📚 What You'll Get

Every study pack includes:

1. **📝 Study Notes**
   - Bullet-point format
   - Key definitions
   - Concept explanations
   - Topic summaries

2. **🔢 Solved Examples** (3-5)
   - Clear problem statements
   - Step-by-step solutions
   - Reasoning explanations
   - Final answers

3. **✅ Practice Quiz**
   - 10 Multiple Choice Questions
   - 5 Short Answer Questions
   - Complete answer key
   - Detailed explanations

4. **🎯 Learning Plan**
   - Learning objectives
   - Study recommendations
   - Topic organization

## 🤝 Need Help?

- Check `README_STUDY_COMPANION.md` for full documentation
- Review agent files in `agents/` directory
- Inspect `tasks.py` for task definitions
- Check logs in console output

---

**Ready to start learning? Run your first command:**

```powershell
python main.py --topic "Your Favorite Subject"
```
