import pandas as pd

def data_treatment(excel_path="data/dados_autoggform.xlsx"):
   
    df = pd.read_excel(excel_path,  dtype={"cpf": str})
    
    # Padroniza nomes das colunas
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    # =========================
    # TRATAMENTO DE NULOS
    # =========================
    df = df.fillna("Não Informado")

    # =========================
    # PADRONIZA TEXTO
    # =========================
    colunas_texto = [
        "nome",
        "sobrenome",
        "email",
        "cpf",
        "estado",
        "rua",
        "complemento"
    ]

    for col in colunas_texto:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.strip()
                .str.title()
            )


    # =========================
    # NORMALIZA ESTADOS
    # =========================
    estados = {
    # Acre
    "Acre": "AC", "ACRE": "AC", "acre": "AC", "acre ": "AC", "AC":"AC",
    
    # Alagoas
    "Alagoas": "AL", "ALAGOAS": "AL", "alagoas": "AL", "AL":"AL",
    
    # Amapá
    "Amapá": "AP", "Amapa": "AP", "AMAPÁ": "AP", "amapa": "AP", "AMAPA": "AP","AP":"AP",
    
    # Amazonas
    "Amazonas": "AM", "AMAZONAS": "AM", "amazonas": "AM","AM":"AM",
    
    # Bahia
    "Bahia": "BA", "BAHIA": "BA", "bahia": "BA","BA":"BA",
    
    # Ceará
    "Ceará": "CE", "Ceara": "CE", "CEARÁ": "CE", "ceara": "CE","CE":"CE",
    
    # Distrito Federal
    "Distrito Federal": "DF", "distrito federal": "DF", "DISTRITO FEDERAL": "DF","DF":"DF",
    "DistritoFederal": "DF", "distritofederal": "DF","":"",
    
    # Espírito Santo
    "Espírito Santo": "ES", "Espirito Santo": "ES", "ESPÍRITO SANTO": "ES","ES":"ES",
    "espirito santo": "ES", "EspiritoSanto": "ES", "espiritosanto": "ES","ES":"ES",
    
    # Goiás
    "Goiás": "GO", "Goias": "GO", "GOIÁS": "GO", "goias": "GO", "GOIAS": "GO","GO":"GO",
    
    # Maranhão
    "Maranhão": "MA", "Maranhao": "MA", "MARANHÃO": "MA", "maranhao": "MA", "MARANHÃO": "MA","MA":"MA",
    
    # Mato Grosso
    "Mato Grosso": "MT", "MATo Grosso": "MT", "matogrosso": "MT","MATOGROSSO":"MT", "MATO GROSSO":"MT","MT":"MT",
    
    # Mato Grosso do Sul
    "Mato Grosso do Sul": "MS", "Mato Grosso Do Sul": "MS", "matogrossodosul": "MS","MS":"MS",
    
    # Minas Gerais
    "Minas Gerais": "MG", "MINAS GERAIS": "MG", "minas gerais": "MG", "minasgerais": "MG","MG":"MG",
    
    # Pará
    "Pará": "PA", "Para": "PA", "PARÁ": "PA", "para": "PA","PA":"PA",
    
    # Paraíba
    "Paraíba": "PB", "Paraiba": "PB", "PARAÍBA": "PB", "paraiba": "PB","PB":"PB",
    
    # Paraná
    "Paraná": "PR", "Parana": "PR", "PARANÁ": "PR", "parana": "PR","PR":"PR",
    
    # Pernambuco
    "Pernambuco": "PE", "PERNAMBUCO": "PE", "pernambuco": "PE","PE":"PE",
    
    # Piauí
    "Piauí": "PI", "Piaui": "PI", "PIAUÍ": "PI", "piaui": "PI","PI":"PI",
    
    # Rio de Janeiro
    "Rio de Janeiro": "RJ", "Rio De Janeiro": "RJ", "RIO DE JANEIRO": "RJ","RJ":"RJ",
    "riodejaneiro": "RJ",
    
    # Rio Grande do Norte
    "Rio Grande do Norte": "RN", "Rio Grande Do Norte": "RN", "RIO GRANDE DO NORTE": "RN","RN":"RN",
    "riograndedonorte": "RN",
    
    # Rio Grande do Sul
    "Rio Grande do Sul": "RS", "Rio Grande Do Sul": "RS", "RIO GRANDE DO SUL": "RS","RS":"RS",
    "riograndedosul": "RS",
    
    # Rondônia
    "Rondônia": "RO", "Rondonia": "RO", "RONDÔNIA": "RO", "rondonia": "RO","RO":"RO",
    
    # Roraima
    "Roraima": "RR", "RORAIMA": "RR", "roraima": "RR","RR":"RR",
    
    # Santa Catarina
    "Santa Catarina": "SC", "SANTA CATARINA": "SC", "santa catarina": "SC","SC":"SC",
    "santacatarina": "SC",
    
    # São Paulo
    "São Paulo": "SP", "Sao Paulo": "SP", "SÃO PAULO": "SP", "saopaulo": "SP", "sao paulo": "SP","SP":"SP",
    
    # Sergipe
    "Sergipe": "SE", "SERGIPE": "SE", "sergipe": "SE","SE":"SE",
    
    # Tocantins
    "Tocantins": "TO", "TOCANTINS": "TO", "tocantins": "TO","TO":"TO",
}

    if "estado" in df.columns:
        df["estado"] = df["estado"].replace(estados)

    # =========================
    # CONVERSÃO DE TIPOS
    # =========================
    if "numero" in df.columns:
        df["numero"] = (
            df["numero"]
            .replace("Não Informado", 0)
            .astype(int)
        )

    if "celular" in df.columns:
        df["celular"] = (
            df["celular"]
            .astype(str)
            .str.replace(r"\D", "", regex=True)
        )

    # =========================
    # TRATAMENTO CPF
    # =========================
    
    if "cpf" in df.columns:

        # remove tudo que não for número
        df["cpf"] = (
            df["cpf"]
            .astype(str)
            .str.replace(r"\D", "", regex=True)
        )

        # preenche com zeros à esquerda (governança)
        df["cpf"] = df["cpf"].str.zfill(11)

        # aplica máscara ###.###.###-##
        df["cpf"] = (
            df["cpf"]
            .str.replace(r"(\d{3})(\d{3})(\d{3})(\d{2})",
                        r"\1.\2.\3-\4",
                        regex=True)
        )



    # =========================
    # CRIA COLUNAS DERIVADAS
    # =========================
    df["etl_status"] = "TRATADO"
    df["data_processamento"] = pd.Timestamp.now()

            
    

    return df
 