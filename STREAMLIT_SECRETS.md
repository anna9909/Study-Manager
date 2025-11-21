# 🔑 Streamlit Cloud Secrets Configuration

Copy and paste this EXACT text into your Streamlit Cloud Secrets:

```toml
OPENROUTER_API_KEY = "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"
```

## How to Add Secrets in Streamlit Cloud:

1. Go to: https://share.streamlit.io/
2. Click on your app
3. Click the **"⋮"** (three dots) menu
4. Select **"Settings"**
5. Click **"Secrets"** tab
6. Paste the line above into the secrets box
7. Click **"Save"**
8. Your app will automatically reboot

## Important Notes:

- ✅ Use TOML format with quotes and equals sign with spaces
- ✅ The key must be exactly: `OPENROUTER_API_KEY`
- ❌ Don't commit `.env` file to GitHub (it's ignored)
- ✅ Secrets are encrypted and secure on Streamlit Cloud

## Verify It Works:

After adding secrets and rebooting, your app should:
1. Load the API key from `st.secrets["OPENROUTER_API_KEY"]`
2. Connect to OpenRouter successfully
3. Generate study materials without 401 errors

---

**Your API Key:** `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`

Copy the line above into Streamlit Cloud Secrets now! 🚀
