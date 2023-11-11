Serão 3 sistemas: Alpha, Beta e Gama

Alpha: Sistema de geração de CTEs
    O Alpha precisa gerar arquivos de CTE de forma constante mas sem uma cadencia exata, precisa ser algo randomico
    
    Dentro de cada arquivo, precisa conter uma chave númerica de 256 digitos, gerados a partir de algum padrão que ainda precisa ser definido
    
    A cada 100 códigos gerados, 5% deve estar fora de conformidade com o padrão.
        Como posso criar um erro sistematico?
    
    Os arquivos devem ser enviados para a pasta ROOT em um FTP



Beta: Sistema de Leitura das CTEs
    O Beta precisa rodar a cada 10 minutos
    Precisa acessar a pasta ROOT no FPT, aonde o Alpha está disponibilizando os arquivos
    Precisa abrir um arquivo por vez
    Analisar a chave númerica dentro do arquivo
        Se a chave estiver certa, deve mover o arquivo TXT para a pasta SUCCESS
        Se a chave estiver errada, deve mover o arquivo TXT para a pasta FAIL




Gama: Sistema de tratamento das CTEs que falharem no processo de leitura do Beta