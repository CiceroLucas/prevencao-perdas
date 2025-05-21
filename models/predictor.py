import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def treinar_modelo(df):
    df = df.copy()
    df["perda"] = (df["quantidade_perdida"] > 0).astype(int)
    encoder = LabelEncoder()
    df["produto_id"] = encoder.fit_transform(df["produto"])

    X = df[["produto_id", "estoque", "vendas", "dias_validade"]]
    y = df["perda"]

    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

    modelo = RandomForestClassifier()
    modelo.fit(X_train, y_train)
    return modelo, encoder

def classificar_risco(estoque, vendas, dias_validade, risco_perda):
    if risco_perda == 0:
        return "Baixo", "Nenhuma ação necessária"
    if dias_validade <= 2 and vendas < estoque * 0.5:
        return "Alto", "Colocar em promoção"
    if vendas < estoque * 0.7:
        return "Médio", "Reduzir compras futuras"
    return "Alto", "Colocar em promoção"

def prever_perda(df, modelo, encoder):
    df = df.copy()
    df["produto_id"] = encoder.transform(df["produto"])
    X = df[["produto_id", "estoque", "vendas", "dias_validade"]]
    df["risco_perda"] = modelo.predict(X)

    riscos = []
    recomendacoes = []

    for _, row in df.iterrows():
        risco, recomendacao = classificar_risco(
            row["estoque"], row["vendas"], row["dias_validade"], row["risco_perda"]
        )
        riscos.append(risco)
        recomendacoes.append(recomendacao)

    df["risco_classificado"] = riscos
    df["recomendacao"] = recomendacoes

    return df[["produto", "estoque", "vendas", "dias_validade", "risco_classificado", "recomendacao"]]
