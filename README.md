# ClarifyMeet AI 🤖

> Transform meeting conversations into actionable insights using AI

ClarifyMeet AI is an intelligent meeting minutes generation tool that automatically extracts structured information from meeting transcripts using **LangGraph** and **Ollama**. Simply upload a text transcript, and AI will extract summaries, action items, decisions, risks, and speaker insights!

![Status](https://img.shields.io/badge/status-ready-green)
![Python](https://img.shields.io/badge/python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-FF4B4B)
![LangGraph](https://img.shields.io/badge/LangGraph-0.0.20-green)

## 🎯 What Does This App Do?

**Input:** A meeting transcript in plain text format  
**Output:** Structured meeting minutes with:
- 📋 **Executive Summary** - Key highlights from the meeting
- ✅ **Action Items** - Tasks with owners, due dates, and priorities
- 💡 **Decisions** - Important decisions made during the meeting
- ⚠️ **Risks & Concerns** - Potential issues identified
- 👥 **Speaker Analysis** - Who said what and their roles

## 📊 How It Works

```mermaid
flowchart LR
    AKey Features

- 📤 **Simple Upload**: Upload `.txt` transcript files with one click
- 🤖 **AI-Powered**: Uses LangGraph + Ollama (TinyLlama) for intelligent analysis
- 📋 **Structured Output**: Automatically extracts 5 key components
- 🎯 **Smart Detection**: Finds task owners, due dates, and priorities automatically
- 💻 **Beautiful UI**: Clean, modern Streamlit interface
- ⚡ **100% Local**: All processing happens on your machine (no cloud APIs needed!)
- 🚀 **Easy Deployment**: Deploy to Streamlit Cloud in minutes
- 📥 **Export Ready**: Download results as JSONfor intelligent parsing
- 📋 **Structured Output**: Extracts Summary, Action Items, Decisions, Risks, and Speakers
- 🎯 **Smart Inference**: Automatically identifies task owners, due dates, and priorities
- 💬 **ChatGPT-like UI**: Modern, responsive interface with dark theme
- 🔄 **In-Session Management**: Edit and manage action items in real-time
- 📊 **Confidence Scoring**: AI confidence levels for extracted information
- ⚡ **Fast & Local**: All processing happens locally with no external API calls
- 🐳 **Docker Ready**: Single-command deployment with Docker Compose

## 🚀 Quick Start
 (3 Steps!)

### Step 1: Install Ollama

Ollama runs the AI model locally on your computer.

```bash
# Download and install from: https://ollama.ai/download
# Then download the TinyLlama model (small and fast)
ollama pull tinyllama
```

### Step 2: Install Dependencies

```bash
# Navigate to project folder
cd Clarify_Meet_AI

# Install Python packages
pip install -r requirements.txt
```

### Step 3: Run the App!

```bash
# Start Streamlit
streamlit run streamlit_app.py
```

That's it! Open your browser to **http://localhost:8501** 🎉

## 📖 Complete Setup Guides

- **[Quick Start Guide](docs/QUICKSTART_STREAMLIT.md)** - Beginner-friendly step-by-step
- **[Streamlit Cloud Deployment](docs/STREAMLIT_DEPLOYMENT.md)** - Deploy to the cloud
- **[Deployment Checklist](docs/DEPLOYMENT_CHECKLIST.md)** - Pre-deployment verification
- **[Testing Guide](docs/TESTING.md)** - Verify your setup

## 🐳 Alternative: Docker Deployment

For production or API access, use Docker:

```bash
cd extras/docker
docker-compose up --build
```

Access at: http://localhost:8000 (includes REST API)

📖 See [extras/docker/SETUP.md](extras/docker/SETUP.md) for details
## 📁 Project Structure

```
ClarifyMeetAI/
├── streamlit_app.py         # 🆕 Streamlit application (new!)
├── backend/                  # FastAPI Backend
│   ├── main.py              # Application entry point
│   ├── app/                 # Main application code
│   │   ├── main.py          # FastAPI routes
│   │   ├── config.py        # Configuration
│   │   ├── langgraph_agent.py  # LangGraph agent
│   │   ├── schemas.py       # Pydantic models
│   │   └── services/        # Business logic
│   ├── agent/               # Legacy agent code
│   ├── models/              # Data models
### 🎯 Main Files (What You Need)

```
Clarify_Meet_AI/
├── streamlit_app.py          # ⭐ Main Streamlit application
├── requirements.txt          # Python dependencies
├── packages.txt              # System packages (for cloud deployment)
├── .streamlit/
│   ├── config.toml          # Theme and UI settings
│   └── secrets.toml         # API keys (not committed to git)
├── backend/                  # AI Processing Engine
│   ├── app/
│   │   ├── langgraph_agent.py  # 🤖 Main AI agent logic
│   │   ├── config.py        # Configuration settings
│   │   └── services/        # Text processing utilities
│   ├── models/              # Data models
│   └── utils/               # Helper functions
└── docs/                     # 📚 Documentation
    ├── QUICKSTART_STREAMLIT.md
    ├── STREAMLIT_DEPLOYMENT.md
    ├── DEPLOYMENT_CHECKLIST.md
    └── TESTING.md
```

### 📦 Extras (Optional)

```
extras/
├── docker/                   # Docker deployment files
│   ├── docker-compose.yaml
│   ├─How to Use (Step-by-Step)

### Step 1: Prepare Your Transcript

Create a `.txt` file with speaker labels:

```text
John: Good morning everyone. Let's start our sprint planning.

Sarah: I'll work on the login page redesign. I can finish it by Friday.

Mike: I'll handle the backend API for authentication. Due date is next Monday.

John: Decision: We will use JWT tokens for authentication.

Sarah: One risk - the design needs approval from stakeholders first.
```

**💡 Tips for better results:**
- Use clear speaker labels (e.g., "John:", "Sarah:")
- Mention dates explicitly ("by Friday", "next Monday")
- Include "I will" statements for action owners
- Mark decisions clearly ("Decision:", "We decided")
- Note risks ("Risk:", "Concern:", "Issue:")

### Step 2: Upload to the  Purpose |
|-----------|-----------|---------|
| **Frontend** | Streamlit 1.31.0 | Beautiful web interface |
| **AI Framework** | LangGraph 0.0.20 | Orchestrates AI workflow |
| **LLM** | Ollama + TinyLlama | Local AI model (no API costs!) |
| **Language** | Python 3.11+ | Backend processing |
| **Deployment** | Streamlit Cloud / Docker | Easy cloud hosting |

### Why These Technologies?
 (Output Details)

### 📋 Executive Summary
- 3-5 bullet points covering meeting highlights
- AI-generated from full transcript context
- Easy to share with stakeholders

### ✅ Action Items
Each action includes:
- **Description** - What needs to be done
- **Owner** - Who's responsible (auto-detected from "I'll" statements)
- **Due Date** - Converts "tomorrow", "Friday", "next week" to actual dates
- **Priority** - High/Medium/Low based on urgency keywords
- **Status** - Pending (default)

**Example:**
```json
{
  "description": "Work on login page redesign",
  "owner": "Sarah",
  "due_date": "2026-01-17",
  "priority": "Medium",
  "status": "Pending"
}
```

### 💡 Decisions
- **Decision** - What was decided
- **Rationale** - Why it was decided
- **Owner** - Who made the decision
- *🌟 Example Use Cases

### For Team Meetings
- Sprint planning sessions
- Retrospectives
- Daily standups
- Design reviews
- Architecture discussions

### For Client Meetings
- Requirements gathering
- Status updates
- Stakeholder reviews
- Decision-making sessions

### For Project Management
- Automatically track action items
- Generate meeting summaries
- Identify risks early
- Monitor decision history Action Items
- **Description**: What needs to be done
- **Owner**: Who is responsible (auto-inferred from "I'll" statements)
- **Due Date**: When it's due (converts relative dates like "tomorrow")
- **Priority**: LOW, MEDIUM, or HIGH
- **Status**: PENDING, IN_PROGRESS, DONE, CANCELLED
- **Confidence**: AI confidence level (LOW, MEDIUM, HIGH)

### Decisions
- **Description**: What was decided
- **Source**: Original utterance from transcript

### Risks & Open Questions
- **Type**: RISK or OPEN_QUESTION
- **Description**: The risk or question identified
- **Source**: Original utterance from transcript

### Speakers
- **Name**: Speaker name
- **Role**: Auto-inferred from context (Developer, QA, PM, etc.)
- **AcCommon Issues & Solutions

### ❌ "Connection refused" or "Ollama not accessible"

**Problem:** Ollama isn't running  
**Solution:**
```bash
# Check if Ollama is running
curl http://localhost:11434/api/tags

# If not, start it (it usually auto-starts)
# Windows: Check system tray for Ollama icon
# Mac/Linux: ollama serve
```

### ❌ "Model 'tinyllama' not found"

**Problem:** Model not downloaded  
**Solution:**
```bash
ollama pull tinyllama
ollama list  # Verify it's there
```

### ❌ "Module not found: streamlit"

**Problem:** Dependencies not installed  
**Solution:**
```bash
pip install -r requirements.txt
```

### � Privacy & Security

✅ **100% Local Processing** - Your data never leaves your computer  
✅ **No Cloud APIs** - No data sent to OpenAI, Google, etc.  
✅ **No Storage** - Transcripts processed in-memory only  
✅ **Open Source** - Review all code yourself  

**Note:** For production use, consider adding:
- User authentication
- Access control
- HTTPS/SSL
- Data encryption

## 🎨 Customization Options

### Change the AI Model

Edit `backend/app/config.py`:
```python
OLLAMA_MODEL: str = "llama2"  # or mistral, codellama, etc.
```

Then download the model:
```bash
ollama pull llama2
```

### Modify UI Theme

Edit `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#FF4B4B"  # Change accent color
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
```

### Adjust Extraction Logic

Edit `backend/app/langgraph_agent.py` to customize:
- Prompt templates
- Extraction rules
- Validation logic
- Output format

## 🚧 Roadmap & Future Plans

- [ ] PDF/DOCX export
- [ ] Audio transcription support
- [ ] Multi-language support
- [ ] Calendar integration (Google Calendar, Outlook)
- [ ] Email notifications for action items
- [ ] Persistent storage option
- [ ] User authentication
We welcome contributions! Here's how:

1. **Fork** this repository
2. **Create** a feature branch: `git checkout -b feature/my-feature`
3. **Make** your changes
4. **Test** thoroughly
5. **Commit**: `git commit -m 'Add my feature'`
6. **Push**: `git push origin feature/my-feature`
7. **Open** a Pull Request

### Ideas for Contributions

- Add new extraction features
- Improve AI prompts
- Enhance UI/UX
- Add more language support
- Write more tests
- Improve documentation

## 📝 What We Built - Complete Overview

This project transforms raw meeting transcripts into actionable insights using:

### Architecture
1. **Frontend** - Streamlit web interface (Python-based)
2. **Backend** - LangGraph agent workflow engine
3. **AI Engine** - Ollama running TinyLlama locally
4. **Processing Pipeline**:
   - Text cleaning & normalization
   - Speaker identification
   - Context understanding via LLM
   - Information extraction (actions, decisions, risks)
   - Validation & warning generation
   - JSON output formatting

### Key Innovations
- ✅ 100% local processing (no cloud dependencies)
- ✅ Smart date conversion ("tomorrow" → "2026-01-14")
- ✅ Automatic owner assignment from "I'll" statements
- ✅ Priority detection from urgency keywords
- ✅ Role inference (PM, Developer, QA, Designer)
- ✅ Confidence scoring for reliability
- ✅ Fallback parser if LLM fails

### Deployment Options
1. **Local** - Run on your laptop with Streamlit
2. **Cloud** - Deploy to Streamlit Cloud (free tier available)
3. **Docker** - Containerized deployment for production
4. **API Mode** - Use FastAPI backend (in extras/)

## 📚 Documentation

- **[Quick Start](docs/QUICKSTART_STREAMLIT.md)** - Get started in 5 minutes
- **[Deployment Guide](docs/STREAMLIT_DEPLOYMENT.md)** - Deploy to cloud
- **[Testing Guide](docs/TESTING.md)** - Verify your setup
- **[Migration Summary](docs/MIGRATION_SUMMARY.md)** - What we changed
- **[Deployment Checklist](docs/DEPLOYMENT_CHECKLIST.md)** - Pre-launch checklist

## 🙏 Acknowledgments

Built with amazing open-source technologies:

- **[Ollama](https://ollama.ai)** - Local LLM runtime
- **[LangGraph](https://github.com/langchain-ai/langgraph)** - AI workflow orchestration
- **[Streamlit](https://streamlit.io)** - Beautiful Python web apps
- **[TinyLlama](https://github.com/jzhang38/TinyLlama)** - Efficient language model
- **[LangChain](https://www.langchain.com)** - LLM framework

## 📞 Support & Questions

- 📖 **Documentation**: Check [docs/](docs/) folder
- 🐛 **Bug Reports**: Open a GitHub issue
- 💡 **Feature Requests**: Open a GitHub discussion
- ❓ **Questions**: See [docs/TESTING.md](docs/TESTING.md)

## 📄 License

This project is open source and available for educational purposes.

---

**Built with ❤️ using AI, LangGraph, and Streamlit**

**Status**: ✅ Production-ready | **Last Updated**: January 2026

**Made by**: GenAI Enthusiasts 🚀
### Modify Extraction Prompts

Edit `backend/agent/prompts.py` to customize how the AI extracts information:

```python
def build_minutes_prompt(transcript, speakers, meeting_date, meeting_title):
    # Customize the prompt template here
    prompt = f"""Your custom instructions..."""
    return prompt
```

### Change LLM Model

In `docker-compose.yml`:
```yaml
environment:
  - OLLAMA_MODEL=llama2  # Or any other Ollama model
```

### Adjust UI Theme

Edit `frontend/style.css` to change colors and styling:
```css
:root {
    --bg-primary: #0f172a;    /* Dark background */
    --accent-primary: #3b82f6; /* Blue accent */
    /* ... more variables ... */
}
```

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is provided as-is for educational and demonstration purposes.

## 🙏 Acknowledgments

- **Ollama** for local LLM inference
- **LangChain/LangGraph** for agent orchestration
- **FastAPI** for the modern Python web framework
- **TinyLlama** for the efficient language model

## 📞 Support

For issues, questions, or suggestions:

1. Check the [SETUP.md](SETUP.md) for detailed instructions
2. Review the [Troubleshooting](SETUP.md#troubleshooting) section
3. Open an issue on GitHub (if applicable)

---

**Built with ❤️ using LangGraph, Ollama, and FastAPI**

**Status**: Production-ready ✅ | Last Updated: December 2025
