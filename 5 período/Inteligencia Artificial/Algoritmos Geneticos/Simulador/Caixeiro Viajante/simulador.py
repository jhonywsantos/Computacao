# Simulacao de Algoritmo Genetico - Otimizacao de Rotas com Visualizacao Aprimorada
# Processing (Python Mode)
import random
import math

# -----------------------------------------
# Configuracoes
# -----------------------------------------
NUM_INDIVIDUOS = 8          # Numero de individuos na populacao em cada geracao
PRE_SELECTION_POOL_SIZE = 12 # Pool inicial para pre-selecao
ELITE_SIZE = 2
TAXA_MUTACAO = 0.2
GERACOES_ESTAGNADAS_MAX = 10 
FRAMES_TRANSICAO = 30
PAUSE_FRAMES = 120 

FITNESS_SCALE_FACTOR = 10000 

# Intervalo de cidades aleatorio
NUM_CIDADES_MIN = 5
NUM_CIDADES_MAX = 10

# Variavel global para o numero de cidades (definida em setup)
NUM_CIDADES = 0

# -----------------------------------------
# Estruturas de dados
# -----------------------------------------
class Individuo:
    def __init__(self, rota=None):
        if rota:
            self.rota = rota[:]
        else:
            self.rota = random.sample(range(NUM_CIDADES), NUM_CIDADES)
        self.fitness = self.calcular_fitness()
        self.elite = False
        self.mutado = False
        self.pais = None 

    def calcular_fitness(self):
        dist = 0
        for i in range(len(self.rota)):
            c1 = cidades[self.rota[i]]
            c2 = cidades[self.rota[(i+1) % len(self.rota)]]
            dist += dist_euclidiana(c1, c2)
        
        if dist == 0: return float('inf') 
        
        return (1 / dist) * FITNESS_SCALE_FACTOR

# -----------------------------------------
# Funcoes auxiliares do AG
# -----------------------------------------
def dist_euclidiana(c1, c2):
    return ((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2) ** 0.5

def criar_populacao_inicial_pool():
    return [Individuo() for _ in range(PRE_SELECTION_POOL_SIZE)]

def criar_populacao():
    return [Individuo() for _ in range(NUM_INDIVIDUOS)]

def selecao_elite(pop):
    pop_ordenada = sorted(pop, key=lambda ind: ind.fitness, reverse=True)
    for i, ind in enumerate(pop_ordenada):
        ind.elite = (i < ELITE_SIZE)
    return pop_ordenada

def crossover(pai, mae):
    start, end = sorted(random.sample(range(NUM_CIDADES), 2))
    filho_rota = [None] * NUM_CIDADES
    filho_rota[start:end] = pai.rota[start:end]
    
    pos = end
    for cidade in mae.rota:
        if cidade not in filho_rota:
            while filho_rota[pos % NUM_CIDADES] is not None:
                pos += 1
            filho_rota[pos % NUM_CIDADES] = cidade
            pos += 1
    
    filho = Individuo(filho_rota)
    filho.pais = (pai, mae)
    return filho

def mutacao(ind):
    if random.random() < TAXA_MUTACAO:
        i, j = random.sample(range(NUM_CIDADES), 2)
        ind.rota[i], ind.rota[j] = ind.rota[j], ind.rota[i]
        ind.mutado = True
        ind.fitness = ind.calcular_fitness()

def proxima_geracao(pop):
    nova_pop = []
    elite = selecao_elite(pop)[:ELITE_SIZE]
    nova_pop.extend(elite)
    
    while len(nova_pop) < NUM_INDIVIDUOS:
        total_fitness = sum(ind.fitness for ind in pop)
        
        pais = []
        for _ in range(2):
            roleta = random.uniform(0, total_fitness)
            acumulado = 0
            for ind in pop:
                acumulado += ind.fitness
                if acumulado >= roleta:
                    pais.append(ind)
                    break
        
        pai, mae = pais[0], pais[1]
        
        filho = crossover(pai, mae)
        mutacao(filho)
        nova_pop.append(filho)
        
    return nova_pop

# -----------------------------------------
# Setup e Draw
# -----------------------------------------
cidades = []
populacao = []
geracao = 0
prev_routes = []
anim_frame = 0
fitness_medias = []
fitness_melhor = []
global_state = "PAUSE" 
best_individual_final = None
geracoes_sem_melhora = 0
melhor_fitness_geral = 0
geracao_final_encontrada = 0
initial_pool = []

def setup():
    global cidades, populacao, geracao, prev_routes, anim_frame, global_state
    global fitness_medias, fitness_melhor, best_individual_final
    global geracoes_sem_melhora, melhor_fitness_geral, geracao_final_encontrada, NUM_CIDADES
    global initial_pool
    
    size(900, 600)
    textFont(createFont("Arial", 12))
    random.seed(random.randint(0, 10000))
    
    NUM_CIDADES = random.randint(NUM_CIDADES_MIN, NUM_CIDADES_MAX)

    cidades = [(random.randint(550, 850), random.randint(100, 550)) for _ in range(NUM_CIDADES)]
    initial_pool = criar_populacao_inicial_pool()
    populacao = []
    geracao = 0
    prev_routes = []
    anim_frame = 0
    
    fitness_medias = []
    fitness_melhor = []
    
    global_state = "PRE_SELECTION"
    best_individual_final = None
    geracoes_sem_melhora = 0
    melhor_fitness_geral = 0
    geracao_final_encontrada = 0
    
def draw():
    global populacao, geracao, prev_routes, anim_frame, global_state
    global fitness_medias, fitness_melhor, best_individual_final
    global geracoes_sem_melhora, melhor_fitness_geral, geracao_final_encontrada
    
    background(240)
    
    if global_state == "PRE_SELECTION":
        draw_pre_selection_panel()
        return

    draw_ui_panel()
    
    if global_state == "END":
        draw_best_route(best_individual_final.rota)
        return

    draw_map_and_routes()

    if global_state == "TRANSITION":
        anim_frame += 1
        if anim_frame > FRAMES_TRANSICAO:
            global_state = "PAUSE"
            anim_frame = 0
    elif global_state == "PAUSE":
        anim_frame += 1
        if anim_frame > PAUSE_FRAMES:
            if geracoes_sem_melhora >= GERACOES_ESTAGNADAS_MAX:
                best_individual_final = selecao_elite(populacao)[0]
                geracao_final_encontrada = geracao
                global_state = "END"
            else:
                prev_routes = [ind.rota[:] for ind in populacao]
                populacao = proxima_geracao(populacao)
                geracao += 1
                
                novo_melhor_fitness = selecao_elite(populacao)[0].fitness
                if novo_melhor_fitness > melhor_fitness_geral:
                    melhor_fitness_geral = novo_melhor_fitness
                    geracoes_sem_melhora = 0
                else:
                    geracoes_sem_melhora += 1
                
                fitness_medias.append(sum(ind.fitness for ind in populacao) / NUM_INDIVIDUOS)
                fitness_melhor.append(novo_melhor_fitness)
                
                global_state = "TRANSITION"
                anim_frame = 0
                
def draw_pre_selection_panel():
    fill(255)
    stroke(200)
    rect(10, 10, 500, 580, 8)
    
    fill(0)
    textSize(18)
    text("Pre-selecao da Populacao Inicial", 20, 30)
    
    textSize(14)
    text("Pressione 'espaco' para iniciar a evolucao", 20, 55)
    
    pop_draw = sorted(initial_pool, key=lambda ind: ind.fitness, reverse=True)
    
    box_w = 230
    box_h = 70
    margin_x = 10
    margin_y = 10
    
    for i, ind in enumerate(pop_draw):
        x_box = 20 + (i % 2) * (box_w + margin_x)
        y_box = 80 + (i // 2) * (box_h + margin_y)
        
        fill(255)
        stroke(200)
        
        if i < NUM_INDIVIDUOS:
            stroke(255, 215, 0)
            strokeWeight(3)
        else:
            stroke(200)
            strokeWeight(1)
            
        rect(x_box, y_box, box_w, box_h, 8)
        
        fill(200, 200, 255, 100)
        noStroke()
        rect(x_box + 5, y_box + 5, box_w-10, box_h-10, 5)

        fill(0)
        textSize(12)
        text("Fitness: {:.2f}".format(ind.fitness), x_box + 15, y_box + 25)
        
        textSize(10)
        rota_txt = "->".join([chr(65+c) for c in ind.rota])
        text("Rota: {}".format(rota_txt), x_box + 15, y_box + 45)
        
    draw_pre_selection_map()

def draw_pre_selection_map():
    map_x_offset = 550
    map_y_offset = 100
    map_width = width - map_x_offset - 50 
    map_height = height - map_y_offset - 50
    
    min_x = min(cidade_x for cidade_x, cidade_y in cidades)
    max_x = max(cidade_x for cidade_x, cidade_y in cidades)
    min_y = min(cidade_y for cidade_x, cidade_y in cidades)
    max_y = max(cidade_y for cidade_x, cidade_y in cidades)
    
    range_x = max_x - min_x
    range_y = max_y - min_y
    
    scale_x = map_width / range_x if range_x != 0 else 1
    scale_y = map_height / range_y if range_y != 0 else 1
    scale = min(scale_x, scale_y)
    
    center_x = map_x_offset + map_width / 2
    center_y = map_y_offset + map_height / 2
    
    cities_center_x = min_x + range_x / 2
    cities_center_y = min_y + range_y / 2

    # Desenha todas as rotas do pool inicial
    stroke(0, 100, 255, 60)
    strokeWeight(1)
    for ind in initial_pool:
        for j in range(len(ind.rota)):
            x1, y1 = cidades[ind.rota[j]]
            x2, y2 = cidades[ind.rota[(j+1) % len(ind.rota)]]
            
            scaled_x1 = (x1 - cities_center_x) * scale + center_x
            scaled_y1 = (y1 - cities_center_y) * scale + center_y
            scaled_x2 = (x2 - cities_center_x) * scale + center_x
            scaled_y2 = (y2 - cities_center_y) * scale + center_y
            
            line(scaled_x1, scaled_y1, scaled_x2, scaled_y2)

    # Desenha as cidades por cima
    for idx_cidade, (x, y) in enumerate(cidades):
        scaled_x = (x - cities_center_x) * scale + center_x
        scaled_y = (y - cities_center_y) * scale + center_y
        fill(0, 150, 0)
        ellipse(scaled_x, scaled_y, 12, 12)
        fill(255)
        textSize(10)
        textAlign(CENTER, CENTER)
        text(chr(65+idx_cidade), int(scaled_x), int(scaled_y))
        textAlign(LEFT, BASELINE)
    
def draw_ui_panel():
    panel_w = 500
    panel_h = 580
    rect(10, 10, panel_w, panel_h, 8)
    
    fill(0)
    textSize(18)
    text("Algoritmo Genetico - Otimizacao de Rotas", 20, 30)
    
    if global_state != "END":
        textSize(14)
        text("Geracao: {}".format(geracao + 1), 20, 55)
        draw_legend(20, 80)
        draw_individuals(20, 150)
        draw_stats_graph(20, 455, 480, 120) 
    else:
        draw_final_info(20, 55)

def draw_final_info(x, y):
    textSize(14)
    fill(0, 100, 0)
    text("SIMULACAO CONCLUIDA!", x, y)
    
    fill(0)
    text("Melhor Rota Encontrada:", x, y + 30)
    
    if best_individual_final:
        rota_txt = "->".join([chr(65+c) for c in best_individual_final.rota])
        text("Geracao: {}".format(geracao_final_encontrada), x + 20, y + 60)
        text("Rota: {}".format(rota_txt), x + 20, y + 80)
        text("Fitness: {:.2f}".format(best_individual_final.fitness), x + 20, y + 100)

def draw_legend(x, y):
    noStroke()
    
    fill(255, 215, 0)
    ellipse(x + 10, y, 15, 15)
    fill(0)
    text("Elite", x + 30, y + 5)

    fill(255, 100, 100)
    ellipse(x + 10, y + 20, 15, 15)
    fill(0)
    text("Mutado", x + 30, y + 25)

    fill(180)
    ellipse(x + 10, y + 40, 15, 15)
    fill(0)
    text("Normal", x + 30, y + 45)

def draw_individuals(x_base, y_base):
    box_w = 230
    box_h = 70
    margin_x = 10
    margin_y = 10
    
    pop_draw = sorted(populacao, key=lambda ind: ind.fitness, reverse=True)

    for i, ind in enumerate(pop_draw):
        x_box = x_base + (i % 2) * (box_w + margin_x)
        y_box = y_base + (i // 2) * (box_h + margin_y)
        
        fill(255)
        stroke(200)
        rect(x_box, y_box, box_w, box_h, 8)
        
        if ind.elite:
            stroke(255, 215, 0)
            strokeWeight(3)
        elif ind.mutado:
            stroke(255, 0, 0)
            strokeWeight(2)
        else:
            stroke(100)
            strokeWeight(1)
            
        fill(200, 200, 255, 100)
        rect(x_box + 5, y_box + 5, box_w-10, box_h-10, 5)

        fill(0)
        textSize(12)
        text("Fitness: {:.2f}".format(ind.fitness), x_box + 15, y_box + 25)
        
        textSize(10)
        rota_txt = "->".join([chr(65+c) for c in ind.rota])
        text("Rota: {}".format(rota_txt), x_box + 15, y_box + 45)
        
        if ind.pais:
            fill(0, 150, 0)
            text("Filho da G{}.".format(geracao), x_box + 15, y_box + 60)

def draw_map_and_routes():
    if best_individual_final: return
    
    map_x_offset = 550
    map_y_offset = 100
    map_width = width - map_x_offset - 50 
    map_height = height - map_y_offset - 50
    
    min_x = min(cidade_x for cidade_x, cidade_y in cidades)
    max_x = max(cidade_x for cidade_x, cidade_y in cidades)
    min_y = min(cidade_y for cidade_x, cidade_y in cidades)
    max_y = max(cidade_y for cidade_x, cidade_y in cidades)
    
    range_x = max_x - min_x
    range_y = max_y - min_y
    
    scale_x = map_width / range_x if range_x != 0 else 1
    scale_y = map_height / range_y if range_y != 0 else 1
    scale = min(scale_x, scale_y)
    
    center_x = map_x_offset + map_width / 2
    center_y = map_y_offset + map_height / 2
    
    cities_center_x = min_x + range_x / 2
    cities_center_y = min_y + range_y / 2
    
    for idx_cidade, (x, y) in enumerate(cidades):
        scaled_x = (x - cities_center_x) * scale + center_x
        scaled_y = (y - cities_center_y) * scale + center_y
        fill(0, 150, 0)
        ellipse(scaled_x, scaled_y, 12, 12)
        fill(255)
        textSize(10)
        textAlign(CENTER, CENTER)
        text(chr(65+idx_cidade), int(scaled_x), int(scaled_y))
        textAlign(LEFT, BASELINE)
    
    t = anim_frame / float(FRAMES_TRANSICAO)
    if t > 1: t = 1
    
    for ind_idx, ind in enumerate(populacao):
        stroke(0, 100, 255, 120)
        strokeWeight(1)
        
        if ind_idx < len(prev_routes):
            prev_rota = prev_routes[ind_idx]
        else:
            prev_rota = ind.rota
            
        for j in range(len(ind.rota)):
            cidade_prev_idx = prev_rota[j % len(prev_rota)]
            cidade_new_idx = ind.rota[j % len(ind.rota)]
            
            x1_prev, y1_prev = cidades[cidade_prev_idx % len(cidades)]
            x1_new, y1_new = cidades[cidade_new_idx % len(cidades)]
            
            x2_prev, y2_prev = cidades[prev_rota[(j+1) % len(prev_rota)] % len(cidades)]
            x2_new, y2_new = cidades[ind.rota[(j+1) % len(ind.rota)] % len(cidades)]
            
            scaled_x1_prev = (x1_prev - cities_center_x) * scale + center_x
            scaled_y1_prev = (y1_prev - cities_center_y) * scale + center_y
            scaled_x1_new = (x1_new - cities_center_x) * scale + center_x
            scaled_y1_new = (y1_new - cities_center_y) * scale + center_y
            
            scaled_x2_prev = (x2_prev - cities_center_x) * scale + center_x
            scaled_y2_prev = (y2_prev - cities_center_y) * scale + center_y
            scaled_x2_new = (x2_new - cities_center_x) * scale + center_x
            scaled_y2_new = (y2_new - cities_center_y) * scale + center_y
            
            x1 = lerp(scaled_x1_prev, scaled_x1_new, t)
            y1 = lerp(scaled_y1_prev, scaled_y1_new, t)
            
            x2 = lerp(scaled_x2_prev, scaled_x2_new, t)
            y2 = lerp(scaled_y2_prev, scaled_y2_new, t)
            
            line(x1, y1, x2, y2)

def draw_best_route(rota):
    map_x_offset = 550
    map_y_offset = 100
    map_width = width - map_x_offset - 50
    map_height = height - map_y_offset - 50
    
    min_x = min(cidade_x for cidade_x, cidade_y in cidades)
    max_x = max(cidade_x for cidade_x, cidade_y in cidades)
    min_y = min(cidade_y for cidade_x, cidade_y in cidades)
    max_y = max(cidade_y for cidade_x, cidade_y in cidades)
    
    range_x = max_x - min_x
    range_y = max_y - min_y
    
    scale_x = map_width / range_x if range_x != 0 else 1
    scale_y = map_height / range_y if range_y != 0 else 1
    scale = min(scale_x, scale_y)
    
    center_x = map_x_offset + map_width / 2
    center_y = map_y_offset + map_height / 2
    
    cities_center_x = min_x + range_x / 2
    cities_center_y = min_y + range_y / 2
    
    for idx_cidade, (x, y) in enumerate(cidades):
        scaled_x = (x - cities_center_x) * scale + center_x
        scaled_y = (y - cities_center_y) * scale + center_y
        fill(0, 150, 0)
        ellipse(scaled_x, scaled_y, 12, 12)
        fill(255)
        textSize(10)
        textAlign(CENTER, CENTER)
        text(chr(65+idx_cidade), int(scaled_x), int(scaled_y))
        textAlign(LEFT, BASELINE)
    
    stroke(255, 0, 0)
    strokeWeight(3)
    for j in range(len(rota)):
        x1, y1 = cidades[rota[j % len(rota)] % len(cidades)]
        x2, y2 = cidades[rota[(j+1) % len(rota)] % len(cidades)]
        
        scaled_x1 = (x1 - cities_center_x) * scale + center_x
        scaled_y1 = (y1 - cities_center_y) * scale + center_y
        scaled_x2 = (x2 - cities_center_x) * scale + center_x
        scaled_y2 = (y2 - cities_center_y) * scale + center_y
        
        line(scaled_x1, scaled_y1, scaled_x2, scaled_y2)
        
def draw_stats_graph(x, y, w, h):
    graph_h = 80 
    
    fill(0)
    textSize(14)
    text("Evolucao da Pontuacao", x, y)
    
    stroke(100); noFill(); rect(x, y + 10, w, graph_h); noStroke()

    if len(fitness_medias) > 1:
        max_fitness = max(max(fitness_medias), max(fitness_melhor))
        min_fitness = 0
        denom = max_fitness - min_fitness if max_fitness > min_fitness else 1.0
        
        stroke(0, 100, 255)
        strokeWeight(2)
        noFill()
        beginShape()
        for i, m in enumerate(fitness_medias):
            px = map(i, 0, max(1, len(fitness_medias)-1), x, x+w)
            py = map(m, min_fitness, max_fitness, y + graph_h + 10, y + 10)
            vertex(px, py)
        endShape()

        stroke(255, 215, 0)
        strokeWeight(2)
        noFill()
        beginShape()
        for i, m in enumerate(fitness_melhor):
            px = map(i, 0, max(1, len(fitness_melhor)-1), x, x+w)
            py = map(m, min_fitness, max_fitness, y + graph_h + 10, y + 10)
            vertex(px, py)
        endShape()
        
    if len(fitness_medias) > 0:
        fill(0)
        textSize(12)
        text("Media Atual: {:.2f}".format(fitness_medias[-1]), x, y + graph_h + 30)
        text("Melhor Atual: {:.2f}".format(fitness_melhor[-1]), x + w/2, y + graph_h + 30)
        
    fill(0)
    textSize(12)
    text("Geracoes sem melhora: {}/{}".format(geracoes_sem_melhora, GERACOES_ESTAGNADAS_MAX), x, y + graph_h + 50)

def keyPressed():
    global global_state, anim_frame, populacao, initial_pool
    if key == ' ':
        if global_state == "PRE_SELECTION":
            # Realiza a selecao e inicializa a primeira geracao
            populacao = sorted(initial_pool, key=lambda ind: ind.fitness, reverse=True)[:NUM_INDIVIDUOS]
            
            global fitness_medias, fitness_melhor, melhor_fitness_geral
            fitness_medias.append(sum(ind.fitness for ind in populacao) / NUM_INDIVIDUOS)
            melhor_fitness = selecao_elite(populacao)[0].fitness
            fitness_melhor.append(melhor_fitness)
            melhor_fitness_geral = melhor_fitness
            
            global_state = "PAUSE"
            anim_frame = 0
            
        elif global_state == "PAUSE":
            anim_frame = PAUSE_FRAMES
        elif global_state == "TRANSITION":
            anim_frame = FRAMES_TRANSICAO
    
    if key == 'r':
        setup()

def mousePressed():
    setup()