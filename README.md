# BeautyBot - Cosmetic Store Chatbot🚀💄
A Python-based intelligent chatbot designed to revolutionize customer support for cosmetic e-commerce platforms. Built with NLTK for natural language processing and Flask for backend services, this solution features a modern, responsive web interface that delivers instant, accurate responses to customer inquiries 24/7.<br>

<img src="https://github.com/user-attachments/assets/398ac72a-470c-4cb2-953d-18c2335b26bd">

### Features ✨
✅ Natural Language Processing (NLP) for intent detection<br>
✅ FAQs Support: Answers common customer queries<br>
✅ Web Interface: Interactive HTML/CSS/JS frontend<br>
✅ Easy Integration: Ready-to-deploy Flask backend<br>
✅ CORS Support: Handles cross-origin requests<br>

### Supported Queries
- Product information & authenticity<br>
- Order placement & payment methods<br>
- Shipping & return policies<br>
- International & local brand availability<br>

### Tech Stack 🛠️
- Component	Technology<br>
- Backend	        Python (Flask)<br>
- NLP	        NLTK (Natural Language Toolkit)<br>
- Frontend	HTML, CSS, JavaScript<br>
- API Handling	Fetch API<br>
- CORS	        Flask-CORS<br>

## Project Structure 📂
cosmetic-chatbot/<br>
├── app.py                # Flask backend & NLP logic<br>
├── requirements.txt      # Python dependencies<br>
├── static/               # CSS/JS/Images<br>
└── templates/<br>
    └── index.html       # Chatbot frontend<br>

## Installation ⚙️
1. Clone the Repository:
   ```bash
   git clone https://github.com/yourusername/cosmetic-chatbot.git
   cd cosmetic-chatbot
2. Set Up a Virtual Environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows
3. Install Dependencies:
   ```bash
   pip install -r requirements.txt
4. Download NLTK Data
   ```bash
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"

## Running the Chatbot ▶️
1. Start the Flask Backend:
   ```bash
   python app.py
The server will run at http://localhost:5000

### Access the Chatbot
Open your browser and visit:
👉 http://localhost:5000 

### Future Enhancements 🔮    
- Database Integration (SQLite/PostgreSQL for dynamic responses)<br>
- User Authentication for order tracking<br>
- Multi-language Support (Spanish, French, etc.)<br>
- Admin Dashboard to manage FAQs<br>
