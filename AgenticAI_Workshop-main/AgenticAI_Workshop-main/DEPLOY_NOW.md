# 🚀 Deploy Your Study Companion in 5 Minutes!

## Step-by-Step Guide for Streamlit Cloud (FREE)

---

## ✅ What You Need
- [x] GitHub account (free)
- [x] Your OpenRouter API key: `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`
- [x] This project folder

---

## 📋 Deployment Steps

### Step 1: Push to GitHub (2 minutes)

Open PowerShell in your project folder and run:

```powershell
cd c:\Users\amnab\Downloads\AgenticAI_Workshop-main\AgenticAI_Workshop-main

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Study Companion - AI Educational System"
```

**Now create a repository on GitHub:**

1. Go to: https://github.com/new
2. Repository name: `study-companion`
3. Make it **Public** or **Private** (both work)
4. Click **"Create repository"**

**Copy the commands shown on GitHub and run them**, OR run these:

```powershell
# Replace YOUR_USERNAME with your actual GitHub username
git remote add origin https://github.com/YOUR_USERNAME/study-companion.git
git branch -M main
git push -u origin main
```

---

### Step 2: Deploy on Streamlit Cloud (2 minutes)

1. **Go to:** https://streamlit.io/cloud
2. **Sign in** with your GitHub account
3. Click **"New app"** button
4. Fill in:
   - **Repository:** Select `study-companion`
   - **Branch:** `main`
   - **Main file path:** `frontend/app.py`

5. Click **"Advanced settings..."**
6. In the **Secrets** box, paste:
   ```
   OPENROUTER_API_KEY = "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"
   ```

7. Click **"Deploy"**

---

### Step 3: Wait for Deployment (1 minute)

Streamlit Cloud will:
- ✅ Install all dependencies automatically
- ✅ Build the vector store
- ✅ Start your app

**Your app will be live at:**
```
https://YOUR-APP-NAME.streamlit.app
```

---

## 🎉 You're Done!

Your Study Companion is now live and accessible from anywhere!

### Test It:
1. Open your Streamlit app URL
2. Enter a topic like "Introduction to Python"
3. Click "Generate Study Pack"
4. Watch the AI agents work!

---

## 🔗 Share Your App

Your Streamlit URL is public (unless you made the GitHub repo private). Share it with:
- Friends
- Students
- Teachers
- On social media

---

## 📊 Monitor Usage

**Check your app:**
- Go to: https://streamlit.io/cloud
- Click on your app
- See logs, metrics, and deployment status

**Check API usage:**
- Go to: https://openrouter.ai/activity
- Monitor your free credits

---

## 🔧 Update Your App

To update your app with changes:

```powershell
cd c:\Users\amnab\Downloads\AgenticAI_Workshop-main\AgenticAI_Workshop-main

# Make your changes, then:
git add .
git commit -m "Updated app"
git push
```

Streamlit Cloud will automatically redeploy! 🎉

---

## 🆘 Troubleshooting

**Problem:** "App won't start"  
**Solution:** Check logs in Streamlit Cloud dashboard for errors

**Problem:** "API key error"  
**Solution:** Go to Settings → Secrets in Streamlit Cloud and verify your API key

**Problem:** "Vector store not found"  
**Solution:** Streamlit will build it automatically on first run - wait a bit longer

**Problem:** "Module not found"  
**Solution:** Check that `requirements.txt` is in your repository

---

## 📞 Need Help?

**Streamlit Community:** https://discuss.streamlit.io/  
**OpenRouter Docs:** https://openrouter.ai/docs  
**CrewAI Docs:** https://docs.crewai.com/

---

## 🎯 Next Steps

1. **Customize agents** - Edit files in `agents/` folder
2. **Add more content** - Put documents in `rag/documents/`
3. **Change the model** - Edit `config/settings.py`
4. **Improve UI** - Modify `frontend/app.py`

---

**Your AI study assistant is ready! 🚀**

Share your deployment URL and help others learn!
