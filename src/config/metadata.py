# Metadata: Define column names and types for each category based on the documentation
METADATA = {
    "estabelecimentos": {
        "cnpj_basico": "VARCHAR",
        "cnpj_ordem": "VARCHAR",
        "cnpj_dv": "VARCHAR",
        "identificador_matriz_filial": "TINYINT",
        "nome_fantasia": "VARCHAR",
        "codigo_situacao_cadastral": "INTEGER",
        "data_situacao_cadastral": "TIMESTAMP",
        "codigo_motivo_situacao_cadastral": "TINYINT",
        "nome_cidade_exterior": "VARCHAR",
        "codigo_pais": "INTEGER",
        "data_inicio_atividade": "TIMESTAMP",
        "codigo_cnae_fiscal_principal": "INTEGER",
        "codigos_cnae_fiscal_secundaria": "VARCHAR[]",
        "tipo_logradouro": "VARCHAR",
        "logradouro": "VARCHAR",
        "numero": "VARCHAR",
        "complemento": "VARCHAR",
        "bairro": "VARCHAR",
        "cep": "VARCHAR",
        "uf": "VARCHAR",
        "codigo_municipio": "INTEGER",
        "ddd_1": "VARCHAR",
        "telefone_1": "VARCHAR",
        "ddd_2": "VARCHAR",
        "telefone_2": "VARCHAR",
        "ddd_fax": "VARCHAR",
        "fax": "VARCHAR",
        "correio_eletronico": "VARCHAR",
        "situacao_especial": "VARCHAR",
        "data_situacao_especial": "TIMESTAMP"
    },
    "socios": {
        "cnpj_basico": "VARCHAR",
        "identificador_socio": "TINYINT",
        "nome_socio_razao_social": "VARCHAR",
        "cpf_cnpj_socio": "VARCHAR",
        "codigo_qualificacao_socio": "SMALLINT",
        "data_entrada_sociedade": "TIMESTAMP",
        "codigo_pais": "INTEGER",
        "cpf_representante_legal": "VARCHAR",
        "nome_representante": "VARCHAR",
        "codigo_qualificacao_representante_legal": "SMALLINT",
        "codigo_faixa_etaria": "TINYINT"
    },
    "simples": {
        "cnpj_basico": "VARCHAR",
        "opcao_simples": "VARCHAR",
        "data_opcao_simples": "TIMESTAMP",
        "data_exclusao_simples": "TIMESTAMP",
        "opcao_mei": "VARCHAR",
        "data_opcao_mei": "TIMESTAMP",
        "data_exclusao_mei": "TIMESTAMP"
    },
    "empresas": {
        "cnpj_basico": "VARCHAR",
        "razao_social": "VARCHAR",
        "codigo_natureza_juridica": "SMALLINT",
        "codigo_qualificacao_responsavel": "SMALLINT",
        "capital_social": "DECIMAL",
        "codigo_porte_empresa": "TINYINT",
        "ente_federativo_responsavel": "VARCHAR"
    },
    "paises": {
        "codigo": "INTEGER",
        "descricao": "VARCHAR"
    },
    "municipios": {
        "codigo": "INTEGER",
        "descricao": "VARCHAR"
    },
    "naturezas": {
        "codigo": "SMALLINT",
        "descricao": "VARCHAR"
    },
    "cnaes": {
        "codigo": "INTEGER",
        "descricao": "VARCHAR"
    },
    "qualificacoes": {
        "codigo": "SMALLINT",
        "descricao": "VARCHAR"
    }
}