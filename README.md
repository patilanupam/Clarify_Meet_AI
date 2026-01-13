# ClarifyMeet AI 🤖: https://clarifymeetai-btra6m4p2msf5es6z9rdnc.streamlit.app/

> Transform meeting conversations into actionable insights using AI

ClarifyMeet AI is an intelligent meeting minutes generation tool that automatically extracts structured information from meeting transcripts using **LangGraph** and **Ollama**. Simply upload a text transcript, and AI will extract summaries, action items, decisions, risks, and speaker insights!

![Status](https://img.shields.io/badge/status-ready-green)
![Python](https://img.shields.io/badge/python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-FF4B4B)
![LangGraph](https://img.shields.io/badge/LangGraph-0.0.20-green)

---

## 🎯 What Does This App Do?

**Input:** A meeting transcript in plain text format  
**Output:** Structured meeting minutes with:

- 📋 **Executive Summary** - Key highlights from the meeting
- ✅ **Action Items** - Tasks with owners, due dates, and priorities
- 💡 **Decisions** - Important decisions made during the meeting
- ⚠️ **Risks & Concerns** - Potential issues identified
- 👥 **Speaker Analysis** - Who said what and their roles

---

## 📊 How It Works

**Simple 6-step workflow:**

```
Upload → Clean Text → Parse Speakers → AI Analysis → Extract Info → Display Results
```

1. **Upload** - You provide a meeting transcript (.txt file)
2. **Clean** - Remove formatting issues and normalize text
3. **Parse** - Identify who said what
4. **Analyze** - AI reads and understands the context
5. **Extract** - Pull out actions, decisions, risks, speaker insights
6. **Display** - Show results in beautiful, organized tabs

---

## ✨ Key Features

- 📤 **Simple Upload** - Upload `.txt` transcript files with one click
- 🤖 **AI-Powered** - Uses LangGraph + Ollama (TinyLlama) for intelligent analysis
- 📋 **Structured Output** - Automatically extracts 5 key components
- 🎯 **Smart Detection** - Finds task owners, due dates, and priorities automatically
- 💻 **Beautiful UI** - Clean, modern Streamlit interface
- ⚡ **100% Local** - All processing happens on your machine (no cloud APIs!)
- 🚀 **Easy Deployment** - Deploy to Streamlit Cloud in minutes
- 📥 **Export Ready** - Download results as JSON

---

## 🚀 Quick Start (3 Steps!)

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

**That's it!** Open your browser to **http://localhost:8501** 🎉

---

## 📖 Complete Setup Guides

- **[Quick Start Guide](docs/QUICKSTART_STREAMLIT.md)** - Beginner-friendly step-by-step
- **[Streamlit Cloud Deployment](docs/STREAMLIT_DEPLOYMENT.md)** - Deploy to the cloud
- **[Deployment Checklist](docs/DEPLOYMENT_CHECKLIST.md)** - Pre-deployment verification
- **[Testing Guide](docs/TESTING.md)** - Verify your setup

---

## 📁 Project Structure

### 🎯 Essential Files (For Streamlit Deployment)

```
Clarify_Meet_AI/
│
├── streamlit_app.py              # ⭐ Main application file
├── requirements.txt              # Python dependencies
├── packages.txt                  # System dependencies
│
├── .streamlit/                   # Streamlit configuration
│   ├── config.toml              # UI theme and settings
│   └── secrets.toml             # API keys (DON'T commit!)
│
├── backend/                      # AI Processing Engine
│   ├── app/                     # Main logic
│   │   ├── langgraph_agent.py  # 🤖 Core AI agent
│   │   ├── config.py           # Settings
│   │   ├── schemas.py          # Data models
│   │   └── services/           # Utilities
│   │       ├── text_cleaner.py
│   │       ├── speaker_parser.py
│   │       └── fallback_parser.py
│   ├── models/                  # Pydantic models
│   └── utils/                   # Helpers
│
└── docs/                         # 📚 Documentation
    ├── QUICKSTART_STREAMLIT.md
    ├── STREAMLIT_DEPLOYMENT.md
    ├── DEPLOYMENT_CHECKLIST.md
    └── TESTING.md
```

### 📦 Optional Files (In `extras/` folder)

Not needed for Streamlit, but available for Docker or original setup:

```
extras/
├── docker/                       # Docker deployment
│   ├── docker-compose.yaml
│   ├── Dockerfile
│   └── SETUP.md
├── frontend/                     # Original HTML/CSS/JS UI
├── samples/                      # Example transcripts
└── scripts/                      # Helper scripts
```

---

## 💡 How to Use (Step-by-Step)

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
- Use clear speaker labels (e.g., `John:`, `Sarah:`)
- Mention dates explicitly ("by Friday", "next Monday")
- Include "I will" statements for task owners
- Mark decisions clearly ("Decision:", "We decided")
- Note risks ("Risk:", "Concern:", "Issue:")

### Step 2: Upload to the App

1. Open **http://localhost:8501**
2. Click "Choose a transcript file (.txt)"
3. Select your transcript
4. Click **"🚀 Analyze Transcript"**
5. Wait 30-60 seconds for AI processing

### Step 3: View Results

The app displays 6 tabs:

| Tab | What You Get |
|-----|--------------|
| 📋 **Summary** | Top 3-5 key points from the meeting |
| ✅ **Action Items** | Tasks with owner, due date, priority, status |
| 💡 **Decisions** | What was decided and why |
| ⚠️ **Risks** | Concerns with mitigation plans |
| 👥 **Speakers** | Who participated and contributions |
| 📊 **Metadata** | Processing details and warnings |

### Step 4: Download Results

Click **"📥 Download JSON Results"** to export everything!

---

## 🎯 What Gets Extracted (Output Details)

### 📋 Executive Summary
- 3-5 bullet points covering meeting highlights
- AI-generated from full transcript context

### ✅ Action Items
Each action includes:
- **Description** - What needs to be done
- **Owner** - Who's responsible (auto-detected)
- **Due Date** - Converts "tomorrow", "Friday" to actual dates
- **Priority** - High/Medium/Low
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
- **Context** - Background information

### ⚠️ Risks & Concerns
- **Risk** - The issue or concern
- **Impact** - High/Medium/Low severity
- **Mitigation** - How to address it
- **Owner** - Who's responsible

### 👥 Speaker Spotlight
- **Name** - Speaker's name
- **Role** - Auto-detected (PM, Developer, QA, Designer)
- **Contribution Count** - Number of times they spoke
- **Key Points** - Their main contributions

---

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Frontend** | Streamlit 1.31.0 | Beautiful web interface |
| **AI Framework** | LangGraph 0.0.20 | Orchestrates AI workflow |
| **LLM** | Ollama + TinyLlama | Local AI model (no API costs!) |
| **Language** | Python 3.11+ | Backend processing |
| **Deployment** | Streamlit Cloud | Easy cloud hosting |

### Why These Technologies?

- **Streamlit** - Makes Python apps look professional with minimal code
- **LangGraph** - Manages complex AI workflows (like an assembly line)
- **Ollama** - Runs AI models locally (fast, private, free)
- **TinyLlama** - Small but powerful (600MB, runs on laptop)

---

## 🧠 How the AI Works (Technical Overview)

```
1. Text Cleaning → Remove noise, fix formatting
2. Speaker Parsing → Identify who said what
3. LLM Analysis → AI reads and understands context
4. Information Extraction → Pull out key details
5. Validation → Check for missing info, add warnings
6. Structured Output → Return organized JSON
```

**Core Components:**

- `langgraph_agent.py` - Orchestrates the AI workflow
- `text_cleaner.py` - Cleans up transcript text
- `speaker_parser.py` - Identifies speakers
- `fallback_parser.py` - Backup if AI fails

---

## 🌟 Example Use Cases

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
- Monitor decision history

---

## 🐛 Common Issues & Solutions

### ❌ "Connection refused" or "Ollama not accessible"

**Problem:** Ollama isn't running  
**Solution:**
```bash
# Check if Ollama is running
curl http://localhost:11434/api/tags

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

### ❌ Processing takes too long

**Problem:** Large transcript or first run  
**Solutions:**
- First run is slower (model loading)
- Keep transcripts under 5000 words
- Close other applications

### ❌ Port 8501 already in use

**Solution:**
```bash
streamlit run streamlit_app.py --server.port 8502
```

📖 **More help:** [docs/TESTING.md](docs/TESTING.md)

---

## 🔒 Privacy & Security

✅ **100% Local Processing** - Data never leaves your computer  
✅ **No Cloud APIs** - No data sent to OpenAI, Google, etc.  
✅ **No Storage** - Transcripts processed in-memory only  
✅ **Open Source** - Review all code yourself  

**Note:** For production, consider adding authentication, HTTPS, and encryption.

---

## 🎨 Customization Options

### Change the AI Model

Edit `backend/app/config.py`:
```python
OLLAMA_MODEL: str = "llama2"  # or mistral, codellama
```

Then:
```bash
ollama pull llama2
```

### Modify UI Theme

Edit `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#FFFFFF"
```

### Adjust Extraction Logic

Edit `backend/app/langgraph_agent.py` to customize prompts and rules.

---

## 🚧 Roadmap & Future Plans

- [ ] PDF/DOCX export
- [ ] Audio transcription support
- [ ] Multi-language support
- [ ] Calendar integration (Google Calendar, Outlook)
- [ ] Email notifications for action items
- [ ] Persistent storage option
- [ ] User authentication
- [ ] Team collaboration features
- [ ] Advanced analytics dashboard

---

## 🐳 Alternative: Docker Deployment

For production or API access:

```bash
cd extras/docker
docker-compose up --build
```

Access at: **http://localhost:8000** (includes REST API)

📖 See [extras/docker/SETUP.md](extras/docker/SETUP.md) for details

---

## 🤝 Contributing

We welcome contributions!

1. **Fork** this repository
2. **Create** a feature branch: `git checkout -b feature/my-feature`
3. **Make** your changes
4. **Test** thoroughly
5. **Commit**: `git commit -m 'Add my feature'`
6. **Push**: `git push origin feature/my-feature`
7. **Open** a Pull Request

**Ideas:** Add features, improve prompts, enhance UI, add languages, write tests, improve docs

---

## 📝 What We Built - Complete Overview

This project transforms raw meeting transcripts into actionable insights.

### Architecture
1. **Frontend** - Streamlit web interface (Python-based)
2. **Backend** - LangGraph agent workflow engine
3. **AI Engine** - Ollama running TinyLlama locally
4. **Pipeline**: Clean text → Parse speakers → AI analysis → Extract info → Validate → Output JSON

### Key Innovations
- ✅ 100% local processing (no cloud)
- ✅ Smart date conversion ("tomorrow" → actual date)
- ✅ Automatic owner assignment from "I'll" statements
- ✅ Priority detection from urgency keywords
- ✅ Role inference (PM, Developer, QA, Designer)
- ✅ Confidence scoring
- ✅ Fallback parser if LLM fails

### Deployment Options
1. **Local** - Run on laptop with Streamlit
2. **Cloud** - Deploy to Streamlit Cloud (free tier)
3. **Docker** - Containerized for production
4. **API** - Use FastAPI backend (in extras/)

---

## 📚 Documentation

- **[Quick Start](docs/QUICKSTART_STREAMLIT.md)** - Get started in 5 minutes
- **[Deployment Guide](docs/STREAMLIT_DEPLOYMENT.md)** - Deploy to cloud
- **[Testing Guide](docs/TESTING.md)** - Verify your setup
- **[Migration Summary](docs/MIGRATION_SUMMARY.md)** - What we changed
- **[Deployment Checklist](docs/DEPLOYMENT_CHECKLIST.md)** - Pre-launch checklist

---

## 🙏 Acknowledgments

Built with amazing open-source technologies:

- **[Ollama](https://ollama.ai)** - Local LLM runtime
- **[LangGraph](https://github.com/langchain-ai/langgraph)** - AI workflow orchestration
- **[Streamlit](https://streamlit.io)** - Beautiful Python web apps
- **[TinyLlama](https://github.com/jzhang38/TinyLlama)** - Efficient language model
- **[LangChain](https://www.langchain.com)** - LLM framework

---

## 📞 Support & Questions

- 📖 **Documentation** - Check [docs/](docs/) folder
- 🐛 **Bug Reports** - Open a GitHub issue
- 💡 **Feature Requests** - Open a GitHub discussion
- ❓ **Questions** - See [docs/TESTING.md](docs/TESTING.md)

---

## 📄 License

This project is open source and available for educational purposes.

---

**Built with ❤️ using AI, LangGraph, and Streamlit**

**Status**: ✅ Production-ready | **Last Updated**: January 2026

**Repository**: [github.com/patilanupam/Clarify_Meet_AI](https://github.com/patilanupam/Clarify_Meet_AI)
