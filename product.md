# Projeto

Para `[idosos ou cuidam de idosos]`, cujo `[problema que precisa ser resolvido é existe um número considerável queda de idosos em ambientes doméstico isso tanto no Brasil quanto no Mundo]`, o `[projeto de app para amenizar esse problema]` é um `[categoria do produto de acessibilidade],`que diferentemente do `[alternativas`], o nosso produto `[possui viés de ser inédito]`.

### Problemas

1) Problema 1 : Segundo dados do Ministério da Saúde,  70% das quedas em idosos ocorrem dentro de casa e acometem idosos com mais de 65 anos. Em idosos acima de 80 anos , a prevalência é ainda mais alta e a mortalidade associada a quedas chega a ser seis vezes maior.
2) Problema 2 : Necessidade de cuidar das quedas do idosos
3) Problema 3 : Necessidade de centralização da resolução desse problema em um único local

### Expectativas

1) Expectativa 1 : Amenizar as consequências da queda. Uma vez que o atendimento seria agilizado.
2) Expectativa 2 : Melhorar a qualidade de vida das pessoas idosas
3) Expectativa 3 : Centralizar esse tipo de cuidado

## Personas

Uma persona representa um usuário do produto e essa descrição deve falar não só o papel, mas também suas necessidades e seus objetivos. Isso cria uma representação realista dos usuários, auxiliando a equipe a descrever funcionalidades a partir do ponto de vista de quem vai usar o produto (Aguiar, 2021).

-Persona cuidador : Um pessoa que possui um parente ou alguém sob seus cuidados e deseja ter um maior controle sobre a situação da pessoa idosa 
-Persona paciente : Um pessoa idosa que está pensando na sua condinção mais debilitada e percebe que precisa de mais cuidados 

### Persona Maria, 75 anos

*O que ela faz?*
Maria é uma idosa que vive sozinha e tem mobilidade reduzida.

*O que ela espera?*
Maria espera um sistema que a ajude a se sentir segura em casa, sabendo que será assistida rapidamente em caso de uma queda.

### Persona João, 35 anos

*O que ela faz?*
João é filho de Maria e seu cuidador principal, mas trabalha fora e não pode estar sempre presente.

*O que ela espera?*
João espera um aplicativo que o avise imediatamente se sua mãe cair, permitindo que ele tome providências rápidas para ajudá-la.

## Marcos

Devemos entregar **pequenas versões frequentes**. A equipe deve definir os marcos do projeto (*milestones)*, definindo os prazos de entrega e quais funcionalidades serão implementados até o final de cada marco. No final de cada marco devemos distribuir uma nova versão do produto, pronta para produção.

Podemos pensar nessas pequenas versões como MVPs (do inglês, *minimum viable product*). MVP é a versão mais simples de um produto que pode ser disponibilizada para a validação de um pequeno conjunto de hipóteses sobre o negócio. Após ser **construído,** o MVP é colocado à prova. Com isso, teremos dados que possibilitam **medir** o seu uso e, portanto, gerar o **aprendizado** desejado (Caroli, 2018).

### Marco 1 - 20/12/2022

Acreditamos que esse `Marco 1` vai conseguir `Uma interface intuitiva para o aplicativo e um servidor para cadastro dos responsáveis`. Saberemos que isso aconteceu com base em `métricas para validar a hipótese do negócio`.

#### Funcionalidades

- [x] Funcionalidade 1. Interfce do app onde onde o responsável pelo idoso terá o acesso.
- [ ] Funcionalidade 2. Backend para cadastro dos responsáveis.

[Release Notes ](release_notes_1.md)

### Marco 2 - 20/01/2023

Acreditamos que esse `Marco 2` vai conseguir `O treinamento de um modelo inicial capaz de identificar quedas`. Saberemos que isso aconteceu com base em `métricas para validar a hipótese do negócio`.

#### Funcionalidades

- [x] Funcionalidade 1. Um modelo capaz de identificar uma queda.

### Marco 3 - 20/01/2023

Acreditamos que esse `Marco 3` vai conseguir `Uma integração da câmera do computador com o servidor do modelo de IA`. Saberemos que isso aconteceu com base em `métricas para validar a hipótese do negócio`.

#### Funcionalidades

- [x] Funcionalidade 1. A partir da câmera do computador, seramos capazes de identificar quedas.


### Marco 4 - 20/01/2023

Acreditamos que esse `Marco 4` vai conseguir `Uma integração entre a captura da imagem, o servidor do modelo e o app`. Saberemos que isso aconteceu com base em `métricas para validar a hipótese do negócio`.

- [x] Funcionalidade 1. Ao detectar uma queda, o sistema avisará ao responsável sobre o ocorrido.


[Release Notes ](release_notes_1.md)

## Riscos

1. **Risco 1** Qualidade do modelo. *Severidade Alta e Probabilidade Alta*.

   Ações para mitigação do risco:

   * Ação de mitigação 1.1. Encontrar boas bases para o treinamento da rede neural.

2. **Invasão de privacidade dos usuários.** *Severidade Alta e Probabilidade Média*.

   Ações para mitigação do risco:

   * Garantir a criptografia de todos os dados.
   * Implementar políticas de privacidade robustas.

3. **Baixa ou Nenhuma conexão com a internet.** *Severidade Alto e Probabilidade baixa*.


## Componentes

### Aplicativo Mobile
No aplicativo, o responsável pelo idoso será avisado caso uma queda seja detectada. No momento em que for avisado, ele terá acesso a uma foto do momento.
https://github.com/edgebr/templates-artefatos

### Servidor para o modelo de IA
No servidor, ao receber a gravação em tempo real, o modelo será capaz de detectar uma queda e o aviso será enviado.

### Servidor para backend
No servidor, será possível realizar cadastro dos usuários e responsáveis. Armenezar informações.

## Stakeholders

Stakeholder 1 <br />
*Key User - Cargo na Empresa X* <br />
*E-mail* <br />
(xx) xxxxx-xxxx

Stakeholder 2 <br />
*Key User - Cargo na Empresa X* <br />
*E-mail* <br />
(xx) xxxxx-xxxx

## Equipe

Itallo Ramon Veiga Paranhos <br />
*Cargo à definir* <br />
*irvp@ic.ufal.br* <br />
https://github.com/italloramon

José Anthony Dantas Santana <br />
*Desenvolvedor Sênior* <br />
*E-mail* <br />
https://github.com/edgebr

Membro 3 <br />
*Analista de Qualidade Pleno* <br />
*E-mail* <br />
https://github.com/edgebr

## Status Reports

[Status Report 1 (20/12/2022)](status_report_1.md)
