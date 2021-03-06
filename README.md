# Desafio Modulo 1
## Enunciado

1. Realizar a ingestão dos dados do Censo Escolar 2020 no AWS S3 ou outro storage
de nuvem de sua escolha. Dados disponíveis em: https://www.gov.br/inep/ptbr/acesso-a-informacao/dados-abertos/microdados/censo-escolar. O método de
ingestão é livre. Os dados devem ser ingeridos na zona raw ou zona crua ou zona
bronze do seu Data Lake.

2. Utilizar alguma tecnologia de Big Data para transformar os dados no formato parquet
e escrevê-los na zona staging ou zona silver do seu Data Lake.

3. Fazer a integração com alguma engine de Data Lake. No caso da AWS, você deve:
    1. Configurar um Crawler para a pasta onde os arquivos na staging estão depositados;
    2. Validar a disponibilização no Athena.
    3. Caso deseje utilizar o Google, disponibilize os dados para consulta usando o BigQuery. Caso utilize outra nuvem, a escolha da engine de Data Lake é livre.

5. Use a ferramenta de Big Data ou a engine de Data Lake (ou o BigQuery, se escolher
trabalhar com Google Cloud) para investigar os dados e responder às perguntas do
desafio.

6. Quando o desenho da arquitetura estiver pronto, crie um repositório no Github (ou Gitlab, ou Bitbucket, ou outro de sua escolha) e coloque o código IaC para a
implantação da infraestrutura. Nenhum recurso deve ser implantado
manualmente.

## Execução
Utilizado o provedor AWS e terraform para a criação dos recursos como código. 

O deploy dos recursos é feito via git actions: 
* Pull request para o main é feita a validação do que será criado. 
* Merge no branch main os recursos são aplicados no provedor.