# Automação ETL com Python e Selenium
## Visão Geral do Projeto

Este projeto simula um cenário real de negócio, onde dados provenientes de um arquivo Excel precisam ser migrados para um sistema web que não possui integração via API, permitindo apenas o cadastro manual por meio de formulários online.

Para resolver esse problema, foi desenvolvido um pipeline de ETL automatizado, utilizando Python, tratamento de dados e automação web com Selenium.

 ## Contexto do Problema

Muitas empresas ainda utilizam sistemas legados que exportam dados em Excel.
Durante processos de migração, é comum que seja necessário cadastrar manualmente grandes volumes de informações em novos sistemas.

Este projeto simula situações como:

Cadastro de alunos

Registro de clientes

Migração de dados entre sistemas

Eliminação de tarefas manuais repetitivas

Arquitetura da Solução (ETL)

O projeto foi estruturado seguindo o conceito de ETL (Extract, Transform, Load):

Extract (Extração)

Leitura dos dados a partir de planilhas Excel utilizando Pandas.

Transform (Transformação)

Tratamento de valores nulos

Padronização de textos

Normalização de estados brasileiros (UF)

Validação e formatação de CPF

Conversão de tipos de dados

Garantia de qualidade dos dados antes da automação

Load (Carga)

Preenchimento automático de formulários web utilizando Selenium

Simulação real de interação humana com o sistema

## Tecnologias Utilizadas

Python

Pandas

Selenium

ETL

Automação Web

Tratamento e qualidade de dados
