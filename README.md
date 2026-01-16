# Local-Ai-Agent-Using-Rag
This is a Python project I built to learn how AI agents work. It takes a CSV file of restaurant reviews, "reads" them, and answers any questions you have about the food, service, or atmosphere.

It uses RAG (Retrieval Augmented Generation), which basically means it looks up the relevant info in a database before answering, so it doesn't make things up.

How It Works
The Brain: Uses Google's Gemini Flash model (it's fast and free) to generate answers.

The Memory: Uses ChromaDB to store the reviews as numbers (vectors) so the AI can search them instantly.

The Glue: Uses LangChain to connect the database to the AI.

Tech Stack
Language: Python

LLM: Google Gemini (gemini-flash-latest)

Embeddings: Google Text Embeddings (models/text-embedding-004)

Database: ChromaDB (Runs locally, no setup needed)

Framework: LangChain
I have given every file in the github repo for everyone to check out.Happy Learning!
