# Computational Anthropology Between Chinese and Sumerian

## Overview
This project explores linguistic properties between **Chinese and Sumerian** by analyzing **textual data, sentiment, and character similarity** using **AI-based models**. Inspired by the book *Chinese and Sumerian*, it incorporates **natural language processing (NLP), topic modeling, and AI-based image similarity analysis**.

## Features
- **Data Collection:** Scrapes over **11,000 texts** from **YouTube and Quora**.
- **Linguistic Analysis:** Applies **sentiment analysis, topic modeling, and word cloud visualization**.
- **AI-Based Character Similarity:** Uses **ResNet, DINOv2, and SSIM** to compare ancient Chinese and Sumerian characters.
- **Interactive Dashboard:** A visually structured homepage with data representations.

## Technologies Used
### **Backend (Python)**
- **Web Scraping:** `BeautifulSoup`, `Selenium`
- **Data Processing:** `pandas`, `NumPy`
- **NLP & Sentiment Analysis:** `spaCy`, `NLTK`, `TextBlob`
- **AI-based Similarity Analysis:** `torch`, `ResNet152`, `DINOv2`, `SSIM`

### **Frontend (React)**
- **Framework:** `React.js`, `Vite`
- **Data Visualization:** `D3.js`, `Recharts`
- **Styling:** `Tailwind CSS`

### **Development Tools**
- **Version Control:** `Git`, `GitHub`
- **Testing:** `pytest`, `Jest`
- **Deployment:** `Docker`, `GitHub Actions`

## Project Structure
```
computational-anthropology/
│── backend/
│   ├── scraper/          # Web scraping modules
│   ├── nlp/              # Text processing (sentiment, topic modeling)
│   ├── similarity/       # AI-based similarity calculations
│   ├── utils/            # Helper functions
│   ├── tests/            # Unit tests
│
│── frontend/
│   ├── src/
│   │   ├── components/   # Reusable UI components
│   │   ├── pages/        # Main views (Home, Analysis, Comparison)
│   │   ├── services/     # API calls to backend
│   │   ├── utils/        # Helper functions
│
│── docs/                 # Project documentation
│── README.md             # Project overview
│── .gitignore            # Ignored files
```

## Installation
### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/computational-anthropology.git
cd computational-anthropology
```

### **2. Set Up Backend**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # (or `venv\Scripts\activate` on Windows)
pip install -r requirements.txt
```

### **3. Set Up Frontend**
```bash
cd frontend
npm install
npm run dev
```

## Usage
- **Run the backend**: `python app.py`
- **Run the frontend**: `npm run dev`
- **Test the system**: `pytest` for Python tests, `npm test` for React tests.

## Git Workflow
### **Branching Strategy**
- `main` → Stable production-ready version
- `dev` → Active development branch
- `feature/<feature-name>` → Individual features (e.g., `feature/topic-modeling`)

### **Commit Conventions**
- `feat: add topic modeling analysis`
- `fix: resolve API issue in scraper`
- `refactor: optimize sentiment analysis`

## Future Enhancements
- **Deep learning-based NLP models** for improved text analysis.
- **Expanded dataset** to include more historical texts.
- **Interactive visualization tools** to explore linguistic similarities.

## Contributors
- **Your Name** (@yourusername)

## License
This project is licensed under the **MIT License**.

