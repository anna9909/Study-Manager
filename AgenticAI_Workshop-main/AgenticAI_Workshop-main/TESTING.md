# 🧪 Testing Your Study Companion Setup

Follow these steps to verify everything is working:

## Step 1: Test API Key ✅

Run the API key test script:

```powershell
cd c:\Users\amnab\Downloads\AgenticAI_Workshop-main\Study-Manager\AgenticAI_Workshop-main\AgenticAI_Workshop-main
python test_api_key.py
```

**Expected output:**
```
✓ Found API key: sk-or-v1-0b0f162bcbd...
🔍 Testing API key with OpenRouter...
✅ API key works! Models retrieved.
✓ Found 200+ available models
```

If you see ❌ errors, check your `.env` file has:
```
OPENROUTER_API_KEY=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
```
(No quotes, no spaces around =)

---

## Step 2: Build Vector Store 📦

Build the knowledge base:

```powershell
python rag\build_vector_db.py
```

**Expected output:**
```
📚 Building vector store...
✅ Vector store created at: rag/vectorstore/
```

---

## Step 3: Test CLI 🖥️

Generate a test study pack:

```powershell
python main.py --topic "Introduction to Python"
```

**This will:**
- ✅ Validate API key
- ✅ Run all 4 AI agents
- ✅ Generate comprehensive study materials
- ⏱️ Take 2-5 minutes

---

## Step 4: Test Web Interface 🌐

Launch Streamlit locally:

```powershell
python -m streamlit run frontend\app.py
```

**Then:**
1. Open: http://localhost:8501
2. Enter a topic
3. Click "Generate Study Pack"
4. Wait for results

---

## ✅ All Tests Pass?

**You're ready to deploy!**

### For GitHub Desktop:
1. Commit all changes
2. Push to GitHub
3. Streamlit Cloud will auto-deploy

### For Streamlit Cloud:
1. Add secret: `OPENROUTER_API_KEY = "your-key"`
2. Path: `AgenticAI_Workshop-main/AgenticAI_Workshop-main/frontend/app.py`
3. Deploy!

---

## 🐛 Troubleshooting

**Problem:** "API key not found"
- Check `.env` file exists in project root
- Verify no quotes around the key
- Restart your terminal/IDE

**Problem:** "Vector store not found"
- Run: `python rag\build_vector_db.py`

**Problem:** "Module not found"
- Run: `pip install -r requirements.txt`

**Problem:** "401 User not found"
- Your API key is invalid
- Get a new one from https://openrouter.ai/keys

---

**Ready? Test your API key first! 🚀**
