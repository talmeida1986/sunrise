# API Sunrise

 Fornece o pôr do sol e o nascer do sol para uma determinada latitude e longitude.

 ### Parâmetros de solicitação

    lat (float): Latitude em graus decimais. Exigido o que é necessário.
    lng (float): Longitude em graus decimais. Exigido o que é necessário.
    data (string): Data no formato YYYY-MM-DD. Também aceita outros formatos de data e até mesmo formatos de data relativa. Se não estiver presente, data de inadimplência para a data atual. Opcional.
    callback (string): Nome da função Callback para resposta JSONP. Opcional.
    formatado (integer): 0 ou 1 (1 é padrão). Os valores do tempo em resposta serão expressos após a ISO 8601 e day_length será expresso em segundos. Opcional.
    tzid (string): Um identificador de fuso horário, como por exemplo: UTC, África/Lagos, Ásia/Hong_Kong ou Europa/Lisboa. A lista de identificadores válidos está disponível nesta lista de fusos horários suportados. Se fornecido, os tempos na resposta serão referenciados ao fuso horário. Opcional.
