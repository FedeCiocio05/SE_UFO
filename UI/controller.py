import flet as ft

class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def populate_dd(self):
        """ Metodo per popolare i dropdown """
        anni = self._model.load_anni()
        for n in anni:
            self._view.dd_year.options.append(ft.dropdown.Option(n))
        self._view.update()
        # TODO

    def scelta_anno(self, e):
        self.populate_dd_shape()

    def populate_dd_shape(self):
        anno = int(self._view.dd_year.value)
        shape = self._model.load_shape(anno)
        for s in shape:
            self._view.dd_shape.options.append(ft.dropdown.Option(s))
        self._view.update()

    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """
        anno = int(self._view.dd_year.value)
        shape = self._view.dd_shape.value
        self._model.build_graph(anno, shape)

        nodi,archi = self._model.get_graph_details()
        self._view.lista_visualizzazione_1.clean()
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f'Numero di vertici: {nodi}; Numero di archi: {archi}'))

        vicini = self._model.vicini()
        for stato,somma in vicini:
            self._view.lista_visualizzazione_1.controls.append(ft.Text(f'Nodo {stato}, somma pesi su archi = {somma}'))
        self._view.update()
        # TODO

    def handle_path(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """
        # TODO
