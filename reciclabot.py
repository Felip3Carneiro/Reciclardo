import discord
from discord.ext import commands
import time, random

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='#', intents=intents)

@bot.event
async def on_ready():
    print(f"Eu sou {bot.user}| ID {bot.user.id}")

@bot.command()
async def AJUDA(ctx):
    embed = discord.Embed(title="Comandos do Bot", description="Aqui estão os comandos disponíveis:", color=0x00ff00)#Verde em hexa rgb->(0, 255, 0)
    embed.add_field(name="#DICADODIA", value="Receba uma dica diária", inline=True)
    embed.add_field(name="#DICA", value="Receba uma dica aleatória", inline=True)
    embed.add_field(name="#REUTILIZAR [material]", value="Receba uma sugestão de como reutilizar o material sugestido", inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def DICADODIA(ctx):
    dicas = [
    "Planeje suas refeições da semana para evitar comprar comida em excesso.",
    "Faça uma lista de compras e siga ela para evitar compras desnecessárias.",
    "Armazene alimentos corretamente para aumentar sua durabilidade.",
    "Aproveite sobras de refeições em novas receitas.",
    "Congele alimentos que não serão consumidos rapidamente.",
    "Prefira produtos com menos embalagens.",
    "Reutilize potes e recipientes sempre que possível.",
    "Evite o uso de descartáveis como copos e talheres.",
    "Leve sua própria garrafa de água reutilizável.",
    "Use sacolas reutilizáveis ao fazer compras.",
    "Compre apenas o necessário, evitando desperdício por validade vencida.",
    "Dê preferência a produtos duráveis ao invés de descartáveis.",
    "Repare objetos quebrados antes de considerar descartá-los.",
    "Doe roupas e objetos que não usa mais.",
    "Evite desperdício de água ao escovar os dentes ou lavar louça.",
    "Tome banhos mais curtos para economizar água e energia.",
    "Desligue aparelhos eletrônicos quando não estiverem em uso.",
    "Use lâmpadas de baixo consumo energético.",
    "Aproveite ao máximo a luz natural durante o dia.",
    "Separe o lixo reciclável corretamente.",
    "Composte resíduos orgânicos, se possível.",
    "Evite imprimir documentos desnecessariamente.",
    "Utilize os dois lados do papel ao imprimir ou escrever.",
    "Prefira produtos digitais em vez de físicos quando possível.",
    "Evite compras por impulso, refletindo antes de adquirir algo.",
    "Priorize qualidade em vez de quantidade nas compras.",
    "Reaproveite materiais para projetos ou estudos.",
    "Compartilhe ou empreste itens que são pouco usados.",
    "Evite o desperdício de alimentos no prato, servindo-se com consciência.",
    "Observe datas de validade e organize alimentos por ordem de uso.",
    "Adote o hábito de revisar o que você já tem antes de comprar mais."
    ]
    dia = time.strftime("%d/%m", time.localtime())
    await ctx.send(f"Dica do dia: {dia}")
    await ctx.send(dicas[int(time.strftime("%d", time.localtime())) - 1])

@bot.command()
async def DICA(ctx):
    dicas = [
    "Planeje suas refeições da semana para evitar comprar comida em excesso.",
    "Faça uma lista de compras e siga ela para evitar compras desnecessárias.",
    "Armazene alimentos corretamente para aumentar sua durabilidade.",
    "Aproveite sobras de refeições em novas receitas.",
    "Congele alimentos que não serão consumidos rapidamente.",
    "Prefira produtos com menos embalagens.",
    "Reutilize potes e recipientes sempre que possível.",
    "Evite o uso de descartáveis como copos e talheres.",
    "Leve sua própria garrafa de água reutilizável.",
    "Use sacolas reutilizáveis ao fazer compras.",
    "Compre apenas o necessário, evitando desperdício por validade vencida.",
    "Dê preferência a produtos duráveis ao invés de descartáveis.",
    "Repare objetos quebrados antes de considerar descartá-los.",
    "Doe roupas e objetos que não usa mais.",
    "Evite desperdício de água ao escovar os dentes ou lavar louça.",
    "Tome banhos mais curtos para economizar água e energia.",
    "Desligue aparelhos eletrônicos quando não estiverem em uso.",
    "Use lâmpadas de baixo consumo energético.",
    "Aproveite ao máximo a luz natural durante o dia.",
    "Separe o lixo reciclável corretamente.",
    "Composte resíduos orgânicos, se possível.",
    "Evite imprimir documentos desnecessariamente.",
    "Utilize os dois lados do papel ao imprimir ou escrever.",
    "Prefira produtos digitais em vez de físicos quando possível.",
    "Evite compras por impulso, refletindo antes de adquirir algo.",
    "Priorize qualidade em vez de quantidade nas compras.",
    "Reaproveite materiais para projetos ou estudos.",
    "Compartilhe ou empreste itens que são pouco usados.",
    "Evite o desperdício de alimentos no prato, servindo-se com consciência.",
    "Observe datas de validade e organize alimentos por ordem de uso.",
    "Adote o hábito de revisar o que você já tem antes de comprar mais."
    ]
    await ctx.send(f"dica aleatória: {random.choice(dicas)}")

@bot.command()
async def REUTILIZAR(ctx, *, material:str):
    materiais = {
    "garrafa pet": "Transformar em vasos de plantas ou regadores",
    "potes de vidro": "Armazenar alimentos ou usar como organizadores",
    "latas de aluminio": "Criar porta-lápis ou pequenos vasos",
    "papel usado": "Utilizar como rascunho ou bloco de anotações",
    "caixas de papelao": "Montar organizadores ou caixas de armazenamento",
    "roupas velhas": "Transformar em panos de limpeza",
    "meias sem_par": "Usar para limpeza ou proteger objetos frágeis",
    "garrafas de vidro": "Fazer luminárias ou decoração",
    "jornais": "Usar para limpeza de vidros ou embalar objetos",
    "sacolas plasticas": "Reutilizar como sacos de lixo",
    "caixas de ovos": "Organizar pequenos itens ou plantar mudas",
    "tubos de papel higienico": "Organizar cabos ou fazer artesanato",
    "escovas de dente usadas": "Limpar áreas pequenas",
    "camisetas velhas": "Transformar em ecobags",
    "potes de sorvete": "Armazenar alimentos ou objetos"
    }
    if material.lower() in materiais:
        await ctx.send(f"Com {material.capitalize()} dá para fazer: {materiais[material]}")
    else:
        await ctx.send("Esse material ainda não foi reutilizado")

if __name__ == "__main__":  
    bot.run(Sua chave aqui!!!)
