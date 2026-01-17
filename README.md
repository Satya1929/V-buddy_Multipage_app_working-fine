<div align="left" style="position: relative;">
<h1>V-Buddy</h1>
<p align="left">
	<em><code>"Empowering Community Support with Context-Aware Generative AI"</code></em>
</p>
<p align="left">
	<!-- <img src="https://img.shields.io/github/last-commit/Satya1929/V-buddy_Multipage_app_working-fine?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit"> -->
	<img src="https://img.shields.io/github/languages/top/Satya1929/V-buddy_Multipage_app_working-fine?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" alt="streamlit">
    <img src="https://img.shields.io/badge/Gemini_2.5_Flash-8E75B2?style=for-the-badge&logo=google-gemini&logoColor=white" alt="gemini">
</p>
</div>
<br clear="right">

## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [⚙️ How It Works](#-how-it-works)
- [ Features](#-features)
- [🛠️ Tech Stack](#-tech-stack)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#-usage)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview
**V-Buddy** is a powerful AI-driven FAQ chatbot designed to streamline information access for communities. Leveraging the power of **Google Gemini 2.5 Flash**, it transforms static documents into an interactive, context-aware Q&A system.

Initially prototyped to help the **VIT** community navigate complex academic regulations, V-Buddy has grown into a scalable solution that supports **6,000+ members**, reducing response times by **50%** and significantly improving user satisfaction.

### 🌐 Live Dashboard
[**Try V-Buddy Live Here →**](https://v-buddy.streamlit.app/AI_QA_Page)

---

## ⚙️ How It Works
1.  **Ingest**: Administrators upload PDF documents (regulations, manuals, FAQs) via a secure Backend Page.
2.  **Index**: The system automatically extracts text and builds a persistent, local knowledge base (`Database PDFs`).
3.  **Interact**: Users ask questions in natural language on the **AI Q&A Page**.
4.  ** Answer**: The AI (Gemini 2.5 Flash) retrieves relevant context from the local database and generates a precise, grounded response.

---

## 👾 Features

- **📂 Persistent Knowledge Base**: Uploaded PDFs are permanently stored and automatically indexed, ensuring the AI "remembers" everything across sessions.
- **� Secure Backend Management**: A password-protected administrative interface (`only for backend people`) ensures only authorized personnel can add context to the knowledge base.
- **⚡ High-Performance AI**: Powered by **Gemini 2.5 Flash**, delivering rapid and accurate responses based strictly on the provided documents.
- **🤖 Context-Aware Q&A**: The AI explicitly informs users how many documents it is referencing (e.g., *"Using context from 10 PDF documents"*), fostering trust and transparency.
- **🎉 Community-Centric**: Designed to support large communities, facilitating better communication and reducing manual support workload.

---

## 🛠️ Tech Stack

### 1. **Core Application**
-   **[Python 3.x](https://www.python.org/):** The primary programming language.
-   **[Streamlit](https://streamlit.io/):** The web framework powering the interactive multi-page UI.

### 2. **Artificial Intelligence**
-   **[Google Generative AI SDK](https://ai.google.dev/):** Interface for the Gemini 2.5 Flash model.
-   **Prompt Engineering:** Custom prompts to ensure the AI acts as a helpful assistant grounded in local files.

### 3. **Data Handling & Backend**
-   **[PyPDF2](https://pypi.org/project/PyPDF2/):** Robust text extraction from uploaded PDF documents.
-   **Local Persistence:** Custom file system management (`utils.py`) to handle long-term storage of knowledge base vectors/text.
-   **Session State Management:** Advanced Streamlit state handling for seamless user flows and security gates.

---

## 📁 Project Structure

```sh
└── V-buddy_Multipage_app/
    ├── Main.py                  # Entry point & Welcome screen
    ├── utils.py                 # Core logic for PDF scanning & persistence
    ├── requirements.txt         # Python dependencies
    ├── Database PDFs/           # Permanent storage for Knowledge Base files
    └── pages/                   # Application Modules
        ├── 1_📂_Backend_Page.py # Admin Uploads (Password Protected)
        ├── 2_🤖_AI_QA_Page.py   # Primary User Interface for Chat
        ├── 3_�_Feedback_Page.py# User Feedback Collection
        └── 4_🎉_Credits_Page.py  # Contributors & Acknowledgments
```

### 📂 Project Index
<details open>
	<summary><b><code>V-BUDDY/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='./Main.py'>Main.py</a></b></td>
				<td>Landing page, introduction, and navigation hub.</td>
			</tr>
			<tr>
				<td><b><a href='./utils.py'>utils.py</a></b></td>
				<td>Utility for recursive PDF loading and text extraction.</td>
			</tr>
			<tr>
				<td><b><a href='./pages/1_📂_Backend_Page.py'>pages/1_📂_Backend_Page.py</a></b></td>
				<td><b>(Secured)</b> Interface for uploading new knowledge base files.</td>
			</tr>
			<tr>
				<td><b><a href='./pages/2_🤖_AI_QA_Page.py'>pages/2_🤖_AI_QA_Page.py</a></b></td>
				<td>The core Chat interface using Gemini 2.5 Flash.</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

-   **Python 3.10+**
-   **Google API Key** (with access to Gemini models)

### ⚙️ Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/Satya1929/V-buddy_Multipage_app_working-fine
    cd V-buddy_Multipage_app_working-fine
    ```

2.  **Set up your environment:**
    *   Create a `.env` file or export your API key:
        ```sh
        export GOOGLE_API_KEY="your_api_key_here"
        ```
    *   *(Optional but recommended)* Create a virtual environment:
        ```sh
        python -m venv .venv
        source .venv/bin/activate  # On Windows: .venv\Scripts\activate
        ```

3.  **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

### 🤖 Usage

Run the dashboard locally:
```sh
streamlit run Main.py
```
*   **For Users:** Navigate to the **AI Q&A Page** to start chatting.
*   **For Admins:** Go to the **Backend Page**, enter the password `Backend1929`, and upload new PDF documents.

---
## 📌 Project Roadmap

- [X] **`Phase 1`**: Prototype & PDF Interaction (Gemini 1.0).
- [X] **`Phase 2`**: Persistent Database & Multi-page Architecture.
- [X] **`Phase 3`**: Security Layers & Model Upgrade (Gemini 2.5 Flash).
- [ ] **`Phase 4`**: Deployment to Streamlit Cloud with Secret Management.
- [ ] **`Phase 5`**: Integration with WhatsApp API for direct community access.

---

## 🔰 Contributing

- [Report Issues](https://github.com/Satya1929/V-buddy_Multipage_app_working-fine/issues): Submit bugs found or log feature requests.

<details closed>
<summary>Contributing Guidelines</summary>

1.  **Fork the Repository**
2.  **Create a Branch**: `git checkout -b feature/AmazingFeature`
3.  **Commit your Changes**: `git commit -m 'Add some AmazingFeature'`
4.  **Push to the Branch**: `git push origin feature/AmazingFeature`
5.  **Open a Pull Request**
</details>

---

## 🙌 Acknowledgments

-   **Development:** Built with [Streamlit](https://streamlit.io/) and [Google Gemini](https://ai.google.dev/).
-   **Community:** Special thanks to the 6,000+ members who provided feedback during the testing phase.
