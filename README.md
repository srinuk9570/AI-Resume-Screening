# AI Resume Screening System

This project is an AI-powered Resume Screening System that automatically evaluates candidate resumes against job descriptions using Natural Language Processing (NLP) techniques. The system extracts skills from resumes and ranks candidates based on semantic similarity with job requirements.

## Features

- Resume parsing using NLP
- Skill extraction from resumes
- Semantic similarity matching
- Ranking candidates based on job requirements
- Web-based dashboard interface

## Tech Stack

- Python (NLP processing)
- Node.js (Backend API)
- Angular (Frontend dashboard)
- Machine Learning (TF-IDF similarity scoring)

## Project Structure

backend/ – API services  
web/ – Frontend interface  
nlp/ – Resume parsing & similarity engine  

## System Architecture

The system follows a modular pipeline:

1. Resume input (PDF format)
2. Text extraction and preprocessing
3. Feature vector generation using NLP techniques
4. Semantic similarity computation with job descriptions
5. Candidate ranking displayed through dashboard interface

## Project Highlights

- Designed an NLP pipeline for automated resume-job matching
- Implemented semantic similarity scoring using TF-IDF embeddings
- Built a full-stack system integrating Python, Node.js, and Angular
- Developed candidate ranking logic for intelligent hiring support

## Future Improvements

- Transformer-based embeddings (BERT / SBERT)
- Real-time resume ranking API
- Deployment using Docker / AWS