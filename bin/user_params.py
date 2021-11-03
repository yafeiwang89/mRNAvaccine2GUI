 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        widget2_layout = {'width': '10%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}
        divider_button_layout={'width':'40%'}

        param_name1 = Button(description='random_seed', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.random_seed = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        param_name2 = Button(description='ignore_smoothing_flag', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.ignore_smoothing_flag = IntText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        div_row1 = Button(description='--Immune activation parameters--', disabled=True, layout=divider_button_layout)

        param_name3 = Button(description='immune_dt', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.immune_dt = FloatText(
          value=10,
          step=1,
          style=style, layout=widget_layout)

        param_name4 = Button(description='immune_z_offset', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.immune_z_offset = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        div_row2 = Button(description='---Initialization Options--', disabled=True, layout=divider_button_layout)

        param_name5 = Button(description='number_of_CD8_Tcells', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.number_of_CD8_Tcells = IntText(
          value=80,
          step=1,
          style=style, layout=widget_layout)

        param_name6 = Button(description='number_of_macrophages', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.number_of_macrophages = IntText(
          value=50,
          step=1,
          style=style, layout=widget_layout)

        param_name7 = Button(description='number_of_DCs', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'lightgreen'

        self.number_of_DCs = IntText(
          value=28,
          step=1,
          style=style, layout=widget_layout)

        param_name8 = Button(description='number_of_CD4_Tcells', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'tan'

        self.number_of_CD4_Tcells = IntText(
          value=20,
          step=1,
          style=style, layout=widget_layout)

        param_name9 = Button(description='DC_induced_CD8_proliferation', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'lightgreen'

        self.DC_induced_CD8_proliferation = FloatText(
          value=0.00208,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name10 = Button(description='DC_induced_CD4_proliferation', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'tan'

        self.DC_induced_CD4_proliferation = FloatText(
          value=0.00208,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name11 = Button(description='DC_induced_CD8_attachment', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'lightgreen'

        self.DC_induced_CD8_attachment = FloatText(
          value=0.04,
          step=0.01,
          style=style, layout=widget_layout)

        param_name12 = Button(description='departure_rate_of_DCs', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'tan'

        self.departure_rate_of_DCs = FloatText(
          value=0.001,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name13 = Button(description='epsilon_distance', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'lightgreen'

        self.epsilon_distance = FloatText(
          value=1.75,
          step=0.1,
          style=style, layout=widget_layout)

        param_name14 = Button(description='perecentage_tissue_vascularized', disabled=True, layout=name_button_layout)
        param_name14.style.button_color = 'tan'

        self.perecentage_tissue_vascularized = FloatText(
          value=8.8,
          step=0.1,
          style=style, layout=widget_layout)

        div_row3 = Button(description='---Cell Color Options--', disabled=True, layout=divider_button_layout)

        param_name15 = Button(description='color_variable', disabled=True, layout=name_button_layout)
        param_name15.style.button_color = 'lightgreen'

        self.color_variable = Text(
          value='assembled_virion',
          style=style, layout=widget_layout)

        param_name16 = Button(description='epithelial_opacity', disabled=True, layout=name_button_layout)
        param_name16.style.button_color = 'tan'

        self.epithelial_opacity = FloatText(
          value=0.65,
          step=0.1,
          style=style, layout=widget_layout)

        param_name17 = Button(description='non_epithelial_opacity', disabled=True, layout=name_button_layout)
        param_name17.style.button_color = 'lightgreen'

        self.non_epithelial_opacity = FloatText(
          value=0.8,
          step=0.1,
          style=style, layout=widget_layout)

        param_name18 = Button(description='apoptotic_tumor_color', disabled=True, layout=name_button_layout)
        param_name18.style.button_color = 'tan'

        self.apoptotic_tumor_color = Text(
          value='black',
          style=style, layout=widget_layout)

        param_name19 = Button(description='apoptotic_immune_color', disabled=True, layout=name_button_layout)
        param_name19.style.button_color = 'lightgreen'

        self.apoptotic_immune_color = Text(
          value='rosybrown',
          style=style, layout=widget_layout)

        param_name20 = Button(description='CD8_Tcell_color', disabled=True, layout=name_button_layout)
        param_name20.style.button_color = 'tan'

        self.CD8_Tcell_color = Text(
          value='red',
          style=style, layout=widget_layout)

        param_name21 = Button(description='CD4_Tcell_color', disabled=True, layout=name_button_layout)
        param_name21.style.button_color = 'lightgreen'

        self.CD4_Tcell_color = Text(
          value='orange',
          style=style, layout=widget_layout)

        param_name22 = Button(description='Macrophage_color', disabled=True, layout=name_button_layout)
        param_name22.style.button_color = 'tan'

        self.Macrophage_color = Text(
          value='rgb(35,139,69)',
          style=style, layout=widget_layout)

        param_name23 = Button(description='activated_macrophage_color', disabled=True, layout=name_button_layout)
        param_name23.style.button_color = 'lightgreen'

        self.activated_macrophage_color = Text(
          value='lime',
          style=style, layout=widget_layout)

        param_name24 = Button(description='exhausted_macrophage_color', disabled=True, layout=name_button_layout)
        param_name24.style.button_color = 'tan'

        self.exhausted_macrophage_color = Text(
          value='rgb(116,196,118)',
          style=style, layout=widget_layout)

        param_name25 = Button(description='hyperactivated_macrophage_color', disabled=True, layout=name_button_layout)
        param_name25.style.button_color = 'lightgreen'

        self.hyperactivated_macrophage_color = Text(
          value='rgb(168,221,181)',
          style=style, layout=widget_layout)

        param_name26 = Button(description='DC_color', disabled=True, layout=name_button_layout)
        param_name26.style.button_color = 'tan'

        self.DC_color = Text(
          value='rgb(129,15,124)',
          style=style, layout=widget_layout)

        param_name27 = Button(description='activated_DC_color', disabled=True, layout=name_button_layout)
        param_name27.style.button_color = 'lightgreen'

        self.activated_DC_color = Text(
          value='hotpink',
          style=style, layout=widget_layout)

        param_name28 = Button(description='phagocytes_virus_uptake_rate', disabled=True, layout=name_button_layout)
        param_name28.style.button_color = 'tan'

        self.phagocytes_virus_uptake_rate = FloatText(
          value=0.0001,
          step=1e-05,
          style=style, layout=widget_layout)

        param_name29 = Button(description='Antibody_binding_rate', disabled=True, layout=name_button_layout)
        param_name29.style.button_color = 'lightgreen'

        self.Antibody_binding_rate = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name30 = Button(description='antibody_half_effect', disabled=True, layout=name_button_layout)
        param_name30.style.button_color = 'tan'

        self.antibody_half_effect = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        div_row4 = Button(description='---mRNA vaccine for cancer treatments--', disabled=True, layout=divider_button_layout)

        param_name31 = Button(description='LNP_fraction_released_at_death', disabled=True, layout=name_button_layout)
        param_name31.style.button_color = 'lightgreen'

        self.LNP_fraction_released_at_death = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name32 = Button(description='ISF_secretion_rate', disabled=True, layout=name_button_layout)
        param_name32.style.button_color = 'tan'

        self.ISF_secretion_rate = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name33 = Button(description='tumor_radius', disabled=True, layout=name_button_layout)
        param_name33.style.button_color = 'lightgreen'

        self.tumor_radius = FloatText(
          value=350,
          step=10,
          style=style, layout=widget_layout)

        param_name34 = Button(description='default_apoptosis_rate', disabled=True, layout=name_button_layout)
        param_name34.style.button_color = 'tan'

        self.default_apoptosis_rate = FloatText(
          value=5.31667e-05,
          step=1e-05,
          style=style, layout=widget_layout)

        param_name35 = Button(description='max_Ig_complex_color', disabled=True, layout=name_button_layout)
        param_name35.style.button_color = 'lightgreen'

        self.max_Ig_complex_color = FloatText(
          value=50,
          step=1,
          style=style, layout=widget_layout)

        param_name36 = Button(description='original_antigen_protein', disabled=True, layout=name_button_layout)
        param_name36.style.button_color = 'tan'

        self.original_antigen_protein = FloatText(
          value=500,
          step=10,
          style=style, layout=widget_layout)

        param_name37 = Button(description='antigen_antibody_inherit_ratio', disabled=True, layout=name_button_layout)
        param_name37.style.button_color = 'lightgreen'

        self.antigen_antibody_inherit_ratio = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name38 = Button(description='Ig_induce_apoptosis', disabled=True, layout=name_button_layout)
        param_name38.style.button_color = 'tan'

        self.Ig_induce_apoptosis = FloatText(
          value=0.005,
          step=0.001,
          style=style, layout=widget_layout)

        param_name39 = Button(description='Ig_antigen_50', disabled=True, layout=name_button_layout)
        param_name39.style.button_color = 'lightgreen'

        self.Ig_antigen_50 = FloatText(
          value=90,
          step=1,
          style=style, layout=widget_layout)

        param_name40 = Button(description='LNP_escape_rate', disabled=True, layout=name_button_layout)
        param_name40.style.button_color = 'tan'

        self.LNP_escape_rate = FloatText(
          value=0.005,
          step=0.001,
          style=style, layout=widget_layout)

        param_name41 = Button(description='uncoated_LNP_rate', disabled=True, layout=name_button_layout)
        param_name41.style.button_color = 'lightgreen'

        self.uncoated_LNP_rate = FloatText(
          value=0.005,
          step=0.001,
          style=style, layout=widget_layout)

        param_name42 = Button(description='uncoated_to_RNA_rate', disabled=True, layout=name_button_layout)
        param_name42.style.button_color = 'tan'

        self.uncoated_to_RNA_rate = FloatText(
          value=0.005,
          step=0.001,
          style=style, layout=widget_layout)

        param_name43 = Button(description='epitope_translation_rate', disabled=True, layout=name_button_layout)
        param_name43.style.button_color = 'lightgreen'

        self.epitope_translation_rate = FloatText(
          value=0.005,
          step=0.001,
          style=style, layout=widget_layout)

        param_name44 = Button(description='mRNA_decay_rate', disabled=True, layout=name_button_layout)
        param_name44.style.button_color = 'tan'

        self.mRNA_decay_rate = FloatText(
          value=0.0012,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name45 = Button(description='antigenic_epitope_decay_rate', disabled=True, layout=name_button_layout)
        param_name45.style.button_color = 'lightgreen'

        self.antigenic_epitope_decay_rate = FloatText(
          value=1.6e-04,
          step=1e-05,
          style=style, layout=widget_layout)

        param_name46 = Button(description='activate_immune_response_time', disabled=True, layout=name_button_layout)
        param_name46.style.button_color = 'tan'

        self.activate_immune_response_time = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name47 = Button(description='cytotoxic_T_response', disabled=True, layout=name_button_layout)
        param_name47.style.button_color = 'lightgreen'

        self.cytotoxic_T_response = Checkbox(
          value=True,
          style=style, layout=widget_layout)

        param_name48 = Button(description='antibody_response', disabled=True, layout=name_button_layout)
        param_name48.style.button_color = 'tan'

        self.antibody_response = Checkbox(
          value=True,
          style=style, layout=widget_layout)

        param_name49 = Button(description='CD8_recruit_rate', disabled=True, layout=name_button_layout)
        param_name49.style.button_color = 'lightgreen'

        self.CD8_recruit_rate = FloatText(
          value=0.0005,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name50 = Button(description='CD4_recruit_rate', disabled=True, layout=name_button_layout)
        param_name50.style.button_color = 'tan'

        self.CD4_recruit_rate = FloatText(
          value=0.0005,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name51 = Button(description='Ig_recruit_rate', disabled=True, layout=name_button_layout)
        param_name51.style.button_color = 'lightgreen'

        self.Ig_recruit_rate = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name52 = Button(description='encapsulate_LNP_initial', disabled=True, layout=name_button_layout)
        param_name52.style.button_color = 'tan'

        self.encapsulate_LNP_initial = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        param_name53 = Button(description='mRNA_doses', disabled=True, layout=name_button_layout)
        param_name53.style.button_color = 'lightgreen'

        self.mRNA_doses = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name54 = Button(description='injection_frequency', disabled=True, layout=name_button_layout)
        param_name54.style.button_color = 'tan'

        self.injection_frequency = FloatText(
          value=7,
          step=0.1,
          style=style, layout=widget_layout)

        param_name55 = Button(description='clearance_rate', disabled=True, layout=name_button_layout)
        param_name55.style.button_color = 'lightgreen'

        self.clearance_rate = FloatText(
          value=4.8135e-04,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name56 = Button(description='start_inject_time', disabled=True, layout=name_button_layout)
        param_name56.style.button_color = 'tan'

        self.start_inject_time = FloatText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name57 = Button(description='introduce_DC_cells_time', disabled=True, layout=name_button_layout)
        param_name57.style.button_color = 'lightgreen'

        self.introduce_DC_cells_time = FloatText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name58 = Button(description='DC_tumor_ratio', disabled=True, layout=name_button_layout)
        param_name58.style.button_color = 'tan'

        self.DC_tumor_ratio = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name59 = Button(description='number_DCs_introduced', disabled=True, layout=name_button_layout)
        param_name59.style.button_color = 'lightgreen'

        self.number_DCs_introduced = IntText(
          value=226,
          step=10,
          style=style, layout=widget_layout)

        param_name60 = Button(description='ISF_needed_for_DC_activation', disabled=True, layout=name_button_layout)
        param_name60.style.button_color = 'tan'

        self.ISF_needed_for_DC_activation = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name61 = Button(description='antigenic_epitope_needed_for_DC_activation', disabled=True, layout=name_button_layout)
        param_name61.style.button_color = 'lightgreen'

        self.antigenic_epitope_needed_for_DC_activation = FloatText(
          value=15,
          step=1,
          style=style, layout=widget_layout)

        units_button1 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'tan'
        units_button4 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'lightgreen'
        units_button5 = Button(description='micron', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'tan'
        units_button6 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'tan'
        units_button7 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'lightgreen'
        units_button8 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'tan'
        units_button9 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'lightgreen'
        units_button10 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'tan'
        units_button11 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'lightgreen'
        units_button12 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'tan'
        units_button13 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'lightgreen'
        units_button14 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'tan'
        units_button15 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button15.style.button_color = 'lightgreen'
        units_button16 = Button(description='percentage', disabled=True, layout=units_button_layout) 
        units_button16.style.button_color = 'tan'
        units_button17 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button17.style.button_color = 'tan'
        units_button18 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button18.style.button_color = 'lightgreen'
        units_button19 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button19.style.button_color = 'tan'
        units_button20 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button20.style.button_color = 'lightgreen'
        units_button21 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button21.style.button_color = 'tan'
        units_button22 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button22.style.button_color = 'lightgreen'
        units_button23 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button23.style.button_color = 'tan'
        units_button24 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button24.style.button_color = 'lightgreen'
        units_button25 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button25.style.button_color = 'tan'
        units_button26 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button26.style.button_color = 'lightgreen'
        units_button27 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button27.style.button_color = 'tan'
        units_button28 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button28.style.button_color = 'lightgreen'
        units_button29 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button29.style.button_color = 'tan'
        units_button30 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button30.style.button_color = 'lightgreen'
        units_button31 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button31.style.button_color = 'tan'
        units_button32 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button32.style.button_color = 'lightgreen'
        units_button33 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button33.style.button_color = 'tan'
        units_button34 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button34.style.button_color = 'tan'
        units_button35 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button35.style.button_color = 'lightgreen'
        units_button36 = Button(description='micron^3/min', disabled=True, layout=units_button_layout) 
        units_button36.style.button_color = 'tan'
        units_button37 = Button(description='micron', disabled=True, layout=units_button_layout) 
        units_button37.style.button_color = 'lightgreen'
        units_button38 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button38.style.button_color = 'tan'
        units_button39 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button39.style.button_color = 'lightgreen'
        units_button40 = Button(description='antigen', disabled=True, layout=units_button_layout) 
        units_button40.style.button_color = 'tan'
        units_button41 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button41.style.button_color = 'lightgreen'
        units_button42 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button42.style.button_color = 'tan'
        units_button43 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button43.style.button_color = 'lightgreen'
        units_button44 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button44.style.button_color = 'tan'
        units_button45 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button45.style.button_color = 'lightgreen'
        units_button46 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button46.style.button_color = 'tan'
        units_button47 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button47.style.button_color = 'lightgreen'
        units_button48 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button48.style.button_color = 'tan'
        units_button49 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button49.style.button_color = 'lightgreen'
        units_button50 = Button(description='hour', disabled=True, layout=units_button_layout) 
        units_button50.style.button_color = 'tan'
        units_button51 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button51.style.button_color = 'lightgreen'
        units_button52 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button52.style.button_color = 'tan'
        units_button53 = Button(description='cells/min', disabled=True, layout=units_button_layout) 
        units_button53.style.button_color = 'lightgreen'
        units_button54 = Button(description='cells/min', disabled=True, layout=units_button_layout) 
        units_button54.style.button_color = 'tan'
        units_button55 = Button(description='Ig/min', disabled=True, layout=units_button_layout) 
        units_button55.style.button_color = 'lightgreen'
        units_button56 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button56.style.button_color = 'tan'
        units_button57 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button57.style.button_color = 'lightgreen'
        units_button58 = Button(description='day', disabled=True, layout=units_button_layout) 
        units_button58.style.button_color = 'tan'
        units_button59 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button59.style.button_color = 'lightgreen'
        units_button60 = Button(description='hour', disabled=True, layout=units_button_layout) 
        units_button60.style.button_color = 'tan'
        units_button61 = Button(description='hour', disabled=True, layout=units_button_layout) 
        units_button61.style.button_color = 'lightgreen'
        units_button62 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button62.style.button_color = 'tan'
        units_button63 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button63.style.button_color = 'lightgreen'
        units_button64 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button64.style.button_color = 'tan'
        units_button65 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button65.style.button_color = 'lightgreen'

        desc_button1 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='how often we check to introduce immune cells' , tooltip='how often we check to introduce immune cells', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='immune cell position over the epithelium' , tooltip='immune cell position over the epithelium', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='initial number of CD8 T cells in tissue' , tooltip='initial number of CD8 T cells in tissue', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='initial number of macrophages' , tooltip='initial number of macrophages', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='initial number of Dendritic Cells' , tooltip='initial number of Dendritic Cells', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='initial number of CD4 Tcells in tissue' , tooltip='initial number of CD4 Tcells in tissue', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='DC induced CD8 proliferation rate' , tooltip='DC induced CD8 proliferation rate', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='DC induced CD4 proliferation rate' , tooltip='DC induced CD4 proliferation rate', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='DC induced CD8 attachement rate' , tooltip='DC induced CD8 attachement rate', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='Departure rate of activated DCs' , tooltip='Departure rate of activated DCs', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'
        desc_button14 = Button(description='percentage of tissue sitting above blood vessels' , tooltip='percentage of tissue sitting above blood vessels', disabled=True, layout=desc_button_layout) 
        desc_button14.style.button_color = 'tan'
        desc_button15 = Button(description='color cells based on this variable' , tooltip='color cells based on this variable', disabled=True, layout=desc_button_layout) 
        desc_button15.style.button_color = 'lightgreen'
        desc_button16 = Button(description='opacity of epithelial cells' , tooltip='opacity of epithelial cells', disabled=True, layout=desc_button_layout) 
        desc_button16.style.button_color = 'tan'
        desc_button17 = Button(description='opacity of non-epithelial cells' , tooltip='opacity of non-epithelial cells', disabled=True, layout=desc_button_layout) 
        desc_button17.style.button_color = 'lightgreen'
        desc_button18 = Button(description='apoptotic tumor cell color' , tooltip='apoptotic tumor cell color', disabled=True, layout=desc_button_layout) 
        desc_button18.style.button_color = 'tan'
        desc_button19 = Button(description='apoptotic immune cell color' , tooltip='apoptotic immune cell color', disabled=True, layout=desc_button_layout) 
        desc_button19.style.button_color = 'lightgreen'
        desc_button20 = Button(description='CD8 T cell color' , tooltip='CD8 T cell color', disabled=True, layout=desc_button_layout) 
        desc_button20.style.button_color = 'tan'
        desc_button21 = Button(description='CD4 T cell color' , tooltip='CD4 T cell color', disabled=True, layout=desc_button_layout) 
        desc_button21.style.button_color = 'lightgreen'
        desc_button22 = Button(description='macrophage color' , tooltip='macrophage color', disabled=True, layout=desc_button_layout) 
        desc_button22.style.button_color = 'tan'
        desc_button23 = Button(description='color of activated macrophage' , tooltip='color of activated macrophage', disabled=True, layout=desc_button_layout) 
        desc_button23.style.button_color = 'lightgreen'
        desc_button24 = Button(description='color of exhausted macrophage' , tooltip='color of exhausted macrophage', disabled=True, layout=desc_button_layout) 
        desc_button24.style.button_color = 'tan'
        desc_button25 = Button(description='color of hyperactivated macrophage' , tooltip='color of hyperactivated macrophage', disabled=True, layout=desc_button_layout) 
        desc_button25.style.button_color = 'lightgreen'
        desc_button26 = Button(description='DC color' , tooltip='DC color', disabled=True, layout=desc_button_layout) 
        desc_button26.style.button_color = 'tan'
        desc_button27 = Button(description='DC color' , tooltip='DC color', disabled=True, layout=desc_button_layout) 
        desc_button27.style.button_color = 'lightgreen'
        desc_button28 = Button(description='Rate that phagocytes uptake virus after activation' , tooltip='Rate that phagocytes uptake virus after activation', disabled=True, layout=desc_button_layout) 
        desc_button28.style.button_color = 'tan'
        desc_button29 = Button(description='Binding rate of antibody to infected cells' , tooltip='Binding rate of antibody to infected cells', disabled=True, layout=desc_button_layout) 
        desc_button29.style.button_color = 'lightgreen'
        desc_button30 = Button(description='Half effect of antibody on macrophage phagocytosis' , tooltip='Half effect of antibody on macrophage phagocytosis', disabled=True, layout=desc_button_layout) 
        desc_button30.style.button_color = 'tan'
        desc_button31 = Button(description='fraction of LNP released at cell death' , tooltip='fraction of LNP released at cell death', disabled=True, layout=desc_button_layout) 
        desc_button31.style.button_color = 'lightgreen'
        desc_button32 = Button(description='ISF secretion rate of tumor cell' , tooltip='ISF secretion rate of tumor cell', disabled=True, layout=desc_button_layout) 
        desc_button32.style.button_color = 'tan'
        desc_button33 = Button(description='Initial tumor radius' , tooltip='Initial tumor radius', disabled=True, layout=desc_button_layout) 
        desc_button33.style.button_color = 'lightgreen'
        desc_button34 = Button(description='tumor cell defatul apoptosis rate' , tooltip='tumor cell defatul apoptosis rate', disabled=True, layout=desc_button_layout) 
        desc_button34.style.button_color = 'tan'
        desc_button35 = Button(description='the threshold of antigen-antibody complex for color tumor cell' , tooltip='the threshold of antigen-antibody complex for color tumor cell', disabled=True, layout=desc_button_layout) 
        desc_button35.style.button_color = 'lightgreen'
        desc_button36 = Button(description='original number of antigen proteins on tumor cell membrane' , tooltip='original number of antigen proteins on tumor cell membrane', disabled=True, layout=desc_button_layout) 
        desc_button36.style.button_color = 'tan'
        desc_button37 = Button(description='inheritance ratio of antigen-antibody complex at tumor cell division' , tooltip='inheritance ratio of antigen-antibody complex at tumor cell division', disabled=True, layout=desc_button_layout) 
        desc_button37.style.button_color = 'lightgreen'
        desc_button38 = Button(description='Antibdy complex induce tumor apoptosis rate' , tooltip='Antibdy complex induce tumor apoptosis rate', disabled=True, layout=desc_button_layout) 
        desc_button38.style.button_color = 'tan'
        desc_button39 = Button(description='Antibdy-antigen complex that kill half tumor cells' , tooltip='Antibdy-antigen complex that kill half tumor cells', disabled=True, layout=desc_button_layout) 
        desc_button39.style.button_color = 'lightgreen'
        desc_button40 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button40.style.button_color = 'tan'
        desc_button41 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button41.style.button_color = 'lightgreen'
        desc_button42 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button42.style.button_color = 'tan'
        desc_button43 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button43.style.button_color = 'lightgreen'
        desc_button44 = Button(description='mRNA degradation rate' , tooltip='mRNA degradation rate', disabled=True, layout=desc_button_layout) 
        desc_button44.style.button_color = 'tan'
        desc_button45 = Button(description='antigenic epitope degradation rate' , tooltip='antigenic epitope degradation rate', disabled=True, layout=desc_button_layout) 
        desc_button45.style.button_color = 'lightgreen'
        desc_button46 = Button(description='when T cells and antibody response activated' , tooltip='when T cells and antibody response activated', disabled=True, layout=desc_button_layout) 
        desc_button46.style.button_color = 'tan'
        desc_button47 = Button(description='enabled cytotoxic T responses or not' , tooltip='enabled cytotoxic T responses or not', disabled=True, layout=desc_button_layout) 
        desc_button47.style.button_color = 'lightgreen'
        desc_button48 = Button(description='enabled antibody responses or not' , tooltip='enabled antibody responses or not', disabled=True, layout=desc_button_layout) 
        desc_button48.style.button_color = 'tan'
        desc_button49 = Button(description='max CD8 T recruitment rate (for antigen epitope)' , tooltip='max CD8 T recruitment rate (for antigen epitope)', disabled=True, layout=desc_button_layout) 
        desc_button49.style.button_color = 'lightgreen'
        desc_button50 = Button(description='max CD4 T recruitment rate (for antigen epitope)' , tooltip='max CD4 T recruitment rate (for antigen epitope)', disabled=True, layout=desc_button_layout) 
        desc_button50.style.button_color = 'tan'
        desc_button51 = Button(description='max antibody recruitment rate (due to CD4 T)' , tooltip='max antibody recruitment rate (due to CD4 T)', disabled=True, layout=desc_button_layout) 
        desc_button51.style.button_color = 'lightgreen'
        desc_button52 = Button(description='If directly encapsulate LNPs in endosome of DC cells directly' , tooltip='If directly encapsulate LNPs in endosome of DC cells directly', disabled=True, layout=desc_button_layout) 
        desc_button52.style.button_color = 'tan'
        desc_button53 = Button(description='LNP injection doses' , tooltip='LNP injection doses', disabled=True, layout=desc_button_layout) 
        desc_button53.style.button_color = 'lightgreen'
        desc_button54 = Button(description='The NP injection frequency' , tooltip='The NP injection frequency', disabled=True, layout=desc_button_layout) 
        desc_button54.style.button_color = 'tan'
        desc_button55 = Button(description='NPs cleaning rate in blood vessel' , tooltip='NPs cleaning rate in blood vessel', disabled=True, layout=desc_button_layout) 
        desc_button55.style.button_color = 'lightgreen'
        desc_button56 = Button(description='when inject mRNA vaccine LNP' , tooltip='when inject mRNA vaccine LNP', disabled=True, layout=desc_button_layout) 
        desc_button56.style.button_color = 'tan'
        desc_button57 = Button(description='when introduce DC cells in tumor domain' , tooltip='when introduce DC cells in tumor domain', disabled=True, layout=desc_button_layout) 
        desc_button57.style.button_color = 'lightgreen'
        desc_button58 = Button(description='the ratio of DCs and tumor cells (viable) when introduceed' , tooltip='the ratio of DCs and tumor cells (viable) when introduceed', disabled=True, layout=desc_button_layout) 
        desc_button58.style.button_color = 'tan'
        desc_button59 = Button(description='number of DCs when introduceed' , tooltip='number of DCs when introduceed', disabled=True, layout=desc_button_layout) 
        desc_button59.style.button_color = 'lightgreen'
        desc_button60 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button60.style.button_color = 'tan'
        desc_button61 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button61.style.button_color = 'lightgreen'

        row1 = [param_name1, self.random_seed, units_button1, desc_button1] 
        row2 = [param_name2, self.ignore_smoothing_flag, units_button2, desc_button2] 
        row3 = [param_name3, self.immune_dt, units_button4, desc_button3] 
        row4 = [param_name4, self.immune_z_offset, units_button5, desc_button4] 
        row5 = [param_name5, self.number_of_CD8_Tcells, units_button7, desc_button5] 
        row6 = [param_name6, self.number_of_macrophages, units_button8, desc_button6] 
        row7 = [param_name7, self.number_of_DCs, units_button9, desc_button7] 
        row8 = [param_name8, self.number_of_CD4_Tcells, units_button10, desc_button8] 
        row9 = [param_name9, self.DC_induced_CD8_proliferation, units_button11, desc_button9] 
        row10 = [param_name10, self.DC_induced_CD4_proliferation, units_button12, desc_button10] 
        row11 = [param_name11, self.DC_induced_CD8_attachment, units_button13, desc_button11] 
        row12 = [param_name12, self.departure_rate_of_DCs, units_button14, desc_button12] 
        row13 = [param_name13, self.epsilon_distance, units_button15, desc_button13] 
        row14 = [param_name14, self.perecentage_tissue_vascularized, units_button16, desc_button14] 
        row15 = [param_name15, self.color_variable, units_button18, desc_button15] 
        row16 = [param_name16, self.epithelial_opacity, units_button19, desc_button16] 
        row17 = [param_name17, self.non_epithelial_opacity, units_button20, desc_button17] 
        row18 = [param_name18, self.apoptotic_tumor_color, units_button21, desc_button18] 
        row19 = [param_name19, self.apoptotic_immune_color, units_button22, desc_button19] 
        row20 = [param_name20, self.CD8_Tcell_color, units_button23, desc_button20] 
        row21 = [param_name21, self.CD4_Tcell_color, units_button24, desc_button21] 
        row22 = [param_name22, self.Macrophage_color, units_button25, desc_button22] 
        row23 = [param_name23, self.activated_macrophage_color, units_button26, desc_button23] 
        row24 = [param_name24, self.exhausted_macrophage_color, units_button27, desc_button24] 
        row25 = [param_name25, self.hyperactivated_macrophage_color, units_button28, desc_button25] 
        row26 = [param_name26, self.DC_color, units_button29, desc_button26] 
        row27 = [param_name27, self.activated_DC_color, units_button30, desc_button27] 
        row28 = [param_name28, self.phagocytes_virus_uptake_rate, units_button31, desc_button28] 
        row29 = [param_name29, self.Antibody_binding_rate, units_button32, desc_button29] 
        row30 = [param_name30, self.antibody_half_effect, units_button33, desc_button30] 
        row31 = [param_name31, self.LNP_fraction_released_at_death, units_button35, desc_button31] 
        row32 = [param_name32, self.ISF_secretion_rate, units_button36, desc_button32] 
        row33 = [param_name33, self.tumor_radius, units_button37, desc_button33] 
        row34 = [param_name34, self.default_apoptosis_rate, units_button38, desc_button34] 
        row35 = [param_name35, self.max_Ig_complex_color, units_button39, desc_button35] 
        row36 = [param_name36, self.original_antigen_protein, units_button40, desc_button36] 
        row37 = [param_name37, self.antigen_antibody_inherit_ratio, units_button41, desc_button37] 
        row38 = [param_name38, self.Ig_induce_apoptosis, units_button42, desc_button38] 
        row39 = [param_name39, self.Ig_antigen_50, units_button43, desc_button39] 
        row40 = [param_name40, self.LNP_escape_rate, units_button44, desc_button40] 
        row41 = [param_name41, self.uncoated_LNP_rate, units_button45, desc_button41] 
        row42 = [param_name42, self.uncoated_to_RNA_rate, units_button46, desc_button42] 
        row43 = [param_name43, self.epitope_translation_rate, units_button47, desc_button43] 
        row44 = [param_name44, self.mRNA_decay_rate, units_button48, desc_button44] 
        row45 = [param_name45, self.antigenic_epitope_decay_rate, units_button49, desc_button45] 
        row46 = [param_name46, self.activate_immune_response_time, units_button50, desc_button46] 
        row47 = [param_name47, self.cytotoxic_T_response, units_button51, desc_button47] 
        row48 = [param_name48, self.antibody_response, units_button52, desc_button48] 
        row49 = [param_name49, self.CD8_recruit_rate, units_button53, desc_button49] 
        row50 = [param_name50, self.CD4_recruit_rate, units_button54, desc_button50] 
        row51 = [param_name51, self.Ig_recruit_rate, units_button55, desc_button51] 
        row52 = [param_name52, self.encapsulate_LNP_initial, units_button56, desc_button52] 
        row53 = [param_name53, self.mRNA_doses, units_button57, desc_button53] 
        row54 = [param_name54, self.injection_frequency, units_button58, desc_button54] 
        row55 = [param_name55, self.clearance_rate, units_button59, desc_button55] 
        row56 = [param_name56, self.start_inject_time, units_button60, desc_button56] 
        row57 = [param_name57, self.introduce_DC_cells_time, units_button61, desc_button57] 
        row58 = [param_name58, self.DC_tumor_ratio, units_button62, desc_button58] 
        row59 = [param_name59, self.number_DCs_introduced, units_button63, desc_button59] 
        row60 = [param_name60, self.ISF_needed_for_DC_activation, units_button64, desc_button60] 
        row61 = [param_name61, self.antigenic_epitope_needed_for_DC_activation, units_button65, desc_button61] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)
        box15 = Box(children=row15, layout=box_layout)
        box16 = Box(children=row16, layout=box_layout)
        box17 = Box(children=row17, layout=box_layout)
        box18 = Box(children=row18, layout=box_layout)
        box19 = Box(children=row19, layout=box_layout)
        box20 = Box(children=row20, layout=box_layout)
        box21 = Box(children=row21, layout=box_layout)
        box22 = Box(children=row22, layout=box_layout)
        box23 = Box(children=row23, layout=box_layout)
        box24 = Box(children=row24, layout=box_layout)
        box25 = Box(children=row25, layout=box_layout)
        box26 = Box(children=row26, layout=box_layout)
        box27 = Box(children=row27, layout=box_layout)
        box28 = Box(children=row28, layout=box_layout)
        box29 = Box(children=row29, layout=box_layout)
        box30 = Box(children=row30, layout=box_layout)
        box31 = Box(children=row31, layout=box_layout)
        box32 = Box(children=row32, layout=box_layout)
        box33 = Box(children=row33, layout=box_layout)
        box34 = Box(children=row34, layout=box_layout)
        box35 = Box(children=row35, layout=box_layout)
        box36 = Box(children=row36, layout=box_layout)
        box37 = Box(children=row37, layout=box_layout)
        box38 = Box(children=row38, layout=box_layout)
        box39 = Box(children=row39, layout=box_layout)
        box40 = Box(children=row40, layout=box_layout)
        box41 = Box(children=row41, layout=box_layout)
        box42 = Box(children=row42, layout=box_layout)
        box43 = Box(children=row43, layout=box_layout)
        box44 = Box(children=row44, layout=box_layout)
        box45 = Box(children=row45, layout=box_layout)
        box46 = Box(children=row46, layout=box_layout)
        box47 = Box(children=row47, layout=box_layout)
        box48 = Box(children=row48, layout=box_layout)
        box49 = Box(children=row49, layout=box_layout)
        box50 = Box(children=row50, layout=box_layout)
        box51 = Box(children=row51, layout=box_layout)
        box52 = Box(children=row52, layout=box_layout)
        box53 = Box(children=row53, layout=box_layout)
        box54 = Box(children=row54, layout=box_layout)
        box55 = Box(children=row55, layout=box_layout)
        box56 = Box(children=row56, layout=box_layout)
        box57 = Box(children=row57, layout=box_layout)
        box58 = Box(children=row58, layout=box_layout)
        box59 = Box(children=row59, layout=box_layout)
        box60 = Box(children=row60, layout=box_layout)
        box61 = Box(children=row61, layout=box_layout)

        self.tab = VBox([
          box1,
          box2,
          div_row1,
          box3,
          box4,
          div_row2,
          box5,
          box6,
          box7,
          box8,
          box9,
          box10,
          box11,
          box12,
          box13,
          box14,
          div_row3,
          box15,
          box16,
          box17,
          box18,
          box19,
          box20,
          box21,
          box22,
          box23,
          box24,
          box25,
          box26,
          box27,
          box28,
          box29,
          box30,
          div_row4,
          box31,
          box32,
          box33,
          box34,
          box35,
          box36,
          box37,
          box38,
          box39,
          box40,
          box41,
          box42,
          box43,
          box44,
          box45,
          box46,
          box47,
          box48,
          box49,
          box50,
          box51,
          box52,
          box53,
          box54,
          box55,
          box56,
          box57,
          box58,
          box59,
          box60,
          box61,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        self.random_seed.value = int(uep.find('.//random_seed').text)
        self.ignore_smoothing_flag.value = int(uep.find('.//ignore_smoothing_flag').text)
        self.immune_dt.value = float(uep.find('.//immune_dt').text)
        self.immune_z_offset.value = float(uep.find('.//immune_z_offset').text)
        self.number_of_CD8_Tcells.value = int(uep.find('.//number_of_CD8_Tcells').text)
        self.number_of_macrophages.value = int(uep.find('.//number_of_macrophages').text)
        self.number_of_DCs.value = int(uep.find('.//number_of_DCs').text)
        self.number_of_CD4_Tcells.value = int(uep.find('.//number_of_CD4_Tcells').text)
        self.DC_induced_CD8_proliferation.value = float(uep.find('.//DC_induced_CD8_proliferation').text)
        self.DC_induced_CD4_proliferation.value = float(uep.find('.//DC_induced_CD4_proliferation').text)
        self.DC_induced_CD8_attachment.value = float(uep.find('.//DC_induced_CD8_attachment').text)
        self.departure_rate_of_DCs.value = float(uep.find('.//departure_rate_of_DCs').text)
        self.epsilon_distance.value = float(uep.find('.//epsilon_distance').text)
        self.perecentage_tissue_vascularized.value = float(uep.find('.//perecentage_tissue_vascularized').text)
        self.color_variable.value = (uep.find('.//color_variable').text)
        self.epithelial_opacity.value = float(uep.find('.//epithelial_opacity').text)
        self.non_epithelial_opacity.value = float(uep.find('.//non_epithelial_opacity').text)
        self.apoptotic_tumor_color.value = (uep.find('.//apoptotic_tumor_color').text)
        self.apoptotic_immune_color.value = (uep.find('.//apoptotic_immune_color').text)
        self.CD8_Tcell_color.value = (uep.find('.//CD8_Tcell_color').text)
        self.CD4_Tcell_color.value = (uep.find('.//CD4_Tcell_color').text)
        self.Macrophage_color.value = (uep.find('.//Macrophage_color').text)
        self.activated_macrophage_color.value = (uep.find('.//activated_macrophage_color').text)
        self.exhausted_macrophage_color.value = (uep.find('.//exhausted_macrophage_color').text)
        self.hyperactivated_macrophage_color.value = (uep.find('.//hyperactivated_macrophage_color').text)
        self.DC_color.value = (uep.find('.//DC_color').text)
        self.activated_DC_color.value = (uep.find('.//activated_DC_color').text)
        self.phagocytes_virus_uptake_rate.value = float(uep.find('.//phagocytes_virus_uptake_rate').text)
        self.Antibody_binding_rate.value = float(uep.find('.//Antibody_binding_rate').text)
        self.antibody_half_effect.value = float(uep.find('.//antibody_half_effect').text)
        self.LNP_fraction_released_at_death.value = float(uep.find('.//LNP_fraction_released_at_death').text)
        self.ISF_secretion_rate.value = float(uep.find('.//ISF_secretion_rate').text)
        self.tumor_radius.value = float(uep.find('.//tumor_radius').text)
        self.default_apoptosis_rate.value = float(uep.find('.//default_apoptosis_rate').text)
        self.max_Ig_complex_color.value = float(uep.find('.//max_Ig_complex_color').text)
        self.original_antigen_protein.value = float(uep.find('.//original_antigen_protein').text)
        self.antigen_antibody_inherit_ratio.value = float(uep.find('.//antigen_antibody_inherit_ratio').text)
        self.Ig_induce_apoptosis.value = float(uep.find('.//Ig_induce_apoptosis').text)
        self.Ig_antigen_50.value = float(uep.find('.//Ig_antigen_50').text)
        self.LNP_escape_rate.value = float(uep.find('.//LNP_escape_rate').text)
        self.uncoated_LNP_rate.value = float(uep.find('.//uncoated_LNP_rate').text)
        self.uncoated_to_RNA_rate.value = float(uep.find('.//uncoated_to_RNA_rate').text)
        self.epitope_translation_rate.value = float(uep.find('.//epitope_translation_rate').text)
        self.mRNA_decay_rate.value = float(uep.find('.//mRNA_decay_rate').text)
        self.antigenic_epitope_decay_rate.value = float(uep.find('.//antigenic_epitope_decay_rate').text)
        self.activate_immune_response_time.value = float(uep.find('.//activate_immune_response_time').text)
        self.cytotoxic_T_response.value = ('true' == (uep.find('.//cytotoxic_T_response').text.lower()) )
        self.antibody_response.value = ('true' == (uep.find('.//antibody_response').text.lower()) )
        self.CD8_recruit_rate.value = float(uep.find('.//CD8_recruit_rate').text)
        self.CD4_recruit_rate.value = float(uep.find('.//CD4_recruit_rate').text)
        self.Ig_recruit_rate.value = float(uep.find('.//Ig_recruit_rate').text)
        self.encapsulate_LNP_initial.value = ('true' == (uep.find('.//encapsulate_LNP_initial').text.lower()) )
        self.mRNA_doses.value = float(uep.find('.//mRNA_doses').text)
        self.injection_frequency.value = float(uep.find('.//injection_frequency').text)
        self.clearance_rate.value = float(uep.find('.//clearance_rate').text)
        self.start_inject_time.value = float(uep.find('.//start_inject_time').text)
        self.introduce_DC_cells_time.value = float(uep.find('.//introduce_DC_cells_time').text)
        self.DC_tumor_ratio.value = float(uep.find('.//DC_tumor_ratio').text)
        self.number_DCs_introduced.value = int(uep.find('.//number_DCs_introduced').text)
        self.ISF_needed_for_DC_activation.value = float(uep.find('.//ISF_needed_for_DC_activation').text)
        self.antigenic_epitope_needed_for_DC_activation.value = float(uep.find('.//antigenic_epitope_needed_for_DC_activation').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        uep.find('.//random_seed').text = str(self.random_seed.value)
        uep.find('.//ignore_smoothing_flag').text = str(self.ignore_smoothing_flag.value)
        uep.find('.//immune_dt').text = str(self.immune_dt.value)
        uep.find('.//immune_z_offset').text = str(self.immune_z_offset.value)
        uep.find('.//number_of_CD8_Tcells').text = str(self.number_of_CD8_Tcells.value)
        uep.find('.//number_of_macrophages').text = str(self.number_of_macrophages.value)
        uep.find('.//number_of_DCs').text = str(self.number_of_DCs.value)
        uep.find('.//number_of_CD4_Tcells').text = str(self.number_of_CD4_Tcells.value)
        uep.find('.//DC_induced_CD8_proliferation').text = str(self.DC_induced_CD8_proliferation.value)
        uep.find('.//DC_induced_CD4_proliferation').text = str(self.DC_induced_CD4_proliferation.value)
        uep.find('.//DC_induced_CD8_attachment').text = str(self.DC_induced_CD8_attachment.value)
        uep.find('.//departure_rate_of_DCs').text = str(self.departure_rate_of_DCs.value)
        uep.find('.//epsilon_distance').text = str(self.epsilon_distance.value)
        uep.find('.//perecentage_tissue_vascularized').text = str(self.perecentage_tissue_vascularized.value)
        uep.find('.//color_variable').text = str(self.color_variable.value)
        uep.find('.//epithelial_opacity').text = str(self.epithelial_opacity.value)
        uep.find('.//non_epithelial_opacity').text = str(self.non_epithelial_opacity.value)
        uep.find('.//apoptotic_tumor_color').text = str(self.apoptotic_tumor_color.value)
        uep.find('.//apoptotic_immune_color').text = str(self.apoptotic_immune_color.value)
        uep.find('.//CD8_Tcell_color').text = str(self.CD8_Tcell_color.value)
        uep.find('.//CD4_Tcell_color').text = str(self.CD4_Tcell_color.value)
        uep.find('.//Macrophage_color').text = str(self.Macrophage_color.value)
        uep.find('.//activated_macrophage_color').text = str(self.activated_macrophage_color.value)
        uep.find('.//exhausted_macrophage_color').text = str(self.exhausted_macrophage_color.value)
        uep.find('.//hyperactivated_macrophage_color').text = str(self.hyperactivated_macrophage_color.value)
        uep.find('.//DC_color').text = str(self.DC_color.value)
        uep.find('.//activated_DC_color').text = str(self.activated_DC_color.value)
        uep.find('.//phagocytes_virus_uptake_rate').text = str(self.phagocytes_virus_uptake_rate.value)
        uep.find('.//Antibody_binding_rate').text = str(self.Antibody_binding_rate.value)
        uep.find('.//antibody_half_effect').text = str(self.antibody_half_effect.value)
        uep.find('.//LNP_fraction_released_at_death').text = str(self.LNP_fraction_released_at_death.value)
        uep.find('.//ISF_secretion_rate').text = str(self.ISF_secretion_rate.value)
        uep.find('.//tumor_radius').text = str(self.tumor_radius.value)
        uep.find('.//default_apoptosis_rate').text = str(self.default_apoptosis_rate.value)
        uep.find('.//max_Ig_complex_color').text = str(self.max_Ig_complex_color.value)
        uep.find('.//original_antigen_protein').text = str(self.original_antigen_protein.value)
        uep.find('.//antigen_antibody_inherit_ratio').text = str(self.antigen_antibody_inherit_ratio.value)
        uep.find('.//Ig_induce_apoptosis').text = str(self.Ig_induce_apoptosis.value)
        uep.find('.//Ig_antigen_50').text = str(self.Ig_antigen_50.value)
        uep.find('.//LNP_escape_rate').text = str(self.LNP_escape_rate.value)
        uep.find('.//uncoated_LNP_rate').text = str(self.uncoated_LNP_rate.value)
        uep.find('.//uncoated_to_RNA_rate').text = str(self.uncoated_to_RNA_rate.value)
        uep.find('.//epitope_translation_rate').text = str(self.epitope_translation_rate.value)
        uep.find('.//mRNA_decay_rate').text = str(self.mRNA_decay_rate.value)
        uep.find('.//antigenic_epitope_decay_rate').text = str(self.antigenic_epitope_decay_rate.value)
        uep.find('.//activate_immune_response_time').text = str(self.activate_immune_response_time.value)
        uep.find('.//cytotoxic_T_response').text = str(self.cytotoxic_T_response.value)
        uep.find('.//antibody_response').text = str(self.antibody_response.value)
        uep.find('.//CD8_recruit_rate').text = str(self.CD8_recruit_rate.value)
        uep.find('.//CD4_recruit_rate').text = str(self.CD4_recruit_rate.value)
        uep.find('.//Ig_recruit_rate').text = str(self.Ig_recruit_rate.value)
        uep.find('.//encapsulate_LNP_initial').text = str(self.encapsulate_LNP_initial.value)
        uep.find('.//mRNA_doses').text = str(self.mRNA_doses.value)
        uep.find('.//injection_frequency').text = str(self.injection_frequency.value)
        uep.find('.//clearance_rate').text = str(self.clearance_rate.value)
        uep.find('.//start_inject_time').text = str(self.start_inject_time.value)
        uep.find('.//introduce_DC_cells_time').text = str(self.introduce_DC_cells_time.value)
        uep.find('.//DC_tumor_ratio').text = str(self.DC_tumor_ratio.value)
        uep.find('.//number_DCs_introduced').text = str(self.number_DCs_introduced.value)
        uep.find('.//ISF_needed_for_DC_activation').text = str(self.ISF_needed_for_DC_activation.value)
        uep.find('.//antigenic_epitope_needed_for_DC_activation').text = str(self.antigenic_epitope_needed_for_DC_activation.value)
