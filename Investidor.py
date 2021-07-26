import Utils #módulo com funções genéricas que auxiliam nos cálculos

#classe que representa um investidor e possui os atributos cpf, carteira e perfil
class Investidor:
    
    #função construtora que recebe cpf e a carteira, o perfil é definido ao chamarmos a função identificar_perfil
    def __init__(self, cpf, carteira, perfil = 'Indefinido'):
        self.cpf = cpf
        self.carteira_investimentos = carteira
        self.perfil = perfil
        
    #identifica o perfil desse investidor em comparação com o perfil de outros investidores usando o algoritmo KNN
    #pode-se definir o k, sendo o automático k = 5
    def identificar_perfil(self, k = 5):
        '''identifica o perfil do investidor, entre conservador, moderado ou agressivo'''
        
        #vetor com objetos do tipo Investidor
        dados = [Investidor(cpf=66707599984, perfil='Conservador', carteira = (5100., 3500., 1400., 200.)),
        Investidor(cpf=55695397315, perfil='Conservador', carteira = (4900., 3000., 1400., 200.)),
        Investidor(cpf=63743886918, perfil='Conservador', carteira = (4700., 3200., 1300., 200.)),
        Investidor(cpf=55941368774, perfil='Conservador', carteira = (4600., 3100., 1500., 200.)),
        Investidor(cpf=75486280874, perfil='Conservador', carteira = (5000., 3600., 1400., 200.)),
        Investidor(cpf=53164949799, perfil='Conservador', carteira = (5400., 3900., 1700., 400.)),
        Investidor(cpf=39898704131, perfil='Conservador', carteira = (4600., 3400., 1400., 300.)),
        Investidor(cpf=53740901207, perfil='Conservador', carteira = (5000., 3400., 1500., 200.)),
        Investidor(cpf=51735950236, perfil='Conservador', carteira = (4400., 2900., 1400., 200.)),
        Investidor(cpf=47305108951, perfil='Conservador', carteira = (4900., 3100., 1500., 100.)),
        Investidor(cpf=63858864633, perfil='Conservador', carteira = (5400., 3700., 1500., 200.)),
        Investidor(cpf=53363167240, perfil='Conservador', carteira = (4800., 3400., 1600., 200.)),
        Investidor(cpf=72133754195, perfil='Conservador', carteira = (4800., 3000., 1400., 100.)),
        Investidor(cpf=52802483512, perfil='Conservador', carteira = (4300., 3000., 1100., 100.)),
        Investidor(cpf=57925287214, perfil='Conservador', carteira = (4800., 3400., 1900., 200.)),
        Investidor(cpf=74354632224, perfil='Conservador', carteira = (5000., 3000., 1600., 200.)),
        Investidor(cpf=64020216626, perfil='Conservador', carteira = (5000., 3400., 1600., 400.)),
        Investidor(cpf=78223722856, perfil='Conservador', carteira = (5200., 3500., 1500., 200.)),
        Investidor(cpf=58245228846, perfil='Conservador', carteira = (5200., 3400., 1400., 200.)),
        Investidor(cpf=74490686776, perfil='Conservador', carteira = (4700., 3200., 1600., 200.)),
        Investidor(cpf=48646824781, perfil='Conservador', carteira = (4800., 3100., 1600., 200.)),
        Investidor(cpf=77381458676, perfil='Conservador', carteira = (5400., 3400., 1500., 400.)),
        Investidor(cpf=41615431874, perfil='Conservador', carteira = (5200., 4100., 1500., 100.)),
        Investidor(cpf=52163844491, perfil='Conservador', carteira = (5500., 4200., 1400., 200.)),
        Investidor(cpf=70276304567, perfil='Conservador', carteira = (4900., 3100., 1500., 200.)),
        Investidor(cpf=69119828185, perfil='Conservador', carteira = (5000., 3200., 1200., 200.)),
        Investidor(cpf=65441690046, perfil='Conservador', carteira = (5500., 3500., 1300., 200.)),
        Investidor(cpf=56457227894, perfil='Conservador', carteira = (4900., 3600., 1400., 100.)),
        Investidor(cpf=46939428126, perfil='Conservador', carteira = (4400., 3000., 1300., 200.)),
        Investidor(cpf=60979942480, perfil='Conservador', carteira = (5100., 3400., 1500., 200.)),
        Investidor(cpf=41648583220, perfil='Conservador', carteira = (5000., 3500., 1300., 300.)),
        Investidor(cpf=50376331791, perfil='Conservador', carteira = (4500., 2300., 1300., 300.)),
        Investidor(cpf=67008801023, perfil='Conservador', carteira = (4400., 3200., 1300., 200.)),
        Investidor(cpf=72149193419, perfil='Conservador', carteira = (5000., 3500., 1600., 600.)),
        Investidor(cpf=62830733382, perfil='Conservador', carteira = (5100., 3800., 1900., 400.)),
        Investidor(cpf=56716675811, perfil='Conservador', carteira = (4800., 3000., 1400., 300.)),
        Investidor(cpf=61089667146, perfil='Conservador', carteira = (5100., 3800., 1600., 200.)),
        Investidor(cpf=47795509468, perfil='Conservador', carteira = (4600., 3200., 1400., 200.)),
        Investidor(cpf=60899885693, perfil='Conservador', carteira = (5300., 3700., 1500., 200.)),
        Investidor(cpf=53433670705, perfil='Conservador', carteira = (5000., 3300., 1400., 200.)),
        Investidor(cpf=54850120580, perfil='Moderado', carteira = (7000., 3200., 4700., 1400.)),
        Investidor(cpf=71457789994, perfil='Moderado', carteira = (6400., 3200., 4500., 1500.)),
        Investidor(cpf=67692777563, perfil='Moderado', carteira = (6900., 3100., 4900., 1500.)),
        Investidor(cpf=43133573182, perfil='Moderado', carteira = (5500., 2300., 4000., 1300.)),
        Investidor(cpf=55150612815, perfil='Moderado', carteira = (6500., 2800., 4600., 1500.)),
        Investidor(cpf=48211725243, perfil='Moderado', carteira = (5700., 2800., 4500., 1300.)),
        Investidor(cpf=76686463776, perfil='Moderado', carteira = (6300., 3300., 4700., 1600.)),
        Investidor(cpf=71971000560, perfil='Moderado', carteira = (4900., 2400., 3300., 1000.)),
        Investidor(cpf=40307235992, perfil='Moderado', carteira = (6600., 2900., 4600., 1300.)),
        Investidor(cpf=44826533081, perfil='Moderado', carteira = (5200., 2700., 3900., 1400.)),
        Investidor(cpf=45735414894, perfil='Moderado', carteira = (5900., 3200., 4800., 1800.)),
        Investidor(cpf=57137146514, perfil='Moderado', carteira = (6100., 2800., 4000., 1300.)),
        Investidor(cpf=53657058251, perfil='Moderado', carteira = (6300., 2500., 4900., 1500.)),
        Investidor(cpf=52941460485, perfil='Moderado', carteira = (6100., 2800., 4700., 1200.)),
        Investidor(cpf=44306600683, perfil='Moderado', carteira = (6400., 2900., 4300., 1300.)),
        Investidor(cpf=43460747924, perfil='Moderado', carteira = (6600., 3000., 4400., 1400.)),
        Investidor(cpf=75590376075, perfil='Moderado', carteira = (6800., 2800., 4800., 1400.)),
        Investidor(cpf=68267282206, perfil='Moderado', carteira = (6700., 3000., 5000., 1700.)),
        Investidor(cpf=77567920298, perfil='Moderado', carteira = (6000., 2900., 4500., 1500.)),
        Investidor(cpf=67600419504, perfil='Moderado', carteira = (5700., 2600., 3500., 1000.)),
        Investidor(cpf=44902189811, perfil='Moderado', carteira = (5500., 2400., 3800., 1100.)),
        Investidor(cpf=62966866614, perfil='Moderado', carteira = (5500., 2400., 3700., 1000.)),
        Investidor(cpf=56182108880, perfil='Moderado', carteira = (5800., 2700., 3900., 1200.)),
        Investidor(cpf=78299785392, perfil='Moderado', carteira = (6000., 2700., 5100., 1600.)),
        Investidor(cpf=45206071878, perfil='Moderado', carteira = (5400., 3000., 4500., 1500.)),
        Investidor(cpf=57381925887, perfil='Moderado', carteira = (6000., 3400., 4500., 1600.)),
        Investidor(cpf=65654934891, perfil='Moderado', carteira = (6700., 3100., 4700., 1500.)),
        Investidor(cpf=56130640481, perfil='Moderado', carteira = (6300., 2300., 4400., 1300.)),
        Investidor(cpf=59667611672, perfil='Moderado', carteira = (5600., 3000., 4100., 1300.)),
        Investidor(cpf=40349334385, perfil='Moderado', carteira = (5500., 2500., 4000., 1300.)),
        Investidor(cpf=68422640081, perfil='Moderado', carteira = (5500., 2600., 4400., 1200.)),
        Investidor(cpf=55245923439, perfil='Moderado', carteira = (6100., 3000., 4600., 1400.)),
        Investidor(cpf=51286696873, perfil='Moderado', carteira = (5800., 2600., 4000., 1200.)),
        Investidor(cpf=41065279767, perfil='Moderado', carteira = (5000., 2300., 3300., 1000.)),
        Investidor(cpf=42866454119, perfil='Moderado', carteira = (5600., 2700., 4200., 1300.)),
        Investidor(cpf=61962944542, perfil='Moderado', carteira = (5700., 3000., 4200., 1200.)),
        Investidor(cpf=48623501235, perfil='Moderado', carteira = (5700., 2900., 4200., 1300.)),
        Investidor(cpf=49475220139, perfil='Moderado', carteira = (6200., 2900., 4300., 1300.)),
        Investidor(cpf=52245218531, perfil='Moderado', carteira = (5100., 2500., 3000., 1100.)),
        Investidor(cpf=50932926697, perfil='Moderado', carteira = (5700., 2800., 4100., 1300.)),
        Investidor(cpf=47432932248, perfil='Agressivo', carteira = (6300., 3300., 6000., 2500.)),
        Investidor(cpf=39321991579, perfil='Agressivo', carteira = (5800., 2700., 5100., 1900.)),
        Investidor(cpf=46283759608, perfil='Agressivo', carteira = (7100., 3000., 5900., 2100.)),
        Investidor(cpf=56996272538, perfil='Agressivo', carteira = (6300., 2900., 5600., 1800.)),
        Investidor(cpf=77232189978, perfil='Agressivo', carteira = (6500., 3000., 5800., 2200.)),
        Investidor(cpf=77183282421, perfil='Agressivo', carteira = (7600., 3000., 6600., 2100.)),
        Investidor(cpf=42857147573, perfil='Agressivo', carteira = (4900., 2500., 4500., 1700.)),
        Investidor(cpf=39331584043, perfil='Agressivo', carteira = (7300., 2900., 6300., 1800.)),
        Investidor(cpf=48130345228, perfil='Agressivo', carteira = (6700., 2500., 5800., 1800.)),
        Investidor(cpf=71422443953, perfil='Agressivo', carteira = (7200., 3600., 6100., 2500.)),
        Investidor(cpf=72508507904, perfil='Agressivo', carteira = (6900., 3200., 5700., 2300.)),
        Investidor(cpf=41188727558, perfil='Agressivo', carteira = (5600., 2800., 4900., 2000.)),
        Investidor(cpf=61358776640, perfil='Agressivo', carteira = (7700., 2800., 6700., 2000.)),
        Investidor(cpf=66934042323, perfil='Agressivo', carteira = (6300., 2700., 4900., 1800.)),
        Investidor(cpf=40622495567, perfil='Agressivo', carteira = (6700., 3300., 5700., 2100.)),
        Investidor(cpf=57221661311, perfil='Agressivo', carteira = (7200., 3200., 6000., 1800.)),
        Investidor(cpf=45159362930, perfil='Agressivo', carteira = (6200., 2800., 4800., 1800.)),
        Investidor(cpf=45018975174, perfil='Agressivo', carteira = (6100., 3000., 4900., 1800.)),
        Investidor(cpf=70685429140, perfil='Agressivo', carteira = (6400., 2800., 5600., 2100.)),
        Investidor(cpf=61808723477, perfil='Agressivo', carteira = (7200., 3000., 5800., 1600.)),
        Investidor(cpf=56363906548, perfil='Agressivo', carteira = (7400., 2800., 6100., 1900.)),
        Investidor(cpf=39646194720, perfil='Agressivo', carteira = (7900., 3800., 6400., 2000.)),
        Investidor(cpf=55385494438, perfil='Agressivo', carteira = (6400., 2800., 5600., 2200.)),
        Investidor(cpf=75796138061, perfil='Agressivo', carteira = (6300., 2800., 5100., 1500.)),
        Investidor(cpf=53595767857, perfil='Agressivo', carteira = (6100., 2600., 5600., 1400.)),
        Investidor(cpf=48758828080, perfil='Agressivo', carteira = (7700., 3000., 6100., 2300.)),
        Investidor(cpf=58387651356, perfil='Agressivo', carteira = (6300., 3400., 5600., 2400.)),
        Investidor(cpf=72846931192, perfil='Agressivo', carteira = (6400., 3100., 5500., 1800.)),
        Investidor(cpf=47046896346, perfil='Agressivo', carteira = (6000., 3000., 4800., 1800.)),
        Investidor(cpf=69730292799, perfil='Agressivo', carteira = (6900., 3100., 5400., 2100.)),
        Investidor(cpf=48177836349, perfil='Agressivo', carteira = (6700., 3100., 5600., 2400.)),
        Investidor(cpf=57976326635, perfil='Agressivo', carteira = (6900., 3100., 5100., 2300.)),
        Investidor(cpf=55710813002, perfil='Agressivo', carteira = (5800., 2700., 5100., 1900.)),
        Investidor(cpf=64028580439, perfil='Agressivo', carteira = (6800., 3200., 5900., 2300.)),
        Investidor(cpf=49962942971, perfil='Agressivo', carteira = (6700., 3300., 5700., 2500.)),
        Investidor(cpf=47250893163, perfil='Agressivo', carteira = (6700., 3000., 5200., 2300.)),
        Investidor(cpf=75559276274, perfil='Agressivo', carteira = (6300., 2500., 5000., 1900.)),
        Investidor(cpf=58529878272, perfil='Agressivo', carteira = (6500., 3000., 5200., 2000.)),
        Investidor(cpf=76005896622, perfil='Agressivo', carteira = (6200., 3400., 5400., 2300.)),
        Investidor(cpf=49212614633, perfil='Agressivo', carteira = (5900., 3000., 5100., 1800.))]
       
        lista_distancias = list()
        
        for cliente_data in dados:
            distancia = Utils.calcular_distancia_2_pontos(self.carteira_investimentos, cliente_data.carteira_investimentos)
            lista_distancias.append(distancia)        
        
        lista_distancias_copia = lista_distancias.copy()
        lista_distancias_copia.sort()

        lista_indices = list()
        for i in range(k):
            indice = lista_distancias.index(lista_distancias_copia[0])
            lista_distancias_copia.pop(0)        
            lista_indices.append(indice)

        contador_conservador = 0
        contador_moderado = 0
        contador_agressivo = 0
        for i in range(k):
            if dados[lista_indices[i]].perfil == "Conservador":
                contador_conservador += 1
            elif dados[lista_indices[i]].perfil == "Moderado":
                contador_moderado += 1
            elif dados[lista_indices[i]].perfil == "Agressivo":
                contador_agressivo += 1

        if(contador_conservador >= contador_moderado and contador_conservador >= contador_agressivo):
            perfil = "Conservador"
        elif(contador_moderado >= contador_conservador and contador_moderado >= contador_agressivo):
            perfil = "Moderado"
        else:
            perfil = "Agressivo"

        self.perfil = perfil
    
    def __repr__(self):
        '''função que define como o objeto da classe é impresso ao se chamar um print()'''
        if(self.perfil != 'Indefinido'):
            return(f'CPF: {self.cpf}\nCarteira de investimentos: {self.carteira_investimentos}\nPerfil: {self.perfil}\n\n')
        else:
            return(f'CPF: {self.cpf}\nCarteira de investimentos: {self.carteira_investimentos}\n\n')
