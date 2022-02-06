# summer
Projeto com a finalidade de estudo de implementações back-end.

## Comandos

### Contruir os conteiners dos serviços:
- docker-compose -f docker-compose.yml build
- docker-compose -f docker-compose.yml -f docker-compose.dev.yml build

### Subir o conteiner: com -d para rodar em backgroud
- docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d

### Verificar logs:
- docker-compose -f docker-compose.yml -f docker-compose.dev.yml logs -f "nome do serviço"

### Reiniciar o conteiner para aplicar as modificações:
- docker-compose -f docker-compose.yml -f docker-compose.dev.yml restart