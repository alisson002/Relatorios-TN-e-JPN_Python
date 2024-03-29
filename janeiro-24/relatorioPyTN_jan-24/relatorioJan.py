from pylatex import Document, Section, Subsection, Command, Tabular, Itemize, Enumerate, LineBreak, LargeText, MiniPage, MediumText, MultiRow, NewPage, Subsubsection, SmallText, FootnoteText, NoEscape, Figure, MiniPage
from pylatex.utils import bold
import graficosRelatorio as GR
import pandas as pd
import rpy2.robjects as robjects


# robjects.r('''
#     library(data.table)
#     library(reshape2)
#     library(ggthemes)
#     library(ggplot2)
#     library(dplyr)
#     library(readr)
#     library(knitr)
#     library(reticulate)
#     options(scipen=100)
#     cor_fb <- "#3b5998"
#     cor_ig <- "#d62976"
# ''')

# Cria um novo documento LaTeX
geometry_options = {"tmargin": "2cm", "rmargin": "2.5cm", "lmargin": "2.5cm"}
doc = Document(geometry_options=geometry_options)
doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))

with doc.create(MiniPage(align='c')):
        doc.append(LargeText(("Relatório de Redes Sociais e Portal")))
        doc.append(LineBreak())
        doc.append(LineBreak())
        doc.append(LineBreak())
        doc.append(MediumText(("Janeiro de 2024")))
        doc.append(LineBreak())

# Adiciona a seção para os resultados
with doc.create(Section('Tribuna do Norte', numbering=False)):
    with doc.create(Subsection('Resultados de janeiro/2024', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(2, data='Portal'), '819.084', '3.503.660', '279.000'))
                table.add_row(('', 'novos usuários', 'visualizações', 'usuários recorrentes'))
                table.add_hline()
                table.add_row((MultiRow(2, data='Instagram'), '1404', '542.064', '151.879'))
                table.add_row(('', 'novos seguidores', 'contas atingidas', 'visitas ao perfil'))
                table.add_hline()
                table.add_row((MultiRow(2, data='Facebook'), '112', '467.889', '32.152'))
                table.add_row(('', 'novos seguidores', 'contas atingidas', 'visitas ao perfil'))
                table.add_hline()
                table.add_row((MultiRow(2, data='Twitter'), '1977', '455.800', '13.186'))
                table.add_row(('', 'novos seguidores', 'impressões', 'engajamentos'))
                table.add_hline()
                table.add_row((MultiRow(2, data='Youtube'), '400', '132.064', '2330'))
                table.add_row(('', 'novos inscritos', 'visualizações', 'horas de exibição'))
                

        # Adiciona informações extras
        # Adiciona uma lista com marcadores
        with doc.create(Itemize()) as itemize:
            itemize.add_item("Ao todo, a Tribuna do Norte entregou seu conteúdo para, aproximadamente, 829.760 novas contas, entre Portal, Instagram, Twitter, Facebook e YouTube.")
            itemize.add_item(Command('textbf', arguments='Instagram'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item("Total de seguidores atual: 529.865. Total de seguidores dezembro/2023: 528.459")
                sublist.add_item("Seguidores adquiridos no mês: 6697. Deixaram de seguir: 5293.")
                sublist.add_item("Taxa de fixação: 21%")
            itemize.add_item(Command('textbf', arguments='Facebook'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item("Total de seguidores atual: 332.603. Total de seguidores dezembro/2023: 332.491")
                sublist.add_item("Seguidores adquiridos no mês: 628. Deixaram de seguir: 516.")
                sublist.add_item("Taxa de fixação: 18%")
            itemize.add_item(Command('textbf', arguments='Twitter'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item("Total de seguidores atual: 311.129. Total de seguidores dezembro/2023: 309.152")
                sublist.add_item("Seguidores adquiridos no mês: 2867. Deixaram de seguir: 890.")
                sublist.add_item("Taxa de fixação: 69%")
            itemize.add_item(Command('textbf', arguments='YouTube'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item("Total de seguidores atual: 34.000. Total de seguidores dezembro/2023: 33.600")
                sublist.add_item("Seguidores adquiridos no mês: 484. Deixaram de seguir: 84")
                sublist.add_item("Taxa de fixação: 83%")

doc.append(NewPage())

with doc.create(Subsection('Análise mensal', numbering=False)):
    with doc.create(Subsubsection('Portal', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(3, data='Mês'), 'Novos usuários', 'Visualizações', 'Usuários recorrentes'))
                table.add_row(('', FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao')))
                table.add_row(('', FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Janeiro'), '819 mil', '3,5 milhões', '279 mil'))
                table.add_row(('', FootnoteText('+2% | +29%'), FootnoteText('+13% | -30%'), FootnoteText('-3,5% | +37,4%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Fevereiro'), '805 mil', '5 milhões', '220 mil'))
                # table.add_row(('', FootnoteText('+26,8% | %'), FootnoteText('-20% | %'), FootnoteText('+8,4% | %')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Março'), '838 mil', '9,3 milhões', '302 mil'))
                # table.add_row(('', FootnoteText('+4,1% | %'), FootnoteText('+132,5% | %'), FootnoteText('+37,3% | %')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Abril'), '649 mil', '6,1 milhões', '205 mil'))
                # table.add_row(('', FootnoteText('-22,6% | +102%'), FootnoteText('-34,4% | +165,2%'), FootnoteText('-32,1% | +184,7%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Maio'), '640 mil', '6,4 milhões', '192 mil'))
                # table.add_row(('', FootnoteText('-1,4% | -5%'), FootnoteText('+5% | -8,6%'), FootnoteText('-6,3% | +28,8%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Junho'), '447 mil', '5,6 milhões', '169 mil'))
                # table.add_row(('', FootnoteText('-30% | -17%'), FootnoteText('-12,5% | 0%'), FootnoteText('-12% | 0,6%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Julho'), '586 mil', '6,1 milhões', '175 mil'))
                # table.add_row(('', FootnoteText('+31,1% | -41,4%'), FootnoteText('+9% | -22,8%'), FootnoteText('+3,5% | -30,5%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Agosto'), '606 mil', '6,1 milhões', '194 mil'))
                # table.add_row(('', FootnoteText('+3,4% | -6,6%'), FootnoteText('0% | -16,44%'), FootnoteText('+10,8% | -17,1%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Setembro'), '586 mil', '5,6 milhões', '186 mil'))
                # table.add_row(('', FootnoteText('-3,3% | -41,4%'), FootnoteText('-8,2% | -30%'), FootnoteText('-4% | -44,3%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Outubro'), '957 mil', '4,4 milhões', '250 mil'))
                # table.add_row(('', FootnoteText('+63,3% | -13%'), FootnoteText('-21,4% | -39,7%'), FootnoteText('+34% | -26%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Novembro'), '776 mil', '3,1 milhões', '270 mil'))
                # table.add_row(('', FootnoteText('-19% | +58,7%'), FootnoteText('-29,5% | -22,5%'), FootnoteText('+8% | +33%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Dezembro'), '', '', ''))
                # table.add_row(('', FootnoteText(''), FootnoteText(''), FootnoteText('')))

        # Adiciona informações extras
        # Adiciona uma lista com marcadores
        # with doc.create(Itemize()) as itemize:
        #     itemize.add_item(Command('textbf', arguments='Mês anterior'))
        #     with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        #         sublist.add_item("")
        #         sublist.add_item("")
        #         sublist.add_item("")
        #     itemize.add_item(Command('textbf', arguments='Mesmo mês em 2023'))
        #     with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        #         sublist.add_item("")
        #         sublist.add_item("")
        #         sublist.add_item("")

doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))
doc.preamble.append(NoEscape(r'\usepackage{float}'))

# ORIGEM PORTAL
GR.origemPortal()       
# Adiciona uma seção ao documento
with doc.create(Subsection('', numbering=False)):
    doc.append("Portal: origem dos usuários")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha

    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(GR.origem_plot_path, width=NoEscape(r'1\textwidth'))

doc.append(NewPage())

# TOP10 PORTAL
GR.top10()
# Adiciona uma seção ao documento
with doc.create(Subsection('', numbering=False)):
    doc.append("Portal: 10 notícias mais vistas")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha

    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(GR.top10_plot_path, width=NoEscape(r'0.8\textwidth'))
        
# TOP15 PORTAL
GR.top15()
# Adiciona uma seção ao documento
with doc.create(Subsection('', numbering=False)):
    doc.append("Portal: 15 notícias mais pesquisadas")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(GR.top15_plot_path, width=NoEscape(r'0.9\textwidth'))

# VISUALIZAÇÕES E USUÁRIOS PORTAL
GR.visualizacoesUsuarios()
# Adiciona uma seção ao documento
with doc.create(Subsection('', numbering=False)):
    doc.append("Portal: comparativo de visualizações e acessos de usuários")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(GR.visualizacoesUsuarios_plot_path, width=NoEscape(r'0.8\textwidth'))
        
# VISUALIZAÇÕES POR FE PORTAL
GR.faixaEtaria()
# Adiciona uma seção ao documento
with doc.create(Subsection('', numbering=False)):
    doc.append("Portal: visualizações por faixa etária")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(GR.faixaEtaria_plot_path, width=NoEscape(r'0.8\textwidth'))

doc.append(NewPage())

GR.faixaEtaria_desconhecidaAndTotal()
# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("Portal: visualizações por faixa etária (desconhecida e total)")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(GR.faixaEtaria_desconhecidaAndTotal_plot_path, width=NoEscape(r'0.8\textwidth'))

doc.append(NewPage())

# recebendo camiho da imagem do gráfico e o total de seguidores do fb e ig
fePublico_FBIG_plot_path, FB_followers, IG_followers = GR.fePublico_FBIG()

with doc.create(Subsection('Análise mensal', numbering=False)):
    with doc.create(Subsubsection('Instagram', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(3, data='Mês'), 'Novos seguidores', 'Alcance', 'Visitas'))
                table.add_row(('', FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao')))
                table.add_row(('', FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Janeiro'), '6,7 mil', '542 mil', '152 mil'))
                table.add_row(('', FootnoteText('+21,8% | +440,3%'), FootnoteText('-7% | -19%'), FootnoteText('+17,2% | -26,2%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Fevereiro'), '805 mil', '5 milhões', '220 mil'))
                # table.add_row(('', FootnoteText('+26,8% | %'), FootnoteText('-20% | %'), FootnoteText('+8,4% | %')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Março'), '838 mil', '9,3 milhões', '302 mil'))
                # table.add_row(('', FootnoteText('+4,1% | %'), FootnoteText('+132,5% | %'), FootnoteText('+37,3% | %')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Abril'), '649 mil', '6,1 milhões', '205 mil'))
                # table.add_row(('', FootnoteText('-22,6% | +102%'), FootnoteText('-34,4% | +165,2%'), FootnoteText('-32,1% | +184,7%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Maio'), '640 mil', '6,4 milhões', '192 mil'))
                # table.add_row(('', FootnoteText('-1,4% | -5%'), FootnoteText('+5% | -8,6%'), FootnoteText('-6,3% | +28,8%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Junho'), '447 mil', '5,6 milhões', '169 mil'))
                # table.add_row(('', FootnoteText('-30% | -17%'), FootnoteText('-12,5% | 0%'), FootnoteText('-12% | 0,6%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Julho'), '586 mil', '6,1 milhões', '175 mil'))
                # table.add_row(('', FootnoteText('+31,1% | -41,4%'), FootnoteText('+9% | -22,8%'), FootnoteText('+3,5% | -30,5%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Agosto'), '606 mil', '6,1 milhões', '194 mil'))
                # table.add_row(('', FootnoteText('+3,4% | -6,6%'), FootnoteText('0% | -16,44%'), FootnoteText('+10,8% | -17,1%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Setembro'), '586 mil', '5,6 milhões', '186 mil'))
                # table.add_row(('', FootnoteText('-3,3% | -41,4%'), FootnoteText('-8,2% | -30%'), FootnoteText('-4% | -44,3%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Outubro'), '957 mil', '4,4 milhões', '250 mil'))
                # table.add_row(('', FootnoteText('+63,3% | -13%'), FootnoteText('-21,4% | -39,7%'), FootnoteText('+34% | -26%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Novembro'), '776 mil', '3,1 milhões', '270 mil'))
                # table.add_row(('', FootnoteText('-19% | +58,7%'), FootnoteText('-29,5% | -22,5%'), FootnoteText('+8% | +33%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Dezembro'), '', '', ''))
                # table.add_row(('', FootnoteText(''), FootnoteText(''), FootnoteText('')))

        # Adiciona informações extras
        # Adiciona uma lista com marcadores
        # with doc.create(Itemize()) as itemize:
        #     # itemize.add_item(Command('textbf', arguments='Legenda'))
        #     # with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        #     #     sublist.add_item(str(Command('textbf', arguments='Alcance: '))+"Esta métrica calcula o alcance da distribuição orgânica ou paga do seu conteúdo do Instagram, incluindo publicações e stories que foram turbinados. O alcance só é calculado uma vez se ocorrer por meio da distribuição orgânica e paga;")
        #     #     sublist.add_item(str(Command('textbf', arguments='Visitas: '))+"número de vezes que usuários visitaram seu perfil.")
        #     itemize.add_item(Command('textbf', arguments='Mês anterior'))
        #     with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        #         sublist.add_item("")
        #         sublist.add_item("")
        #         sublist.add_item("")
        #     itemize.add_item(Command('textbf', arguments='Mesmo mês em 2023'))
        #     with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        #         sublist.add_item("")
        #         sublist.add_item("")
        #         sublist.add_item("")

# doc.append(NewPage())

with doc.create(Subsection('Análise mensal', numbering=False)):
    with doc.create(Subsubsection('Facebook', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(3, data='Mês'), 'Novos seguidores', 'Alcance', 'Visitas'))
                table.add_row(('', FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao')))
                table.add_row(('', FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Janeiro'), '628', '468 mil', '32 mil'))
                table.add_row(('', FootnoteText('+38% | +20%'), FootnoteText('-5% | -7,5%'), FootnoteText('+9,6% | +4,2%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Fevereiro'), '805 mil', '5 milhões', '220 mil'))
                # table.add_row(('', FootnoteText('+26,8% | %'), FootnoteText('-20% | %'), FootnoteText('+8,4% | %')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Março'), '838 mil', '9,3 milhões', '302 mil'))
                # table.add_row(('', FootnoteText('+4,1% | %'), FootnoteText('+132,5% | %'), FootnoteText('+37,3% | %')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Abril'), '649 mil', '6,1 milhões', '205 mil'))
                # table.add_row(('', FootnoteText('-22,6% | +102%'), FootnoteText('-34,4% | +165,2%'), FootnoteText('-32,1% | +184,7%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Maio'), '640 mil', '6,4 milhões', '192 mil'))
                # table.add_row(('', FootnoteText('-1,4% | -5%'), FootnoteText('+5% | -8,6%'), FootnoteText('-6,3% | +28,8%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Junho'), '447 mil', '5,6 milhões', '169 mil'))
                # table.add_row(('', FootnoteText('-30% | -17%'), FootnoteText('-12,5% | 0%'), FootnoteText('-12% | 0,6%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Julho'), '586 mil', '6,1 milhões', '175 mil'))
                # table.add_row(('', FootnoteText('+31,1% | -41,4%'), FootnoteText('+9% | -22,8%'), FootnoteText('+3,5% | -30,5%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Agosto'), '606 mil', '6,1 milhões', '194 mil'))
                # table.add_row(('', FootnoteText('+3,4% | -6,6%'), FootnoteText('0% | -16,44%'), FootnoteText('+10,8% | -17,1%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Setembro'), '586 mil', '5,6 milhões', '186 mil'))
                # table.add_row(('', FootnoteText('-3,3% | -41,4%'), FootnoteText('-8,2% | -30%'), FootnoteText('-4% | -44,3%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Outubro'), '957 mil', '4,4 milhões', '250 mil'))
                # table.add_row(('', FootnoteText('+63,3% | -13%'), FootnoteText('-21,4% | -39,7%'), FootnoteText('+34% | -26%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Novembro'), '776 mil', '3,1 milhões', '270 mil'))
                # table.add_row(('', FootnoteText('-19% | +58,7%'), FootnoteText('-29,5% | -22,5%'), FootnoteText('+8% | +33%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Dezembro'), '', '', ''))
                # table.add_row(('', FootnoteText(''), FootnoteText(''), FootnoteText('')))

        # Adiciona informações extras
        # Adiciona uma lista com marcadores
        # with doc.create(Itemize()) as itemize:
        #     # itemize.add_item(Command('textbf', arguments='Legenda'))
        #     # with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        #     #     sublist.add_item(str(Command('textbf', arguments='Alcance: '))+"Esta métrica calcula o alcance da distribuição orgânica ou paga do seu conteúdo do Instagram, incluindo publicações e stories que foram turbinados. O alcance só é calculado uma vez se ocorrer por meio da distribuição orgânica e paga;")
        #     #     sublist.add_item(str(Command('textbf', arguments='Visitas: '))+"número de vezes que usuários visitaram seu perfil ou página.")
        #     itemize.add_item(Command('textbf', arguments='Mês anterior'))
        #     with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        #         sublist.add_item("")
        #         sublist.add_item("")
        #         sublist.add_item("")
        #     itemize.add_item(Command('textbf', arguments='Mesmo mês em 2023'))
        #     with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        #         sublist.add_item("")
        #         sublist.add_item("")
        #         sublist.add_item("")

doc.append(NewPage())

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("FB e IG: audiência por sexo e faixa etária")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(fePublico_FBIG_plot_path, width=NoEscape(r'0.8\textwidth'))

publicoCidades_plot_path = GR.publicoCidades()

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("FB e IG: audiência por cidades")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(publicoCidades_plot_path, width=NoEscape(r'0.8\textwidth'))

doc.append(NewPage())

# curtidasFB_plot_path = GR.curtidasFB()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("FB: curtidas ao longo do mês")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(curtidasFB_plot_path, width=NoEscape(r'0.45\textwidth'))

visitasFB_plot_path = GR.visitasFB()

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("FB: visitas ao longo do mês")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(visitasFB_plot_path, width=NoEscape(r'0.75\textwidth'))

alcanceFB_plot_path = GR.alcanceFB()

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("FB: alcance ao longo do mês")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(alcanceFB_plot_path, width=NoEscape(r'0.75\textwidth'))

seguidoresIG_plot_path, seguidoresIG = GR.seguidoresIG()

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("IG: ganho de seguidores ao longo do mês")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(seguidoresIG_plot_path, width=NoEscape(r'0.45\textwidth'))

visitasIG_plot_path, visitasIG = GR.visitasIG()

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("IG: visitas ao perfil ao longo do mês")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(visitasIG_plot_path, width=NoEscape(r'0.45\textwidth'))

alcanceIG_plot_path, alcanceIG = GR.alcanceIG()

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("IG: alcance do perfil ao longo do mês")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(alcanceIG_plot_path, width=NoEscape(r'0.45\textwidth'))

doc.append(NewPage())

dadosIG_plot_path = GR.dadosIG()

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("IG: comparativo de seguidores, visitas e alcance. (Obs.: dados fora de escala para uma melhor visualização)")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(dadosIG_plot_path, width=NoEscape(r'1\textwidth'))

doc.append(NewPage())

with doc.create(Subsection('Análise mensal', numbering=False)):
    with doc.create(Subsubsection('Twitter', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(3, data='Mês'), 'Novos seguidores', 'Impressões', 'Engajamento'))
                table.add_row(('', FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao')))
                table.add_row(('', FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Janeiro'), '2,9 mil', '455,8 mil', '13,2 mil'))
                table.add_row(('', FootnoteText('+81,3% | +75,8%'), FootnoteText('+6% | -59%'), FootnoteText('+22,2% | -26,7%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Fevereiro'), '805 mil', '5 milhões', '220 mil'))
                # table.add_row(('', FootnoteText('+26,8% | %'), FootnoteText('-20% | %'), FootnoteText('+8,4% | %')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Março'), '838 mil', '9,3 milhões', '302 mil'))
                # table.add_row(('', FootnoteText('+4,1% | %'), FootnoteText('+132,5% | %'), FootnoteText('+37,3% | %')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Abril'), '649 mil', '6,1 milhões', '205 mil'))
                # table.add_row(('', FootnoteText('-22,6% | +102%'), FootnoteText('-34,4% | +165,2%'), FootnoteText('-32,1% | +184,7%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Maio'), '640 mil', '6,4 milhões', '192 mil'))
                # table.add_row(('', FootnoteText('-1,4% | -5%'), FootnoteText('+5% | -8,6%'), FootnoteText('-6,3% | +28,8%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Junho'), '447 mil', '5,6 milhões', '169 mil'))
                # table.add_row(('', FootnoteText('-30% | -17%'), FootnoteText('-12,5% | 0%'), FootnoteText('-12% | 0,6%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Julho'), '586 mil', '6,1 milhões', '175 mil'))
                # table.add_row(('', FootnoteText('+31,1% | -41,4%'), FootnoteText('+9% | -22,8%'), FootnoteText('+3,5% | -30,5%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Agosto'), '606 mil', '6,1 milhões', '194 mil'))
                # table.add_row(('', FootnoteText('+3,4% | -6,6%'), FootnoteText('0% | -16,44%'), FootnoteText('+10,8% | -17,1%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Setembro'), '586 mil', '5,6 milhões', '186 mil'))
                # table.add_row(('', FootnoteText('-3,3% | -41,4%'), FootnoteText('-8,2% | -30%'), FootnoteText('-4% | -44,3%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Outubro'), '957 mil', '4,4 milhões', '250 mil'))
                # table.add_row(('', FootnoteText('+63,3% | -13%'), FootnoteText('-21,4% | -39,7%'), FootnoteText('+34% | -26%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Novembro'), '776 mil', '3,1 milhões', '270 mil'))
                # table.add_row(('', FootnoteText('-19% | +58,7%'), FootnoteText('-29,5% | -22,5%'), FootnoteText('+8% | +33%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Dezembro'), '', '', ''))
                # table.add_row(('', FootnoteText(''), FootnoteText(''), FootnoteText('')))

        # Adiciona informações extras
        # Adiciona uma lista com marcadores
        # with doc.create(Itemize()) as itemize:
        #     # itemize.add_item(Command('textbf', arguments='Legenda'))
        #     # with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        #     #     sublist.add_item(str(Command('textbf', arguments='Impressões: '))+"número de vezes que usuários viram o(s) Tweet(s);")
        #     #     sublist.add_item(str(Command('textbf', arguments='Engajamentos: '))+"número total de vezes que um usuário interagiu com o(s) Tweet(s). Isso inclui todos os cliques em qualquer lugar no Tweet como: hashtags, links, avatar, nome de usuário e expansão do Tweet, Retweets, respostas e favoritos.")
        #     itemize.add_item(Command('textbf', arguments='Mês anterior'))
        #     with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        #         sublist.add_item("")
        #         sublist.add_item("")
        #         sublist.add_item("")
        #     itemize.add_item(Command('textbf', arguments='Mesmo mês em 2023'))
        #     with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        #         sublist.add_item("")
        #         sublist.add_item("")
        #         sublist.add_item("")

doc.append(NewPage())

engajamentoTW_plot_path = GR.engajamentoTW()

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("TW: engajamento do twitter")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(engajamentoTW_plot_path, width=NoEscape(r'0.45\textwidth'))

impressoesTW_plot_path = GR.impressoesTW()

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("TW: impressões do twitter")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(impressoesTW_plot_path, width=NoEscape(r'0.45\textwidth'))

seguidoresTW_plot_path = GR.seguidoresTW()

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("TW: ganho de seguidores no twitter ao logo do mês. (Esses dados levam em consideração apenas os ganhos)")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(seguidoresTW_plot_path, width=NoEscape(r'0.45\textwidth'))

doc.append(NewPage())

with doc.create(Subsection('Análise mensal', numbering=False)):
    with doc.create(Subsubsection('YouTube', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(3, data='Mês'), 'Novos inscritos', 'Visualizações', 'Horas de exibição'))
                table.add_row(('', FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao')))
                table.add_row(('', FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Janeiro'), '484', '132 mil', '2,3 mil'))
                table.add_row(('', FootnoteText('+95,2% | +389%'), FootnoteText('+95,3% | +288%'), FootnoteText('+48% | +172,2%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Fevereiro'), '805 mil', '5 milhões', '220 mil'))
                # table.add_row(('', FootnoteText('+26,8% | %'), FootnoteText('-20% | %'), FootnoteText('+8,4% | %')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Março'), '838 mil', '9,3 milhões', '302 mil'))
                # table.add_row(('', FootnoteText('+4,1% | %'), FootnoteText('+132,5% | %'), FootnoteText('+37,3% | %')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Abril'), '649 mil', '6,1 milhões', '205 mil'))
                # table.add_row(('', FootnoteText('-22,6% | +102%'), FootnoteText('-34,4% | +165,2%'), FootnoteText('-32,1% | +184,7%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Maio'), '640 mil', '6,4 milhões', '192 mil'))
                # table.add_row(('', FootnoteText('-1,4% | -5%'), FootnoteText('+5% | -8,6%'), FootnoteText('-6,3% | +28,8%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Junho'), '447 mil', '5,6 milhões', '169 mil'))
                # table.add_row(('', FootnoteText('-30% | -17%'), FootnoteText('-12,5% | 0%'), FootnoteText('-12% | 0,6%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Julho'), '586 mil', '6,1 milhões', '175 mil'))
                # table.add_row(('', FootnoteText('+31,1% | -41,4%'), FootnoteText('+9% | -22,8%'), FootnoteText('+3,5% | -30,5%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Agosto'), '606 mil', '6,1 milhões', '194 mil'))
                # table.add_row(('', FootnoteText('+3,4% | -6,6%'), FootnoteText('0% | -16,44%'), FootnoteText('+10,8% | -17,1%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Setembro'), '586 mil', '5,6 milhões', '186 mil'))
                # table.add_row(('', FootnoteText('-3,3% | -41,4%'), FootnoteText('-8,2% | -30%'), FootnoteText('-4% | -44,3%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Outubro'), '957 mil', '4,4 milhões', '250 mil'))
                # table.add_row(('', FootnoteText('+63,3% | -13%'), FootnoteText('-21,4% | -39,7%'), FootnoteText('+34% | -26%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Novembro'), '776 mil', '3,1 milhões', '270 mil'))
                # table.add_row(('', FootnoteText('-19% | +58,7%'), FootnoteText('-29,5% | -22,5%'), FootnoteText('+8% | +33%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Dezembro'), '', '', ''))
                # table.add_row(('', FootnoteText(''), FootnoteText(''), FootnoteText('')))

        # Adiciona informações extras
        # Adiciona uma lista com marcadores
        # with doc.create(Itemize()) as itemize:
        #     itemize.add_item(Command('textbf', arguments='Mês anterior'))
        #     with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        #         sublist.add_item("")
        #         sublist.add_item("")
        #         sublist.add_item("")
        #     itemize.add_item(Command('textbf', arguments='Mesmo mês em 2023'))
        #     with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        #         sublist.add_item("")
        #         sublist.add_item("")
        #         sublist.add_item("")

visualizacoesIdadeYTB_plot_path = GR.visualizacoesIdadeYTB()
# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("YouTube: visualizações por faixa etári a")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(visualizacoesIdadeYTB_plot_path, width=NoEscape(r'0.7\textwidth'))

doc.append(NewPage())

horasIdadeYTB_plot_path = GR.horasIdadeYTB()
# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("YouTube: horas de exibição por faixa etária")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(horasIdadeYTB_plot_path, width=NoEscape(r'0.7\textwidth'))
        
generoYTB_plot_path = GR.generoYTB()
# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("YouTube: sexo do público")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(generoYTB_plot_path, width=NoEscape(r'0.6\textwidth'))
        
visualizacoesCidadeYTB_plot_path = GR.visualizacoesCidadeYTB()
# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("YouTube: visualizações por cidade")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(visualizacoesCidadeYTB_plot_path, width=NoEscape(r'0.7\textwidth'))


doc.append(NewPage())

with doc.create(Itemize()) as itemize:
            # itemize.add_item('Em geral, março vem sendo o melhor mês da Tribuna do Norte nas redes sociais e setembro o pior.')
            itemize.add_item('Funcionamento dos algoritmos:')
            #doc.append(NoEscape(r'\newline'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item(NoEscape(r'\textbf{Facebook:} O algoritmo do Facebook prioriza os conteúdos que geram mais interações, como curtidas, comentários e compartilhamentos. Ele também considera o grau de relacionamento entre os usuários e as contas que eles seguem, mostrando mais publicações de amigos e familiares do que de páginas. Além disso, o Facebook leva em conta a relevância e a atualidade dos conteúdos, dando mais destaque para as notícias e os assuntos do momento;'))
                sublist.add_item(NoEscape(r'\textbf{Instagram:} O algoritmo do Instagram também se baseia no engajamento, no relacionamento e na temporalidade dos conteúdos. Ele mostra primeiro as postagens e as histórias das contas com as quais o usuário mais interage, seja por meio de curtidas, comentários, mensagens diretas ou buscas. Ele também valoriza os conteúdos mais recentes e mais relevantes para o usuário, de acordo com os seus interesses e hábitos;'))
                sublist.add_item(NoEscape(r'\textbf{Twitter:} O algoritmo do Twitter tem duas formas de exibir os conteúdos: o modo cronológico e o modo destacado. No modo cronológico, o usuário vê os tweets mais recentes em ordem de publicação. No modo destacado, o usuário vê os tweets mais relevantes para ele, de acordo com o seu perfil, as suas interações e os assuntos do momento. O Twitter também mostra os tweets mais populares e mais comentados na seção “O que está acontecendo”;'))
                sublist.add_item(NoEscape(r'\textbf{YouTube:} O algoritmo do YouTube tem como objetivo aumentar o tempo de permanência dos usuários na plataforma, recomendando os vídeos que eles têm mais chances de assistir e se engajar. Para isso, ele considera fatores como o histórico de visualização, as preferências, as inscrições, a localização e o feedback dos usuários. Ele também leva em conta a qualidade e a relevância dos vídeos, analisando aspectos como o título, descrição, tags, miniaturas e os metadados.'))

# with doc.create(MiniPage(width=r'\textwidth', pos='t!')) as page:
#     page.append(NoEscape(r'\hspace{4em}-'))
#     page.append(Command('textbf', arguments='Facebook: '))
#     page.append(NoEscape(' O algoritmo do Facebook prioriza os conteúdos que geram mais interações, como curtidas, comentários e compartilhamentos. Ele também considera o grau de relacionamento entre os usuários e as contas que eles seguem, mostrando mais publicações de amigos e familiares do que de páginas. Além disso, o Facebook leva em conta a relevância e a atualidade dos conteúdos, dando mais destaque para as notícias e os assuntos do momento.'))
                    
# Gera o arquivo LaTeX
doc.generate_pdf('Relatório-TN_Jan-2024', clean_tex=True)

print("Relatório em LaTeX gerado com sucesso!")
