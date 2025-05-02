SQL_INSERT_TEMPLATES = {
    "estabelecimentos": """
        INSERT INTO estabelecimentos
        SELECT 
            cnpj_basico,
            cnpj_ordem,
            cnpj_dv,
            identificador_matriz_filial::tinyint as identificador_matriz_filial,
            nome_fantasia,
            codigo_situacao_cadastral::integer as codigo_situacao_cadastral,
            TRY_STRPTIME(data_situacao_cadastral, '%Y%m%d') as data_situacao_cadastral,
            codigo_motivo_situacao_cadastral::tinyint as codigo_motivo_situacao_cadastral,
            nome_cidade_exterior,
            codigo_pais::integer as codigo_pais,
            TRY_STRPTIME(data_inicio_atividade, '%Y%m%d') as data_inicio_atividade,
            codigo_cnae_fiscal_principal::integer as codigo_cnae_fiscal_principal,
            STRING_SPLIT(codigos_cnae_fiscal_secundaria, ',') as codigos_cnae_fiscal_secundaria,
            tipo_logradouro,
            logradouro,
            numero,
            complemento,
            bairro,
            cep,
            uf,
            codigo_municipio::integer as codigo_municipio,
            ddd_1,
            telefone_1,
            ddd_2,
            telefone_2,
            ddd_fax,
            fax,
            correio_eletronico,
            situacao_especial,
            TRY_STRPTIME(data_situacao_especial, '%Y%m%d') as data_situacao_especial
        FROM read_csv('{csv_file}',
            delim=';',
            header=False,
            column_names={metadata},
            quote='"',
            escape='"',
            encoding='utf-8',
            all_varchar=True,
            max_line_size=10000000)
    """,
    "empresas": """
        INSERT INTO empresas
        SELECT 
            cnpj_basico,
            razao_social,
            codigo_natureza_juridica::smallint as codigo_natureza_juridica,
            codigo_qualificacao_responsavel::smallint as codigo_qualificacao_responsavel,
            CAST(REPLACE(capital_social, ',', '.') AS DECIMAL) as capital_social,
            codigo_porte_empresa::tinyint as codigo_porte_empresa,
            ente_federativo_responsavel
        FROM read_csv('{csv_file}',
            delim=';',
            header=False,
            column_names={metadata},
            quote='"',
            escape='"',
            encoding='utf-8',
            all_varchar=True)
    """,
    "socios": """
        INSERT INTO socios
        SELECT 
            cnpj_basico,
            identificador_socio::tinyint as identificador_socio,
            nome_socio_razao_social,
            cpf_cnpj_socio,
            codigo_qualificacao_socio::smallint as codigo_qualificacao_socio,
            TRY_STRPTIME(data_entrada_sociedade, '%Y%m%d') as data_entrada_sociedade,
            codigo_pais::integer as codigo_pais,
            cpf_representante_legal,
            nome_representante,
            codigo_qualificacao_representante_legal::smallint as codigo_qualificacao_representante_legal,
            codigo_faixa_etaria::tinyint as codigo_faixa_etaria
        FROM read_csv('{csv_file}',
            delim=';',
            header=False,
            column_names={metadata},
            quote='"',
            escape='"',
            encoding='utf-8',
            all_varchar=True)
    """,
    "simples": """
        INSERT INTO simples
        SELECT 
            cnpj_basico,
            opcao_simples,
            TRY_STRPTIME(data_opcao_simples, '%Y%m%d') as data_opcao_simples,
            TRY_STRPTIME(data_exclusao_simples, '%Y%m%d') as data_exclusao_simples,
            opcao_mei,
            TRY_STRPTIME(data_opcao_mei, '%Y%m%d') as data_opcao_mei,
            TRY_STRPTIME(data_exclusao_mei, '%Y%m%d') as data_exclusao_mei
        FROM read_csv('{csv_file}',
            delim=';',
            header=False,
            column_names={metadata},
            quote='"',
            escape='"',
            encoding='utf-8',
            all_varchar=True)
    """,
    "cnaes": """
        INSERT INTO cnaes
        SELECT 
            codigo::integer as codigo,
            descricao
        FROM read_csv('{csv_file}',
            delim=';',
            header=False,
            column_names={metadata},
            quote='"',
            escape='"',
            encoding='utf-8',
            all_varchar=True)
    """,
    "municipios": """
        INSERT INTO municipios
        SELECT 
            codigo::integer as codigo,
            descricao
        FROM read_csv('{csv_file}',
            delim=';',
            header=False,
            column_names={metadata},
            quote='"',
            escape='"',
            encoding='utf-8',
            all_varchar=True)
    """,
    "paises": """
        INSERT INTO paises
        SELECT 
            codigo::integer as codigo,
            descricao
        FROM read_csv('{csv_file}',
            delim=';',
            header=False,
            column_names={metadata},
            quote='"',
            escape='"',
            encoding='utf-8',
            all_varchar=True)
    """,
    "qualificacoes": """
        INSERT INTO qualificacoes
        SELECT 
            codigo::smallint as codigo,
            descricao
        FROM read_csv('{csv_file}',
            delim=';',
            header=False,
            column_names={metadata},
            quote='"',
            escape='"',
            encoding='utf-8',
            all_varchar=True)
    """,
    "naturezas": """
        INSERT INTO naturezas
        SELECT 
            codigo::smallint as codigo,
            descricao
        FROM read_csv('{csv_file}',
            delim=';',
            header=False,
            column_names={metadata},
            quote='"',
            escape='"',
            encoding='utf-8',
            all_varchar=True)
    """
}

AUX_TABLES_SQL = [
    # Table: aux_porte_empresa
    """
    CREATE TABLE IF NOT EXISTS aux_porte_empresa (
        codigo TINYINT PRIMARY KEY,
        descricao VARCHAR
    );
    INSERT INTO aux_porte_empresa (codigo, descricao) VALUES
        (0, 'NÃO INFORMADO'),
        (1, 'MICRO EMPRESA'),
        (3, 'EMPRESA DE PEQUENO PORTE'),
        (5, 'DEMAIS')
        ON CONFLICT DO NOTHING;
    """,

    # Table: aux_identificador_matriz_filial
    """
    CREATE TABLE IF NOT EXISTS aux_identificador_matriz_filial (
        codigo TINYINT PRIMARY KEY,
        descricao VARCHAR
    );
    INSERT INTO aux_identificador_matriz_filial (codigo, descricao) VALUES
        (1, 'MATRIZ'),
        (2, 'FILIAL')
        ON CONFLICT DO NOTHING;
    """,

    # Table: aux_situacao_cadastral
    """
    CREATE TABLE IF NOT EXISTS aux_situacao_cadastral (
        codigo INTEGER PRIMARY KEY,
        descricao VARCHAR
    );
    INSERT INTO aux_situacao_cadastral (codigo, descricao) VALUES
        (1, 'NULA'),
        (2, 'ATIVA'),
        (3, 'SUSPENSA'),
        (4, 'INAPTA'),
        (8, 'BAIXADA')
        ON CONFLICT DO NOTHING;
    """,

    # Table: aux_identificador_socio
    """
    CREATE TABLE IF NOT EXISTS aux_identificador_socio (
        codigo TINYINT PRIMARY KEY,
        descricao VARCHAR
    );
    INSERT INTO aux_identificador_socio (codigo, descricao) VALUES
        (1, 'PESSOA JURÍDICA'),
        (2, 'PESSOA FÍSICA'),
        (3, 'ESTRANGEIRO')
        ON CONFLICT DO NOTHING;
    """,

    # Table: aux_faixa_etaria
    """
    CREATE TABLE IF NOT EXISTS aux_faixa_etaria (
        codigo TINYINT PRIMARY KEY,
        descricao VARCHAR
    );
    INSERT INTO aux_faixa_etaria (codigo, descricao) VALUES
        (0, 'NÃO SE APLICA'),
        (1, '0 a 12 anos'),
        (2, '13 a 20 anos'),
        (3, '21 a 30 anos'),
        (4, '31 a 40 anos'),
        (5, '41 a 50 anos'),
        (6, '51 a 60 anos'),
        (7, '61 a 70 anos'),
        (8, '71 a 80 anos'),
        (9, 'Mais de 80 anos')
        ON CONFLICT DO NOTHING;;
    """
]