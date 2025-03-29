# 🔍 Golden Section Search Visualizer

An interactive web application to visualize the **Golden Section Search** optimization algorithm, built using **Streamlit** and **Plotly**. You can input any mathematical function, choose to minimize or maximize it, and watch the algorithm converge with animated graphs and detailed step logs.

---

## Features

- 📈 Real-time interactive visualization with Plotly
- 🧠 Step-by-step optimization history
- ✅ Supports both minimization and maximization
- 📤 Clean UI with Streamlit
- 🧮 User-defined mathematical function input
- 💡 Domain warnings and error handling included

---

## 📦 Installation & Run

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/golden-section-visualizer.git
cd golden-section-visualizer
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app:
```bash
streamlit run main.py
```

Once started, open your browser at:
```
http://localhost:8501
```

---

## ✍️ Example Functions to Try

| Expression | Notes |
|------------|-------|
| `np.sin(x)` | Oscillating function |
| `(x - 3)**2 + 2` | Simple quadratic with minimum at x=3 |
| `x**2 + np.sin(5 * x)` | Non-convex, multiple minima |
| `np.log(x + 2) + np.sin(x)` | Domain-restricted function |
| `np.exp(-x) + (x - 1)**2` | Sharp exponential valley |

---

## 📁 Project Structure

```
golden-section-visualizer/
├── main.py              # Streamlit app
├── optimizer.py         # Golden Section Search algorithm
├── animate.py           # Plotly animation builder
├── utils.py             # Safe math function parsing
├── requirements.txt     # Python dependencies
└── README.md            # You're reading it :)
```

---

## ⚠️ Notes

- When using functions like `log(x)` or `1/x`, ensure your interval is within a valid domain.
- If you see a warning like `RuntimeWarning: invalid value encountered`, the app will still handle it gracefully.

---

## 🌐 Live Demo

Try it out here:  
👉 [GSS Streamlit App](https://golden-section-visualizer.streamlit.app)


---

## 📖 License

MIT License – feel free to use, modify, and share this project.

---

## ✨ Author
*Umut Alkan*
