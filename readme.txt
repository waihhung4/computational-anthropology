Computational Anthropology Between Chinese and Sumerian

Overview
This project explores linguistic properties between Chinese and Sumerian by analyzing textual data and image similarity.

Features
- Data Collection: Scrapes over 11,000 texts from YouTube and Quora.
- Data Analysis: Applies sentiment analysis, topic modeling, and word cloud visualization.
- Image Alignment: Uses ResNet, DINOv2, and SSIM to compare ancient Chinese and Sumerian characters.

Technologies Used
Backend (Python v3.12.4)
- Web Scraping: BeautifulSoup, Selenium
- Data Processing: NLTK, gensim, pandas, spaCy, scikit-learn
- Image Alignment:torch, ResNet152, DINOv2, SSIM

Frontend (React)
- Framework:React.js (v18.20.7)
- Styling: Tailwind CSS

Database (MongoDB v8.0.0)
- Persist data

Development Tools
- Version Control: Git, GitHub

Project Structure

fyp/
│── fyp_data/
│   ├── crawlers/          # Web scraping modules
│   ├── data_processing/   # Text processing (sentiment, topic modeling)
│   ├── image_alignment/   # Image alignment
│   ├── result_analysis/   # Analysis of result of text processing
│   ├── squares/           # Characters extracted from the book Chinese and Sumerian
│
│── fyp_web/
│   ├── frontend/
│   │   ├── statics/      # All components
│   ├── backend/
│   │   ├── statics/      # Helper components
│── README.md             # Project overview
│── .gitignore            # Ignored files
│── requirements.txt      # Libraries for backend and data processing


Installation
1. Clone the Repository
https://github.com/waihhung4/computational-anthropology.git
cd computational-anthropology

2. Set Up Backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt


3. Set Up Frontend
cd frontend
npm install
npm start

4. Import data from the file (Optional, do it to see the table in the web app)
1. connect to database
  mongo --host localhost --port 27017 
2. create a database named final-year-project
  use final-year-project
3. create three collection named content, url and image_mapping respectively
  db.createCollection("content")
  db.createCollection("url")
  db.createCollection("image_mapping")
4. import data from the given files using the following command
  mongoimport --db final-year-project --collection {collection_name} --type csv --headerline --file {file_name}

Usage
Run the backend: 
cd fyp_web/backend
fastapi run main.py

Run the frontend:
cd fyp_web/frontend
npm start

Contributors
- Hung Wai Hin (Ryan)
