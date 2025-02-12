from pylatex import Document, Section, Subsection, Command, Tabular, Itemize, Enumerate, LineBreak, LargeText, MiniPage, MediumText, MultiRow, NewPage, Subsubsection, SmallText, FootnoteText, NoEscape, Figure, MiniPage, Math
from pylatex.utils import bold
import graficosRelatorioSemanal as GR
import pandas as pd
import rpy2.robjects as robjects
import numpy

# Cria um novo documento LaTeX
geometry_options = {"tmargin": "2cm", "rmargin": "2.5cm", "lmargin": "2.5cm", "landscape": True}
doc = Document(geometry_options=geometry_options)
doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))

with doc.create(MiniPage(align='c')):
        doc.append(LargeText(("Relatório do Portal e YouTube")))
        doc.append(LineBreak())
        doc.append(LineBreak())
        doc.append(LineBreak())
        doc.append(MediumText(("Relatório semanal")))
        doc.append(LineBreak())

portal_usuariosUnicos_2024Table = [276184,441269,455979,340868,369804,272294,293971,459877,326566,369497,302557,358037,308259,358280,294016,371248,552230,347410,389320,357439,567253,418934,318670,336115,324685,314522,336800,378852,361139,706462,283310,382522,283476,302664,372105,353182,310670,568090,423814,317576,302953,330100]
portal_usuariosRescorrentes_2024Table = [123944,197378,172485,156579,169541,124341,135747,202480,151029,160475,147401,154262,133798,142551,126291,137344,177835,134973,132433,149747,186295,176389,148123,143912,136329,148085,157154,181330,158074,234256,131005,147944,130517,133439,138919,129991,139492,167879,161574,152746,148547,152654]

portal_usuariosUnicos_2024Analytics = [213000,331000,370000,261000,283000,210000,226000,357000,259000,292000,231000,286000,244000,295000,233000,304000,469000,314000,330000,287000,491000,340000,254000,272000,260000,244000,266000,299000,284000,604000,222000,314000,244000,243000,308000,292000,245000,496000,358000,247000,233000,257000]
portal_usuariosRescorrentes_2024Analytics = [73000,113000,105000,92000,100000,73000,79000,122000,93000,98000,88000,93000,80000,90000,75000,83000,115000,85000,83000,92000,126000,111000,91000,90000,84000,88000,99000,115000,97000,159000,78000,91000,84000,82000,82000,76000,80000,108000,104000,92000,87000,87000]

portal_visualizacoes_2024 = [621206,965340,924908,765698,829407,635989,664666,907045,698454,764245,671189,745886,682403,733301,648784,782882,992290,742668,763963,715304,924041,790025,657113,655361,673549,667495,702230,910372,740670,1154334,650090,768296,595760,605010,699928,663877,651132,922972,757296,654624,649462,685431] # mesmo valor na tabela e no analytics
portal_novosUsuarios_2024 = [147518,242760,278732,177038,198428,144767,155648,255141,170986,204845,151741,200186,170757,214285,164265,233626,374522,237463,256978,207660,382013,243507,170937,194476,186105,167547,180528,200898,201074,476829,150861,233911,152128,168000,234427,225031,174169,404775,268157,166042,156950,180076] # mesmo valor na tabela e no analytics

#TWITTER
tw_seg_2024 = [359,455,1249,892,801,725,1009,2464,886,2460]
tw_impressões_2024 = [86012,102051,96123,100004,113293,95767,95199,90299,78103,89681]
tw_engajamentos_2024 = [2390,3324,3242,3257,4164,2661,3219,4553,2650,4576]

#ADICIONAR TOTAL DA SEMANA SEGUINTE
tw_seg_2024_total = [312146,312041,312437,312722,312797,313181,314742,315456,317307,319917]
tw_seg_2024_perdeu = [890,tw_seg_2024[1]-(tw_seg_2024_total[1]-tw_seg_2024_total[0]),tw_seg_2024[2]-(tw_seg_2024_total[2]-tw_seg_2024_total[1]),tw_seg_2024[3]-(tw_seg_2024_total[3]-tw_seg_2024_total[2]),tw_seg_2024[4]-(tw_seg_2024_total[4]-tw_seg_2024_total[3]),tw_seg_2024[5]-(tw_seg_2024_total[5]-tw_seg_2024_total[4]),abs(tw_seg_2024[6]-(tw_seg_2024_total[6]-tw_seg_2024_total[5])),tw_seg_2024[7]-(tw_seg_2024_total[7]-tw_seg_2024_total[6]),abs(tw_seg_2024[8]-(tw_seg_2024_total[8]-tw_seg_2024_total[7])),abs(tw_seg_2024[9]-(tw_seg_2024_total[9]-tw_seg_2024_total[8]))] #sabe a quantidade que perdeu de acordo com a diferença de seguidores entre um mês e outro e o ganho total de seguidores no mês

#YOUTUBE
yb_inc_2024 = [505,241,552,155,268,162,135,81,82,89,121,123,89,110,103,141,171,186,274,614,222,559,334,161,834,374,78,199,90,126,115,145,74,107,44,154,76,80,617,218,204,274]
yb_inc_2024_perdeu = [30,15,31,17,30,15,19,21,16,22,18,18,16,19,22,22,24,21,20,48,29,39,33,32,55,46,15,30,22,26,32,22,13,18,11,29,23,15,29,27,24,21]
yb_visualizacoes_2024 = [134255,69730,149424,40127,73821,39688,35024,29843,22657,20998,21575,27314,19991,35636,22941,39314,40865,45122,92628,139771,53904,140104,91364,26819,370283,164890,16203,83540,47889,42861,24733,37780,15380,56673,12634,49003,19852,14348,140900,53348,36570,50523]
yb_horas_2024 = [1785,1114,2142,671,1265,632,660,768,715,596,586,555,420,537,553,557,661,630,1312,1626,791,1556,1039,508,5986,1767,292,926,656,537,504,539,286,467,229,580,342,330,2022,1198,950,1137]

#ADICIONAR TOTAL DA SEMANA SEGUINTE
yb_inc_2024_total = [35940,36167,36685,36863,37062,37214,37333,37380,37544,37631,37729,37846,37922,37987,38076,38250,38337,38507,38751,39324,39515,40032,40329,40464,41239,41571,41651,41797,41872,41972,42052,42174,42234,42322,42354,42484,42534,42599,43200,43391,43565,43818]

# #YOUTUBE - TN: MONETIZAÇÃO
# impressoes_yb_TN=[16429,182696,85235]
# visuMonetizadas_yb_TN=[15531,173212,85466]
# receitaBruta_yb_TN=[73,1050,573]
# premium_yb_TN=[1,16,6]
# AdSense_yb_TN=[40,578,315]

# #YOUTUBE - JPN: MONETIZAÇÃO
# impressoes_yb_JPN=[39593,16737]
# visuMonetizadas_yb_JPN=[33296,13781]
# receitaBruta_yb_JPN=[185,90]
# premium_yb_JPN=[7,6]
# AdSense_yb_JPN=[102,49]

# Adiciona a seção para os resultados
with doc.create(Section('Tribuna do Norte', numbering=False)):
    with doc.create(Subsection(f'{GR.penultimo_domingo().strftime("%d-%m-%Y")} a {GR.ultimo_sabado().strftime("%d-%m-%Y")}', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(2, data='Portal'), GR.formataNumero(portal_novosUsuarios_2024[-1]), GR.formataNumero(portal_visualizacoes_2024[-1]), GR.formataNumero(portal_usuariosRescorrentes_2024Table[-1]), GR.formataNumero(portal_usuariosUnicos_2024Table[-1])))
                table.add_row(('', 'novos usuários', 'visualizações', 'usuários recorrentes','usuários únicos'))
                table.add_hline()
                # table.add_row((MultiRow(2, data='Instagram'), GR.formataNumero(ig_seg_2024_total[-1]-ig_seg_2024_total[-2]), GR.formataNumero(ig_alcance_2024[-1]), GR.formataNumero(ig_vivitas_2024[-1]), GR.formataNumero(ig_visualizacoes[-1])))
                # table.add_row(('', 'novos seguidores', 'contas atingidas', 'visitas ao perfil', 'visualizações'))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Facebook'), GR.formataNumero(fb_seg_2024_total[-1]-fb_seg_2024_total[-2]), GR.formataNumero(fb_alcance_2024[-1]), GR.formataNumero(fb_vivitas_2024[-1]), GR.formataNumero(fb_visualizacoes[-1])))
                # table.add_row(('', 'novos seguidores', 'contas atingidas', 'visitas ao perfil', 'visualizações'))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Twitter'), '-', '-', '-'))
                # table.add_row(('', 'novos seguidores', 'impressões', 'engajamentos'))
                # table.add_hline()
                table.add_row((MultiRow(2, data='Youtube'), GR.formataNumero(yb_inc_2024_total[-1]-yb_inc_2024_total[-2]), GR.formataNumero(yb_visualizacoes_2024[-1]), GR.formataNumero(yb_horas_2024[-1]),'-'))
                table.add_row(('', 'novos inscritos', 'visualizações', 'horas de exibição','-'))
                

        # Adiciona informações extras
        # Adiciona uma lista com marcadores
        # with doc.create(Itemize()) as itemize:
        #     itemize.add_item(f"Ao todo, a Tribuna do Norte entregou seu conteúdo para, aproximadamente, {GR.formataNumero(portal_novosUsuarios_2024[-1]+(ig_seg_2024_total[-1]-ig_seg_2024_total[-2])+(fb_seg_2024_total[-1]-fb_seg_2024_total[-2])+(yb_inc_2024_total[-1]-yb_inc_2024_total[-2]))} novas contas, entre Portal, Instagram, Twitter, Facebook e YouTube.")
        with doc.create(Itemize()) as itemize:
            itemize.add_item(f"Ao todo, a Tribuna do Norte entregou seu conteúdo para, aproximadamente, {GR.formataNumero(portal_novosUsuarios_2024[-1]+(yb_inc_2024_total[-1]-yb_inc_2024_total[-2]))} novas contas, entre Portal e YouTube.")
            #+(tw_seg_2024_total[-1]-tw_seg_2024_total[-2])
            # itemize.add_item(Command('textbf', arguments='Portal'))
            # with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
            #      sublist.add_item(NoEscape(r"Na semana analisada a notícia \textbf{Investidor da SAF do América, Marcelo mostra otimismo com o trabalho e promete vir mais ao clube} ficou no top 1 teve \textbf{63.381} visualizações, que representam apenas \textbf{8.4\%} do total. Isso pode acontecer não apenas por conta das visualizações mais baixas na semana analisada, mas tembém por conta de uma distribuição 'melhor' entre as notícias."))
            #      sublist.add_item(NoEscape(r"Também tivemos \textbf{'Rodolitos em Ponta Negra: entenda origem das estruturas e aparecimento na praia} com \textbf{39.734} visualizações e \textbf{'Justiça autoriza Governo do RN a escalonar pagamento do 13º salário até janeiro} com \textbf{19.437} visualizações. As 3 somam \textbf{122.552} visualizações que representam \textbf{16.2\%} do total."))
            #     #  sublist.add_item(NoEscape(r"A página do \textbf{Clube do Assinante} teve um grande número de acessos, fazendo com que fique no top 3 pela primeira vez;"))
            #      sublist.add_item(NoEscape(r"As \textbf{15 notícias mais vitas} juntas somam \textbf{241.307} visualizações, que representam \textbf{32\%} do total. As visualizações do top 15 ficaram abaixo das 391.535 da semana annterior."))
            itemize.add_item(Command('textbf', arguments='YouTube'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item(f"Total de seguidores atual: {GR.formataNumero(yb_inc_2024_total[-1])}. Total de seguidores na semana anterior: {GR.formataNumero(yb_inc_2024_total[-2])}")
                sublist.add_item(f"Seguidores adquiridos na semana: {GR.formataNumero(yb_inc_2024_total[-1]-yb_inc_2024_total[-2]+yb_inc_2024_perdeu[-1])}. Deixaram de seguir: {GR.formataNumero(yb_inc_2024_perdeu[-1])}")
                sublist.add_item(f"Taxa de fixação: {GR.fixacao(yb_inc_2024_total[-1]-yb_inc_2024_total[-2]+yb_inc_2024_perdeu[-1],yb_inc_2024_perdeu[-1])}")
                # sublist.add_item(NoEscape(r"O vídeo mais visto foi \textbf{'Motorista de caminhão envolvido em acidente com 41 mortos em MG se entrega à polícia'} com \textbf{110.843} visualizações, que representa \textbf{78.7\%} do total. Logo em seguida temos \textbf{'[TV TRIBUNA] Espanta conta Cabaré da Leila'} com \textbf{20.002} visualizações e \textbf{'Carro que utilizava botijão de gás de cozinha explode em Natal'} com \textbf{1.105} visualizações, com cada um representando, respectivamente, \textbf{14.2\% e 0.8\%} do total."))
                # sublist.add_item(NoEscape(r"O segundo e terceiro lugar da semana atual são, respectivamente, o primeiro e segundo da semana passada. Além disso, os dois estão com bem mais visualizações que na semana anterior."))
                # sublist.add_item(NoEscape(r"Os dosi videos mais vistos dessa semana sozinhos representam mais de 90\% das visualizações."))

doc.append(NewPage())

with doc.create(Subsection('Análise semanal', numbering=False)):
    with doc.create(Subsubsection('Portal', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(3, data='Semana'), 'Novos usuários', 'Visualizações', 'Usuários recorrentes', 'Usuários únicos'))
                table.add_row(('', FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a')))
                table.add_row(('', FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior')))
                table.add_hline()
                table.add_row((MultiRow(2, data=f'{GR.penultimo_domingo().strftime("%d-%m-%Y")} a {GR.ultimo_sabado().strftime("%d-%m-%Y")}'), GR.numeroPorExtensso(portal_novosUsuarios_2024[-1]), GR.numeroPorExtensso(portal_visualizacoes_2024[-1]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Table[-1]), GR.numeroPorExtensso(portal_usuariosUnicos_2024Table[-1])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[-1],portal_novosUsuarios_2024[-2])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[-1],portal_visualizacoes_2024[-2])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Table[-1],portal_usuariosRescorrentes_2024Table[-2])}'), FootnoteText(f'{GR.crescimento(portal_usuariosUnicos_2024Table[-1],portal_usuariosUnicos_2024Table[-2])}')))

        # Adiciona informações extras
        # Adiciona uma lista com marcadores
        with doc.create(Itemize()) as itemize:
            # itemize.add_item('Em geral, março vem sendo o melhor mês da Tribuna do Norte nas redes sociais e setembro o pior.')
            itemize.add_item('Legenda:')
            #doc.append(NoEscape(r'\newline'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item(NoEscape(r'\textbf{Usuários únicos:} número de usuários únicos que interagiram com seu site ou app. É qualquer usuário que tenha uma sessão engajada ou quando o Google Analytics coleta o evento "first\_open", que é quando o usuário abre o site pela primeira vez dentro do período especificado;'))
                sublist.add_item(NoEscape(r'\textbf{Novos usuários:} número de novos usuários únicos que visitaram o site ou app pela primeira vez;'))
                sublist.add_item(NoEscape(r'\textbf{Usuários recorrentes:} número de usuários que iniciaram pelo menos uma sessão anterior, independentemente de ter sido ou não uma sessão engajada no período especificado;'))
                sublist.add_item(NoEscape(r'\textbf{Visualizações:} quantas telas do app para dispositivos móveis ou páginas da Web seus usuários acessaram. Exibições repetidas de uma única tela ou página são consideradas. Nesse caso tembém deve ser lavada em consideração a informação de que Jonathas fez alterações em relação as exibições repetidas;'))
                sublist.add_item(NoEscape(r'\textbf{Sessões engajadas:} correspondem ao número de sessões com mais de 10 segundos, que geraram um ou mais eventos de conversão ou tiveram duas ou mais visualizações de página/tela. Vá para a ultima página para saber a definição de uma sessão de acordo com o Google Analytics.'))

doc.append(NewPage())

NovosUsu_plot_path = GR.seguidorIG()
Recorrentes_plot_path = GR.visitaIG()
Visua_plot_path = GR.alcanceeIG()
Usuunico_plot_path = GR.visualizacoeesIG()
with doc.create(Subsection('', numbering=False)):
    doc.append("Portal: novos usuários, visualizações, usuários recorrentes e usuários únicos")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='h')) as plot:
        plot.add_image(NovosUsu_plot_path, width=NoEscape(r'0.5\textwidth'))
        plot.add_image(Visua_plot_path, width=NoEscape(r'0.5\textwidth'))
    with doc.create(Figure(position='h')) as plot:
        plot.add_image(Recorrentes_plot_path, width=NoEscape(r'0.5\textwidth'))
        plot.add_image(Usuunico_plot_path, width=NoEscape(r'0.5\textwidth'))
# doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))
# doc.preamble.append(NoEscape(r'\usepackage{float}'))

# # ORIGEM PORTAL
# GR.origemPortal()       
# # Adiciona uma seção ao documento
# with doc.create(Subsection('', numbering=False)):
#     doc.append("Portal: origem dos usuários")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha

#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(GR.origem_plot_path, width=NoEscape(r'1\textwidth'))

# with doc.create(Enumerate(enumeration_symbol=r"")) as itemize:
#             itemize.add_item('O acesso direto representa os usuários que digitaram a URL da Tribuna do Norte diretamente no navegador,adicionaram o site aos favoritos ou clicaram diretamente em um link compartilhado, desta forma, indo diretamente para o site sem precisar pesquisa-lo.')
#             itemize.add_item('As outras informações representam o acesso através da plataforma indicada pelo título da respectiva barra.')

# doc.append(NewPage())

# # TOP10 PORTAL
# GR.top10()
# # Adiciona uma seção ao documento
# with doc.create(Subsection('', numbering=False)):
#     doc.append("Portal: 10 notícias mais vistas")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha

#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(GR.top10_plot_path, width=NoEscape(r'0.9\textwidth'))
        
# # TOP15 PORTAL
# GR.top15()
# # Adiciona uma seção ao documento
# with doc.create(Subsection('', numbering=False)):
#     doc.append("Portal: 15 notícias mais pesquisadas")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(GR.top15_plot_path, width=NoEscape(r'0.9\textwidth'))

# # TOP15 PORTAL
# GR.top15cliques()
# # Adiciona uma seção ao documento
# with doc.create(Subsection('', numbering=False)):
#     doc.append("Portal: 15 notícias com mais cliques pelo google")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(GR.top15cliques_plot_path, width=NoEscape(r'1\textwidth'))

# doc.append(NewPage())

# # VISUALIZAÇÕES E USUÁRIOS PORTAL
# GR.visualizacoesUsuarios()
# # Adiciona uma seção ao documento
# with doc.create(Subsection('', numbering=False)):
#     doc.append("Portal: comparativo de visualizações e acessos de usuários")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(GR.visualizacoesUsuarios_plot_path, width=NoEscape(r'1\textwidth'))

# with doc.create(Enumerate(enumeration_symbol=r"")) as itemize:
#             itemize.add_item(NoEscape(r'\small{Este gráfico mostra a semelhança de compatamento entre diferentes dados do portal ao longo do período analisado.}'))

# doc.append(NewPage())

# # VISUALIZAÇÕES
# GR.visu_cumsum()
# # Adiciona uma seção ao documento
# with doc.create(Subsection('', numbering=False)):
#     doc.append("Portal: visualizações com valores acumulativos")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(GR.visu_cumsum_plot_path, width=NoEscape(r'0.9\textwidth'))

# # usuariso unicos
# GR.usuUni_cumsum()
# # Adiciona uma seção ao documento
# with doc.create(Subsection('', numbering=False)):
#     doc.append("Portal: usuários únicos com valores acumulativos")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(GR.usuUni_cumsum_plot_path, width=NoEscape(r'0.9\textwidth'))

# doc.append(NewPage())

# # usuariso unicos
# GR.newUsu_cumsum()
# # Adiciona uma seção ao documento
# with doc.create(Subsection('', numbering=False)):
#     doc.append("Portal: novos usuários com valores acumulativos")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(GR.newUsu_cumsum_plot_path, width=NoEscape(r'0.9\textwidth'))

# # usuariso unicos
# GR.usuRec_cumsum()
# # Adiciona uma seção ao documento
# with doc.create(Subsection('', numbering=False)):
#     doc.append("Portal: usuários recorrente com valores acumulativos")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(GR.usuRec_cumsum_plot_path, width=NoEscape(r'0.9\textwidth'))

# doc.append(NewPage())

# # VISUALIZAÇÕES POR FE PORTAL
# GR.faixaEtaria()
# # Adiciona uma seção ao documento
# with doc.create(Subsection('', numbering=False)):
#     doc.append("Portal: visualizações por faixa etária")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(GR.faixaEtaria_plot_path, width=NoEscape(r'0.8\textwidth'))

# GR.faixaEtaria_desconhecidaAndTotal()
# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("Portal: visualizações por faixa etária (desconhecida e total)")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(GR.faixaEtaria_desconhecidaAndTotal_plot_path, width=NoEscape(r'0.8\textwidth'))

# doc.append(NewPage())

# # recebendo camiho da imagem do gráfico e o total de seguidores do fb e ig
# fePublico_FBIG_plot_path, FB_followers, IG_followers = GR.fePublico_FBIG()

# with doc.create(Subsection('Análise semanal', numbering=False)):
# with doc.create(Subsubsection('Instagram', numbering=False)):
#     with doc.create(MiniPage(align='c')):
#         # Adiciona a tabela de resultados
#         with doc.create(Tabular('|c|c|c|c|c|', booktabs =True)) as table:
            
#             table.add_row((MultiRow(3, data='Semana'), 'Novos seguidores', 'Alcance', 'Visitas','Visualizações'))
#             table.add_row(('', FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a')))
#             table.add_row(('', FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior')))
#             table.add_hline()
#             table.add_row((MultiRow(2, data=f'{GR.penultimo_domingo().strftime("%d-%m-%Y")} a {GR.ultimo_sabado().strftime("%d-%m-%Y")}'), GR.numeroPorExtensso(ig_seg_2024[-1]), GR.numeroPorExtensso(ig_alcance_2024[-1]), GR.numeroPorExtensso(ig_vivitas_2024[-1]), GR.numeroPorExtensso(ig_visualizacoes[-1])))
#             table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[-1],ig_seg_2024[-2])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[-1],ig_alcance_2024[-2])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[-1],ig_vivitas_2024[-2])}'), FootnoteText(f'{GR.crescimento(ig_visualizacoes[-1],ig_visualizacoes[-2])}')))

# doc.append(NewPage())
# pocentoMaior = 93.6
# pocentoMenor = 6.4
# publicacoes = 78.9
# reels = 11.1
# stories = 10
# visualizacoesIG_plot_path = GR.visualizacoesIG(7694872, 8851512,pocentoMaior, pocentoMenor)
# grafico_barras_composto_plot_path = GR.grafico_barras_composto([(publicacoes/100)*pocentoMaior,(publicacoes/100)*pocentoMenor,publicacoes,(reels/100)*pocentoMaior,(reels/100)*pocentoMenor,reels,(stories/100)*pocentoMaior,(stories/100)*pocentoMenor,stories,0,0,0])
# with doc.create(Subsection('', numbering=False)):
#     doc.append("Instagram: Visualizações e público")
#     doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='h')) as plot:
#         plot.add_image(visualizacoesIG_plot_path, width=NoEscape(r'0.5\textwidth'))
#         plot.add_image(grafico_barras_composto_plot_path, width=NoEscape(r'0.5\textwidth'))


         

# doc.append(NewPage())
# cidadesIG_plot_path = GR.grafico_cidades(['Natal', 'Parnamirim', 'Mossoró', 'Ceará-Mirim','Macaiba','Caicó','Assu','Currais Novos'],[43.7,11.2,2.5,2.2,1.6,0.9,0.8,0.8])
# FEIG_plot_path = GR.grafico_faixa_etaria(['13-17', '18-24', '25-34', '35-44', '45-54', '55-64', '65+'],[0.7,9.3,31.3,31.7,15.4,7.5,3.8])
# with doc.create(Subsection('', numbering=False)):
#     doc.append("Instagram: Cidades e faixa etária")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='h')) as plot:
#         plot.add_image(cidadesIG_plot_path, width=NoEscape(r'0.5\textwidth'))
#         plot.add_image(FEIG_plot_path, width=NoEscape(r'0.5\textwidth'))

# doc.append(NewPage())
# pocentoMaior2 = 96.9
# pocentoMenor2 = 3.1
# publicacoes2 = 90
# reels2 = 9.7
# stories2 = 0.3
# sexoIG_plot_path = GR.sexoIG(ig_seg_2024_total[-1],ig_seg_2024_total[-2],61.7,38.3)
# interacoesIG_plot_path = GR.interacoesIG(184100,177700,96.9,3.1)
# grafico_barras_composto2_plot_path = GR.grafico_barras_composto2([(publicacoes2/100)*pocentoMaior2,(publicacoes2/100)*pocentoMenor2,publicacoes2,(reels2/100)*pocentoMaior2,(reels2/100)*pocentoMenor2,reels2,(stories2/100)*pocentoMaior2,(stories2/100)*pocentoMenor2,stories2,0,0,0])
# with doc.create(Subsection('', numbering=False)):
#     doc.append("Instagram: interações")
#     with doc.create(Figure(position='h')) as plot:
#         plot.add_image(interacoesIG_plot_path, width=NoEscape(r'0.5\textwidth'))
#         plot.add_image(grafico_barras_composto2_plot_path, width=NoEscape(r'0.5\textwidth'))

doc.append(NewPage())

# with doc.create(Subsubsection('Facebook', numbering=False)):
#     with doc.create(MiniPage(align='c')):
#         # Adiciona a tabela de resultados
#         with doc.create(Tabular('|c|c|c|c|c|', booktabs =True)) as table:
            
#             table.add_row((MultiRow(3, data='Semana'), 'Novos seguidores', 'Alcance', 'Visitas','Visualizações'))
#             table.add_row(('', FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a')))
#             table.add_row(('', FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior')))
#             table.add_hline()
#             table.add_row((MultiRow(2, data=f'{GR.penultimo_domingo().strftime("%d-%m-%Y")} a {GR.ultimo_sabado().strftime("%d-%m-%Y")}'), GR.numeroPorExtensso(fb_seg_2024[-1]), GR.numeroPorExtensso(fb_alcance_2024[-1]), GR.numeroPorExtensso(fb_vivitas_2024[-1]), GR.numeroPorExtensso(fb_visualizacoes[-1])))
#             table.add_row(('', FootnoteText(f'{GR.crescimento(fb_seg_2024[-1],fb_seg_2024[-2])}'), FootnoteText(f'{GR.crescimento(fb_alcance_2024[-1],fb_alcance_2024[-2])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[-1],fb_vivitas_2024[-2])}'), FootnoteText(f'{GR.crescimento(fb_visualizacoes[-1],fb_visualizacoes[-2])}')))


        # # Adiciona informações extras
        # # Adiciona uma lista com marcadores
        # with doc.create(Itemize()) as itemize:
        #     # itemize.add_item('Em geral, março vem sendo o melhor mês da Tribuna do Norte nas redes sociais e setembro o pior.')
        #     itemize.add_item('Legenda:')
        #     #doc.append(NoEscape(r'\newline'))
        #     with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        #         sublist.add_item(NoEscape(r'\textbf{Alcance:} Essa métrica calcula o alcance da distribuição orgânica ou paga do seu conteúdo do Instagram e/ou Facebook, incluindo publicações e stories que foram turbinados. Também pode ser interpretada como a quantidade de contas atingidas;'))
        #         sublist.add_item(NoEscape(r'\textbf{Visitas:} número de vezes que usuários visitaram seu perfil.'))

# with doc.create(Enumerate(enumeration_symbol=r"")) as itemize:
#             itemize.add_item(NoEscape(r'\textbf{Os detales demográficos (faixa etária, gênero e cidades) do facebook e instagram estavam indisponíveis.}'))


# doc.append(NewPage())
# cidadesFB_plot_path = GR.grafico_cidadesFB(['Natal', 'Parnamirim', 'Mossoró', 'Ceará-Mirim','Macaiba'],[43.5,5.5,2.4,0.9,0.9])
# totalFB = 331654
# fe1824 = (totalFB*(2.5)+totalFB*(2))/totalFB
# fe2534 = (totalFB*(18.4)+totalFB*(14.3))/totalFB
# fe3544 = (totalFB*(18.3)+totalFB*(13.7))/totalFB
# fe4554 = (totalFB*(9.7)+totalFB*(7.1))/totalFB
# fe5564 = (totalFB*(5.3)+totalFB*(3.5))/totalFB
# fe65 = (totalFB*(3.1)+totalFB*(2.1))/totalFB
# FEFB_plot_path = GR.grafico_faixa_etariaFB(['13-17', '18-24', '25-34', '35-44', '45-54', '55-64', '65+'],[0,fe1824,fe2534,fe3544,fe4554,fe5564,fe65])
# with doc.create(Subsection('', numbering=False)):
#     doc.append("Instagram: Cidades e faixa etária")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='h')) as plot:
#         plot.add_image(cidadesFB_plot_path, width=NoEscape(r'0.5\textwidth'))
#         plot.add_image(FEFB_plot_path, width=NoEscape(r'0.5\textwidth'))

# # fePublico_FBIG_plot_path, FB_followers, IG_followers = GR.fePublico_FBIG
# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("FB e IG: audiência por sexo e faixa etária")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(fePublico_FBIG_plot_path, width=NoEscape(r'0.8\textwidth'))

# doc.append(NewPage())

# publicoCidades_plot_path = GR.publicoCidades()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("FB e IG: audiência por cidades")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(publicoCidades_plot_path, width=NoEscape(r'1\textwidth'))

doc.append(NewPage())

# curtidasFB_plot_path = GR.curtidasFB()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("FB: novos seguidores ao longo do mês")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(curtidasFB_plot_path, width=NoEscape(r'0.9\textwidth'))

# visitasFB_plot_path = GR.visitasFB()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("FB: visitas ao longo do mês")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(visitasFB_plot_path, width=NoEscape(r'0.9\textwidth'))

# doc.append(NewPage())

# alcanceFB_plot_path = GR.alcanceFB()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("FB: alcance ao longo do mês")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(alcanceFB_plot_path, width=NoEscape(r'0.9\textwidth'))

# dadosFB_plot_path = GR.dadosFB()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("FB: comparativo de seguidores, visitas e alcance. (Obs.: dados fora de escala para uma melhor visualização)")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(dadosFB_plot_path, width=NoEscape(r'0.75\textwidth'))

# doc.append(NewPage())

# # with doc.create(Enumerate(enumeration_symbol=r"")) as itemize:
# #             itemize.add_item(NoEscape(r'\textbf{Os dados diários de seguidores do Instagram não foram disponobilizados pela Meta essa semana.}'))
# seguidoresIG_plot_path, seguidoresIG = GR.seguidoresIG()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("IG: ganho de seguidores ao longo do mês")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(seguidoresIG_plot_path, width=NoEscape(r'0.9\textwidth'))

# visitasIG_plot_path, visitasIG = GR.visitasIG()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("IG: visitas ao perfil ao longo do mês")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(visitasIG_plot_path, width=NoEscape(r'0.9\textwidth'))

# doc.append(NewPage())

# alcanceIG_plot_path, alcanceIG = GR.alcanceIG()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("IG: alcance do perfil ao longo do mês")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(alcanceIG_plot_path, width=NoEscape(r'0.9\textwidth'))

# doc.append(NewPage())

# dadosIG_plot_path = GR.dadosIG(40,500)

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("IG: comparativo de seguidores, visitas e alcance. (Obs.: dados fora de escala para uma melhor visualização)")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(dadosIG_plot_path, width=NoEscape(r'1\textwidth'))

# with doc.create(Enumerate(enumeration_symbol=r"")) as itemize:
#             itemize.add_item(NoEscape(r'\small{Este gráfico mostra a semelhança de compatamento entre diferentes dados do portal ao longo do período analisado.}'))
# doc.append(NewPage())

# with doc.create(Subsection('Análise semanal', numbering=False)):
#     with doc.create(Subsubsection('Twitter', numbering=False)):
#         with doc.create(MiniPage(align='c')):
#             # Adiciona a tabela de resultados
#             with doc.create(Tabular('|c|c|c|c|', booktabs =True)) as table:
                
#                 table.add_row((MultiRow(3, data='Semana'), 'Novos seguidores', 'Impressões', 'Engajamentos'))
#                 table.add_row(('', FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a')))
#                 table.add_row(('', FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior')))
#                 table.add_hline()
#                 table.add_row((MultiRow(2, data=f'{GR.penultimo_domingo().strftime("%d-%m-%Y")} a {GR.ultimo_sabado().strftime("%d-%m-%Y")}'), GR.numeroPorExtensso(tw_seg_2024[-1]), GR.numeroPorExtensso(tw_impressões_2024[-1]), GR.numeroPorExtensso(tw_engajamentos_2024[-1])))
#                 table.add_row(('', FootnoteText(f'{GR.crescimento(tw_seg_2024[-1],tw_seg_2024[-2])}'), FootnoteText(f'{GR.crescimento(tw_impressões_2024[-1],tw_impressões_2024[-2])}'), FootnoteText(f'{GR.crescimento(tw_engajamentos_2024[-1],tw_engajamentos_2024[-2])}')))

#         # Adiciona informações extras
#         # Adiciona uma lista com marcadores
#         with doc.create(Itemize()) as itemize:
#             # itemize.add_item('Em geral, março vem sendo o melhor mês da Tribuna do Norte nas redes sociais e setembro o pior.')
#             itemize.add_item('Legenda:')
#             #doc.append(NoEscape(r'\newline'))
#             with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
#                 sublist.add_item(NoEscape(r'\textbf{Impressões:} número de vezes que os usuários viram o(s) Tweet(s);'))
#                 sublist.add_item(NoEscape(r'\textbf{Engajamentos:} número total de vezes que um usuário interagiu com o(s) Tweet(s). Isso inclui todos os cliques em qualquer lugar no Tweet como: hashtags, links, avatar, nome de usuário e expansão do Tweet, Retweets, respostas e favoritos.'))

doc.append(NewPage())

# engajamentoTW_plot_path = GR.engajamentoTW()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("TW: engajamento do twitter")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(engajamentoTW_plot_path, width=NoEscape(r'0.8\textwidth'))

# impressoesTW_plot_path = GR.impressoesTW()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("TW: impressões do twitter")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(impressoesTW_plot_path, width=NoEscape(r'0.8\textwidth'))

# doc.append(NewPage())

# seguidoresTW_plot_path = GR.seguidoresTW()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("TW: ganho de seguidores no twitter ao logo do mês. (Esses dados levam em consideração apenas os ganhos)")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(seguidoresTW_plot_path, width=NoEscape(r'0.8\textwidth'))

# dadosTW_plot_path = GR.dadosTW()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("TW: comparativo de engajamentos, impressões e seguidores. (Obs.: dados fora de escala para uma melhor visualização)")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(dadosTW_plot_path, width=NoEscape(r'0.8\textwidth'))

# doc.append(NewPage())

with doc.create(Subsection('Análise semanal', numbering=False)):
    with doc.create(Subsubsection('YouTube', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(3, data='Semana'), 'Novos inscritos', 'Visualizações', 'Horas de exibição'))
                table.add_row(('', FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a')))
                table.add_row(('', FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior')))
                table.add_hline()
                table.add_row((MultiRow(2, data=f'{GR.penultimo_domingo().strftime("%d-%m-%Y")} a {GR.ultimo_sabado().strftime("%d-%m-%Y")}'), GR.numeroPorExtensso(yb_inc_2024[-1]), GR.numeroPorExtensso(yb_visualizacoes_2024[-1]), GR.numeroPorExtensso(yb_horas_2024[-1])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(yb_inc_2024[-1],yb_inc_2024[-2])}'), FootnoteText(f'{GR.crescimento(yb_visualizacoes_2024[-1],yb_visualizacoes_2024[-2])}'), FootnoteText(f'{GR.crescimento(yb_horas_2024[-1],yb_horas_2024[-2])}')))

# with doc.create(Subsection('', numbering=False)):
#     with doc.create(Subsubsection('YouTube - TN: Monetização', numbering=False)):
#         with doc.create(MiniPage(align='c')):
#             # Adiciona a tabela de resultados            
#             with doc.create(Tabular('|c|c|c|c|c|c|', booktabs =True)) as table:
            
#                 table.add_row((MultiRow(5, data='Semana'), FootnoteText('Impressões de anúncios'), FootnoteText('Visualizações monetizadas'), FootnoteText('Receita bruta'), FootnoteText('YTB Premium'), FootnoteText('Receita estimada (AdSense)')))
#                 table.add_row(('', FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a')))
#                 table.add_row(('', FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior')))
#                 table.add_hline()
#                 table.add_row((MultiRow(2, data=f'{GR.penultimo_domingo().strftime("%d-%m-%Y")} a {GR.ultimo_sabado().strftime("%d-%m-%Y")}'), GR.numeroPorExtensso(impressoes_yb_TN[-1]), GR.numeroPorExtensso(visuMonetizadas_yb_TN[-1]), GR.numeroPorExtensso(receitaBruta_yb_TN[-1]), GR.numeroPorExtensso(premium_yb_TN[-1]), GR.numeroPorExtensso(AdSense_yb_TN[-1])))
#                 table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_TN[-1],impressoes_yb_TN[-2])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_TN[-1],visuMonetizadas_yb_TN[-2])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_TN[-1],receitaBruta_yb_TN[-2])}'), FootnoteText(f'{GR.crescimento(premium_yb_TN[-1],premium_yb_TN[-2])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_TN[-1],AdSense_yb_TN[-2])}')))

# with doc.create(Subsection('', numbering=False)):
#     with doc.create(Subsubsection('YouTube - JPN: Monetização', numbering=False)):
#         with doc.create(MiniPage(align='c')):
#             # Adiciona a tabela de resultados            
#             with doc.create(Tabular('|c|c|c|c|c|c|', booktabs =True)) as table:
            
#                 table.add_row((MultiRow(5, data='Semana'), 'Impressões de anúncios', 'Visualizações monetizadas', 'Receita bruta', 'YTB Premium', 'Receita estimada (AdSense)'))
#                 table.add_row(('', FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a')))
#                 table.add_row(('', FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior')))
#                 table.add_hline()
#                 table.add_row((MultiRow(2, data=f'{GR.penultimo_domingo().strftime("%d-%m-%Y")} a {GR.ultimo_sabado().strftime("%d-%m-%Y")}'), GR.numeroPorExtensso(impressoes_yb_JPN[-1]), GR.numeroPorExtensso(visuMonetizadas_yb_JPN[-1]), GR.numeroPorExtensso(receitaBruta_yb_JPN[-1]), GR.numeroPorExtensso(premium_yb_JPN[-1]), GR.numeroPorExtensso(AdSense_yb_JPN[-1])))
#                 table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_JPN[-1],impressoes_yb_JPN[-2])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_JPN[-1],visuMonetizadas_yb_JPN[-2])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_JPN[-1],receitaBruta_yb_JPN[-2])}'), FootnoteText(f'{GR.crescimento(premium_yb_JPN[-1],premium_yb_JPN[-2])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_JPN[-1],AdSense_yb_JPN[-2])}')))

#         # Adiciona informações extras
#         # Adiciona uma lista com marcadores
#         with doc.create(Itemize()) as itemize:
#             # itemize.add_item('Em geral, março vem sendo o melhor mês da Tribuna do Norte nas redes sociais e setembro o pior.')
#             itemize.add_item('Legenda:')
#             #doc.append(NoEscape(r'\newline'))
#             with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
#                 sublist.add_item(NoEscape(r'\textbf{Impressões de anúncios:} quantidade de vezes que o anúncio apareceu na tela dos usuários, ou seja, o anúncio começou a ser carregado no dispositivo do usuário, e em alguns casos pode nem ter sido carregado por completo;'))
#                 sublist.add_item(NoEscape(r'\textbf{Visualizações monetizadas:} uma reprodução monetizada ocorre quando um espectador assiste um vídeo e pelo menos uma impressão de anúncios é exibida. Esse tipo de reprodução também é contabilizado quando o espectador para de assistir durante o anúncio precedente sem assistir o vídeo;'))
#                 sublist.add_item(NoEscape(r'\textbf{Receita bruta:} receita bruta estimada de todas as fontes de publicidade vendidas pelo Google para o período selecionado. Não se deve confundir receita de anúncios do YouTube com receita estimada ou receita líquida que são calculadas em seus contratos de participação nos lucros. ;'))
#                 sublist.add_item(NoEscape(r'\textbf{YouTube Premium:} receita estimada do YouTube Premium para o período selecionado;'))
#                 sublist.add_item(NoEscape(r'\textbf{Receita estimada (AdSense):} receita estimada de publicidade vendida pelo Google AdSense para o período selecionado. Esse valor é o que é de direito do propietario do canal, já com os descontos feitos pelo YouTube de acordo com o contrato e o que diz respeito a participação de lucros.'))
# visualizacoesIdadeYTB_plot_path = GR.visualizacoesIdadeYTB()
# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("YouTube: visualizações por faixa etária")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(visualizacoesIdadeYTB_plot_path, width=NoEscape(r'0.7\textwidth'))

# doc.append(NewPage())

# horasIdadeYTB_plot_path = GR.horasIdadeYTB()
# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("YouTube: horas de exibição por faixa etária")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(horasIdadeYTB_plot_path, width=NoEscape(r'0.7\textwidth'))
        
# generoYTB_plot_path = GR.generoYTB()
# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("YouTube: sexo do público")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(generoYTB_plot_path, width=NoEscape(r'0.6\textwidth'))
        
# visualizacoesCidadeYTB_plot_path = GR.visualizacoesCidadeYTB()
# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("YouTube: visualizações por cidade")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(visualizacoesCidadeYTB_plot_path, width=NoEscape(r'0.7\textwidth'))


doc.append(NewPage())

with doc.create(Itemize()) as itemize:
            # itemize.add_item('Em geral, março vem sendo o melhor mês da Tribuna do Norte nas redes sociais e setembro o pior.')
            itemize.add_item('Funcionamento do algoritmo:')
            #doc.append(NoEscape(r'\newline'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                # sublist.add_item(NoEscape(r'\textbf{Facebook:} O algoritmo do Facebook prioriza os conteúdos que geram mais interações, como curtidas, comentários e compartilhamentos. Ele também considera o grau de relacionamento entre os usuários e as contas que eles seguem, mostrando mais publicações de amigos e familiares do que de páginas. Além disso, o Facebook leva em conta a relevância e a atualidade dos conteúdos, dando mais destaque para as notícias e os assuntos do momento;'))
                # sublist.add_item(NoEscape(r'\textbf{Instagram:} O a lgoritmo do Instagram também se baseia no engajamento, no relacionamento e na temporalidade dos conteúdos. Ele mostra primeiro as postagens e as histórias das contas com as quais o usuário mais interage, seja por meio de curtidas, comentários, mensagens diretas ou buscas. Ele também valoriza os conteúdos mais recentes e mais relevantes para o usuário, de acordo com os seus interesses e hábitos;'))
                # sublist.add_item(NoEscape(r'\textbf{Twitter:} O algoritmo do Twitter tem duas formas de exibir os conteúdos: o modo cronológico e o modo destacado. No modo cronológico, o usuário vê os tweets mais recentes em ordem de publicação. No modo destacado, o usuário vê os tweets mais relevantes para ele, de acordo com o seu perfil, as suas interações e os assuntos do momento. O Twitter também mostra os tweets mais populares e mais comentados na seção “O que está acontecendo”;'))
                sublist.add_item(NoEscape(r'\textbf{YouTube:} O algoritmo do YouTube tem como objetivo aumentar o tempo de permanência dos usuários na plataforma, recomendando os vídeos que eles têm mais chances de assistir e se engajar. Para isso, ele considera fatores como o histórico de visualização, as preferências, as inscrições, a localização e o feedback dos usuários. Ele também leva em conta a qualidade e a relevância dos vídeos, analisando aspectos como o título, descrição, tags, miniaturas e os metadados.'))

doc.append(NewPage())

with doc.create(MiniPage(align='c')):
    doc.append(MediumText(("Observações")))

with doc.create(Itemize()) as itemize:
            # itemize.add_item('Em geral, março vem sendo o melhor mês da Tribuna do Norte nas redes sociais e setembro o pior.')
            itemize.add_item('Sessões:')
            #doc.append(NoEscape(r'\newline'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item(NoEscape(f'Por padrão, a sessão é encerrada após 30 minutos de inatividade, mas é possível ajustar esse limite para que ela dure de alguns segundos a várias horas.'))
            with itemize.create(Enumerate(enumeration_symbol=r"")) as sublist:
                sublist.add_item(NoEscape('O Google Analytics começa a contar a partir do momento em que um usuário acessa seu site. Se depois de 30 minutos este usuário não fizer uma interação, a sessão é finalizada. No entanto, toda vez que ocorre uma interação com um elemento (como um evento, interação de rede social ou uma nova página), o Google Analytics reinicia o tempo de vencimento adicionando 30 minutos a partir do momento da interação.\n Um único usuário pode abrir várias sessões. Essas sessões podem ocorrer no mesmo dia ou em vários dias, semanas ou meses. Assim que uma sessão termina, existe a oportunidade de iniciar uma nova sessão. Há dois métodos para o encerramento de uma sessão:'))
            with itemize.create(Enumerate(enumeration_symbol=r"")) as sublist:
                sublist.add_item(NoEscape('Um único usuário pode abrir várias sessões. Essas sessões podem ocorrer no mesmo dia ou em vários dias, semanas ou meses. Assim que uma sessão termina, existe a oportunidade de iniciar uma nova sessão. Há dois métodos para o encerramento de uma sessão:'))
                with sublist.create(Enumerate(enumeration_symbol=r"•")) as subsublist:
                    subsublist.add_item(NoEscape('Vencimento por tempo:'))
                    with subsublist.create(Enumerate(enumeration_symbol=r"•")) as subsubsublist:
                        subsubsublist.add_item(NoEscape('Depois de 30 minutos de inatividade;'))
                        subsubsublist.add_item(NoEscape('À meia-noite.'))
                with sublist.create(Enumerate(enumeration_symbol=r"•")) as subsublist:
                    subsublist.add_item(NoEscape('Mudança de campanha:'))
                    with subsublist.create(Enumerate(enumeration_symbol=r"•")) as subsubsublist:
                        subsubsublist.add_item(NoEscape('Se um usuário entra por uma campanha, sai e depois volta para outra. (Fecha o site e entra novamente, por exemplo).'))
            itemize.add_item('Seguidores:')
            with itemize.create(Enumerate(enumeration_symbol=r"")) as sublist:
                sublist.add_item(NoEscape(f'É  possível observar que o número de novos seguidores ou inscritos adquiridos nos mês pode diferir um pouco na primeira tabela, na descrição dela e em cada uma das tabelas seguintes das respectivas redes sociais.'))
                sublist.add_item(NoEscape(f'Nas tabelas de cada rede social está a quantidade total de usuários que seguiram ao logo do mês analisado, mas nesse caso é o dado que foi informado diretamente pela rede social em questão. Chamaremos esse dado de "follows" e os que deixaram de seguir de "unfollows", para uma melhor identificação.'))
                sublist.add_item(NoEscape(f'Na primeira tabela do relatório está o númere referente a quantidade de seguidores que realmente continuaram seguindo a(o) página/perfil/canal ao final do mês. Logo abaixo, o dado "Seguidores adquiridos no mês:" é a quantidade total de usuários que seguiram ao logo do mês analisado. Nesses dois casos os valores são obtidos atraves da quantidade total de seguidores no mês atual e anterior e quantos usuários deixaram de seguir no mês atual.'))
                sublist.add_item(NoEscape(f'Por exemplo: se subtrairmos a quantidade total de seguidores do mês atual pela anterior e somarmos isso a quantos deixaram de seguir (atual - anterior + unfollow), teremos a quantidade total de "Seguidores adquiridos no mês:". Esse valor seria o mesmo dado de seguidores adquiridos que está nas tabelas de cada rede social (follows). E a quantidade de usuários que continuaram seguindo a página seria apenas a diferença do total de seguidores do mês atual e anterior (atual - anterior), que deveria dar no mesmo de subtrair "follows" por "unfollows" (follows - unfollows). Para que fique mais claro, a diferença entre "follows" e "unfollows" somada a quantidade total de seguidores do mês anterior deveria ser igual a quantidade total do mês atual (follows - unfollows + total seg. anterior = total seg. atual).'))
                sublist.add_item(NoEscape(f'Todos esses dados são fornecidos pelas próprias plataformas, mas eles podem acabar sendo um pouco diferentes para sua respectiva rede social.'))
            # itemize.add_item('Top15 notícias mais pesquisadas: as impressões são referentes a quantidade de vezes que uma pesquisa sobre determinado assunto foi realizada e foi possível visualizar o link da notícia no portal do TN entre os resultados.')
            
# with doc.create(Itemize()) as itemize:
#             # itemize.add_item('Em geral, março vem sendo o melhor mês da Tribuna do Norte nas redes sociais e setembro o pior.')
#             itemize.add_item('Calculos de porcentagem:')
#             #doc.append(NoEscape(r'\newline'))
#             with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
#                 sublist.add_item(NoEscape(r'\textbf{Variação:} \Large{\left\(\frac{Mês\ Atual\ -\ Mês\ Anterior}{|Mês\ Anterior|}\right\)}\normalsize * 100.'))
#             with itemize.create(Enumerate(enumeration_symbol=r"")) as sublist:
#                 sublist.add_item(NoEscape(r'O cálculo é feito dessa forma pois quero saber  qual a diferença, em porcentagem, do valor atual em relação ao anterior, seja esse valor anterior o do mês passado ou o do mesmo mês no ano passado. Em outras palavras, quero saber o quanto o valor do mês atual cresceu ou diminuiu em ralação ao outro.'))
#                 sublist.add_item(NoEscape(r'Caso a variação do mês atual com o anterior seja de +10,6\%, além da constatação óbvia de que é um número 10,6\% maior, também quer dizer que essa porcentagem equivale a 10,6\% do valor do mês anterior. Ou seja, se somarmos o valor equivalente a essa porcentagem ao mês anterior o resultado será o valor do mês atual (ou pelo menos algo MUITO próximo).'))
#                 sublist.add_item(NoEscape(r'Por exemplo: se no mês atual o portal teve 957 novos seguidores e o anterior 586, isso quer dizer que o mês atual teve aumento de,  aproxiamdamente, 63,33\%. E sabendo que 63,33\% de 586 é, aproximadamente, 371, podemos provar que 957 - 371 = 586 ou que 586 + 371 = 957.'))
            
#             with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
#                 sublist.add_item(NoEscape(r'\textbf{Taxa de fixação:} \Large{\left\(\frac{Total\ de\ novos\ seg.\ no\ mês\ -\ Total\ de\ seg.\ perdidos\ no\ mês}{Total\ de\ novos\ seg.\ no\ mês}\right\)}\normalsize * 100.'))
#             with itemize.create(Enumerate(enumeration_symbol=r"")) as sublist:
#                 sublist.add_item(NoEscape(r'Nesse cálculo eu quero saber quantos por cento do total de seguidores ganhos continuaram seguindo a rede social em questão.'))
#                 sublist.add_item(NoEscape(r'É importante obeservar que as pessoas que deixaram de seguir não fazem parte apenas dos mesmos que seguiram durante o mês analisado (caso o cálculo ou o texto passem essa impressão), ou apenas dos usuários que já seguiam antes. E saber de qual grupo faz parte a pessoa que deixou de seguir é um dado que não é possível de se obter.'))
                
                
# Gera o arquivo LaTeX
doc.generate_pdf(fr'C:\Users\{GR.path_Usuarios}\Documents\Repositórios\Relatórios\TNsemanal\RelatórioSemanal-TN_Portal e YouTube_{GR.penultimo_domingo().strftime("%d-%m-%Y")} a {GR.ultimo_sabado().strftime("%d-%m-%Y")}', clean_tex=True)

print("Relatório em LaTeX gerado com sucesso!")
