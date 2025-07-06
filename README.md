# Autism Detection App - Flask + Google Cloud Run

This repository contains a deployed machine learning web application for screening Autism Spectrum Disorder (ASD) traits based on user input.

## Features

- Flask-based web interface for user input
- Machine learning model trained and serialized using "joblib"
- Dockerized and deployed on Google Cloud Run
- Supports both web interface and **REST API** endpoint ("/predict")

## Project Structure

autism-flask-app/
├── app.py
├── autism_model.pkl
├── templates/
│ └── index.html
├── Dockerfile
├── .dockerignore
├── Deployment_Report.pdf


## [Open Deployed App on Google Cloud Run](https://autism-flask-app-351118108840.europe-west1.run.app)

## Deployment Report

All steps (auth, Docker, deployment, logs, result) are documented in ["Deployment_Report.pdf"](Deployment_Report.pdf)

## Author

Ruslan Kurmashev  
Internship Week 5 – Data Science  
Submitted on: July 6, 2025
