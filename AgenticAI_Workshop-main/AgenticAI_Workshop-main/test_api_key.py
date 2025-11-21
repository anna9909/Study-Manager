"""Test script to verify OpenRouter API key is working correctly."""
import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env
load_dotenv()

# Get the API key
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("❌ No OpenRouter API key found in .env")

print(f"✓ Found API key: {api_key[:20]}...")

# Quick test: call OpenRouter models endpoint
url = "https://openrouter.ai/api/v1/models"
headers = {"Authorization": f"Bearer {api_key}"}

print("\n🔍 Testing API key with OpenRouter...")

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("✅ API key works! Models retrieved.")
    models = response.json()
    print(f"✓ Found {len(models.get('data', []))} available models")
else:
    print(f"❌ Error: {response.status_code} - {response.text}")
    
print("\n" + "="*60)
print("Next step: Run 'python rag\\build_vector_db.py' to build vector store")
print("="*60)
