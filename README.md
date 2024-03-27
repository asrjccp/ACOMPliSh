# ACOMPliSh

---
## About
ACOMPliSh is a prompt-engineered generative AI web app to help A-level students learn H2 Computing. We are always work in progress. :) 

---

## How to start developing!
* Clone the repo to your computer
* Create a virtual envrionment by using the command `python -m venv .venv` before selecting the venv (there should be a prompt to use the new environment in VS Code)
* Kill the current terminal and run any Python file in the directory (you will get an error here)
* Run `pip install -r requirements.txt` to install the needed Python modules
* Create a folder called `.streamlit` in the root directory and create a file named `secrets.toml`
* Enter your variable `OPENAI_API_KEY = "(insert your own API Key here)"`
* In the root directory, use `streamlit run ACOMPliSh.py` to launch the web-app
* Create a pull request to update any content and do not sync directly to the repo
---
## Structure
```
ACOMPliSh/
├── pages (name)/
│   ├── chapter1.py
│   ├── chapter2.py
│   └── ...
├── images/
│   └── chapter1/
│       ├── picture1.png
│       ├── picture2.png
│       └── ...
├── code (for RAG)/
│   └── chapter1/
│       ├── code1.py
│       ├── code2.py
│       └── ...
├── .streamlit/
│   └── secrets.toml
└── requirements.txt
```
---
## Quick-Start Guide with Streamlit
Streamlit mainly uses `Markdown` to present content and its way to format text, math equations and pictures are found <a href="https://docs.streamlit.io/library/api-reference">here</a>.
To present pictures in the web-app, put the image file in the `images` directory first and use this <a href="https://docs.streamlit.io/library/api-reference/media/st.image">method</a> to show the picture
To access the OPENAI_API_KEY, use "st.secrets["OPENAI_API_KEY"] to access the key
## Credits
Core developer: Adapted from <a href= "https://github.com/DangerousPotential">Teh Kim Wee (23/25)</a>
Contributors: ASRJC Computing Students

