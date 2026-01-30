
from etl.transform import data_treatment
from automation.google_form_bot import send_form


def main():
    df = data_treatment()

    send_form(df)

    print(df.head(10))
    print("✅ Cadastros finalizados com sucesso!")
  
if __name__ == "__main__":
    main()
