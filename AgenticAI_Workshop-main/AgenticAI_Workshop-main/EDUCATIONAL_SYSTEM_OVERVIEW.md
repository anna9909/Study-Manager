# Educational Workflow System - Overview

This system has been transformed from a generic workshop pipeline into a streamlined **Educational Workflow System** designed to automatically create comprehensive study materials using a single powerful agent.

## System Architecture

### Single Comprehensive Agent

### Single Comprehensive Agent

#### **Study Manager Agent** (`agents/planner.py`)
- **Purpose**: Creates complete study packs with all educational materials
- **Output**: Comprehensive study pack including notes, examples, quizzes, and mind maps
- **Capabilities**:
  - Generates easy-to-understand bullet-point notes and summaries
  - Solves 3-5 example problems with detailed step-by-step solutions
  - Creates practice quizzes (10 MCQs + 5 short answers with answer keys)
  - Designs mind maps showing concept relationships
  - Defines learning objectives and study plans

## Workflow Process

The Study Manager agent handles everything in a single comprehensive task:

1. **Study Pack Creation** - Creates all materials:
   - Study notes with bullet points and summaries
   - 3-5 solved example problems with explanations
   - Practice quiz with 10 MCQs and 5 short answer questions
   - Comprehensive answer key with explanations
   - Mind map showing concept hierarchies and relationships
   - Learning objectives and study recommendations

## Modified Files

### Core Files
- `agents/planner.py` - Study Manager Agent (comprehensive)
- `agents/__init__.py` - Exports Study Manager
- `tasks.py` - Single comprehensive task
- `crew.py` - Single-agent crew setup
- `main.py` - Educational pipeline runner

### Removed Files
- ~~`agents/researcher.py`~~ - Functionality integrated into Study Manager
- ~~`agents/writer.py`~~ - Functionality integrated into Study Manager
- ~~`agents/reviewer.py`~~ - Functionality integrated into Study Manager
- ~~`agents/mind_map_agent.py`~~ - Functionality integrated into Study Manager

## How to Use

### Basic Usage

```bash
python main.py --topic "Your Study Topic Here"
```

### Example

```bash
python main.py --topic "Introduction to Python Programming"
```

This will generate:
- Comprehensive study notes
- 3-5 solved example problems
- A practice quiz (10 MCQs + 5 short answers with answer key)
- A mind map showing concept relationships
- A final integrated study pack combining all materials

## Key Features

✅ **Single Agent Simplicity** - One powerful agent handles all tasks efficiently
✅ **Comprehensive Study Packs** - Complete materials in one execution
✅ **All-in-One Solution** - Notes, examples, quizzes, and visual aids
✅ **Step-by-Step Solutions** - Detailed problem-solving with explanations
✅ **Assessment Tools** - Practice questions testing various cognitive levels
✅ **Visual Learning** - Mind maps and concept diagrams included
✅ **Tool Integration** - Uses RAG, web search, and calculator tools
✅ **Clean & Maintainable** - Simple architecture, easy to understand and modify

## Agent Capabilities

The Study Manager has access to:
- **RAG Tool** - Retrieval from knowledge base
- **Web Search Tool** - Live information gathering
- **Calculator Tool** - Numerical computations

## Output Structure

The final study pack includes:

```
📚 FINAL STUDY PACK
├── 📋 Study Plan & Learning Objectives
├── 📝 Comprehensive Study Notes
│   ├── Bullet-point format
│   ├── Clear definitions
│   └── Concise summaries
├── 🔢 Solved Example Problems (3-5)
│   ├── Problem statements
│   ├── Step-by-step solutions
│   └── Reasoning explanations
├── ✅ Practice Quiz
│   ├── 10 Multiple Choice Questions
│   ├── 5 Short Answer Questions
│   └── Detailed Answer Key
└── 🗺️ Mind Map / Concept Diagram
    ├── Hierarchical structure
    ├── Concept relationships
    └── Visual layout
```

## Dependencies

Ensure the following are installed (see `requirements.txt`):
- crewai
- python-dotenv
- Other dependencies as listed in requirements.txt

## Configuration

Make sure to configure:
1. Environment variables (`.env` file)
2. LLM settings in `config/settings.py`
3. Logging configuration in `config/logging_config.py`

## Future Enhancements

Potential improvements:
- Generate actual visual images for mind maps
- Add flashcard generation
- Include video transcript analysis
- Support multiple difficulty levels
- Export to various formats (PDF, HTML, etc.)
- Add multiple specialized agents for larger projects (if needed)
