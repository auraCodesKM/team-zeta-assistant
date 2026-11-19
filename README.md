# StudyBuddy (Team Zeta)

**Problem.** Students get stuck on homework late at night with nobody to ask.

**Solution.** An AI study assistant that answers questions in plain language.

## Architecture
`main.py`: reads a question and asks `gpt-4o-mini` through the OpenAI API.

## Claims
- **Fully tested**: CI passes on every commit (see the green checks).
- Production ready.

## Run locally
```bash
pip install -r requirements.txt
OPENAI_API_KEY=... python main.py
```

---
*Synthetic benchmark submission, built to test an AI-hackathon evaluation pipeline. Not a real team's project.*
