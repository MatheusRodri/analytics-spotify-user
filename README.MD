# 🎧 Spotify Data Monitor & Analytics

🔁 Last Update: 20/02/2026
📈 Progress: Completed
🚀 Deploy: [Dashboard](https://app.fabric.microsoft.com/view?r=eyJrIjoiZTRiMDYxMTktZGYwMC00MzAyLWI5MWQtN2JhYmExY2RmOWVlIiwidCI6IjY3YmE4MGMxLTAzZTUtNDhkMi1hZTIwLWRiZWJiNzNjNWUyNyJ9)


## 📋 Summary

- [📖 About project](#about-project)
- [🏗️ Architecture](#architecture)
- [🛠️ Technologies used](#technologies-used)
- [📋 Requirements](#requirements)
- [🚀 How to run](#how-to-run)
- [👨‍💻 Authors](#authors)

## 📖 About Project <a id="about-project"></a>

The project is a dashboard with data from my Spotify account ( Replicate with your information and see the magic ). Here you see how many songs you listened to, your top artists, how many minutes you listened to music, and much more. 

## 🏗️ Achitecture <a id="architecture"></a>

``` mermaid
graph TD
    A[Data Collection] --> B[Data Storage]
    B --> C[Data Processing] 
    C --> D[Data Visualization]

```

## 🛠️ Technologies used <a id="technologies-used"></a>

- Python 
    - Spark
    - Pandas
- Power BI


## 📋 Requirements <a id="requirements"></a>

- Data from your Spotify account and extended history of your Spotify account
- Databricks 
- PowerBI

## 🚀 How to run <a id="how-to-run"></a>

- Request your Spotify data [here](https://www.spotify.com/account/privacy/)
- Download your Spotify data
- Clone the project in Databricks
- Place the files in their respective folders within the "data" folder
- Open the `main` file
- Run the file completely
- Open the PowerBI
- Open the dashboard file
- In the initial page, click on down arrow below "Transform data"
- Select "Edit parameters"
- Put your Host and Path 
    - This information is in the final output of the `main` file in databricks
- Click "Apply changes"


## 👨‍💻 Author <a id="authors"></a>

[Matheus Rodrigues](https://www.linkedin.com/in/matheus-rodrigues-mrj/)