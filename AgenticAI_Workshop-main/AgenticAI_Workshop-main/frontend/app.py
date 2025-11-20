"""Streamlit frontend for the Study Companion system."""
from __future__ import annotations

import sys
from pathlib import Path
from datetime import datetime

import streamlit as st
from dotenv import load_dotenv

# Ensure we can import the backend modules
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from main import run_pipeline  # noqa: E402

load_dotenv()

st.set_page_config(
    page_title="Study Companion - AI Study Pack Generator",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
.main-header {
    font-size: 2.5rem;
    font-weight: 700;
    color: #1f77b4;
    margin-bottom: 0.5rem;
}
.sub-header {
    font-size: 1.2rem;
    color: #666;
    margin-bottom: 2rem;
}
.feature-box {
    padding: 1rem;
    border-radius: 0.5rem;
    background-color: #f0f2f6;
    margin: 0.5rem 0;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">📚 Study Companion</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">AI-Powered Educational Material Generator</div>', unsafe_allow_html=True)

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    st.markdown("### 📖 Study Topic")
    topic = st.text_area(
        "Enter your study topic",
        value="Introduction to Python Programming",
        height=100,
        help="Be specific! E.g., 'Calculus: Derivatives and Integrals' or 'World War II: European Theater'"
    )
    
    st.markdown("### 🎯 Options")
    
    # Advanced options (collapsed by default)
    with st.expander("Advanced Settings"):
        include_examples = st.checkbox("Include Example Problems", value=True)
        include_quiz = st.checkbox("Include Practice Quiz", value=True)
        difficulty = st.select_slider(
            "Difficulty Level",
            options=["Beginner", "Intermediate", "Advanced"],
            value="Intermediate"
        )
    
    st.markdown("---")
    
    generate_button = st.button("🚀 Generate Study Pack", type="primary", use_container_width=True)
    
    st.markdown("---")
    st.caption("💡 **Tip**: The more specific your topic, the better the results!")
    
# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🌟 What You'll Get")
    
with col2:
    pass  # Empty column for spacing

# Feature boxes
feat_col1, feat_col2, feat_col3, feat_col4 = st.columns(4)

with feat_col1:
    st.markdown("""
    <div class="feature-box">
        <h4>📝 Study Notes</h4>
        <p>Clear, bullet-point summaries</p>
    </div>
    """, unsafe_allow_html=True)

with feat_col2:
    st.markdown("""
    <div class="feature-box">
        <h4>🔢 Solved Examples</h4>
        <p>Step-by-step solutions</p>
    </div>
    """, unsafe_allow_html=True)

with feat_col3:
    st.markdown("""
    <div class="feature-box">
        <h4>✅ Practice Quiz</h4>
        <p>MCQs + answer keys</p>
    </div>
    """, unsafe_allow_html=True)

with feat_col4:
    st.markdown("""
    <div class="feature-box">
        <h4>🎯 Learning Plan</h4>
        <p>Structured objectives</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Generation logic
if generate_button:
    if not topic.strip():
        st.error("⚠️ Please enter a study topic!")
    else:
        st.info(f"🤖 AI agents are creating your study pack for: **{topic}**")
        st.markdown("This may take 2-5 minutes depending on topic complexity...")
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Simulate progress
        status_text.text("📋 Study Manager: Planning learning objectives...")
        progress_bar.progress(25)
        
        try:
            status_text.text("📝 Notes Generator: Creating study notes...")
            progress_bar.progress(40)
            
            output = run_pipeline(topic)
            
            status_text.text("🔢 Example Solver: Solving practice problems...")
            progress_bar.progress(65)
            
            status_text.text("✅ Quiz Maker: Generating practice questions...")
            progress_bar.progress(85)
            
            status_text.text("✨ Finalizing your study pack...")
            progress_bar.progress(100)
            
            st.success("🎉 Your study pack is ready!")
            
            # Display output
            st.markdown("---")
            st.markdown("### 📚 Your Complete Study Pack")
            
            # Add download button
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"study_pack_{topic[:30].replace(' ', '_')}_{timestamp}.md"
            
            st.download_button(
                label="📥 Download Study Pack",
                data=output,
                file_name=filename,
                mime="text/markdown",
                use_container_width=True
            )
            
            st.markdown("---")
            
            # Display the content in an expandable section
            with st.expander("📖 View Study Pack Content", expanded=True):
                st.markdown(output)
            
        except Exception as exc:
            progress_bar.empty()
            status_text.empty()
            st.error(f"❌ Error generating study pack: {exc}")
            st.markdown("""
            **Troubleshooting:**
            - Check your OpenRouter API key in `.env`
            - Ensure vector store is built: `python rag\\build_vector_db.py`
            - Verify internet connection
            - Try a simpler topic
            """)

# Footer
st.markdown("---")
col_f1, col_f2, col_f3 = st.columns(3)

with col_f1:
    st.markdown("**📚 Example Topics:**")
    if st.button("📐 Trigonometry Basics"):
        st.session_state.topic = "Trigonometry: Sine, Cosine, and Tangent"
        st.rerun()

with col_f2:
    st.markdown("**💻 Programming:**")
    if st.button("🐍 Python Data Structures"):
        st.session_state.topic = "Python: Lists, Dictionaries, and Sets"
        st.rerun()

with col_f3:
    st.markdown("**🔬 Science:**")
    if st.button("⚛️ Atomic Structure"):
        st.session_state.topic = "Chemistry: Atomic Structure and Periodic Table"
        st.rerun()

st.markdown("---")
st.caption(
    "Built with ❤️ using CrewAI | Powered by OpenRouter | "
    "💡 Customize agents in `agents/` directory"
)
