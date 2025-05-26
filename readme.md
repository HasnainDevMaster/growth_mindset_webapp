# Assignment Comleted: 4 May 2025 (local Storage)

# Growth Mindset Tracker Web App

A simple, interactive web application built with Streamlit to help you develop and maintain a growth mindset through daily reflections and goal setting.

---

## Features

- **Daily Reflection:**  
  Record daily challenges and what you learned from them. The app tracks your reflection streak and motivates you to keep going.

- **Set a Goal:**  
  Define learning goals with descriptions and deadlines. All your goals are saved and can be reviewed anytime.

- **My Progress:**  
  Visualize your reflection streak, see your progress over time, and review your goals.

- **Growth Wall:**  
  View your recent reflections and all your goals in one place for inspiration and motivation.

---

## Live Demo

Try the app online:  
[https://hasnaindevmaster-growth-mindset-webapp-main-eczkgv.streamlit.app/](https://hasnaindevmaster-growth-mindset-webapp-main-eczkgv.streamlit.app/)

---

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/HasnainDevMaster/growth_mindset_webapp
   cd growth_mindset_webapp
   ```

2. **Create a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

---

## Usage

1. **Run the Streamlit app:**
   ```sh
   streamlit run main.py
   ```

2. **Open your browser:**  
   Visit the local URL provided by Streamlit (usually http://localhost:8501).

---

## File Structure

```
growth_mindset_webapp/
│
├── main.py              # Main Streamlit application
├── growth_data.json     # Data file (auto-created on first run)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## Data Storage

- All reflections and goals are stored in a local JSON file (`growth_data.json`) in the project directory.
- No data is sent to any external server.

---

## Dependencies

- streamlit
- pandas

(See `requirements.txt` for the full list.)

---

## Customization

- You can modify the UI or add new features by editing `main.py`.
- The data schema is simple and can be extended to include more fields if needed.

---

