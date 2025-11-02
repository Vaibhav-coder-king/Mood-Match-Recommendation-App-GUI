# 🎬 Mood Match Recommendation App

## 📖 Description
**Mood Match Recommendation App** is an interactive **CustomTkinter-based GUI** that helps users find and explore **Movies, Web Series, K-Dramas, and Anime** recommendations based on **name** or **genre**.  
It combines **local data (CSV)** with live movie details fetched via the **OMDb API**, offering both fun animations and informative results — all in one visually rich interface.  

---

## ✨ Key Features

- 🎨 **Modern CustomTkinter GUI** with dark/light themes  
- 🧠 **Smart Recommendation Engine**  
  - Search by **Name** (live OMDb API)  
  - Search by **Genre** (from local CSV datasets)  
- 📚 **Supports multiple categories:**
  - Movies  
  - Web Series  
  - K-Dramas  
  - Anime  
- 🖼️ **Poster and Details View**
  - Automatically displays poster, ratings, year, plot, director, runtime, etc.  
- 💾 **Auto Save to Local Database**
  - Automatically adds new found titles to CSV files for offline use.  
- ⚙️ **Smooth Page Transitions**
  - Unique animated transitions between pages (slide, zoom, fade).  
- 🌗 **Dark/Light Theme Toggle**  
- 🚪 **Exit & Navigation**
  - One-click back, home, and exit options.  

---


## 📸 Screenshots

<img width="1918" height="985" alt="Screenshot 2025-11-02 154212" src="https://github.com/user-attachments/assets/2b1c0443-b971-4543-8c07-ccdf86d30b81" />

<img width="1919" height="1017" alt="Screenshot 2025-11-02 154232" src="https://github.com/user-attachments/assets/04f46415-f73d-40d7-af32-fefd50ee59fa" />

<img width="1904" height="807" alt="Screenshot 2025-11-02 154315" src="https://github.com/user-attachments/assets/b7ffc960-e466-4aad-9db5-f40757ed9291" />

<img width="1903" height="906" alt="Screenshot 2025-11-02 154338" src="https://github.com/user-attachments/assets/97e51c29-176e-4788-b272-00fb9dc38d48" />

<img width="1903" height="951" alt="Screenshot 2025-11-02 154507" src="https://github.com/user-attachments/assets/797d984f-c7aa-45fb-ac44-b59818cb1a64" />

<img width="1885" height="961" alt="Screenshot 2025-11-02 154536" src="https://github.com/user-attachments/assets/51a0629d-8b16-4bfc-80f3-693acd91e1b2" />

<img width="1847" height="946" alt="Screenshot 2025-11-02 154549" src="https://github.com/user-attachments/assets/2bc9944d-1d51-4deb-8189-c8545b8c5326" />

<img width="1863" height="936" alt="Screenshot 2025-11-02 154605" src="https://github.com/user-attachments/assets/b34917ec-df49-4b4d-a0e2-6de1acc80801" />

<img width="1858" height="929" alt="Screenshot 2025-11-02 154635" src="https://github.com/user-attachments/assets/fbeebf1e-ef08-441f-b507-0f5ca66c55ca" />

<img width="1912" height="943" alt="Screenshot 2025-11-02 154708" src="https://github.com/user-attachments/assets/ee24e021-8759-4c6c-95a0-40c660de273e" />

---
## 🧩 Tech Stack

- **Python 3.10+**
- **CustomTkinter** for UI  
- **Pillow (PIL)** for image processing  
- **urllib** + **json** for OMDb API integration  
- **csv** for dataset handling  
- **threading** for smooth UI  
- **OMDb API** for live movie information  

---

## 📂 Folder Structure

```
Movies and Web Series Recommendation App/
│
├── main.py # Main application file (this script)
├── Api_omdb.txt # File containing your OMDb API key
├── Movies.csv # Local dataset for movies
├── Webseries.csv # Local dataset for web series
├── K_drama.csv # Local dataset for K-dramas
├── Anime.csv # Local dataset for anime
└── Recommendation App GUI/
└── Back_photo_laptop.png # Background image for the GUI
```
---

## ⚙️ Setup & Usage

### 1. 🧠 Install Dependencies
```bash
pip install customtkinter pillow
```

### 2. 🔑 Set Your OMDb API Key
Create a file named Api_omdb.txt

Paste your OMDb API key inside it (no extra spaces or newlines)

### 3. 📁 Prepare Local CSV Files

Each CSV file should have proper columns:

Movies.csv: Title, Year, Genre, IMDb Rating, Language, Director, Country

Webseries.csv: Title, Year, Platform, Genre, Language, IMDb Rating, Country

K_drama.csv: Title, Year, Platform, Genre, Language, IMDb Rating, Country

Anime.csv: Title, Genre, IMDb Rating, Language, Country

### 4. ▶️ Run the App
bash
Copy code
python main.py

### 5. 🧭 Navigation
Tap Anywhere on the home screen to start

Choose your Category (Movies / Webseries / K-Drama / Anime)

Select Search by Name or Genre

View Results and Recommendations

## 🌐 OMDb API

Get your API key for free at:
👉 https://www.omdbapi.com/apikey.aspx

## 🧑‍💻 Author
Created by 
