# 🎧 Spotify Data Monitor & Analytics

- 🔁 Last Update: 12/04/2026
- 🚀 Deploy: [Dashboard](https://app.powerbi.com/view?r=eyJrIjoiOGIzMjI2NWEtNjIxNS00MGYxLTg0MGYtZTkzY2Y4YmQzNGU0IiwidCI6ImU5MDVhOGVjLTdkNGQtNGM4Ny1iNzY4LTdlMzQzNjkyMmVjNiJ9)


## 📋 Summary

- [📖 About project](#about-project)
- [🛠️ Technologies used](#technologies-used)
- [📋 Requirements](#requirements)
- [🚀 How to run](#how-to-run)
- [👨‍💻 Authors](#authors)

## 📖 About Project <a id="about-project"></a>

The project is a dashboard with data from my Spotify account ( Replicate with your information and see the magic ). Here you see how many songs you listened to, your top artists, how many minutes you listened to music, and much more. 

## 🛠️ Technologies used <a id="technologies-used"></a>

- Python 
    - Spark
    - Pandas
- Power BI


## 📋 Requirements <a id="requirements"></a>

- Data from your Spotify account and extended history of your Spotify account
- PowerBI
- Run local:
    - Visual Studio Code or another code editor
    - Python
    - UV
    - With you need a guide access: [UV and spark installation](https://github.com/MatheusRodri/doc-template-files/tree/main/pyspark)
- Run in cloud:
    - Databricks

## 🚀 How to run <a id="how-to-run"></a>

- Request your Spotify data [here](https://www.spotify.com/account/privacy/)
- Download your Spotify data
- Run local:
    - Clone the repository in your local machine
    - Open the folder in your code editor
    - Put the downloaded files in the `data\extended` folder
    - In terminal, run the following command:
        - `uv sync` to install the dependencies
    - Run the `00-Ingestion`, `01-Transform` and `02-Gold` files
    - Open the PowerBI
    - Open the `dashboard_spotify_local.pbix` file
    - In the initial page, click on `update` button



- Upload the files in separate folder in Volumes
    - If you not know how upload files, follow the steps:
        - In the sidebar, click the Workspace icon
        - Navigate to the directory where you want to create the new folder.
        - Right-click on the parent folder's name or the main workspace area, and select Create > Folder.
        - Enter a name for the new folder in the dialog box and press Enter or click outside the field to save it.
- copy the path of uploaded files
- Open the `notebooks/00-setup` file
- Find "REPLACE WITH YOUR OWN PATH" Use `ctrl + f` or `cmd + f`
- Replace to your path
- Run the `01-Extration` and `02-Transform` files
- Open the PowerBI
- Open the dashboard file
- In the initial page, click on down arrow below "Transform data"
- Select "Edit parameters"
- Put your Host and Path 
    - This information is in the `03-BI` notebook ( Run the notebook to capture your Host and Path )
- Click "Apply changes"


## 👨‍💻 Author <a id="authors"></a>

### [Matheus Rodrigues](https://www.linkedin.com/in/matheus-rodrigues-mrj/)