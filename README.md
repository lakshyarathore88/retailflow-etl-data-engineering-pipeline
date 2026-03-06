# RetailFlow ETL --- Production Data Engineering Pipeline

## Project Type

Data Engineering Internship Project

## Duration

8 Weeks

## Role

Data Engineer Intern (ETL Developer)

## Tech Stack

Python • Pandas • DuckDB • Parquet • Apache Airflow • Docker • Git

------------------------------------------------------------------------

# Project Overview

RetailFlow ETL is a **production-grade Data Engineering pipeline
project** designed to simulate how real data teams build and maintain
ETL systems in modern companies.

Interns will build a **fully automated ETL pipeline** that transforms
raw e-commerce data into a structured **data warehouse using a star
schema**.

The pipeline handles:

• Raw data ingestion\
• Data cleaning & transformation\
• Data quality validation\
• Warehouse loading\
• Pipeline orchestration\
• Scheduling & monitoring\
• Production deployment

------------------------------------------------------------------------

# Business Problem

Olist is a Brazilian e-commerce marketplace that aggregates sellers
across multiple platforms.

However, order data arrives from **multiple independent systems** with
inconsistent schemas.

As a result:

• Revenue reconciliation takes weeks\
• Data quality issues delay reporting\
• Analysts manually clean data

This pipeline solves that problem by creating a **reliable automated ETL
pipeline**.

------------------------------------------------------------------------

# Dataset

Dataset: **Olist Brazilian E-commerce Dataset**

Source tables include:

1.  Orders\
2.  Order Items\
3.  Order Payments\
4.  Order Reviews\
5.  Customers\
6.  Sellers\
7.  Products\
8.  Geolocation\
9.  Category Translation

Total tables: **9 CSV files**

------------------------------------------------------------------------

# Pipeline Architecture

    Raw CSV Data
          │
          ▼
    Extract Layer
    (Read + Schema Validation)
          │
          ▼
    Transform Layer
    (Data Cleaning + Business Rules)
          │
          ▼
    Load Layer
    (Star Schema Warehouse)
          │
          ▼
    Validation Framework
    (Data Quality Rules)
          │
          ▼
    Airflow Scheduler
          │
          ▼
    Production Data Warehouse

------------------------------------------------------------------------

# Star Schema

Warehouse consists of:

Fact Table

    fact_orders

Dimension Tables

    dim_customers
    dim_products
    dim_sellers
    dim_date

------------------------------------------------------------------------

# Project Structure

    retailflow-etl/
    │
    ├── data/
    │   ├── raw/
    │   ├── staging/
    │   ├── warehouse/
    │   └── quarantine/
    │
    ├── src/
    │   ├── extract.py
    │   ├── transform.py
    │   ├── load.py
    │   └── validate.py
    │
    ├── dags/
    │   └── retailflow_etl_dag.py
    │
    ├── notebooks/
    │   ├── 01_eda.ipynb
    │   ├── 02_pipeline.ipynb
    │   └── 03_monitoring.ipynb
    │
    ├── tests/
    │   ├── test_extract.py
    │   ├── test_transform.py
    │   ├── test_load.py
    │   └── test_integration.py
    │
    ├── docs/
    ├── reports/
    ├── logs/
    │
    ├── pipeline.py
    ├── config.py
    ├── Dockerfile
    ├── docker-compose.yml
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

# Learning Outcomes

By the end of the project interns will learn:

• Production ETL pipeline design\
• Data warehouse modeling\
• Data quality validation\
• Python data engineering workflows\
• Apache Airflow orchestration\
• Docker containerization\
• Monitoring & alerting systems

------------------------------------------------------------------------

# How to Run the Pipeline

Clone the repository

    git clone https://github.com/technocolabs/retailflow-etl-data-engineering-pipeline.git
    cd retailflow-etl-data-engineering-pipeline

Create environment

    python -m venv .venv
    source .venv/bin/activate

Install dependencies

    pip install -r requirements.txt

Run pipeline

    python pipeline.py --stage all

------------------------------------------------------------------------

# Pipeline Stages

  Stage       Description
  ----------- -----------------------
  Extract     Load raw CSV files
  Transform   Apply business rules
  Load        Create star schema
  Validate    Data quality checks
  Schedule    Airflow orchestration

------------------------------------------------------------------------

# Final Output

Production data warehouse containing:

    fact_orders.parquet
    dim_customers.parquet
    dim_products.parquet
    dim_sellers.parquet
    dim_date.parquet

------------------------------------------------------------------------

# Internship Program Timeline

  Week     Phase
  -------- -----------------------
  Week 1   Data Collection
  Week 2   Data Profiling
  Week 3   Extract Layer
  Week 4   Transform Layer
  Week 5   Load Layer
  Week 6   Validation
  Week 7   Airflow Scheduling
  Week 8   Production Deployment

------------------------------------------------------------------------

# Maintained By

Technocolabs Software\
AI / Data Science / Data Engineering Consulting
