# eduardo

#### Interface em Python para o [Robô Ed](http://www.ed.conpet.gov.br/br/converse.php)

## Uso

```
from eduardo import Ed

ed = Ed()

print('Pressione <ctrl> + C para sair')

while True:
    msg = input('Você: ')
    texto = ed.name + ': ' + ed.say(msg)
    print(texto)
```

Vide o script `dialogo.py` para um exemplo mais elaborado.

## Parâmetros

**name**: nome do robô (Eduardo por padrão)

**port**: necessária para a interação entre robôs distintos (8085 por padrão)

**server**: "servidor" de onde partirão os requests (0.0.0.0 por padrão)

**url**: url do servidor (URL do Robô Ed por padrão)
