import sys
from Consts.enums import SelectionMechods, CrossingMechods, MutationMechods, MinMax, FunctionsOptions, InversionMethods
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QLabel, QComboBox, QRadioButton, \
    QHBoxLayout

from Helpers.layout import makeSlider
from Helpers.lern import Model


class MainWindow(QWidget):
    populationSize = 40
    numberOfParents = 30
    numberOfEpoch = 100
    elitismRate = 0.1
    crossingProb = 0.1
    mutationProb = 0.1
    inversionProb = 0.1
    numberOfDimensions = 2
    q = 1
    tournament_size = 1
    mean = 50
    sigma = 5
    start_value = -5  # Dodajemy deklarację atrybutu start_value
    end_value = 5
   
  

    selectionName = SelectionMechods.BEST_STRING.value
     
    crossingName = CrossingMechods.SINGLE_POINT_ARITHMETIC_STRING.value
    mutationName = MutationMechods.UNIFORM_STRING.value
    inversionName = InversionMethods.TWO_POINT_STRING.value
    minmax = MinMax.MIN
    selection_method = SelectionMechods.BEST
    crossing_method = CrossingMechods.SINGLE_POINT_ARITHMETIC
    mutation_method = MutationMechods.UNIFORM
    func = FunctionsOptions.RASTRIGIN
    inversion_method = InversionMethods.TWO_POINT

    def start_calc(self):
        local_model = Model(number_of_epoch=self.numberOfEpoch,
                            size_of_population=self.populationSize,
                            number_of_parents=self.numberOfParents,
                            elitism_rate=self.elitismRate,
                            crossing_function=self.crossing_method,
                            mutation_function=self.mutation_method,
                            selection_function=self.selection_method,
                            crossing_probability=self.crossingProb,
                            mutation_prob=self.mutationProb,
                            inversion_prob=self.inversionProb,
                            inversion_function=self.inversion_method,
                            number_of_dimensions=self.numberOfDimensions,
                            mean=self.mean,
                            sigma=self.sigma,
                            start_value = self.start_value,
                            end_value = self.end_value,
                            func=self.func,
                            title=f'{self.selectionName} - {self.crossingName}',
                            direction=self.minmax,
                            tournament_size=self.tournament_size,
                            q=self.q)
        final_string = ''
        final_string += local_model.getStartString()
        local_model.fitness()
        final_string += local_model.getEndString()
        local_model.getCharts()
        self.resLabel.setText(f'Wyniki {final_string}')

    def set_selection_method(self, option: int):
        self.selection_options_label.hide()
        self.selection_options_slider.hide()
        match option:
            case SelectionMechods.BEST.value:
                self.selection_method = SelectionMechods.BEST
                self.selectionName = SelectionMechods.BEST_STRING.value
            case SelectionMechods.ROULETTE.value:
                self.selection_method = SelectionMechods.ROULETTE
                self.selectionName = SelectionMechods.ROULETTE_STRING.value
            case SelectionMechods.TOURNAMENT.value:
                self.selection_options_label.setText(f'Wielkość tunrieju {self.selection_options_slider.value()}')
                self.selection_options_label.show()
                self.selection_options_slider.valueChanged.connect(self.set_tournament_size)
                self.selection_options_slider.show()
                self.selection_method = SelectionMechods.TOURNAMENT
                self.selectionName = SelectionMechods.TOURNAMENT_STRING.value

    def set_crossing_method(self, option: int):
        self.crossing_options_label.hide()
        self.crossing_options_slider.hide()
        match option:
            case CrossingMechods.SINGLE_POINT_ARITHMETIC.value:
                self.crossingName = CrossingMechods.SINGLE_POINT_ARITHMETIC_STRING.value
                self.crossing_method = CrossingMechods.SINGLE_POINT_ARITHMETIC
            case CrossingMechods.ARITHMETIC.value:
                self.crossingName = CrossingMechods.ARITHMETIC_STRING.value
                self.crossing_method = CrossingMechods.ARITHMETIC
            case CrossingMechods.LINEAR.value:
                self.crossingName = CrossingMechods.LINEAR_STRING.value
                self.crossing_method = CrossingMechods.LINEAR
            case CrossingMechods.BLEND_ALFA.value:
                self.crossingName = CrossingMechods.BLEND_ALFA_STRING.value
                self.crossing_method = CrossingMechods.BLEND_ALFA
            case CrossingMechods.BLEND_ALFA_BETA.value:
                self.crossingName = CrossingMechods.BLEND_ALFA_BETA_STRING.value
                self.crossing_method = CrossingMechods.BLEND_ALFA_BETA
            case CrossingMechods.AVERAGE.value:
                self.crossingName = CrossingMechods.AVERAGE_STRING.value
                self.crossing_method = CrossingMechods.AVERAGE
            case CrossingMechods.RANDOM.value:
                self.crossingName = CrossingMechods.RANDOM_STRING.value
                self.crossing_method = CrossingMechods.RANDOM
            case CrossingMechods.SIMPLE.value:
                self.crossingName = CrossingMechods.SIMPLE_STRING.value
                self.crossing_method = CrossingMechods.SIMPLE


    def set_mutation_method(self, option: int):
        self.mean_label.hide()
        self.sigma_label.hide()
        self.mean_slider.hide()
        self.sigma_slider.hide()
        match option:
            case MutationMechods.UNIFORM.value:
                self.mutationName = MutationMechods.UNIFORM_STRING.value
                self.mutation_method = MutationMechods.UNIFORM
            case MutationMechods.GAUSS.value:
                self.mean_label.setText(f'Średnia {self.mean_slider.value()}')
                self.mean_label.show()
                self.mean_slider.valueChanged.connect(self.set_mean)
                self.mean_slider.show()
                self.sigma_label.setText(f'Odchylenie standardowe {self.sigma_slider.value()}')
                self.sigma_label.show()
                self.sigma_slider.valueChanged.connect(self.set_sigma)
                self.sigma_slider.show()
                self.mutationName = MutationMechods.GAUSS_STRING.value
                self.mutation_method = MutationMechods.GAUSS

    def set_inversion_method(self, option: int):
        match option:
            case InversionMethods.TWO_POINT.value:
                self.inversionName = InversionMethods.TWO_POINT_STRING.value
                self.inversion_method = InversionMethods.TWO_POINT

    def set_population_size(self, val):
        self.populationSize = val
        self.populationSizeLabel.setText(f'Wielkość populacji {self.populationSize}')

    def set_dimensions_size(self, val):
        self.numberOfDimensions = val
        self.dimensionsSizeLabel.setText(f'Liczba wymiarów {self.numberOfDimensions}')

    def set_start_value(self,val):
        self.start_value = val
        self.start_value_label.setText(f'Początkowy zakres: {self.start_value}')

    def set_end_value(self,val):
        self.end_value = val
        self.end_value_label.setText(f'Końcowy zakres: {self.end_value}')

    def set_number_of_parents(self, val):
        self.numberOfParents = val
        self.numberOfParentsLabel.setText(f'Liczba osobników selekcji {self.numberOfParents}')

    def set_number_of_epoch(self, val):
        self.numberOfEpoch = val
        self.numberOfEpochLabel.setText(f'Liczba epok {self.numberOfEpoch}')

    def set_elitism_rate(self, val):
        self.elitismRate = val / 1000
        self.elitismRateLabel.setText(f'Procent osobników elitarnych {self.elitismRate}')

    def set_crossing_prob(self, val):
        self.crossingProb = val / 1000
        self.crossingProbLabel.setText(f'Prawdopodobieństwo krzyżowania {self.crossingProb}')

    def set_mutation_prob(self, val):
        self.mutationProb = val / 1000
        self.mutationLabel.setText(f'Prawdopodobieństwo mutacji {self.mutationProb}')

    def set_inversion_prob(self, val):
        self.inversionProb = val / 1000
        self.inversionProbLabel.setText(f'Prawdopodobieństwo inwersji {self.inversionProb}')

    def set_mean(self, val):
        self.meanValue = val
        self.mean_label.setText(f'Średnia {self.meanValue}')

    def set_sigma(self, val):
        self.sigmaValue = val
        self.sigma_label.setText(f'Odchylenie standardowe {self.sigmaValue}')

    def set_q(self, val):
        self.crossing_options_label.setText(f'q {val}')

    def set_tournament_size(self, val):
        self.selection_options_label.setText(f'Wielkość turnieju {val}')
        self.tournament_size = val

    def set_min_max(self):
        if self.min_radio.isChecked():
            self.minmax = MinMax.MIN
        else:
            self.minmax = MinMax.MAX

    def set_function(self):
        if self.rastrigin_radio.isChecked():
            self.func = FunctionsOptions.RASTRIGIN
            self.start_value = -5
            self.end_value = 5
            
        else:
            self.func = FunctionsOptions.SCHWEFEK
            self.start_value = -500
            self.end_value = 500
        
        self.start_value_label.setText(f'Początkowy zakres: {self.start_value}')
        self.end_value_label.setText(f'Końcowy zakres: {self.end_value}')

    def __init__(self):
        super().__init__()

        self.setWindowTitle("OE Proj 4. Wieczorek, Piwko, Ratowska")
        layout_items = []


        function_layout = QHBoxLayout()
        function_layout.setContentsMargins(0, 0, 0, 0)

        function_label = QLabel("Wybierz funkcję:")
        function_layout.addWidget(function_label)

        self.rastrigin_radio = QRadioButton("Rastrigin")
        self.rastrigin_radio.setChecked(True)
        self.rastrigin_radio.toggled.connect(self.set_function)
        function_layout.addWidget(self.rastrigin_radio)

        self.schwefel_radio = QRadioButton("Schwefel")
        self.schwefel_radio.toggled.connect(self.set_function)
        function_layout.addWidget(self.schwefel_radio)

        function_container = QWidget()  # Tworzymy kontener dla układu w poziomie
        function_container.setLayout(function_layout)  # Ustawiamy układ w poziomie w kontenerze

        layout_items.append(function_container)  # Dodajemy kontener do głównego układu

        # MinMax selection
        minmax_layout = QHBoxLayout()
        minmax_layout.setContentsMargins(0, 0, 0, 0)

        minmax_label = QLabel("Szukaj:")
        minmax_layout.addWidget(minmax_label)

        self.min_radio = QRadioButton("Minimum")
        self.min_radio.setChecked(True)
        self.min_radio.toggled.connect(self.set_min_max)
        minmax_layout.addWidget(self.min_radio)

        self.max_radio = QRadioButton("Maksimum")
        self.max_radio.toggled.connect(self.set_min_max)
        minmax_layout.addWidget(self.max_radio)

        minmax_container = QWidget()  # Tworzymy kontener dla układu w poziomie
        minmax_container.setLayout(minmax_layout)  # Ustawiamy układ w poziomie w kontenerze

        layout_items.append(minmax_container)

        # Number of dimentions
        self.dimensionsSizeLabel = QLabel(f'Liczba wymiarów {self.numberOfDimensions}')
        layout_items.append(self.dimensionsSizeLabel)

        dimensions_size_slider = makeSlider(1, 100, self.numberOfDimensions)
        dimensions_size_slider.valueChanged.connect(self.set_dimensions_size)
        layout_items.append(dimensions_size_slider)

        # Population Size
        self.populationSizeLabel = QLabel(f'Wielkość populacji {self.populationSize}')
        layout_items.append(self.populationSizeLabel)

        population_size_slider = makeSlider(10, 1000, self.populationSize)
        population_size_slider.valueChanged.connect(self.set_population_size)
        layout_items.append(population_size_slider)

        # Parents
        self.numberOfParentsLabel = QLabel(f'Liczba osobników selekcji {self.numberOfParents}')
        layout_items.append(self.numberOfParentsLabel)

        num_of_parents_slider = makeSlider(10, 1000, self.numberOfParents)
        num_of_parents_slider.valueChanged.connect(self.set_number_of_parents)
        layout_items.append(num_of_parents_slider)

        #Range
        self.start_value_label = QLabel(f'Początkowy zakres: {self.start_value}')
        layout_items.append(self.start_value_label)

        start_value_slider = makeSlider(-20 if self.rastrigin_radio.isChecked() else -1000, 20 if self.rastrigin_radio.isChecked() else 1000, self.start_value)
        start_value_slider.valueChanged.connect(self.set_start_value)
        layout_items.append(start_value_slider)

        self.end_value_label = QLabel(f'Końcowy zakres: {self.end_value}')
        layout_items.append(self.end_value_label)

        end_value_slider = makeSlider(-20 if self.rastrigin_radio.isChecked() else -1000, 20 if self.rastrigin_radio.isChecked() else 1000, self.end_value)
        end_value_slider.valueChanged.connect(self.set_end_value)
        layout_items.append(end_value_slider)


        # Epoch
        self.numberOfEpochLabel = QLabel(f'Liczba epok {self.numberOfEpoch}')
        layout_items.append(self.numberOfEpochLabel)

        num_of_epoch_slider = makeSlider(1, 10_000, self.numberOfEpoch)
        num_of_epoch_slider.valueChanged.connect(self.set_number_of_epoch)
        layout_items.append(num_of_epoch_slider)

        # Elitism
        self.elitismRateLabel = QLabel(f'Procent osobników elitarnych {self.elitismRate}')
        layout_items.append(self.elitismRateLabel)

        elitism_rate_slider = makeSlider(1, 1000, self.elitismRate * 1000)
        elitism_rate_slider.valueChanged.connect(self.set_elitism_rate)
        layout_items.append(elitism_rate_slider)

        # Crossing
        crossing_layout = QHBoxLayout()
        crossing_layout.setContentsMargins(0, 0, 0, 0)

        self.crossingProbLabel = QLabel(f'Prawdopodobieństwo krzyżowania {self.crossingProb}')
        crossing_layout.addWidget(self.crossingProbLabel)

        crossing_prob_slider = makeSlider(1, 1000, self.crossingProb * 1000)
        crossing_prob_slider.valueChanged.connect(self.set_crossing_prob)
        crossing_layout.addWidget(crossing_prob_slider)

        crossing_container = QWidget()
        crossing_container.setLayout(crossing_layout)
        layout_items.append(crossing_container)

        # Inversion
        self.inversionProbLabel = QLabel(f'Prawdopodobieństwo inwersji {self.inversionProb}')
        layout_items.append(self.inversionProbLabel)

        inversion_prob_slider = makeSlider(1, 1000, self.inversionProb * 1000)
        inversion_prob_slider.valueChanged.connect(self.set_inversion_prob)
        layout_items.append(inversion_prob_slider)

        # Selection
        selection_layout = QHBoxLayout()
        selection_layout.setContentsMargins(0, 0, 0, 0)
        selection_method_label = QLabel('Wybierz metodę selekcji')
        selection_layout.addWidget(selection_method_label)

        selection_combo_box = QComboBox(self)
        selection_combo_box.addItems(SelectionMechods.ALL_OPTIONS_STRING.value)

        selection_combo_box.currentIndexChanged.connect(self.set_selection_method)
        selection_layout.addWidget(selection_combo_box)

        selection_container = QWidget()
        selection_container.setLayout(selection_layout)
        layout_items.append(selection_container)

        self.selection_options_label = QLabel('')
        self.selection_options_label.hide()
        layout_items.append(self.selection_options_label)
        self.selection_options_slider = makeSlider(1, 10, 1)
        self.selection_options_slider.hide()
        layout_items.append(self.selection_options_slider)



        # Crossing
        crossing_layout = QHBoxLayout()
        crossing_layout.setContentsMargins(0, 0, 0, 0)
        selection_method_label = QLabel('Wybierz formę krzyżowania')
        crossing_layout.addWidget(selection_method_label)

        crossing_combo_box = QComboBox(self)
        crossing_combo_box.addItems(CrossingMechods.ALL_OPTIONS_STRING.value)
        crossing_combo_box.currentIndexChanged.connect(self.set_crossing_method)
        crossing_layout.addWidget(crossing_combo_box)

        crossing_container = QWidget()
        crossing_container.setLayout(crossing_layout)
        layout_items.append(crossing_container)

        self.crossing_options_label = QLabel('')
        self.crossing_options_label.hide()
        layout_items.append(self.crossing_options_label)
        self.crossing_options_slider = makeSlider(1, 10, 1)
        self.crossing_options_slider.hide()
        layout_items.append(self.crossing_options_slider)

        # Mutations
        mutation_layout = QHBoxLayout()
        mutation_layout.setContentsMargins(0, 0, 0, 0)

        mutation_label = QLabel('Wybierz formę mutacji')
        mutation_layout.addWidget(mutation_label)

        mutation_combo_box = QComboBox(self)
        mutation_combo_box.addItems(MutationMechods.ALL_OPTIONS_STRING.value)
        mutation_combo_box.currentIndexChanged.connect(self.set_mutation_method)
        mutation_layout.addWidget(mutation_combo_box)

        mutation_container = QWidget()
        mutation_container.setLayout(mutation_layout)
        layout_items.append(mutation_container)

        self.mean_label = QLabel('')
        self.mean_label.hide()
        layout_items.append(self.mean_label)

        self.mean_slider = makeSlider(1, 1000, self.mean)
        self.mean_slider.hide()
        layout_items.append(self.mean_slider)

        self.sigma_label = QLabel('')
        self.sigma_label.hide()
        layout_items.append(self.sigma_label)

        self.sigma_slider = makeSlider(1, 500, self.sigma)
        self.sigma_slider.hide()
        layout_items.append(self.sigma_slider)

        mutation_prob_layout = QHBoxLayout()
        mutation_prob_layout.setContentsMargins(0, 0, 0, 0)
        self.mutationLabel = QLabel(f'Prawdopodobieństwo mutacji {self.mutationProb}')
        mutation_prob_layout.addWidget(self.mutationLabel)

        mutation_slider = makeSlider(1, 1000, self.mutationProb * 1000)
        mutation_slider.valueChanged.connect(self.set_mutation_prob)
        mutation_prob_layout.addWidget(mutation_slider)

        mutation_prob_container = QWidget()
        mutation_prob_container.setLayout(mutation_prob_layout)
        layout_items.append(mutation_prob_container)

        # Inwersja
        inversion_layout = QHBoxLayout()
        inversion_layout.setContentsMargins(0, 0, 0, 0)
        inversion_label = QLabel('Wybierz formę inwersji')
        inversion_layout.addWidget(inversion_label)

        inversion_combo_box = QComboBox(self)
        inversion_combo_box.addItems(InversionMethods.ALL_OPTIONS_STRING.value)
        inversion_combo_box.currentIndexChanged.connect(self.set_inversion_method)
        inversion_layout.addWidget(inversion_combo_box)

        inversion_container = QWidget()
        inversion_container.setLayout(inversion_layout)
        layout_items.append(inversion_container)


        # Start
        button = QPushButton("Oblicz")
        button.clicked.connect(self.start_calc)
        layout_items.append(button)

        # retrun of learn
        self.resLabel = QLabel('Wyniki:')
        layout_items.append(self.resLabel)

        layout = QVBoxLayout()

        for item in layout_items:
            layout.addWidget(item)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()
