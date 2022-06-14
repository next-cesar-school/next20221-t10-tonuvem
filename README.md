# next20221-t10-tonuvem

## Controle de Armazenamento de Arquivos na Nuvem

#### Contexto:
    Com a finalidade de limitar o armazenamento de arquivos em um serviço de nuvem por um determinado usuário dependendo do plano contratado por ele. É necessário um serviço que controle o número de arquivos e capacidade de armazenamento de acordo com o plano do usuário.

#### Objetivo:
    Implementar uma API que fornece operações necessárias para:

    - Cadastrar/Atualizar usuário definindo o plano contratado por ele.
    - Receber o arquivo e armazenar em algum serviço na nuvem (AWS, Google Cloud, IBM Cloud, etc.). Ao receber o arquivo, deverá haver uma validação de acordo com o plano do usuário, verificando se o usuário possui espaço livre de armazenamento.
    - Remover arquivo do armazenamento.
    - Listar arquivos armazenados, de preferência com paginação.
    - Status do armazenamento: espaço disponível e número de arquivos.
