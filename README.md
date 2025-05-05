This project builds a complete data pipeline that extracts website session data from an AWS RDS MySQL database and transforms it into actionable insights in Looker Studio. A scheduled Python script loads session data into a Postgres data warehouse, organizing it through raw, staging, and warehouse schemas using dbt. GitHub Actions automate the extraction and loading process every 15 minutes, while GitHub Secrets securely manage credentials. The pipeline applies data modeling and aggregation to calculate daily sessions and repeat session percentages by UTM source. Visualizations in Looker Studio present interactive reports on session trends, enabling dynamic filtering by date and source. The entire system is version-controlled, modular, and cloud-native, with all development managed through GitHub Codespaces.

***The data pipeline visual illustrates how website session data flows from AWS RDS MySQL into a Postgres data warehouse, is transformed through dbt into staging and warehouse layers, and is ultimately visualized in Looker Studio. It highlights the tools, schemas, automation, and infrastructure used at each stage of the workflow***

![Website_Sessions](https://github.com/user-attachments/assets/d1983595-6c09-4ace-80c8-f4305dc0821f)

### 🧰 Technologies Used

- **Data Infrastructure**: AWS RDS MySQL (source), AWS RDS Postgres (warehouse)
- **Development Tools**: Python, Pandas, SQLAlchemy, dbt, SQL, GitHub Codespaces
- **Automation & Deployment**: GitHub Actions, GitHub Secrets
- **Visualization**: Looker Studio
- **Version Control**: Git, GitHub

### 📊 Pipeline Layers

| Layer     | Object(s)                                        |
|-----------|--------------------------------------------------|
| Source    | `website_sessions` table in MySQL                |
| Raw       | Raw tables in Postgres `raw` schema              |
| Staging   | `stg_website_sessions` (view)                    |
| Warehouse | `fct_website_sessions_utm_source_daily` (table)  |
| Looker    | Dashboard with daily metrics by UTM source       |

### 🔗 Looker Dashboard (Unlisted)

[https://lookerstudio.google.com/reporting/5566edf4-0c14-482f-84e6-37325c2706f0](https://lookerstudio.google.com/reporting/5566edf4-0c14-482f-84e6-37325c2706f0)
