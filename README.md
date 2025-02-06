# 📊 Data Science Job Market Insights Dashboard
<img width="1408" alt="Screenshot 2025-02-06 at 16 47 37" src="https://github.com/user-attachments/assets/8eb9c5e2-1a90-4e5c-9d1b-05c44eb1e159" />

This **Streamlit-based dashboard** provides real-time insights into the most in-demand data science skills by analyzing job postings. 

## 🚀 Pipeline Overview
1. **Data Collection**  
   - Scrapes job postings from **[Djinni.co](https://djinni.co/)**  
   - Supports **manual vacancy uploads** to Google Drive  

2. **Data Processing**  
   - Merges scraped and manually uploaded job data  
   - Aggregates skills and technologies mentioned in listings  

3. **LLM-Powered Analysis**  
   - Uses **OpenAI API** to extract key trends  
   - Generates structured insights on required skills  

4. **Storage & Access**  
   - Saves processed datasets to Google Drive.

5. **Visualization**  
   - **Streamlit app** dynamically updates with the latest insights  
   - Displays **charts, plots, and tables**  

## 📊 Dashboard Features
✅ **Hard & Soft Skills Analysis** – Identifies key technical & interpersonal skills  
✅ **Education vs. Experience** – Tracks job postings requiring degrees vs. hands-on experience  
✅ **Technology Popularity** – Highlights the top 20 most in-demand tools  
✅ **Job Title Trends** – Shows the most widespread data roles  

## 🛠 Tech Stack
- **Python** (Pandas, NumPy)  
- **Streamlit** (UI & Visualization)  
- **Matplotlib, Altair, Plotly** (Charts & Graphs)  
- **OpenAI API** (LLM-driven insights)  

📌 *Data source: scraped job listings from [Djinni.co](https://djinni.co/)*  
