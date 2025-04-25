# Dados Abertos CNPJ

This project provides tools to download, process, and analyze public data from the Brazilian Federal Revenue's National Registry of Legal Entities (CNPJ). It facilitates the extraction and transformation of large-scale datasets into a structured format suitable for analysis and integration.

---

## 📁 Project Structure

- **`main.py`**: Primary script that orchestrates the data processing pipeline.
- **`requirements.txt`**: Lists Python dependencies required to run the project.
- **`cnpj-metadados.pdf`**: Documentation detailing the layout and structure of the CNPJ data files.
- **`src/`**: Directory containing auxiliary modules and scripts used in data processing.

---

## 📦 Output Information

The processed data is stored in a DuckDB database (`dados_abertos_cnpj.db`) and includes the following tables:

### **1. estabelecimentos**
Details about establishments (branches or headquarters) of companies:
- `cnpj_basico`: Basic CNPJ number (first 8 digits).
- `cnpj_ordem`: Order number (next 4 digits of the CNPJ).
- `cnpj_dv`: Verification digit (last 2 digits of the CNPJ).
- `identificador_matriz_filial`: Indicates whether the establishment is a branch or headquarters.
- `nome_fantasia`: Trade name of the establishment.
- `codigo_situacao_cadastral`: Registration status code.
- `data_situacao_cadastral`: Date of the registration status.
- `codigo_motivo_situacao_cadastral`: Reason for the registration status.
- `nome_cidade_exterior`: Name of the foreign city (if applicable).
- `codigo_pais`: Country code (if applicable).
- `data_inicio_atividade`: Start date of the establishment's activities.
- `codigo_cnae_fiscal_principal`: Primary CNAE (economic activity) code.
- `codigos_cnae_fiscal_secundaria`: Secondary CNAE codes (comma-separated).
- `tipo_logradouro`: Type of street (e.g., Avenue, Street).
- `logradouro`: Street name.
- `numero`: Street number.
- `complemento`: Address complement.
- `bairro`: Neighborhood.
- `cep`: Postal code.
- `uf`: State abbreviation.
- `codigo_municipio`: Municipality code.
- `ddd_1`, `telefone_1`: Primary phone number.
- `ddd_2`, `telefone_2`: Secondary phone number.
- `ddd_fax`, `fax`: Fax number.
- `correio_eletronico`: Email address.
- `situacao_especial`: Special situation (if applicable).
- `data_situacao_especial`: Date of the special situation.

### **2. empresas**
Details about companies:
- `cnpj_basico`: Basic CNPJ number (first 8 digits).
- `razao_social`: Legal name of the company.
- `codigo_natureza_juridica`: Code for the legal nature of the company.
- `codigo_qualificacao_responsavel`: Qualification code of the responsible person.
- `capital_social`: Declared social capital of the company.
- `codigo_porte_empresa`: Company size classification.
- `ente_federativo_responsavel`: Responsible federal entity (if applicable).

### **3. socios**
Details about partners or shareholders:
- `cnpj_basico`: Basic CNPJ number (first 8 digits).
- `codigo_identificador_socio`: Identifies the type of partner (e.g., individual, legal entity).
- `nome_socio_razao_social`: Name of the partner or shareholder.
- `cpf_cnpj_socio`: CPF or CNPJ of the partner.
- `codigo_qualificacao_socio`: Qualification code of the partner.
- `data_entrada_sociedade`: Date the partner joined the company.
- `codigo_pais`: Country code (if applicable).
- `cpf_representante_legal`: CPF of the legal representative (if applicable).
- `nome_representante`: Name of the legal representative.
- `codigo_qualificacao_representante_legal`: Qualification code of the legal representative.
- `codigo_faixa_etaria`: Age range classification of the partner.

### **4. simples**
Details about Simples Nacional tax regime:
- `cnpj_basico`: Basic CNPJ number (first 8 digits).
- `opcao_simples`: Indicates whether the company opted for Simples Nacional.
- `data_opcao_simples`: Date of opting for Simples Nacional.
- `data_exclusao_simples`: Date of exclusion from Simples Nacional.
- `opcao_mei`: Indicates whether the company opted for MEI (Micro Entrepreneur Individual).
- `data_opcao_mei`: Date of opting for MEI.
- `data_exclusao_mei`: Date of exclusion from MEI.

### **5. cnaes**
Details about CNAE (economic activity) codes:
- `codigo`: CNAE code.
- `descricao`: Description of the economic activity.

### **6. municipios**
Details about municipalities:
- `codigo`: Municipality code.
- `descricao`: Municipality name.

### **7. paises**
Details about countries:
- `codigo`: Country code.
- `descricao`: Country name.

### **8. qualificacoes**
Details about qualification codes:
- `codigo`: Qualification code.
- `descricao`: Qualification description.

### **9. naturezas**
Details about the nature of legal entities:
- `codigo`: Nature code.
- `descricao`: Nature description.

### **Auxiliary Tables**
Predefined lookup tables:
- `aux_porte_empresa`: Company size classifications.
- `aux_identificador_matriz_filial`: Identifies whether an establishment is a branch or headquarters.
- `aux_situacao_cadastral`: Registration status codes.
- `aux_identificador_socio`: Identifies the type of partner (e.g., individual, legal entity).
- `aux_faixa_etaria`: Age range classifications.

---

## 🛠️ Technical Details and Tools Used

- **Language**: Python
- **Database**: DuckDB for efficient analytical queries.
- **Libraries**:
  - `requests`: For HTTP requests to download files.
  - `beautifulsoup4`: For scraping download links from the Receita Federal website.
  - `duckdb`: For database operations.
  - `pyarrow`: For handling Parquet files (if needed in the future).
- **Data Sources**: Downloads data from the official Receita Federal portal: [dados.gov.br](https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica---cnpj).

---

## 🚀 How the Project Works

The project follows these steps:

1. **Dynamic URL Resolution**:
   - Automatically identifies the most recent CNPJ data available on the Receita Federal website.

2. **Download and Extraction**:
   - Downloads ZIP files containing CSV data.
   - Extracts the CSV files into a structured directory.

3. **Data Transformation and Loading**:
   - Converts CSV files to UTF-8 encoding.
   - Loads data into DuckDB using SQL transformations defined in `sql_templates.py`.

4. **Auxiliary Table Creation**:
   - Creates predefined lookup tables (e.g., company size, registration status).

5. **Quality Control**:
   - Logs row mismatches and skips invalid files.

---

## 🚀 How to Run the Project

### **1. Prerequisites**
- Python 3.8 or higher installed.
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### **2. Clone the Repository**
   ```bash
   git clone https://github.com/ricardonascimentosoares/dados-abertos-cnpj.git
   cd dados-abertos-cnpj
   ```

### **3. Download CNPJ Data**
   Obtain the latest CNPJ data files from the Receita Federal's open data portal:
   [https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica---cnpj](https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica---cnpj)

### **4. Run the Processing Script**
   Execute the main script to process the downloaded data:
   ```bash
   python main.py
   ```

   *Note*: Ensure that the downloaded data files are placed in the appropriate directory as expected by the script.

## 🌟 Possible Improvements

- **Enhanced Error Handling**: Implement robust error checking and exception handling to manage unexpected data anomalies or processing errors.
- **Logging Mechanism**: Integrate a logging system to monitor the processing pipeline and facilitate debugging.
- **Data Validation**: Incorporate validation steps to ensure data integrity and consistency post-processing.
- **Database Integration**: Extend the project to load processed data into a relational database (e.g., PostgreSQL) for more efficient querying and analysis.
- **Command-Line Interface (CLI)**: Develop a user-friendly CLI to allow users to specify parameters and control the processing workflow.
- **Parallel Processing**: Optimize the data processing pipeline to handle large datasets more efficiently by leveraging parallel processing techniques.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📬 Contact

For questions or suggestions, please open an issue on the [GitHub repository](https://github.com/ricardonascimentosoares/dados-abertos-cnpj/issues).
