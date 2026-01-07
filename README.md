# From Video to Notes

 From Video to Notes
An AI-Powered Lecture Understanding System

This project builds a step-by-step pipeline that converts YouTube lecture videos into clean text and then into concise summaries, forming the foundation of an automated video-to-notes system.

The project is divided into milestones, each focusing on a core capability.

Project Milestones Covered

Milestone 1: YouTube Video → Clean Text (Transcript Extraction)

Milestone 2: Robust Text Summarization Engine (Hierarchical NLP)

Milestone 1 — YouTube Video to Text

Transcript Extraction & Preprocessing

Objective

Build a reliable and clean pipeline that converts a YouTube lecture video into readable text, which can later be used for summarization and note generation.

This milestone focuses only on:

Transcript extraction

Cleaning and preprocessing

No AI models
No summarization
No frontend

What This Milestone Does

Given a YouTube video URL, the system:

Extracts the video ID

Fetches the transcript using youtube-transcript-api

Handles:

Manual captions

Auto-generated captions

English language fallback

Cleans the transcript:

Removes timestamps

Merges text segments in correct order

Normalizes whitespace

Saves outputs in two formats

Folder Structure — Milestone 1
week_1_transcript_extraction/
│
├── transcript_extraction.py
├── transcript_extraction.ipynb
├── sample_video_url.txt
├── transcript_clean.txt
└── transcript_raw.json

Output Files

transcript_clean.txt
✔ Clean, readable text
✔ No timestamps
✔ Ready for NLP processing

transcript_raw.json
✔ Raw transcript data
✔ Preserves metadata

Technologies Used

Python 

youtube-transcript-api

Regular Expressions (re)

JSON handling

Milestone 1 Outcome

By the end of this milestone, the system can reliably convert YouTube lectures into clean text, forming a strong preprocessing foundation for NLP tasks.

Milestone 2 — Robust Text Summarization Engine

Hierarchical NLP Summarization

Objective

Implement a scalable and reliable text summarization pipeline capable of summarizing very long documents (10,000+ characters) while respecting transformer context limits.

Problem Statement

Most transformer-based summarization models (such as BART or T5) cannot process long documents directly due to token limits.

This milestone solves that problem using hierarchical summarization.

Core Approach (Hierarchical Summarization)

The pipeline follows these steps:

Split long text into overlapping chunks

Summarize each chunk independently

Merge intermediate summaries

Re-summarize merged text to produce a final coherent summary

This approach ensures:

Context preservation

Scalability

High-quality summaries

Folder Structure — Milestone 2
week_2_text_summarization/
│
├── summarization_pipeline.py
├── summarization.ipynb
├── sample_input.txt
├── intermediate_summaries.txt
└── final_summary.txt

Functional Components
🔹 Chunking Engine

Splits text into chunks of 800–1400 characters

Uses overlap (100–200 characters) to preserve context

🔹 Summarization Model

Hugging Face Transformers 

Model used: facebook/bart-large-cnn

🔹 Hierarchical Pipeline

Chunk-level summaries

Final second-level summary

 Output Files

intermediate_summaries.txt
Chunk-wise summaries
Helps analyze model behavior

final_summary.txt
Clean, concise final summary
Ready for note formatting

Technologies Used

Python 

Hugging Face transformers

PyTorch

NLP pipelines

Milestone 2 Outcome

By the end of this milestone, the system can reliably summarize long-form lecture transcripts, overcoming transformer limitations using a hierarchical NLP approach.

## Author
Ritesh Srivastava
