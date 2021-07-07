from django.shortcuts import render
from .models import Thing
from django.http import Http404
from plotly.offline import plot
from plotly.subplots import make_subplots
import plotly.graph_objects as x
from plotly.offline import plot


def mvp(request):
    get = Thing.get(hash="key1", sort="key2")
    context = {'item': get}
    return render(request, 'template/teste.html', context)


def home(request):
    def bar():
        get = Thing.get(hash="key1", sort="key2")
        fig = make_subplots(
            vertical_spacing=0.15,
            horizontal_spacing=0.05,
            rows=2, cols=2
        )

        fig.add_trace(x.Bar(
            name='Tensão',
            x=[get],
            y=[15, 25, 35]
        ),
            row=1, col=1)

        #fig.add_trace(x.Scatter(
         #   name='CB',
          #  x=[1, 2, 3],
           # y=[0.1, 0.2, 0.3]),
            #row=1, col=2
       # )

        carai = plot(figure_or_data=fig, output_type='div', include_plotlyjs=False)
        return carai

    context = {'plot1': bar}

    return render(request, 'template/plot.html', context)

