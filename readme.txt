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


Usage
Run the backend: 
cd fyp_web/backend
fastapi run main.py

Run the frontend:
cd fyp_web/frontend
npm start

Contributors
- Hung Wai Hin (Ryan)
