from django.shortcuts import render
from .models import Thing
from django.http import Http404
from plotly.offline import plot
from plotly.subplots import make_subplots
import plotly.graph_objects as x
from plotly.offline import plot
import pandas
import dash

def mvp(request):
    get = Thing.get(hash="key1", sort="key2")
    context = {'item': get}
    return render(request, 'template/teste.html', context)


def home(request):
    def bar():
        get = Thing.get(hash="key1", sort="key2")
        eixo = get.to_dict()
        v0 = eixo["coluna"][0]
        v1 = eixo["coluna"][1]
        v2 = eixo["coluna"][2]
        v3 = eixo["coluna"][3]
        v4 = eixo["coluna"][4]

        fig = make_subplots(
            vertical_spacing=0.15,
            horizontal_spacing=0.05,
            rows=1, cols=1
        )
        fig.add_trace(x.Bar(
            name='Tensão',
            x=[10, 20, 30, 40, 50],
            y=[v0, v1, v2, v3, v4]
        ),
            row=1, col=1)

        plotar = plot(figure_or_data=fig, output_type='div', include_plotlyjs=False)
        return plotar

    context = {'plot1': bar}

    return render(request, 'template/plot.html', context)









def dashmodelo(request):
    def dashboard():
        get = Thing.get(hash="key1", sort="key2")
        eixo = get.to_dict()
        v0 = eixo["coluna"][0]
        v1 = eixo["coluna"][1]
        v2 = eixo["coluna"][2]
        v3 = eixo["coluna"][3]
        v4 = eixo["coluna"][4]
        df = pandas.read_csv('https://raw.githubusercontent.com/MatheusEmanuelBlackJango/Gr-fico-pra-entrega2/main/planilha%20gr%C3%A1ficos%20pra%20entrega%202.csv')

        fig = make_subplots(
            vertical_spacing=0.15,
            horizontal_spacing=0.05,
            # subplot_titles=('TENSÃO', 'CORRENTE', 'CARGA ESPECÍFICA', 'CARGA DO BANCO'),
            rows=2, cols=3

        )

        fig.add_trace(x.Bar(
            name='Tensão',
            x=[v4, v1, v0],
            y=[v1, v2, v3]),
            row=1, col=2
        )

        fig.add_trace(x.Bar(
            name='Corrente',
            x=[v1, v2, v3],
            y=[v4, v1, v0]),
            row=1, col=3
        )


        fig.add_trace(x.Scatter(
            name='CE1',
            x=[v1, v2, v3],
            y=[v2, v0, v4],
            hovertemplate='célula1 - %{x} horas - %{y}% de carga'),
            row=2, col=2
        )

        fig.add_trace(x.Scatter(
            name='CE2',
            x=[v1, v2, v3],
            y=[v2, v0, v4],
            hovertemplate='célula2 - %{x} horas - %{y}% de carga'),
            row=2, col=2
        )

        # noinspection PyTypeChecker
        fig.add_trace(x.Scatter(
            x=[v1, v2, v3],
            y=[v2, v0, v4],
            marker_color='rgba(203, 254, 0, 0.8)',
            hovertemplate='célula3 - %{x} horas - %{y}% de carga'),
            row=2, col=2
        )

        fig.add_trace(x.Scatter(
            name='CB',
            x=[v0, v1, v4],
            y=[v1, v2, v3],),
            row=2, col=3
        )

        fig.add_trace(x.Indicator(
            mode="gauge+number",
            value=v1,
            title={'text': "temperatura(C°)"},
            domain={'x': [0, 0.2], 'y': [0.4, 1]}
        ))

        fig.update_layout(
            # template= 'plotly_dark', #modelo
            width=1550,  # dimencionamento horizontal da área de plotagem (paper)
            height=750,  # dimensionamento vertical do paper
            title_xanchor='left',  # posição do título
            title='Monitoramento de Baterias',
            titlefont={'family': "Arial", 'size': 40, 'color': 'white'},  # dados do título
            legend_orientation="v", legend=dict(x=1, y=1),  # orientação, posição da legenda (séries)
            plot_bgcolor='powderblue',  # cor da área do gráfico
            paper_bgcolor='lightgreen',
            modebar_orientation='v', modebar_bgcolor='steelblue',  # orientação  e cor da modbarra
        )

        # expressura e cor da borda dos gráficos:

        fig.data[0].marker.line.width = 3
        fig.data[0].marker.line.color = 'white'

        fig.data[1].marker.line.width = 3
        fig.data[1].marker.line.color = 'white'

        fig.data[2].marker.line.width = 3
        fig.data[2].marker.line.color = 'white'

        fig.data[3].marker.line.width = 3
        fig.data[3].marker.line.color = 'white'

        fig.data[4].marker.line.width = 3
        fig.data[4].marker.line.color = 'white'

        fig.data[5].marker.line.width = 3
        fig.data[5].marker.line.color = 'white'

        plotar = plot(figure_or_data=fig, output_type='div', include_plotlyjs=False)
        return plotar

    context = {'plotmodelo': dashboard}

    return render(request, 'template/dash-modelos.html', context)
