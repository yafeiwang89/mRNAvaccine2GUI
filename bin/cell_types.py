 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box,Dropdown
    
class CellTypesTab(object):

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
        widget_layout_long = {'width': '20%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}
        divider_button_layout={'width':'40%'}
        divider_button_layout={'width':'60%'}
        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')

        self.cell_type_dropdown = Dropdown(description='Cell type:',)
        self.cell_type_dropdown.style = {'description_width': '%sch' % str(len(self.cell_type_dropdown.description) + 1)}

        cell_type_names_layout={'width':'30%'}
        cell_type_names_style={'description_width':'initial'}
        # self.parent_name = Text(value='None',description='inherits properties from parent type:',disabled=True, style=cell_type_names_style, layout=cell_type_names_layout)

        # explain_inheritance = Label(value='    This cell line inherits its properties from its parent type. Any settings below override those inherited properties.')  # , style=cell_type_names_style, layout=cell_type_names_layout)

        # self.cell_type_parent_row = HBox([self.cell_type_dropdown, self.parent_name])
        self.cell_type_parent_row = HBox([self.cell_type_dropdown])
        # self.cell_type_parent_dict = {}

        self.cell_type_dict = {}
        self.cell_type_dict['default'] = 'default'
        self.cell_type_dict['immune'] = 'immune'
        self.cell_type_dict['tumor cell'] = 'tumor cell'
        self.cell_type_dict['CD8 Tcell'] = 'CD8 Tcell'
        self.cell_type_dict['macrophage'] = 'macrophage'
        self.cell_type_dict['DC'] = 'DC'
        self.cell_type_dict['CD4 Tcell'] = 'CD4 Tcell'
        self.cell_type_dropdown.options = self.cell_type_dict

        self.cell_type_dropdown.observe(self.cell_type_cb)

        self.cell_def_vboxes = []
        #  >>>>>>>>>>>>>>>>> <cell_definition> = default
        #  ------------------------- 
        div_row1 = Button(description='phenotype:cycle (model: flow_cytometry_separated_cycle_model; code=6)', disabled=True, layout=divider_button_layout)
        div_row1.style.button_color = 'orange'
        name_btn = Button(description='Phase 0 -> Phase 1 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float0 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float0, units_btn, ]
        box0 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 1 -> Phase 2 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float1 = FloatText(value='0.00208333', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float1, units_btn, ]
        box1 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 2 -> Phase 3 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float2 = FloatText(value='0.00416667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float2, units_btn, ]
        box2 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 3 -> Phase 0 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float3 = FloatText(value='0.0166667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float3, units_btn, ]
        box3 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row2 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row2.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float4 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float4, units_btn, ]
        box4 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float5 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float5, units_btn, ]
        box5 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float6 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float6, units_btn, ]
        box6 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float7 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float7, units_btn, ]
        box7 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float8 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float8, units_btn, ]
        box8 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float9 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float9, units_btn, ]
        box9 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float10 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float10, units_btn, ]
        box10 = Box(children=row, layout=box_layout)

        death_model2 = Button(description='model: necrosis', disabled=True, layout={'width':'30%'})
        death_model2.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float11 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float11, units_btn, ]
        box11 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float12 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float12, units_btn, ]
        box12 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float13 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float13, units_btn, ]
        box13 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float14 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float14, units_btn, ]
        box14 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float15 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float15, units_btn, ]
        box15 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float16 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float16, units_btn, ]
        box16 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float17 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float17, units_btn, ]
        box17 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row3 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row3.style.button_color = 'orange'
        name_btn = Button(description='total', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float18 = FloatText(value='2494', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float18, units_btn, ]
        box18 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float19 = FloatText(value='0.75', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float19, units_btn, ]
        box19 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float20 = FloatText(value='540', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float20, units_btn, ]
        box20 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float21 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float21, units_btn, ]
        box21 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float22 = FloatText(value='0.0045', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float22, units_btn, ]
        box22 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float23 = FloatText(value='0.0055', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float23, units_btn, ]
        box23 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcified_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float24 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float24, units_btn, ]
        box24 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float25 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float25, units_btn, ]
        box25 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float26 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float26, units_btn, ]
        box26 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row4 = Button(description='phenotype:mechanics', disabled=True, layout=divider_button_layout)
        div_row4.style.button_color = 'orange'
        name_btn = Button(description='cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float27 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float27, units_btn, ]
        box27 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cell_cell_repulsion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float28 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float28, units_btn, ]
        box28 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float29 = FloatText(value='1.25', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float29, units_btn, ]
        box29 = Box(children=row, layout=box_layout)

        self.bool0 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_relative_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float30 = FloatText(value='1.8', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [self.bool0, name_btn, self.float30, units_btn, ]
        box30 = Box(children=row, layout=box_layout)

        self.bool1 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_absolute_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float31 = FloatText(value='15.12', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [self.bool1, name_btn, self.float31, units_btn, ]
        box31 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row5 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row5.style.button_color = 'orange'

        name_btn = Button(description='speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float32 = FloatText(value='4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float32, units_btn]
        box32 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float33 = FloatText(value='5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float33, units_btn]
        box33 = Box(children=row, layout=box_layout)

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float34 = FloatText(value='0.7', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float34, units_btn]
        box34 = Box(children=row, layout=box_layout)
        self.bool2 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        self.bool3 = Checkbox(description='use_2D', value=True,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})
        chemotaxis_btn.style.button_color = '#ffde6b'

        self.bool4 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.chemotaxis_substrate1 = Text(value='ISF', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_substrate1]
        box35 = Box(children=row, layout=box_layout)

        name_btn = Button(description='direction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.chemotaxis_direction1 = Text(value='1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_direction1]
        box36 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row6 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row6.style.button_color = 'orange'
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text0 = Text(value='ISF', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text0]
        box37 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float35 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float35, units_btn]
        box38 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text1 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text1]
        box39 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float36 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float36, units_btn]
        box40 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text2 = Text(value='Ig', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text2]
        box41 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float37 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float37, units_btn]
        box42 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row7 = Button(description='phenotype:molecular', disabled=True, layout=divider_button_layout)
        div_row7.style.button_color = 'orange'

#      ================== <custom_data>, if present ==================

        div_row8 = Button(description='Custom Data',disabled=True, layout=divider_button_layout)
        div_row8.style.button_color = 'cyan'
        name_btn = Button(description='unbound_external_receptor', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float38 = FloatText(value='200', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of unbound receptors on DC surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float38, units_btn, description_btn] 

        box43 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_external_receptor', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float39 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of bound receptors on DC surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float39, units_btn, description_btn] 

        box44 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_internal_receptor', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float40 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of internalized unbound receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float40, units_btn, description_btn] 

        box45 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_internal_receptor', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float41 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of internalized bound receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float41, units_btn, description_btn] 

        box46 = Box(children=row, layout=box_layout)
        name_btn = Button(description='receptor_binding_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float42 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='DC receptor-LNP binding rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float42, units_btn, description_btn] 

        box47 = Box(children=row, layout=box_layout)
        name_btn = Button(description='receptor_endocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float43 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='DC receptor-LNP endocytosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float43, units_btn, description_btn] 

        box48 = Box(children=row, layout=box_layout)
        name_btn = Button(description='receptor_cargo_release_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float44 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='DC receptor-LNP cargo release rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float44, units_btn, description_btn] 

        box49 = Box(children=row, layout=box_layout)
        name_btn = Button(description='receptor_recycling_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float45 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='DC receptor recycling rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float45, units_btn, description_btn] 

        box50 = Box(children=row, layout=box_layout)
        name_btn = Button(description='debris_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float46 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate that dead cells release debris', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float46, units_btn, description_btn] 

        box51 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_detection', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float47 = FloatText(value='10', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='protein', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='protein value at which a T Cell can detect an infected cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float47, units_btn, description_btn] 

        box52 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float48 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='tracks total contact time with CD8 T cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float48, units_btn, description_btn] 

        box53 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float49 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='the rate at which the cell attaches to cells in contact', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float49, units_btn, description_btn] 

        box54 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_lifetime', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float50 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='the mean duration of a cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float50, units_btn, description_btn] 

        box55 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_death_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float51 = FloatText(value='90', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='threshold CD8 T cell contact time to trigger apoptosis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float51, units_btn, description_btn] 

        box56 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_attachment_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float52 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float52, units_btn, description_btn] 

        box57 = Box(children=row, layout=box_layout)
        name_btn = Button(description='elastic_attachment_coefficient', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float53 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='elastic coefficient for cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float53, units_btn, description_btn] 

        box58 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_to_next_phagocytosis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float54 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='time it takes for the apoptotic material to be phagocytosed', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float54, units_btn, description_btn] 

        box59 = Box(children=row, layout=box_layout)
        name_btn = Button(description='material_internalisation_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float55 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float55, units_btn, description_btn] 

        box60 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_macrophage_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float56 = FloatText(value='6500', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float56, units_btn, description_btn] 

        box61 = Box(children=row, layout=box_layout)
        name_btn = Button(description='exhausted_macrophage_death_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float57 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float57, units_btn, description_btn] 

        box62 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ability_to_phagocytose_infected_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float58 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Boolean for whether macrophages can phagocytose infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float58, units_btn, description_btn] 

        box63 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_of_DC_departure', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float59 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Time DC leaves tissue after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float59, units_btn, description_btn] 

        box64 = Box(children=row, layout=box_layout)
        name_btn = Button(description='phagocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float60 = FloatText(value='0.167', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float60, units_btn, description_btn] 

        box65 = Box(children=row, layout=box_layout)
        name_btn = Button(description='phagocytosis_relative_target_cutoff_size', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float61 = FloatText(value='1.1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float61, units_btn, description_btn] 

        box66 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_debris_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float62 = FloatText(value='1.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='relative sensitivity to debris in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float62, units_btn, description_btn] 

        box67 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_ISF_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float63 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='relative sensitivity to ISF in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float63, units_btn, description_btn] 

        box68 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float64 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='speed after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float64, units_btn, description_btn] 

        box69 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float65 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate of secreting pro-inflamatory cytokine after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float65, units_btn, description_btn] 

        box70 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_immune_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float66 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='used internally to track activation state', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float66, units_btn, description_btn] 

        box71 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antiinflammatory_cytokine_secretion_rate_by_macrophage', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float67 = FloatText(value='0.07', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='secretion rate of anti-inflammatory from macrophage', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float67, units_btn, description_btn] 

        box72 = Box(children=row, layout=box_layout)
        name_btn = Button(description='generation', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float68 = FloatText(value='3', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='cell proliferation generation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float68, units_btn, description_btn] 

        box73 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antigen_protein', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float69 = FloatText(value='500', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='antigen', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='number of unbound antigen proteins on tumor cell membrane', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float69, units_btn, description_btn] 

        box74 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antibody_antigen_complex', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float70 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='complex', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='number of antibody-antigen protein complex on tumor cell membrane', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float70, units_btn, description_btn] 

        box75 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antibody_binding_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float71 = FloatText(value='0.08', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='antigen protein-antibody binding rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float71, units_btn, description_btn] 

        box76 = Box(children=row, layout=box_layout)
        name_btn = Button(description='last_cycle_entry_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float72 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='mins', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='time that tumor cell entry cycle when division', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float72, units_btn, description_btn] 

        box77 = Box(children=row, layout=box_layout)
        name_btn = Button(description='division_generation', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float73 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='generation', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='how many generations tumor cell has divided', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float73, units_btn, description_btn] 

        box78 = Box(children=row, layout=box_layout)
        name_btn = Button(description='E_Ig_complex', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float74 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='the effect of antibody-antigen protein complex', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float74, units_btn, description_btn] 

        box79 = Box(children=row, layout=box_layout)
        name_btn = Button(description='total_intern_LNP', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float75 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='LNP', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float75, units_btn, description_btn] 

        box80 = Box(children=row, layout=box_layout)
        name_btn = Button(description='endosome_LNP', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float76 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='LNP', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float76, units_btn, description_btn] 

        box81 = Box(children=row, layout=box_layout)
        name_btn = Button(description='free_LNP', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float77 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='LNP', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float77, units_btn, description_btn] 

        box82 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_LNP', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float78 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='LNP', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float78, units_btn, description_btn] 

        box83 = Box(children=row, layout=box_layout)
        name_btn = Button(description='mRNA', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float79 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='mRNA', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float79, units_btn, description_btn] 

        box84 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antigenic_epitope', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float80 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='epitope', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float80, units_btn, description_btn] 

        box85 = Box(children=row, layout=box_layout)

        self.cell_def_vbox0 = VBox([
          div_row1, box0, box1, box2, box3, div_row2, death_model1,box4, box5, box6, box7, box8, box9, box10, death_model2,box11, box12, box13, box14, box15, box16, box17, div_row3, box18, box19, box20, box21, box22, box23, box24, box25, box26, div_row4, box27, box28, box29, box30, box31, div_row5, box32,box33,box34,self.bool2,self.bool3,chemotaxis_btn,self.bool4,box35,box36,div_row6, box37,box38,box39,box40,box41,box42,div_row7, div_row8,          box43,
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
          box62,
          box63,
          box64,
          box65,
          box66,
          box67,
          box68,
          box69,
          box70,
          box71,
          box72,
          box73,
          box74,
          box75,
          box76,
          box77,
          box78,
          box79,
          box80,
          box81,
          box82,
          box83,
          box84,
          box85,
        ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox0)

        #  >>>>>>>>>>>>>>>>> <cell_definition> = immune
        #  ------------------------- 
        div_row9 = Button(description='phenotype:cycle (model: flow_cytometry_separated_cycle_model; code=6)', disabled=True, layout=divider_button_layout)
        div_row9.style.button_color = 'orange'
        name_btn = Button(description='Phase 0 -> Phase 1 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float81 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float81, units_btn, ]
        box86 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 1 -> Phase 2 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float82 = FloatText(value='0.00208333', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float82, units_btn, ]
        box87 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 2 -> Phase 3 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float83 = FloatText(value='0.00416667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float83, units_btn, ]
        box88 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 3 -> Phase 0 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float84 = FloatText(value='0.0166667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float84, units_btn, ]
        box89 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row10 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row10.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float85 = FloatText(value='5e-4', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float85, units_btn, ]
        box90 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float86 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float86, units_btn, ]
        box91 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float87 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float87, units_btn, ]
        box92 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float88 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float88, units_btn, ]
        box93 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float89 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float89, units_btn, ]
        box94 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float90 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float90, units_btn, ]
        box95 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float91 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float91, units_btn, ]
        box96 = Box(children=row, layout=box_layout)

        death_model2 = Button(description='model: necrosis', disabled=True, layout={'width':'30%'})
        death_model2.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float92 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float92, units_btn, ]
        box97 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float93 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float93, units_btn, ]
        box98 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float94 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float94, units_btn, ]
        box99 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float95 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float95, units_btn, ]
        box100 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float96 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float96, units_btn, ]
        box101 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float97 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float97, units_btn, ]
        box102 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float98 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float98, units_btn, ]
        box103 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row11 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row11.style.button_color = 'orange'
        name_btn = Button(description='total', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float99 = FloatText(value='2494', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float99, units_btn, ]
        box104 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float100 = FloatText(value='0.75', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float100, units_btn, ]
        box105 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float101 = FloatText(value='540', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float101, units_btn, ]
        box106 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float102 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float102, units_btn, ]
        box107 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float103 = FloatText(value='0.0045', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float103, units_btn, ]
        box108 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float104 = FloatText(value='0.0055', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float104, units_btn, ]
        box109 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcified_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float105 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float105, units_btn, ]
        box110 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float106 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float106, units_btn, ]
        box111 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float107 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float107, units_btn, ]
        box112 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row12 = Button(description='phenotype:mechanics', disabled=True, layout=divider_button_layout)
        div_row12.style.button_color = 'orange'
        name_btn = Button(description='cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float108 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float108, units_btn, ]
        box113 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cell_cell_repulsion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float109 = FloatText(value='10', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float109, units_btn, ]
        box114 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float110 = FloatText(value='1.25', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float110, units_btn, ]
        box115 = Box(children=row, layout=box_layout)

        self.bool5 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_relative_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float111 = FloatText(value='1.8', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [self.bool5, name_btn, self.float111, units_btn, ]
        box116 = Box(children=row, layout=box_layout)

        self.bool6 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_absolute_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float112 = FloatText(value='15.12', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [self.bool6, name_btn, self.float112, units_btn, ]
        box117 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row13 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row13.style.button_color = 'orange'

        name_btn = Button(description='speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float113 = FloatText(value='4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float113, units_btn]
        box118 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float114 = FloatText(value='5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float114, units_btn]
        box119 = Box(children=row, layout=box_layout)

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float115 = FloatText(value='0.70', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float115, units_btn]
        box120 = Box(children=row, layout=box_layout)
        self.bool7 = Checkbox(description='enabled', value=True,layout=name_button_layout)
        self.bool8 = Checkbox(description='use_2D', value=True,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})
        chemotaxis_btn.style.button_color = '#ffde6b'

        self.bool9 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.chemotaxis_substrate2 = Text(value='ISF', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_substrate2]
        box121 = Box(children=row, layout=box_layout)

        name_btn = Button(description='direction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.chemotaxis_direction2 = Text(value='1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_direction2]
        box122 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row14 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row14.style.button_color = 'orange'
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text3 = Text(value='ISF', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text3]
        box123 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float116 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float116, units_btn]
        box124 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text4 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text4]
        box125 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float117 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float117, units_btn]
        box126 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text5 = Text(value='Ig', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text5]
        box127 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float118 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float118, units_btn]
        box128 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row15 = Button(description='phenotype:molecular', disabled=True, layout=divider_button_layout)
        div_row15.style.button_color = 'orange'

#      ================== <custom_data>, if present ==================

        div_row16 = Button(description='Custom Data',disabled=True, layout=divider_button_layout)
        div_row16.style.button_color = 'cyan'
        name_btn = Button(description='unbound_external_receptor', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float119 = FloatText(value='200', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of unbound receptors on DC surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float119, units_btn, description_btn] 

        box129 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_external_receptor', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float120 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of bound receptors on DC surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float120, units_btn, description_btn] 

        box130 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_internal_receptor', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float121 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of internalized unbound receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float121, units_btn, description_btn] 

        box131 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_internal_receptor', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float122 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of internalized bound receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float122, units_btn, description_btn] 

        box132 = Box(children=row, layout=box_layout)
        name_btn = Button(description='receptor_binding_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float123 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='DC receptor-LNP binding rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float123, units_btn, description_btn] 

        box133 = Box(children=row, layout=box_layout)
        name_btn = Button(description='receptor_endocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float124 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='DC receptor-LNP endocytosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float124, units_btn, description_btn] 

        box134 = Box(children=row, layout=box_layout)
        name_btn = Button(description='receptor_cargo_release_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float125 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='DC receptor-LNP cargo release rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float125, units_btn, description_btn] 

        box135 = Box(children=row, layout=box_layout)
        name_btn = Button(description='receptor_recycling_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float126 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='DC receptor recycling rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float126, units_btn, description_btn] 

        box136 = Box(children=row, layout=box_layout)
        name_btn = Button(description='debris_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float127 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate that dead cells release debris', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float127, units_btn, description_btn] 

        box137 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_detection', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float128 = FloatText(value='10', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='protein', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='protein value at which a T Cell can detect an infected cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float128, units_btn, description_btn] 

        box138 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float129 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='tracks total contact time with CD8 T cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float129, units_btn, description_btn] 

        box139 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float130 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='the rate at which the cell attaches to cells in contact', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float130, units_btn, description_btn] 

        box140 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_lifetime', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float131 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='the mean duration of a cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float131, units_btn, description_btn] 

        box141 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_death_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float132 = FloatText(value='90', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='threshold CD8 T cell contact time to trigger apoptosis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float132, units_btn, description_btn] 

        box142 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_attachment_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float133 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float133, units_btn, description_btn] 

        box143 = Box(children=row, layout=box_layout)
        name_btn = Button(description='elastic_attachment_coefficient', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float134 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='elastic coefficient for cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float134, units_btn, description_btn] 

        box144 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_to_next_phagocytosis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float135 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='time it takes for the apoptotic material to be phagocytosed', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float135, units_btn, description_btn] 

        box145 = Box(children=row, layout=box_layout)
        name_btn = Button(description='material_internalisation_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float136 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float136, units_btn, description_btn] 

        box146 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_macrophage_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float137 = FloatText(value='6500', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float137, units_btn, description_btn] 

        box147 = Box(children=row, layout=box_layout)
        name_btn = Button(description='exhausted_macrophage_death_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float138 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float138, units_btn, description_btn] 

        box148 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ability_to_phagocytose_infected_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float139 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Boolean for whether macrophages can phagocytose infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float139, units_btn, description_btn] 

        box149 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_of_DC_departure', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float140 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Time DC leaves tissue after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float140, units_btn, description_btn] 

        box150 = Box(children=row, layout=box_layout)
        name_btn = Button(description='phagocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float141 = FloatText(value='0.167', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float141, units_btn, description_btn] 

        box151 = Box(children=row, layout=box_layout)
        name_btn = Button(description='phagocytosis_relative_target_cutoff_size', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float142 = FloatText(value='1.1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float142, units_btn, description_btn] 

        box152 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_debris_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float143 = FloatText(value='1.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='relative sensitivity to debris in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float143, units_btn, description_btn] 

        box153 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_ISF_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float144 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='relative sensitivity to ISF in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float144, units_btn, description_btn] 

        box154 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float145 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='speed after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float145, units_btn, description_btn] 

        box155 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float146 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate of secreting pro-inflamatory cytokine after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float146, units_btn, description_btn] 

        box156 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_immune_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float147 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='used internally to track activation state', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float147, units_btn, description_btn] 

        box157 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antiinflammatory_cytokine_secretion_rate_by_macrophage', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float148 = FloatText(value='0.07', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='secretion rate of anti-inflammatory from macrophage', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float148, units_btn, description_btn] 

        box158 = Box(children=row, layout=box_layout)
        name_btn = Button(description='generation', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float149 = FloatText(value='3', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='cell proliferation generation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float149, units_btn, description_btn] 

        box159 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antigen_protein', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float150 = FloatText(value='500', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='antigen', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='number of unbound antigen proteins on tumor cell membrane', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float150, units_btn, description_btn] 

        box160 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antibody_antigen_complex', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float151 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='complex', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='number of antibody-antigen protein complex on tumor cell membrane', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float151, units_btn, description_btn] 

        box161 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antibody_binding_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float152 = FloatText(value='0.08', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='antigen protein-antibody binding rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float152, units_btn, description_btn] 

        box162 = Box(children=row, layout=box_layout)
        name_btn = Button(description='last_cycle_entry_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float153 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='mins', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='time that tumor cell entry cycle when division', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float153, units_btn, description_btn] 

        box163 = Box(children=row, layout=box_layout)
        name_btn = Button(description='division_generation', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float154 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='generation', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='how many generations tumor cell has divided', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float154, units_btn, description_btn] 

        box164 = Box(children=row, layout=box_layout)
        name_btn = Button(description='E_Ig_complex', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float155 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='the effect of antibody-antigen protein complex', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float155, units_btn, description_btn] 

        box165 = Box(children=row, layout=box_layout)
        name_btn = Button(description='total_intern_LNP', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float156 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='LNP', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float156, units_btn, description_btn] 

        box166 = Box(children=row, layout=box_layout)
        name_btn = Button(description='endosome_LNP', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float157 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='LNP', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float157, units_btn, description_btn] 

        box167 = Box(children=row, layout=box_layout)
        name_btn = Button(description='free_LNP', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float158 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='LNP', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float158, units_btn, description_btn] 

        box168 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_LNP', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float159 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='LNP', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float159, units_btn, description_btn] 

        box169 = Box(children=row, layout=box_layout)
        name_btn = Button(description='mRNA', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float160 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='mRNA', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float160, units_btn, description_btn] 

        box170 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antigenic_epitope', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float161 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='epitope', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float161, units_btn, description_btn] 

        box171 = Box(children=row, layout=box_layout)

        self.cell_def_vbox1 = VBox([
          div_row9, box86, box87, box88, box89, div_row10, death_model1,box90, box91, box92, box93, box94, box95, box96, death_model2,box97, box98, box99, box100, box101, box102, box103, div_row11, box104, box105, box106, box107, box108, box109, box110, box111, box112, div_row12, box113, box114, box115, box116, box117, div_row13, box118,box119,box120,self.bool7,self.bool8,chemotaxis_btn,self.bool9,box121,box122,div_row14, box123,box124,box125,box126,box127,box128,div_row15, div_row16,          box129,
          box130,
          box131,
          box132,
          box133,
          box134,
          box135,
          box136,
          box137,
          box138,
          box139,
          box140,
          box141,
          box142,
          box143,
          box144,
          box145,
          box146,
          box147,
          box148,
          box149,
          box150,
          box151,
          box152,
          box153,
          box154,
          box155,
          box156,
          box157,
          box158,
          box159,
          box160,
          box161,
          box162,
          box163,
          box164,
          box165,
          box166,
          box167,
          box168,
          box169,
          box170,
          box171,
        ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox1)

        #  >>>>>>>>>>>>>>>>> <cell_definition> = tumor cell
        #  ------------------------- 
        div_row17 = Button(description='phenotype:cycle (model: flow_cytometry_separated_cycle_model; code=6)', disabled=True, layout=divider_button_layout)
        div_row17.style.button_color = 'orange'
        name_btn = Button(description='Phase 0 -> Phase 1 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float162 = FloatText(value='0.00072', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float162, units_btn, ]
        box172 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 1 -> Phase 2 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float163 = FloatText(value='0.00208333', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float163, units_btn, ]
        box173 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 2 -> Phase 3 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float164 = FloatText(value='0.00416667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float164, units_btn, ]
        box174 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 3 -> Phase 0 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float165 = FloatText(value='0.0166667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float165, units_btn, ]
        box175 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row18 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row18.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float166 = FloatText(value='5.31667e-05', step='1e-05', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float166, units_btn, ]
        box176 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float167 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float167, units_btn, ]
        box177 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float168 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float168, units_btn, ]
        box178 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float169 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float169, units_btn, ]
        box179 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float170 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float170, units_btn, ]
        box180 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float171 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float171, units_btn, ]
        box181 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float172 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float172, units_btn, ]
        box182 = Box(children=row, layout=box_layout)

        death_model2 = Button(description='model: necrosis', disabled=True, layout={'width':'30%'})
        death_model2.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float173 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float173, units_btn, ]
        box183 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float174 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float174, units_btn, ]
        box184 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float175 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float175, units_btn, ]
        box185 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float176 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float176, units_btn, ]
        box186 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float177 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float177, units_btn, ]
        box187 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float178 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float178, units_btn, ]
        box188 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float179 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float179, units_btn, ]
        box189 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row19 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row19.style.button_color = 'orange'
        name_btn = Button(description='total', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float180 = FloatText(value='2494', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float180, units_btn, ]
        box190 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float181 = FloatText(value='0.75', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float181, units_btn, ]
        box191 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float182 = FloatText(value='540', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float182, units_btn, ]
        box192 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float183 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float183, units_btn, ]
        box193 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float184 = FloatText(value='0.0045', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float184, units_btn, ]
        box194 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float185 = FloatText(value='0.0055', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float185, units_btn, ]
        box195 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcified_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float186 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float186, units_btn, ]
        box196 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float187 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float187, units_btn, ]
        box197 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float188 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float188, units_btn, ]
        box198 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row20 = Button(description='phenotype:mechanics', disabled=True, layout=divider_button_layout)
        div_row20.style.button_color = 'orange'
        name_btn = Button(description='cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float189 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float189, units_btn, ]
        box199 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cell_cell_repulsion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float190 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float190, units_btn, ]
        box200 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float191 = FloatText(value='1.25', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float191, units_btn, ]
        box201 = Box(children=row, layout=box_layout)

        self.bool10 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_relative_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float192 = FloatText(value='1.8', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [self.bool10, name_btn, self.float192, units_btn, ]
        box202 = Box(children=row, layout=box_layout)

        self.bool11 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_absolute_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float193 = FloatText(value='15.12', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [self.bool11, name_btn, self.float193, units_btn, ]
        box203 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row21 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row21.style.button_color = 'orange'

        name_btn = Button(description='speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float194 = FloatText(value='4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float194, units_btn]
        box204 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float195 = FloatText(value='5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float195, units_btn]
        box205 = Box(children=row, layout=box_layout)

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float196 = FloatText(value='0.7', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float196, units_btn]
        box206 = Box(children=row, layout=box_layout)
        self.bool12 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        self.bool13 = Checkbox(description='use_2D', value=True,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})
        chemotaxis_btn.style.button_color = '#ffde6b'

        self.bool14 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.chemotaxis_substrate3 = Text(value='ISF', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_substrate3]
        box207 = Box(children=row, layout=box_layout)

        name_btn = Button(description='direction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.chemotaxis_direction3 = Text(value='1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_direction3]
        box208 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row22 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row22.style.button_color = 'orange'
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text6 = Text(value='ISF', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text6]
        box209 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float197 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float197, units_btn]
        box210 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text7 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text7]
        box211 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float198 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float198, units_btn]
        box212 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text8 = Text(value='Ig', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text8]
        box213 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float199 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float199, units_btn]
        box214 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row23 = Button(description='phenotype:molecular', disabled=True, layout=divider_button_layout)
        div_row23.style.button_color = 'orange'

#      ================== <custom_data>, if present ==================

        div_row24 = Button(description='Custom Data',disabled=True, layout=divider_button_layout)
        div_row24.style.button_color = 'cyan'
        name_btn = Button(description='unbound_external_receptor', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float200 = FloatText(value='200', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of unbound receptors on DC surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float200, units_btn, description_btn] 

        box215 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_external_receptor', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float201 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of bound receptors on DC surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float201, units_btn, description_btn] 

        box216 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_internal_receptor', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float202 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of internalized unbound receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float202, units_btn, description_btn] 

        box217 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_internal_receptor', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float203 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of internalized bound receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float203, units_btn, description_btn] 

        box218 = Box(children=row, layout=box_layout)
        name_btn = Button(description='receptor_binding_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float204 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='DC receptor-LNP binding rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float204, units_btn, description_btn] 

        box219 = Box(children=row, layout=box_layout)
        name_btn = Button(description='receptor_endocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float205 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='DC receptor-LNP endocytosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float205, units_btn, description_btn] 

        box220 = Box(children=row, layout=box_layout)
        name_btn = Button(description='receptor_cargo_release_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float206 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='DC receptor-LNP cargo release rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float206, units_btn, description_btn] 

        box221 = Box(children=row, layout=box_layout)
        name_btn = Button(description='receptor_recycling_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float207 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='DC receptor recycling rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float207, units_btn, description_btn] 

        box222 = Box(children=row, layout=box_layout)
        name_btn = Button(description='debris_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float208 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate that dead cells release debris', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float208, units_btn, description_btn] 

        box223 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_detection', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float209 = FloatText(value='10', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='protein', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='protein value at which a T Cell can detect an infected cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float209, units_btn, description_btn] 

        box224 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float210 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='tracks total contact time with CD8 T cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float210, units_btn, description_btn] 

        box225 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float211 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='the rate at which the cell attaches to cells in contact', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float211, units_btn, description_btn] 

        box226 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_lifetime', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float212 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='the mean duration of a cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float212, units_btn, description_btn] 

        box227 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_death_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float213 = FloatText(value='90', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='threshold CD8 T cell contact time to trigger apoptosis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float213, units_btn, description_btn] 

        box228 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_attachment_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float214 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float214, units_btn, description_btn] 

        box229 = Box(children=row, layout=box_layout)
        name_btn = Button(description='elastic_attachment_coefficient', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float215 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='elastic coefficient for cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float215, units_btn, description_btn] 

        box230 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_to_next_phagocytosis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float216 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='time it takes for the apoptotic material to be phagocytosed', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float216, units_btn, description_btn] 

        box231 = Box(children=row, layout=box_layout)
        name_btn = Button(description='material_internalisation_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float217 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float217, units_btn, description_btn] 

        box232 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_macrophage_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float218 = FloatText(value='6500', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float218, units_btn, description_btn] 

        box233 = Box(children=row, layout=box_layout)
        name_btn = Button(description='exhausted_macrophage_death_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float219 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float219, units_btn, description_btn] 

        box234 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ability_to_phagocytose_infected_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float220 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Boolean for whether macrophages can phagocytose infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float220, units_btn, description_btn] 

        box235 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_of_DC_departure', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float221 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Time DC leaves tissue after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float221, units_btn, description_btn] 

        box236 = Box(children=row, layout=box_layout)
        name_btn = Button(description='phagocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float222 = FloatText(value='0.167', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float222, units_btn, description_btn] 

        box237 = Box(children=row, layout=box_layout)
        name_btn = Button(description='phagocytosis_relative_target_cutoff_size', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float223 = FloatText(value='1.1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float223, units_btn, description_btn] 

        box238 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_debris_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float224 = FloatText(value='1.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='relative sensitivity to debris in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float224, units_btn, description_btn] 

        box239 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_ISF_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float225 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='relative sensitivity to ISF in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float225, units_btn, description_btn] 

        box240 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float226 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='speed after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float226, units_btn, description_btn] 

        box241 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float227 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate of secreting pro-inflamatory cytokine after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float227, units_btn, description_btn] 

        box242 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_immune_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float228 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='used internally to track activation state', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float228, units_btn, description_btn] 

        box243 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antiinflammatory_cytokine_secretion_rate_by_macrophage', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float229 = FloatText(value='0.07', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='secretion rate of anti-inflammatory from macrophage', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float229, units_btn, description_btn] 

        box244 = Box(children=row, layout=box_layout)
        name_btn = Button(description='generation', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float230 = FloatText(value='3', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='cell proliferation generation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float230, units_btn, description_btn] 

        box245 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antigen_protein', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float231 = FloatText(value='500', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='antigen', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='number of unbound antigen proteins on tumor cell membrane', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float231, units_btn, description_btn] 

        box246 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antibody_antigen_complex', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float232 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='complex', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='number of antibody-antigen protein complex on tumor cell membrane', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float232, units_btn, description_btn] 

        box247 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antibody_binding_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float233 = FloatText(value='0.08', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='antigen protein-antibody binding rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float233, units_btn, description_btn] 

        box248 = Box(children=row, layout=box_layout)
        name_btn = Button(description='last_cycle_entry_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float234 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='mins', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='time that tumor cell entry cycle when division', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float234, units_btn, description_btn] 

        box249 = Box(children=row, layout=box_layout)
        name_btn = Button(description='division_generation', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float235 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='generation', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='how many generations tumor cell has divided', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float235, units_btn, description_btn] 

        box250 = Box(children=row, layout=box_layout)
        name_btn = Button(description='E_Ig_complex', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float236 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='the effect of antibody-antigen protein complex', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float236, units_btn, description_btn] 

        box251 = Box(children=row, layout=box_layout)
        name_btn = Button(description='total_intern_LNP', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float237 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='LNP', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float237, units_btn, description_btn] 

        box252 = Box(children=row, layout=box_layout)
        name_btn = Button(description='endosome_LNP', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float238 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='LNP', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float238, units_btn, description_btn] 

        box253 = Box(children=row, layout=box_layout)
        name_btn = Button(description='free_LNP', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float239 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='LNP', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float239, units_btn, description_btn] 

        box254 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_LNP', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float240 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='LNP', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float240, units_btn, description_btn] 

        box255 = Box(children=row, layout=box_layout)
        name_btn = Button(description='mRNA', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float241 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='mRNA', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float241, units_btn, description_btn] 

        box256 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antigenic_epitope', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float242 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='epitope', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float242, units_btn, description_btn] 

        box257 = Box(children=row, layout=box_layout)

        self.cell_def_vbox2 = VBox([
          div_row17, box172, box173, box174, box175, div_row18, death_model1,box176, box177, box178, box179, box180, box181, box182, death_model2,box183, box184, box185, box186, box187, box188, box189, div_row19, box190, box191, box192, box193, box194, box195, box196, box197, box198, div_row20, box199, box200, box201, box202, box203, div_row21, box204,box205,box206,self.bool12,self.bool13,chemotaxis_btn,self.bool14,box207,box208,div_row22, box209,box210,box211,box212,box213,box214,div_row23, div_row24,          box215,
          box216,
          box217,
          box218,
          box219,
          box220,
          box221,
          box222,
          box223,
          box224,
          box225,
          box226,
          box227,
          box228,
          box229,
          box230,
          box231,
          box232,
          box233,
          box234,
          box235,
          box236,
          box237,
          box238,
          box239,
          box240,
          box241,
          box242,
          box243,
          box244,
          box245,
          box246,
          box247,
          box248,
          box249,
          box250,
          box251,
          box252,
          box253,
          box254,
          box255,
          box256,
          box257,
        ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox2)

        #  >>>>>>>>>>>>>>>>> <cell_definition> = CD8 Tcell
        #  ------------------------- 
        div_row25 = Button(description='phenotype:cycle (model: flow_cytometry_separated_cycle_model; code=6)', disabled=True, layout=divider_button_layout)
        div_row25.style.button_color = 'orange'
        name_btn = Button(description='Phase 0 -> Phase 1 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float243 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float243, units_btn, ]
        box258 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 1 -> Phase 2 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float244 = FloatText(value='0.00208333', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float244, units_btn, ]
        box259 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 2 -> Phase 3 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float245 = FloatText(value='0.00416667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float245, units_btn, ]
        box260 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 3 -> Phase 0 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float246 = FloatText(value='0.0166667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float246, units_btn, ]
        box261 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row26 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row26.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float247 = FloatText(value='2.8e-4', step='1e-05', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float247, units_btn, ]
        box262 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float248 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float248, units_btn, ]
        box263 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float249 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float249, units_btn, ]
        box264 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float250 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float250, units_btn, ]
        box265 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float251 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float251, units_btn, ]
        box266 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float252 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float252, units_btn, ]
        box267 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float253 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float253, units_btn, ]
        box268 = Box(children=row, layout=box_layout)

        death_model2 = Button(description='model: necrosis', disabled=True, layout={'width':'30%'})
        death_model2.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float254 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float254, units_btn, ]
        box269 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float255 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float255, units_btn, ]
        box270 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float256 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float256, units_btn, ]
        box271 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float257 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float257, units_btn, ]
        box272 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float258 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float258, units_btn, ]
        box273 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float259 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float259, units_btn, ]
        box274 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float260 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float260, units_btn, ]
        box275 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row27 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row27.style.button_color = 'orange'
        name_btn = Button(description='total', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float261 = FloatText(value='478', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float261, units_btn, ]
        box276 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float262 = FloatText(value='0.75', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float262, units_btn, ]
        box277 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float263 = FloatText(value='47.8', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float263, units_btn, ]
        box278 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float264 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float264, units_btn, ]
        box279 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float265 = FloatText(value='0.0045', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float265, units_btn, ]
        box280 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float266 = FloatText(value='0.0055', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float266, units_btn, ]
        box281 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcified_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float267 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float267, units_btn, ]
        box282 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float268 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float268, units_btn, ]
        box283 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float269 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float269, units_btn, ]
        box284 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row28 = Button(description='phenotype:mechanics', disabled=True, layout=divider_button_layout)
        div_row28.style.button_color = 'orange'
        name_btn = Button(description='cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float270 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float270, units_btn, ]
        box285 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cell_cell_repulsion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float271 = FloatText(value='10', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float271, units_btn, ]
        box286 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float272 = FloatText(value='1.25', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float272, units_btn, ]
        box287 = Box(children=row, layout=box_layout)

        self.bool15 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_relative_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float273 = FloatText(value='1.8', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [self.bool15, name_btn, self.float273, units_btn, ]
        box288 = Box(children=row, layout=box_layout)

        self.bool16 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_absolute_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float274 = FloatText(value='15.12', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [self.bool16, name_btn, self.float274, units_btn, ]
        box289 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row29 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row29.style.button_color = 'orange'

        name_btn = Button(description='speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float275 = FloatText(value='4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float275, units_btn]
        box290 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float276 = FloatText(value='5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float276, units_btn]
        box291 = Box(children=row, layout=box_layout)

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float277 = FloatText(value='0.70', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float277, units_btn]
        box292 = Box(children=row, layout=box_layout)
        self.bool17 = Checkbox(description='enabled', value=True,layout=name_button_layout)
        self.bool18 = Checkbox(description='use_2D', value=True,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})
        chemotaxis_btn.style.button_color = '#ffde6b'

        self.bool19 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.chemotaxis_substrate4 = Text(value='ISF', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_substrate4]
        box293 = Box(children=row, layout=box_layout)

        name_btn = Button(description='direction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.chemotaxis_direction4 = Text(value='1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_direction4]
        box294 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row30 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row30.style.button_color = 'orange'
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text9 = Text(value='ISF', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text9]
        box295 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float278 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float278, units_btn]
        box296 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text10 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text10]
        box297 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float279 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float279, units_btn]
        box298 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text11 = Text(value='Ig', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text11]
        box299 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float280 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float280, units_btn]
        box300 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row31 = Button(description='phenotype:molecular', disabled=True, layout=divider_button_layout)
        div_row31.style.button_color = 'orange'

#      ================== <custom_data>, if present ==================

        div_row32 = Button(description='Custom Data',disabled=True, layout=divider_button_layout)
        div_row32.style.button_color = 'cyan'
        name_btn = Button(description='unbound_external_receptor', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float281 = FloatText(value='200', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of unbound receptors on DC surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float281, units_btn, description_btn] 

        box301 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_external_receptor', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float282 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of bound receptors on DC surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float282, units_btn, description_btn] 

        box302 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_internal_receptor', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float283 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of internalized unbound receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float283, units_btn, description_btn] 

        box303 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_internal_receptor', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float284 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of internalized bound receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float284, units_btn, description_btn] 

        box304 = Box(children=row, layout=box_layout)
        name_btn = Button(description='receptor_binding_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float285 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='DC receptor-LNP binding rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float285, units_btn, description_btn] 

        box305 = Box(children=row, layout=box_layout)
        name_btn = Button(description='receptor_endocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float286 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='DC receptor-LNP endocytosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float286, units_btn, description_btn] 

        box306 = Box(children=row, layout=box_layout)
        name_btn = Button(description='receptor_cargo_release_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float287 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='DC receptor-LNP cargo release rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float287, units_btn, description_btn] 

        box307 = Box(children=row, layout=box_layout)
        name_btn = Button(description='receptor_recycling_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float288 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='DC receptor recycling rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float288, units_btn, description_btn] 

        box308 = Box(children=row, layout=box_layout)
        name_btn = Button(description='debris_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float289 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate that dead cells release debris', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float289, units_btn, description_btn] 

        box309 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_detection', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float290 = FloatText(value='10', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='protein', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='protein value at which a T Cell can detect an infected cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float290, units_btn, description_btn] 

        box310 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float291 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='tracks total contact time with CD8 T cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float291, units_btn, description_btn] 

        box311 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float292 = FloatText(value='0.02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='the rate at which the cell attaches to cells in contact', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float292, units_btn, description_btn] 

        box312 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_lifetime', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float293 = FloatText(value='8.5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='the mean duration of a cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float293, units_btn, description_btn] 

        box313 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_death_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float294 = FloatText(value='90', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='threshold CD8 T cell contact time to trigger apoptosis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float294, units_btn, description_btn] 

        box314 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_attachment_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float295 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float295, units_btn, description_btn] 

        box315 = Box(children=row, layout=box_layout)
        name_btn = Button(description='elastic_attachment_coefficient', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float296 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='elastic coefficient for cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float296, units_btn, description_btn] 

        box316 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_to_next_phagocytosis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float297 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='time it takes for the apoptotic material to be phagocytosed', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float297, units_btn, description_btn] 

        box317 = Box(children=row, layout=box_layout)
        name_btn = Button(description='material_internalisation_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float298 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float298, units_btn, description_btn] 

        box318 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_macrophage_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float299 = FloatText(value='6500', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float299, units_btn, description_btn] 

        box319 = Box(children=row, layout=box_layout)
        name_btn = Button(description='exhausted_macrophage_death_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float300 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float300, units_btn, description_btn] 

        box320 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ability_to_phagocytose_infected_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float301 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Boolean for whether macrophages can phagocytose infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float301, units_btn, description_btn] 

        box321 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_of_DC_departure', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float302 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Time DC leaves tissue after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float302, units_btn, description_btn] 

        box322 = Box(children=row, layout=box_layout)
        name_btn = Button(description='phagocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float303 = FloatText(value='0.167', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float303, units_btn, description_btn] 

        box323 = Box(children=row, layout=box_layout)
        name_btn = Button(description='phagocytosis_relative_target_cutoff_size', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float304 = FloatText(value='1.1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float304, units_btn, description_btn] 

        box324 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_debris_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float305 = FloatText(value='1.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='relative sensitivity to debris in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float305, units_btn, description_btn] 

        box325 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_ISF_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float306 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='relative sensitivity to ISF in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float306, units_btn, description_btn] 

        box326 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float307 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='speed after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float307, units_btn, description_btn] 

        box327 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float308 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate of secreting pro-inflamatory cytokine after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float308, units_btn, description_btn] 

        box328 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_immune_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float309 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='used internally to track activation state', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float309, units_btn, description_btn] 

        box329 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antiinflammatory_cytokine_secretion_rate_by_macrophage', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float310 = FloatText(value='0.07', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='secretion rate of anti-inflammatory from macrophage', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float310, units_btn, description_btn] 

        box330 = Box(children=row, layout=box_layout)
        name_btn = Button(description='generation', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float311 = FloatText(value='3', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='cell proliferation generation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float311, units_btn, description_btn] 

        box331 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antigen_protein', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float312 = FloatText(value='500', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='antigen', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='number of unbound antigen proteins on tumor cell membrane', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float312, units_btn, description_btn] 

        box332 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antibody_antigen_complex', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float313 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='complex', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='number of antibody-antigen protein complex on tumor cell membrane', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float313, units_btn, description_btn] 

        box333 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antibody_binding_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float314 = FloatText(value='0.08', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='antigen protein-antibody binding rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float314, units_btn, description_btn] 

        box334 = Box(children=row, layout=box_layout)
        name_btn = Button(description='last_cycle_entry_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float315 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='mins', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='time that tumor cell entry cycle when division', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float315, units_btn, description_btn] 

        box335 = Box(children=row, layout=box_layout)
        name_btn = Button(description='division_generation', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float316 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='generation', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='how many generations tumor cell has divided', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float316, units_btn, description_btn] 

        box336 = Box(children=row, layout=box_layout)
        name_btn = Button(description='E_Ig_complex', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float317 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='the effect of antibody-antigen protein complex', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float317, units_btn, description_btn] 

        box337 = Box(children=row, layout=box_layout)
        name_btn = Button(description='total_intern_LNP', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float318 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='LNP', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float318, units_btn, description_btn] 

        box338 = Box(children=row, layout=box_layout)
        name_btn = Button(description='endosome_LNP', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float319 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='LNP', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float319, units_btn, description_btn] 

        box339 = Box(children=row, layout=box_layout)
        name_btn = Button(description='free_LNP', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float320 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='LNP', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float320, units_btn, description_btn] 

        box340 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_LNP', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float321 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='LNP', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float321, units_btn, description_btn] 

        box341 = Box(children=row, layout=box_layout)
        name_btn = Button(description='mRNA', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float322 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='mRNA', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float322, units_btn, description_btn] 

        box342 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antigenic_epitope', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float323 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='epitope', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float323, units_btn, description_btn] 

        box343 = Box(children=row, layout=box_layout)

        self.cell_def_vbox3 = VBox([
          div_row25, box258, box259, box260, box261, div_row26, death_model1,box262, box263, box264, box265, box266, box267, box268, death_model2,box269, box270, box271, box272, box273, box274, box275, div_row27, box276, box277, box278, box279, box280, box281, box282, box283, box284, div_row28, box285, box286, box287, box288, box289, div_row29, box290,box291,box292,self.bool17,self.bool18,chemotaxis_btn,self.bool19,box293,box294,div_row30, box295,box296,box297,box298,box299,box300,div_row31, div_row32,          box301,
          box302,
          box303,
          box304,
          box305,
          box306,
          box307,
          box308,
          box309,
          box310,
          box311,
          box312,
          box313,
          box314,
          box315,
          box316,
          box317,
          box318,
          box319,
          box320,
          box321,
          box322,
          box323,
          box324,
          box325,
          box326,
          box327,
          box328,
          box329,
          box330,
          box331,
          box332,
          box333,
          box334,
          box335,
          box336,
          box337,
          box338,
          box339,
          box340,
          box341,
          box342,
          box343,
        ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox3)

        #  >>>>>>>>>>>>>>>>> <cell_definition> = macrophage
        #  ------------------------- 
        div_row33 = Button(description='phenotype:cycle (model: flow_cytometry_separated_cycle_model; code=6)', disabled=True, layout=divider_button_layout)
        div_row33.style.button_color = 'orange'
        name_btn = Button(description='Phase 0 -> Phase 1 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float324 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float324, units_btn, ]
        box344 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 1 -> Phase 2 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float325 = FloatText(value='0.00208333', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float325, units_btn, ]
        box345 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 2 -> Phase 3 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float326 = FloatText(value='0.00416667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float326, units_btn, ]
        box346 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 3 -> Phase 0 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float327 = FloatText(value='0.0166667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float327, units_btn, ]
        box347 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row34 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row34.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float328 = FloatText(value='2.1e-4', step='1e-05', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float328, units_btn, ]
        box348 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float329 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float329, units_btn, ]
        box349 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float330 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float330, units_btn, ]
        box350 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float331 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float331, units_btn, ]
        box351 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float332 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float332, units_btn, ]
        box352 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float333 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float333, units_btn, ]
        box353 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float334 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float334, units_btn, ]
        box354 = Box(children=row, layout=box_layout)

        death_model2 = Button(description='model: necrosis', disabled=True, layout={'width':'30%'})
        death_model2.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float335 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float335, units_btn, ]
        box355 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float336 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float336, units_btn, ]
        box356 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float337 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float337, units_btn, ]
        box357 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float338 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float338, units_btn, ]
        box358 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float339 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float339, units_btn, ]
        box359 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float340 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float340, units_btn, ]
        box360 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float341 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float341, units_btn, ]
        box361 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row35 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row35.style.button_color = 'orange'
        name_btn = Button(description='total', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float342 = FloatText(value='4849', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float342, units_btn, ]
        box362 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float343 = FloatText(value='0.75', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float343, units_btn, ]
        box363 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float344 = FloatText(value='485', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float344, units_btn, ]
        box364 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float345 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float345, units_btn, ]
        box365 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float346 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float346, units_btn, ]
        box366 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float347 = FloatText(value='0.0055', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float347, units_btn, ]
        box367 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcified_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float348 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float348, units_btn, ]
        box368 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float349 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float349, units_btn, ]
        box369 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float350 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float350, units_btn, ]
        box370 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row36 = Button(description='phenotype:mechanics', disabled=True, layout=divider_button_layout)
        div_row36.style.button_color = 'orange'
        name_btn = Button(description='cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float351 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float351, units_btn, ]
        box371 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cell_cell_repulsion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float352 = FloatText(value='10', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float352, units_btn, ]
        box372 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float353 = FloatText(value='1.25', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float353, units_btn, ]
        box373 = Box(children=row, layout=box_layout)

        self.bool20 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_relative_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float354 = FloatText(value='1.8', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [self.bool20, name_btn, self.float354, units_btn, ]
        box374 = Box(children=row, layout=box_layout)

        self.bool21 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_absolute_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float355 = FloatText(value='15.12', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [self.bool21, name_btn, self.float355, units_btn, ]
        box375 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row37 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row37.style.button_color = 'orange'

        name_btn = Button(description='speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float356 = FloatText(value='4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float356, units_btn]
        box376 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float357 = FloatText(value='5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float357, units_btn]
        box377 = Box(children=row, layout=box_layout)

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float358 = FloatText(value='0.7', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float358, units_btn]
        box378 = Box(children=row, layout=box_layout)
        self.bool22 = Checkbox(description='enabled', value=True,layout=name_button_layout)
        self.bool23 = Checkbox(description='use_2D', value=True,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})
        chemotaxis_btn.style.button_color = '#ffde6b'

        self.bool24 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.chemotaxis_substrate5 = Text(value='ISF', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_substrate5]
        box379 = Box(children=row, layout=box_layout)

        name_btn = Button(description='direction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.chemotaxis_direction5 = Text(value='1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_direction5]
        box380 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row38 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row38.style.button_color = 'orange'
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text12 = Text(value='ISF', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text12]
        box381 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float359 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float359, units_btn]
        box382 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text13 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text13]
        box383 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float360 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float360, units_btn]
        box384 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text14 = Text(value='Ig', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text14]
        box385 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float361 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float361, units_btn]
        box386 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row39 = Button(description='phenotype:molecular', disabled=True, layout=divider_button_layout)
        div_row39.style.button_color = 'orange'

#      ================== <custom_data>, if present ==================

        div_row40 = Button(description='Custom Data',disabled=True, layout=divider_button_layout)
        div_row40.style.button_color = 'cyan'
        name_btn = Button(description='unbound_external_receptor', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float362 = FloatText(value='200', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of unbound receptors on DC surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float362, units_btn, description_btn] 

        box387 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_external_receptor', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float363 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of bound receptors on DC surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float363, units_btn, description_btn] 

        box388 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_internal_receptor', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float364 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of internalized unbound receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float364, units_btn, description_btn] 

        box389 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_internal_receptor', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float365 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of internalized bound receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float365, units_btn, description_btn] 

        box390 = Box(children=row, layout=box_layout)
        name_btn = Button(description='receptor_binding_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float366 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='DC receptor-LNP binding rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float366, units_btn, description_btn] 

        box391 = Box(children=row, layout=box_layout)
        name_btn = Button(description='receptor_endocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float367 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='DC receptor-LNP endocytosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float367, units_btn, description_btn] 

        box392 = Box(children=row, layout=box_layout)
        name_btn = Button(description='receptor_cargo_release_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float368 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='DC receptor-LNP cargo release rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float368, units_btn, description_btn] 

        box393 = Box(children=row, layout=box_layout)
        name_btn = Button(description='receptor_recycling_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float369 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='DC receptor recycling rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float369, units_btn, description_btn] 

        box394 = Box(children=row, layout=box_layout)
        name_btn = Button(description='debris_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float370 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate that dead cells release debris', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float370, units_btn, description_btn] 

        box395 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_detection', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float371 = FloatText(value='10', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='protein', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='protein value at which a T Cell can detect an infected cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float371, units_btn, description_btn] 

        box396 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float372 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='tracks total contact time with CD8 T cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float372, units_btn, description_btn] 

        box397 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float373 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='the rate at which the cell attaches to cells in contact', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float373, units_btn, description_btn] 

        box398 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_lifetime', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float374 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='the mean duration of a cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float374, units_btn, description_btn] 

        box399 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_death_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float375 = FloatText(value='90', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='threshold CD8 T cell contact time to trigger apoptosis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float375, units_btn, description_btn] 

        box400 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_attachment_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float376 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float376, units_btn, description_btn] 

        box401 = Box(children=row, layout=box_layout)
        name_btn = Button(description='elastic_attachment_coefficient', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float377 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='elastic coefficient for cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float377, units_btn, description_btn] 

        box402 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_to_next_phagocytosis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float378 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='time it takes for the apoptotic material to be phagocytosed', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float378, units_btn, description_btn] 

        box403 = Box(children=row, layout=box_layout)
        name_btn = Button(description='material_internalisation_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float379 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float379, units_btn, description_btn] 

        box404 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_macrophage_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float380 = FloatText(value='6500', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float380, units_btn, description_btn] 

        box405 = Box(children=row, layout=box_layout)
        name_btn = Button(description='exhausted_macrophage_death_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float381 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float381, units_btn, description_btn] 

        box406 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ability_to_phagocytose_infected_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float382 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Boolean for whether macrophages can phagocytose infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float382, units_btn, description_btn] 

        box407 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_of_DC_departure', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float383 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Time DC leaves tissue after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float383, units_btn, description_btn] 

        box408 = Box(children=row, layout=box_layout)
        name_btn = Button(description='phagocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float384 = FloatText(value='0.167', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float384, units_btn, description_btn] 

        box409 = Box(children=row, layout=box_layout)
        name_btn = Button(description='phagocytosis_relative_target_cutoff_size', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float385 = FloatText(value='1.1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float385, units_btn, description_btn] 

        box410 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_debris_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float386 = FloatText(value='1.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='relative sensitivity to debris in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float386, units_btn, description_btn] 

        box411 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_ISF_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float387 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='relative sensitivity to ISF in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float387, units_btn, description_btn] 

        box412 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float388 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='speed after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float388, units_btn, description_btn] 

        box413 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float389 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate of secreting pro-inflamatory cytokine after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float389, units_btn, description_btn] 

        box414 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_immune_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float390 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='used internally to track activation state', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float390, units_btn, description_btn] 

        box415 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antiinflammatory_cytokine_secretion_rate_by_macrophage', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float391 = FloatText(value='0.07', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='secretion rate of anti-inflammatory from macrophage', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float391, units_btn, description_btn] 

        box416 = Box(children=row, layout=box_layout)
        name_btn = Button(description='generation', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float392 = FloatText(value='3', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='cell proliferation generation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float392, units_btn, description_btn] 

        box417 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antigen_protein', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float393 = FloatText(value='500', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='antigen', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='number of unbound antigen proteins on tumor cell membrane', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float393, units_btn, description_btn] 

        box418 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antibody_antigen_complex', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float394 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='complex', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='number of antibody-antigen protein complex on tumor cell membrane', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float394, units_btn, description_btn] 

        box419 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antibody_binding_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float395 = FloatText(value='0.08', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='antigen protein-antibody binding rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float395, units_btn, description_btn] 

        box420 = Box(children=row, layout=box_layout)
        name_btn = Button(description='last_cycle_entry_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float396 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='mins', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='time that tumor cell entry cycle when division', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float396, units_btn, description_btn] 

        box421 = Box(children=row, layout=box_layout)
        name_btn = Button(description='division_generation', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float397 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='generation', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='how many generations tumor cell has divided', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float397, units_btn, description_btn] 

        box422 = Box(children=row, layout=box_layout)
        name_btn = Button(description='E_Ig_complex', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float398 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='the effect of antibody-antigen protein complex', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float398, units_btn, description_btn] 

        box423 = Box(children=row, layout=box_layout)
        name_btn = Button(description='total_intern_LNP', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float399 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='LNP', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float399, units_btn, description_btn] 

        box424 = Box(children=row, layout=box_layout)
        name_btn = Button(description='endosome_LNP', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float400 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='LNP', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float400, units_btn, description_btn] 

        box425 = Box(children=row, layout=box_layout)
        name_btn = Button(description='free_LNP', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float401 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='LNP', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float401, units_btn, description_btn] 

        box426 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_LNP', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float402 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='LNP', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float402, units_btn, description_btn] 

        box427 = Box(children=row, layout=box_layout)
        name_btn = Button(description='mRNA', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float403 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='mRNA', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float403, units_btn, description_btn] 

        box428 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antigenic_epitope', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float404 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='epitope', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float404, units_btn, description_btn] 

        box429 = Box(children=row, layout=box_layout)

        self.cell_def_vbox4 = VBox([
          div_row33, box344, box345, box346, box347, div_row34, death_model1,box348, box349, box350, box351, box352, box353, box354, death_model2,box355, box356, box357, box358, box359, box360, box361, div_row35, box362, box363, box364, box365, box366, box367, box368, box369, box370, div_row36, box371, box372, box373, box374, box375, div_row37, box376,box377,box378,self.bool22,self.bool23,chemotaxis_btn,self.bool24,box379,box380,div_row38, box381,box382,box383,box384,box385,box386,div_row39, div_row40,          box387,
          box388,
          box389,
          box390,
          box391,
          box392,
          box393,
          box394,
          box395,
          box396,
          box397,
          box398,
          box399,
          box400,
          box401,
          box402,
          box403,
          box404,
          box405,
          box406,
          box407,
          box408,
          box409,
          box410,
          box411,
          box412,
          box413,
          box414,
          box415,
          box416,
          box417,
          box418,
          box419,
          box420,
          box421,
          box422,
          box423,
          box424,
          box425,
          box426,
          box427,
          box428,
          box429,
        ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox4)

        #  >>>>>>>>>>>>>>>>> <cell_definition> = DC
        #  ------------------------- 
        div_row41 = Button(description='phenotype:cycle (model: flow_cytometry_separated_cycle_model; code=6)', disabled=True, layout=divider_button_layout)
        div_row41.style.button_color = 'orange'
        name_btn = Button(description='Phase 0 -> Phase 1 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float405 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float405, units_btn, ]
        box430 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 1 -> Phase 2 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float406 = FloatText(value='0.00208333', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float406, units_btn, ]
        box431 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 2 -> Phase 3 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float407 = FloatText(value='0.00416667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float407, units_btn, ]
        box432 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 3 -> Phase 0 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float408 = FloatText(value='0.0166667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float408, units_btn, ]
        box433 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row42 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row42.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float409 = FloatText(value='8.9e-4', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float409, units_btn, ]
        box434 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float410 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float410, units_btn, ]
        box435 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float411 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float411, units_btn, ]
        box436 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float412 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float412, units_btn, ]
        box437 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float413 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float413, units_btn, ]
        box438 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float414 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float414, units_btn, ]
        box439 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float415 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float415, units_btn, ]
        box440 = Box(children=row, layout=box_layout)

        death_model2 = Button(description='model: necrosis', disabled=True, layout={'width':'30%'})
        death_model2.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float416 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float416, units_btn, ]
        box441 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float417 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float417, units_btn, ]
        box442 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float418 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float418, units_btn, ]
        box443 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float419 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float419, units_btn, ]
        box444 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float420 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float420, units_btn, ]
        box445 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float421 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float421, units_btn, ]
        box446 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float422 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float422, units_btn, ]
        box447 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row43 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row43.style.button_color = 'orange'
        name_btn = Button(description='total', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float423 = FloatText(value='1767', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float423, units_btn, ]
        box448 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float424 = FloatText(value='0.75', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float424, units_btn, ]
        box449 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float425 = FloatText(value='176.7', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float425, units_btn, ]
        box450 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float426 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float426, units_btn, ]
        box451 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float427 = FloatText(value='0.045', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float427, units_btn, ]
        box452 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float428 = FloatText(value='0.0055', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float428, units_btn, ]
        box453 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcified_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float429 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float429, units_btn, ]
        box454 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float430 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float430, units_btn, ]
        box455 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float431 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float431, units_btn, ]
        box456 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row44 = Button(description='phenotype:mechanics', disabled=True, layout=divider_button_layout)
        div_row44.style.button_color = 'orange'
        name_btn = Button(description='cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float432 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float432, units_btn, ]
        box457 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cell_cell_repulsion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float433 = FloatText(value='10', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float433, units_btn, ]
        box458 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float434 = FloatText(value='1.25', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float434, units_btn, ]
        box459 = Box(children=row, layout=box_layout)

        self.bool25 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_relative_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float435 = FloatText(value='1.8', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [self.bool25, name_btn, self.float435, units_btn, ]
        box460 = Box(children=row, layout=box_layout)

        self.bool26 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_absolute_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float436 = FloatText(value='15.12', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [self.bool26, name_btn, self.float436, units_btn, ]
        box461 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row45 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row45.style.button_color = 'orange'

        name_btn = Button(description='speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float437 = FloatText(value='2', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float437, units_btn]
        box462 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float438 = FloatText(value='5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float438, units_btn]
        box463 = Box(children=row, layout=box_layout)

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float439 = FloatText(value='0.7', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float439, units_btn]
        box464 = Box(children=row, layout=box_layout)
        self.bool27 = Checkbox(description='enabled', value=True,layout=name_button_layout)
        self.bool28 = Checkbox(description='use_2D', value=True,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})
        chemotaxis_btn.style.button_color = '#ffde6b'

        self.bool29 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.chemotaxis_substrate6 = Text(value='ISF', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_substrate6]
        box465 = Box(children=row, layout=box_layout)

        name_btn = Button(description='direction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.chemotaxis_direction6 = Text(value='1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_direction6]
        box466 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row46 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row46.style.button_color = 'orange'
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text15 = Text(value='ISF', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text15]
        box467 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float440 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float440, units_btn]
        box468 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text16 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text16]
        box469 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float441 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float441, units_btn]
        box470 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text17 = Text(value='Ig', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text17]
        box471 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float442 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float442, units_btn]
        box472 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row47 = Button(description='phenotype:molecular', disabled=True, layout=divider_button_layout)
        div_row47.style.button_color = 'orange'

#      ================== <custom_data>, if present ==================

        div_row48 = Button(description='Custom Data',disabled=True, layout=divider_button_layout)
        div_row48.style.button_color = 'cyan'
        name_btn = Button(description='unbound_external_receptor', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float443 = FloatText(value='200', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of unbound receptors on DC surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float443, units_btn, description_btn] 

        box473 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_external_receptor', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float444 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of bound receptors on DC surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float444, units_btn, description_btn] 

        box474 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_internal_receptor', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float445 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of internalized unbound receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float445, units_btn, description_btn] 

        box475 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_internal_receptor', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float446 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of internalized bound receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float446, units_btn, description_btn] 

        box476 = Box(children=row, layout=box_layout)
        name_btn = Button(description='receptor_binding_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float447 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='DC receptor-LNP binding rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float447, units_btn, description_btn] 

        box477 = Box(children=row, layout=box_layout)
        name_btn = Button(description='receptor_endocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float448 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='DC receptor-LNP endocytosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float448, units_btn, description_btn] 

        box478 = Box(children=row, layout=box_layout)
        name_btn = Button(description='receptor_cargo_release_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float449 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='DC receptor-LNP cargo release rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float449, units_btn, description_btn] 

        box479 = Box(children=row, layout=box_layout)
        name_btn = Button(description='receptor_recycling_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float450 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='DC receptor recycling rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float450, units_btn, description_btn] 

        box480 = Box(children=row, layout=box_layout)
        name_btn = Button(description='debris_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float451 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate that dead cells release debris', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float451, units_btn, description_btn] 

        box481 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_detection', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float452 = FloatText(value='10', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='protein', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='protein value at which a T Cell can detect an infected cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float452, units_btn, description_btn] 

        box482 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float453 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='tracks total contact time with CD8 T cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float453, units_btn, description_btn] 

        box483 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float454 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='the rate at which the cell attaches to cells in contact', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float454, units_btn, description_btn] 

        box484 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_lifetime', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float455 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='the mean duration of a cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float455, units_btn, description_btn] 

        box485 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_death_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float456 = FloatText(value='90', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='threshold CD8 T cell contact time to trigger apoptosis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float456, units_btn, description_btn] 

        box486 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_attachment_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float457 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float457, units_btn, description_btn] 

        box487 = Box(children=row, layout=box_layout)
        name_btn = Button(description='elastic_attachment_coefficient', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float458 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='elastic coefficient for cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float458, units_btn, description_btn] 

        box488 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_to_next_phagocytosis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float459 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='time it takes for the apoptotic material to be phagocytosed', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float459, units_btn, description_btn] 

        box489 = Box(children=row, layout=box_layout)
        name_btn = Button(description='material_internalisation_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float460 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float460, units_btn, description_btn] 

        box490 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_macrophage_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float461 = FloatText(value='6500', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float461, units_btn, description_btn] 

        box491 = Box(children=row, layout=box_layout)
        name_btn = Button(description='exhausted_macrophage_death_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float462 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float462, units_btn, description_btn] 

        box492 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ability_to_phagocytose_infected_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float463 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Boolean for whether macrophages can phagocytose infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float463, units_btn, description_btn] 

        box493 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_of_DC_departure', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float464 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Time DC leaves tissue after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float464, units_btn, description_btn] 

        box494 = Box(children=row, layout=box_layout)
        name_btn = Button(description='phagocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float465 = FloatText(value='0.167', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float465, units_btn, description_btn] 

        box495 = Box(children=row, layout=box_layout)
        name_btn = Button(description='phagocytosis_relative_target_cutoff_size', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float466 = FloatText(value='1.1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float466, units_btn, description_btn] 

        box496 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_debris_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float467 = FloatText(value='1.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='relative sensitivity to debris in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float467, units_btn, description_btn] 

        box497 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_ISF_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float468 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='relative sensitivity to ISF in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float468, units_btn, description_btn] 

        box498 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float469 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='speed after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float469, units_btn, description_btn] 

        box499 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float470 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate of secreting pro-inflamatory cytokine after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float470, units_btn, description_btn] 

        box500 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_immune_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float471 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='used internally to track activation state', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float471, units_btn, description_btn] 

        box501 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antiinflammatory_cytokine_secretion_rate_by_macrophage', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float472 = FloatText(value='0.07', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='secretion rate of anti-inflammatory from macrophage', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float472, units_btn, description_btn] 

        box502 = Box(children=row, layout=box_layout)
        name_btn = Button(description='generation', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float473 = FloatText(value='3', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='cell proliferation generation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float473, units_btn, description_btn] 

        box503 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antigen_protein', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float474 = FloatText(value='500', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='antigen', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='number of unbound antigen proteins on tumor cell membrane', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float474, units_btn, description_btn] 

        box504 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antibody_antigen_complex', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float475 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='complex', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='number of antibody-antigen protein complex on tumor cell membrane', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float475, units_btn, description_btn] 

        box505 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antibody_binding_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float476 = FloatText(value='0.08', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='antigen protein-antibody binding rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float476, units_btn, description_btn] 

        box506 = Box(children=row, layout=box_layout)
        name_btn = Button(description='last_cycle_entry_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float477 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='mins', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='time that tumor cell entry cycle when division', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float477, units_btn, description_btn] 

        box507 = Box(children=row, layout=box_layout)
        name_btn = Button(description='division_generation', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float478 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='generation', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='how many generations tumor cell has divided', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float478, units_btn, description_btn] 

        box508 = Box(children=row, layout=box_layout)
        name_btn = Button(description='E_Ig_complex', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float479 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='the effect of antibody-antigen protein complex', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float479, units_btn, description_btn] 

        box509 = Box(children=row, layout=box_layout)
        name_btn = Button(description='total_intern_LNP', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float480 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='LNP', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float480, units_btn, description_btn] 

        box510 = Box(children=row, layout=box_layout)
        name_btn = Button(description='endosome_LNP', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float481 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='LNP', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float481, units_btn, description_btn] 

        box511 = Box(children=row, layout=box_layout)
        name_btn = Button(description='free_LNP', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float482 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='LNP', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float482, units_btn, description_btn] 

        box512 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_LNP', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float483 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='LNP', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float483, units_btn, description_btn] 

        box513 = Box(children=row, layout=box_layout)
        name_btn = Button(description='mRNA', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float484 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='mRNA', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float484, units_btn, description_btn] 

        box514 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antigenic_epitope', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float485 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='epitope', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float485, units_btn, description_btn] 

        box515 = Box(children=row, layout=box_layout)

        self.cell_def_vbox5 = VBox([
          div_row41, box430, box431, box432, box433, div_row42, death_model1,box434, box435, box436, box437, box438, box439, box440, death_model2,box441, box442, box443, box444, box445, box446, box447, div_row43, box448, box449, box450, box451, box452, box453, box454, box455, box456, div_row44, box457, box458, box459, box460, box461, div_row45, box462,box463,box464,self.bool27,self.bool28,chemotaxis_btn,self.bool29,box465,box466,div_row46, box467,box468,box469,box470,box471,box472,div_row47, div_row48,          box473,
          box474,
          box475,
          box476,
          box477,
          box478,
          box479,
          box480,
          box481,
          box482,
          box483,
          box484,
          box485,
          box486,
          box487,
          box488,
          box489,
          box490,
          box491,
          box492,
          box493,
          box494,
          box495,
          box496,
          box497,
          box498,
          box499,
          box500,
          box501,
          box502,
          box503,
          box504,
          box505,
          box506,
          box507,
          box508,
          box509,
          box510,
          box511,
          box512,
          box513,
          box514,
          box515,
        ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox5)

        #  >>>>>>>>>>>>>>>>> <cell_definition> = CD4 Tcell
        #  ------------------------- 
        div_row49 = Button(description='phenotype:cycle (model: flow_cytometry_separated_cycle_model; code=6)', disabled=True, layout=divider_button_layout)
        div_row49.style.button_color = 'orange'
        name_btn = Button(description='Phase 0 -> Phase 1 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float486 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float486, units_btn, ]
        box516 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 1 -> Phase 2 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float487 = FloatText(value='0.00208333', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float487, units_btn, ]
        box517 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 2 -> Phase 3 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float488 = FloatText(value='0.00416667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float488, units_btn, ]
        box518 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 3 -> Phase 0 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float489 = FloatText(value='0.0166667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float489, units_btn, ]
        box519 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row50 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row50.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float490 = FloatText(value='2.8e-4', step='1e-05', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float490, units_btn, ]
        box520 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float491 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float491, units_btn, ]
        box521 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float492 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float492, units_btn, ]
        box522 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float493 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float493, units_btn, ]
        box523 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float494 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float494, units_btn, ]
        box524 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float495 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float495, units_btn, ]
        box525 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float496 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float496, units_btn, ]
        box526 = Box(children=row, layout=box_layout)

        death_model2 = Button(description='model: necrosis', disabled=True, layout={'width':'30%'})
        death_model2.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float497 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float497, units_btn, ]
        box527 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float498 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float498, units_btn, ]
        box528 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float499 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float499, units_btn, ]
        box529 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float500 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float500, units_btn, ]
        box530 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float501 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float501, units_btn, ]
        box531 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float502 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float502, units_btn, ]
        box532 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float503 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float503, units_btn, ]
        box533 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row51 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row51.style.button_color = 'orange'
        name_btn = Button(description='total', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float504 = FloatText(value='478', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float504, units_btn, ]
        box534 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float505 = FloatText(value='0.75', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float505, units_btn, ]
        box535 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float506 = FloatText(value='47.8', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float506, units_btn, ]
        box536 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float507 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float507, units_btn, ]
        box537 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float508 = FloatText(value='0.0045', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float508, units_btn, ]
        box538 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float509 = FloatText(value='0.0055', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float509, units_btn, ]
        box539 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcified_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float510 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float510, units_btn, ]
        box540 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float511 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float511, units_btn, ]
        box541 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float512 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float512, units_btn, ]
        box542 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row52 = Button(description='phenotype:mechanics', disabled=True, layout=divider_button_layout)
        div_row52.style.button_color = 'orange'
        name_btn = Button(description='cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float513 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float513, units_btn, ]
        box543 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cell_cell_repulsion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float514 = FloatText(value='10', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float514, units_btn, ]
        box544 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float515 = FloatText(value='1.25', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float515, units_btn, ]
        box545 = Box(children=row, layout=box_layout)

        self.bool30 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_relative_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float516 = FloatText(value='1.8', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [self.bool30, name_btn, self.float516, units_btn, ]
        box546 = Box(children=row, layout=box_layout)

        self.bool31 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_absolute_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float517 = FloatText(value='15.12', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [self.bool31, name_btn, self.float517, units_btn, ]
        box547 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row53 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row53.style.button_color = 'orange'

        name_btn = Button(description='speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float518 = FloatText(value='4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float518, units_btn]
        box548 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float519 = FloatText(value='5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float519, units_btn]
        box549 = Box(children=row, layout=box_layout)

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float520 = FloatText(value='0.70', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float520, units_btn]
        box550 = Box(children=row, layout=box_layout)
        self.bool32 = Checkbox(description='enabled', value=True,layout=name_button_layout)
        self.bool33 = Checkbox(description='use_2D', value=True,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})
        chemotaxis_btn.style.button_color = '#ffde6b'

        self.bool34 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.chemotaxis_substrate7 = Text(value='ISF', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_substrate7]
        box551 = Box(children=row, layout=box_layout)

        name_btn = Button(description='direction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.chemotaxis_direction7 = Text(value='1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_direction7]
        box552 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row54 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row54.style.button_color = 'orange'
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text18 = Text(value='ISF', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text18]
        box553 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float521 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float521, units_btn]
        box554 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text19 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text19]
        box555 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float522 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float522, units_btn]
        box556 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text20 = Text(value='Ig', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text20]
        box557 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float523 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float523, units_btn]
        box558 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row55 = Button(description='phenotype:molecular', disabled=True, layout=divider_button_layout)
        div_row55.style.button_color = 'orange'

#      ================== <custom_data>, if present ==================

        div_row56 = Button(description='Custom Data',disabled=True, layout=divider_button_layout)
        div_row56.style.button_color = 'cyan'
        name_btn = Button(description='unbound_external_receptor', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float524 = FloatText(value='200', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of unbound receptors on DC surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float524, units_btn, description_btn] 

        box559 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_external_receptor', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float525 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of bound receptors on DC surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float525, units_btn, description_btn] 

        box560 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_internal_receptor', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float526 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of internalized unbound receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float526, units_btn, description_btn] 

        box561 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_internal_receptor', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float527 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of internalized bound receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float527, units_btn, description_btn] 

        box562 = Box(children=row, layout=box_layout)
        name_btn = Button(description='receptor_binding_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float528 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='DC receptor-LNP binding rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float528, units_btn, description_btn] 

        box563 = Box(children=row, layout=box_layout)
        name_btn = Button(description='receptor_endocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float529 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='DC receptor-LNP endocytosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float529, units_btn, description_btn] 

        box564 = Box(children=row, layout=box_layout)
        name_btn = Button(description='receptor_cargo_release_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float530 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='DC receptor-LNP cargo release rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float530, units_btn, description_btn] 

        box565 = Box(children=row, layout=box_layout)
        name_btn = Button(description='receptor_recycling_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float531 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='DC receptor recycling rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float531, units_btn, description_btn] 

        box566 = Box(children=row, layout=box_layout)
        name_btn = Button(description='debris_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float532 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate that dead cells release debris', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float532, units_btn, description_btn] 

        box567 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_detection', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float533 = FloatText(value='10', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='protein', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='protein value at which a T Cell can detect an infected cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float533, units_btn, description_btn] 

        box568 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float534 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='tracks total contact time with CD8 T cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float534, units_btn, description_btn] 

        box569 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float535 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='the rate at which the cell attaches to cells in contact', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float535, units_btn, description_btn] 

        box570 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_lifetime', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float536 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='the mean duration of a cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float536, units_btn, description_btn] 

        box571 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_death_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float537 = FloatText(value='90', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='threshold CD8 T cell contact time to trigger apoptosis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float537, units_btn, description_btn] 

        box572 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_attachment_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float538 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float538, units_btn, description_btn] 

        box573 = Box(children=row, layout=box_layout)
        name_btn = Button(description='elastic_attachment_coefficient', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float539 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='elastic coefficient for cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float539, units_btn, description_btn] 

        box574 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_to_next_phagocytosis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float540 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='time it takes for the apoptotic material to be phagocytosed', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float540, units_btn, description_btn] 

        box575 = Box(children=row, layout=box_layout)
        name_btn = Button(description='material_internalisation_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float541 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float541, units_btn, description_btn] 

        box576 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_macrophage_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float542 = FloatText(value='6500', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float542, units_btn, description_btn] 

        box577 = Box(children=row, layout=box_layout)
        name_btn = Button(description='exhausted_macrophage_death_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float543 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float543, units_btn, description_btn] 

        box578 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ability_to_phagocytose_infected_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float544 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Boolean for whether macrophages can phagocytose infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float544, units_btn, description_btn] 

        box579 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_of_DC_departure', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float545 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Time DC leaves tissue after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float545, units_btn, description_btn] 

        box580 = Box(children=row, layout=box_layout)
        name_btn = Button(description='phagocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float546 = FloatText(value='0.167', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float546, units_btn, description_btn] 

        box581 = Box(children=row, layout=box_layout)
        name_btn = Button(description='phagocytosis_relative_target_cutoff_size', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float547 = FloatText(value='1.1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float547, units_btn, description_btn] 

        box582 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_debris_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float548 = FloatText(value='1.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='relative sensitivity to debris in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float548, units_btn, description_btn] 

        box583 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_ISF_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float549 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='relative sensitivity to ISF in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float549, units_btn, description_btn] 

        box584 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float550 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='speed after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float550, units_btn, description_btn] 

        box585 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float551 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate of secreting pro-inflamatory cytokine after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float551, units_btn, description_btn] 

        box586 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_immune_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float552 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='used internally to track activation state', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float552, units_btn, description_btn] 

        box587 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antiinflammatory_cytokine_secretion_rate_by_macrophage', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float553 = FloatText(value='0.07', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='secretion rate of anti-inflammatory from macrophage', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float553, units_btn, description_btn] 

        box588 = Box(children=row, layout=box_layout)
        name_btn = Button(description='generation', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float554 = FloatText(value='3', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='cell proliferation generation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float554, units_btn, description_btn] 

        box589 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antigen_protein', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float555 = FloatText(value='500', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='antigen', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='number of unbound antigen proteins on tumor cell membrane', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float555, units_btn, description_btn] 

        box590 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antibody_antigen_complex', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float556 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='complex', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='number of antibody-antigen protein complex on tumor cell membrane', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float556, units_btn, description_btn] 

        box591 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antibody_binding_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float557 = FloatText(value='0.08', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='antigen protein-antibody binding rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float557, units_btn, description_btn] 

        box592 = Box(children=row, layout=box_layout)
        name_btn = Button(description='last_cycle_entry_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float558 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='mins', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='time that tumor cell entry cycle when division', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float558, units_btn, description_btn] 

        box593 = Box(children=row, layout=box_layout)
        name_btn = Button(description='division_generation', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float559 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='generation', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='how many generations tumor cell has divided', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float559, units_btn, description_btn] 

        box594 = Box(children=row, layout=box_layout)
        name_btn = Button(description='E_Ig_complex', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float560 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='the effect of antibody-antigen protein complex', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float560, units_btn, description_btn] 

        box595 = Box(children=row, layout=box_layout)
        name_btn = Button(description='total_intern_LNP', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float561 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='LNP', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float561, units_btn, description_btn] 

        box596 = Box(children=row, layout=box_layout)
        name_btn = Button(description='endosome_LNP', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float562 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='LNP', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float562, units_btn, description_btn] 

        box597 = Box(children=row, layout=box_layout)
        name_btn = Button(description='free_LNP', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float563 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='LNP', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float563, units_btn, description_btn] 

        box598 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_LNP', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float564 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='LNP', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float564, units_btn, description_btn] 

        box599 = Box(children=row, layout=box_layout)
        name_btn = Button(description='mRNA', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float565 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='mRNA', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float565, units_btn, description_btn] 

        box600 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antigenic_epitope', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float566 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='epitope', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float566, units_btn, description_btn] 

        box601 = Box(children=row, layout=box_layout)

        self.cell_def_vbox6 = VBox([
          div_row49, box516, box517, box518, box519, div_row50, death_model1,box520, box521, box522, box523, box524, box525, box526, death_model2,box527, box528, box529, box530, box531, box532, box533, div_row51, box534, box535, box536, box537, box538, box539, box540, box541, box542, div_row52, box543, box544, box545, box546, box547, div_row53, box548,box549,box550,self.bool32,self.bool33,chemotaxis_btn,self.bool34,box551,box552,div_row54, box553,box554,box555,box556,box557,box558,div_row55, div_row56,          box559,
          box560,
          box561,
          box562,
          box563,
          box564,
          box565,
          box566,
          box567,
          box568,
          box569,
          box570,
          box571,
          box572,
          box573,
          box574,
          box575,
          box576,
          box577,
          box578,
          box579,
          box580,
          box581,
          box582,
          box583,
          box584,
          box585,
          box586,
          box587,
          box588,
          box589,
          box590,
          box591,
          box592,
          box593,
          box594,
          box595,
          box596,
          box597,
          box598,
          box599,
          box600,
          box601,
        ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox6)



        row = [name_btn, self.float566, units_btn, description_btn] 
        box558 = Box(children=row, layout=box_layout)

        self.tab = VBox([
          self.cell_type_parent_row,  
self.cell_def_vbox0, self.cell_def_vbox1, self.cell_def_vbox2, self.cell_def_vbox3, self.cell_def_vbox4, self.cell_def_vbox5, self.cell_def_vbox6,         ])
    #------------------------------
    def cell_type_cb(self, change):
        if change['type'] == 'change' and change['name'] == 'value':
            # print("changed to %s" % change['new'])
            # self.parent_name.value = self.cell_type_parent_dict[change['new']]
            # idx_selected = list(self.cell_type_parent_dict.keys()).index(change['new'])
            idx_selected = list(self.cell_type_dict.keys()).index(change['new'])

            # print('index=',idx_selected)
            # self.vbox1.layout.visibility = 'hidden'  # vs. visible
            # self.vbox1.layout.visibility = None 

            # There's probably a better way to do this, but for now,
            # we hide all vboxes containing the widgets for the different cell defs
            # and only display the contents of the selected one.
            for vb in self.cell_def_vboxes:
                vb.layout.display = 'none'   # vs. 'contents'
            self.cell_def_vboxes[idx_selected].layout.display = 'contents'   # vs. 'contents'


    #------------------------------
    def display_cell_type_default(self):
        # print("display_cell_type_default():")
        #print("    self.cell_type_parent_dict = ",self.cell_type_parent_dict)

        # There's probably a better way to do this, but for now,
        # we hide all vboxes containing the widgets for the different cell defs
        # and only display the contents of 'default'
        for vb in self.cell_def_vboxes:
            vb.layout.display = 'none'   # vs. 'contents'
        self.cell_def_vboxes[0].layout.display = 'contents'


    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//cell_definitions')  # find unique entry point

        # ------------------ cell_definition: default
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        self.float0.value = float(uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[1]').text)
        self.float1.value = float(uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[2]').text)
        self.float2.value = float(uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[3]').text)
        self.float3.value = float(uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[4]').text)
        # ---------  death 
        self.float4.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//death_rate').text)
        self.float5.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text)
        self.float6.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text)
        self.float7.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float8.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text)
        self.float9.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//calcification_rate').text)
        self.float10.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//relative_rupture_volume').text)
        self.float11.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//death_rate').text)
        self.float12.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text)
        self.float13.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text)
        self.float14.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float15.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text)
        self.float16.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//calcification_rate').text)
        self.float17.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//relative_rupture_volume').text)
        # ---------  volume 
        self.float18.value = float(uep.find('.//cell_definition[1]//phenotype//volume//total').text)
        self.float19.value = float(uep.find('.//cell_definition[1]//phenotype//volume//fluid_fraction').text)
        self.float20.value = float(uep.find('.//cell_definition[1]//phenotype//volume//nuclear').text)
        self.float21.value = float(uep.find('.//cell_definition[1]//phenotype//volume//fluid_change_rate').text)
        self.float22.value = float(uep.find('.//cell_definition[1]//phenotype//volume//cytoplasmic_biomass_change_rate').text)
        self.float23.value = float(uep.find('.//cell_definition[1]//phenotype//volume//nuclear_biomass_change_rate').text)
        self.float24.value = float(uep.find('.//cell_definition[1]//phenotype//volume//calcified_fraction').text)
        self.float25.value = float(uep.find('.//cell_definition[1]//phenotype//volume//calcification_rate').text)
        self.float26.value = float(uep.find('.//cell_definition[1]//phenotype//volume//relative_rupture_volume').text)
        # ---------  mechanics 
        self.float27.value = float(uep.find('.//cell_definition[1]//phenotype//mechanics//cell_cell_adhesion_strength').text)
        self.float28.value = float(uep.find('.//cell_definition[1]//phenotype//mechanics//cell_cell_repulsion_strength').text)
        self.float29.value = float(uep.find('.//cell_definition[1]//phenotype//mechanics//relative_maximum_adhesion_distance').text)
        self.bool0.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'].lower()))
        self.bool1.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'].lower()))
        # ---------  motility 
        self.float32.value = float(uep.find('.//cell_definition[1]//phenotype//motility//speed').text)
        self.float33.value = float(uep.find('.//cell_definition[1]//phenotype//motility//persistence_time').text)
        self.float34.value = float(uep.find('.//cell_definition[1]//phenotype//motility//migration_bias').text)
        self.bool2.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//motility//options//enabled').text.lower()))
        self.bool3.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//motility//options//use_2D').text.lower()))
        self.bool4.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        self.chemotaxis_substrate1.value = uep.find('.//cell_definition[1]//phenotype//motility//options//chemotaxis//substrate').text
        self.chemotaxis_direction1.value = uep.find('.//cell_definition[1]//phenotype//motility//options//chemotaxis//direction').text
        # ---------  secretion 
        self.text0.value = uep.find('.//cell_definition[1]//phenotype//secretion//substrate[1]').attrib['name']
        self.float35.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[1]//secretion_target').text)
        self.text1.value = uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]').attrib['name']
        self.float36.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]//secretion_target').text)
        self.text2.value = uep.find('.//cell_definition[1]//phenotype//secretion//substrate[3]').attrib['name']
        self.float37.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[3]//secretion_target').text)
        # ---------  molecular
        # ------------------ cell_definition: immune
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        self.float81.value = float(uep.find('.//cell_definition[2]//phenotype//cycle//phase_transition_rates//rate[1]').text)
        self.float82.value = float(uep.find('.//cell_definition[2]//phenotype//cycle//phase_transition_rates//rate[2]').text)
        self.float83.value = float(uep.find('.//cell_definition[2]//phenotype//cycle//phase_transition_rates//rate[3]').text)
        self.float84.value = float(uep.find('.//cell_definition[2]//phenotype//cycle//phase_transition_rates//rate[4]').text)
        # ---------  death 
        self.float85.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[1]//death_rate').text)
        self.float86.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text)
        self.float87.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text)
        self.float88.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float89.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text)
        self.float90.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//calcification_rate').text)
        self.float91.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//relative_rupture_volume').text)
        self.float92.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[2]//death_rate').text)
        self.float93.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text)
        self.float94.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text)
        self.float95.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float96.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text)
        self.float97.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//calcification_rate').text)
        self.float98.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//relative_rupture_volume').text)
        # ---------  volume 
        self.float99.value = float(uep.find('.//cell_definition[2]//phenotype//volume//total').text)
        self.float100.value = float(uep.find('.//cell_definition[2]//phenotype//volume//fluid_fraction').text)
        self.float101.value = float(uep.find('.//cell_definition[2]//phenotype//volume//nuclear').text)
        self.float102.value = float(uep.find('.//cell_definition[2]//phenotype//volume//fluid_change_rate').text)
        self.float103.value = float(uep.find('.//cell_definition[2]//phenotype//volume//cytoplasmic_biomass_change_rate').text)
        self.float104.value = float(uep.find('.//cell_definition[2]//phenotype//volume//nuclear_biomass_change_rate').text)
        self.float105.value = float(uep.find('.//cell_definition[2]//phenotype//volume//calcified_fraction').text)
        self.float106.value = float(uep.find('.//cell_definition[2]//phenotype//volume//calcification_rate').text)
        self.float107.value = float(uep.find('.//cell_definition[2]//phenotype//volume//relative_rupture_volume').text)
        # ---------  mechanics 
        self.float108.value = float(uep.find('.//cell_definition[2]//phenotype//mechanics//cell_cell_adhesion_strength').text)
        self.float109.value = float(uep.find('.//cell_definition[2]//phenotype//mechanics//cell_cell_repulsion_strength').text)
        self.float110.value = float(uep.find('.//cell_definition[2]//phenotype//mechanics//relative_maximum_adhesion_distance').text)
        self.bool5.value = ('true' == (uep.find('.//cell_definition[2]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'].lower()))
        self.bool6.value = ('true' == (uep.find('.//cell_definition[2]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'].lower()))
        # ---------  motility 
        self.float113.value = float(uep.find('.//cell_definition[2]//phenotype//motility//speed').text)
        self.float114.value = float(uep.find('.//cell_definition[2]//phenotype//motility//persistence_time').text)
        self.float115.value = float(uep.find('.//cell_definition[2]//phenotype//motility//migration_bias').text)
        self.bool7.value = ('true' == (uep.find('.//cell_definition[2]//phenotype//motility//options//enabled').text.lower()))
        self.bool8.value = ('true' == (uep.find('.//cell_definition[2]//phenotype//motility//options//use_2D').text.lower()))
        self.bool9.value = ('true' == (uep.find('.//cell_definition[2]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        self.chemotaxis_substrate2.value = uep.find('.//cell_definition[2]//phenotype//motility//options//chemotaxis//substrate').text
        self.chemotaxis_direction2.value = uep.find('.//cell_definition[2]//phenotype//motility//options//chemotaxis//direction').text
        # ---------  secretion 
        self.text3.value = uep.find('.//cell_definition[2]//phenotype//secretion//substrate[1]').attrib['name']
        self.float116.value = float(uep.find('.//cell_definition[2]//phenotype//secretion//substrate[1]//secretion_target').text)
        self.text4.value = uep.find('.//cell_definition[2]//phenotype//secretion//substrate[2]').attrib['name']
        self.float117.value = float(uep.find('.//cell_definition[2]//phenotype//secretion//substrate[2]//secretion_target').text)
        self.text5.value = uep.find('.//cell_definition[2]//phenotype//secretion//substrate[3]').attrib['name']
        self.float118.value = float(uep.find('.//cell_definition[2]//phenotype//secretion//substrate[3]//secretion_target').text)
        # ---------  molecular
        # ------------------ cell_definition: tumor cell
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        self.float162.value = float(uep.find('.//cell_definition[3]//phenotype//cycle//phase_transition_rates//rate[1]').text)
        self.float163.value = float(uep.find('.//cell_definition[3]//phenotype//cycle//phase_transition_rates//rate[2]').text)
        self.float164.value = float(uep.find('.//cell_definition[3]//phenotype//cycle//phase_transition_rates//rate[3]').text)
        self.float165.value = float(uep.find('.//cell_definition[3]//phenotype//cycle//phase_transition_rates//rate[4]').text)
        # ---------  death 
        self.float166.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[1]//death_rate').text)
        self.float167.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text)
        self.float168.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text)
        self.float169.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float170.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text)
        self.float171.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//calcification_rate').text)
        self.float172.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//relative_rupture_volume').text)
        self.float173.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[2]//death_rate').text)
        self.float174.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text)
        self.float175.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text)
        self.float176.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float177.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text)
        self.float178.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//calcification_rate').text)
        self.float179.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//relative_rupture_volume').text)
        # ---------  volume 
        self.float180.value = float(uep.find('.//cell_definition[3]//phenotype//volume//total').text)
        self.float181.value = float(uep.find('.//cell_definition[3]//phenotype//volume//fluid_fraction').text)
        self.float182.value = float(uep.find('.//cell_definition[3]//phenotype//volume//nuclear').text)
        self.float183.value = float(uep.find('.//cell_definition[3]//phenotype//volume//fluid_change_rate').text)
        self.float184.value = float(uep.find('.//cell_definition[3]//phenotype//volume//cytoplasmic_biomass_change_rate').text)
        self.float185.value = float(uep.find('.//cell_definition[3]//phenotype//volume//nuclear_biomass_change_rate').text)
        self.float186.value = float(uep.find('.//cell_definition[3]//phenotype//volume//calcified_fraction').text)
        self.float187.value = float(uep.find('.//cell_definition[3]//phenotype//volume//calcification_rate').text)
        self.float188.value = float(uep.find('.//cell_definition[3]//phenotype//volume//relative_rupture_volume').text)
        # ---------  mechanics 
        self.float189.value = float(uep.find('.//cell_definition[3]//phenotype//mechanics//cell_cell_adhesion_strength').text)
        self.float190.value = float(uep.find('.//cell_definition[3]//phenotype//mechanics//cell_cell_repulsion_strength').text)
        self.float191.value = float(uep.find('.//cell_definition[3]//phenotype//mechanics//relative_maximum_adhesion_distance').text)
        self.bool10.value = ('true' == (uep.find('.//cell_definition[3]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'].lower()))
        self.bool11.value = ('true' == (uep.find('.//cell_definition[3]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'].lower()))
        # ---------  motility 
        self.float194.value = float(uep.find('.//cell_definition[3]//phenotype//motility//speed').text)
        self.float195.value = float(uep.find('.//cell_definition[3]//phenotype//motility//persistence_time').text)
        self.float196.value = float(uep.find('.//cell_definition[3]//phenotype//motility//migration_bias').text)
        self.bool12.value = ('true' == (uep.find('.//cell_definition[3]//phenotype//motility//options//enabled').text.lower()))
        self.bool13.value = ('true' == (uep.find('.//cell_definition[3]//phenotype//motility//options//use_2D').text.lower()))
        self.bool14.value = ('true' == (uep.find('.//cell_definition[3]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        self.chemotaxis_substrate3.value = uep.find('.//cell_definition[3]//phenotype//motility//options//chemotaxis//substrate').text
        self.chemotaxis_direction3.value = uep.find('.//cell_definition[3]//phenotype//motility//options//chemotaxis//direction').text
        # ---------  secretion 
        self.text6.value = uep.find('.//cell_definition[3]//phenotype//secretion//substrate[1]').attrib['name']
        self.float197.value = float(uep.find('.//cell_definition[3]//phenotype//secretion//substrate[1]//secretion_target').text)
        self.text7.value = uep.find('.//cell_definition[3]//phenotype//secretion//substrate[2]').attrib['name']
        self.float198.value = float(uep.find('.//cell_definition[3]//phenotype//secretion//substrate[2]//secretion_target').text)
        self.text8.value = uep.find('.//cell_definition[3]//phenotype//secretion//substrate[3]').attrib['name']
        self.float199.value = float(uep.find('.//cell_definition[3]//phenotype//secretion//substrate[3]//secretion_target').text)
        # ---------  molecular
        # ------------------ cell_definition: CD8 Tcell
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        self.float243.value = float(uep.find('.//cell_definition[4]//phenotype//cycle//phase_transition_rates//rate[1]').text)
        self.float244.value = float(uep.find('.//cell_definition[4]//phenotype//cycle//phase_transition_rates//rate[2]').text)
        self.float245.value = float(uep.find('.//cell_definition[4]//phenotype//cycle//phase_transition_rates//rate[3]').text)
        self.float246.value = float(uep.find('.//cell_definition[4]//phenotype//cycle//phase_transition_rates//rate[4]').text)
        # ---------  death 
        self.float247.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[1]//death_rate').text)
        self.float248.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text)
        self.float249.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text)
        self.float250.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float251.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text)
        self.float252.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//calcification_rate').text)
        self.float253.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//relative_rupture_volume').text)
        self.float254.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[2]//death_rate').text)
        self.float255.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text)
        self.float256.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text)
        self.float257.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float258.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text)
        self.float259.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//calcification_rate').text)
        self.float260.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//relative_rupture_volume').text)
        # ---------  volume 
        self.float261.value = float(uep.find('.//cell_definition[4]//phenotype//volume//total').text)
        self.float262.value = float(uep.find('.//cell_definition[4]//phenotype//volume//fluid_fraction').text)
        self.float263.value = float(uep.find('.//cell_definition[4]//phenotype//volume//nuclear').text)
        self.float264.value = float(uep.find('.//cell_definition[4]//phenotype//volume//fluid_change_rate').text)
        self.float265.value = float(uep.find('.//cell_definition[4]//phenotype//volume//cytoplasmic_biomass_change_rate').text)
        self.float266.value = float(uep.find('.//cell_definition[4]//phenotype//volume//nuclear_biomass_change_rate').text)
        self.float267.value = float(uep.find('.//cell_definition[4]//phenotype//volume//calcified_fraction').text)
        self.float268.value = float(uep.find('.//cell_definition[4]//phenotype//volume//calcification_rate').text)
        self.float269.value = float(uep.find('.//cell_definition[4]//phenotype//volume//relative_rupture_volume').text)
        # ---------  mechanics 
        self.float270.value = float(uep.find('.//cell_definition[4]//phenotype//mechanics//cell_cell_adhesion_strength').text)
        self.float271.value = float(uep.find('.//cell_definition[4]//phenotype//mechanics//cell_cell_repulsion_strength').text)
        self.float272.value = float(uep.find('.//cell_definition[4]//phenotype//mechanics//relative_maximum_adhesion_distance').text)
        self.bool15.value = ('true' == (uep.find('.//cell_definition[4]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'].lower()))
        self.bool16.value = ('true' == (uep.find('.//cell_definition[4]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'].lower()))
        # ---------  motility 
        self.float275.value = float(uep.find('.//cell_definition[4]//phenotype//motility//speed').text)
        self.float276.value = float(uep.find('.//cell_definition[4]//phenotype//motility//persistence_time').text)
        self.float277.value = float(uep.find('.//cell_definition[4]//phenotype//motility//migration_bias').text)
        self.bool17.value = ('true' == (uep.find('.//cell_definition[4]//phenotype//motility//options//enabled').text.lower()))
        self.bool18.value = ('true' == (uep.find('.//cell_definition[4]//phenotype//motility//options//use_2D').text.lower()))
        self.bool19.value = ('true' == (uep.find('.//cell_definition[4]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        self.chemotaxis_substrate4.value = uep.find('.//cell_definition[4]//phenotype//motility//options//chemotaxis//substrate').text
        self.chemotaxis_direction4.value = uep.find('.//cell_definition[4]//phenotype//motility//options//chemotaxis//direction').text
        # ---------  secretion 
        self.text9.value = uep.find('.//cell_definition[4]//phenotype//secretion//substrate[1]').attrib['name']
        self.float278.value = float(uep.find('.//cell_definition[4]//phenotype//secretion//substrate[1]//secretion_target').text)
        self.text10.value = uep.find('.//cell_definition[4]//phenotype//secretion//substrate[2]').attrib['name']
        self.float279.value = float(uep.find('.//cell_definition[4]//phenotype//secretion//substrate[2]//secretion_target').text)
        self.text11.value = uep.find('.//cell_definition[4]//phenotype//secretion//substrate[3]').attrib['name']
        self.float280.value = float(uep.find('.//cell_definition[4]//phenotype//secretion//substrate[3]//secretion_target').text)
        # ---------  molecular
        # ------------------ cell_definition: macrophage
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        self.float324.value = float(uep.find('.//cell_definition[5]//phenotype//cycle//phase_transition_rates//rate[1]').text)
        self.float325.value = float(uep.find('.//cell_definition[5]//phenotype//cycle//phase_transition_rates//rate[2]').text)
        self.float326.value = float(uep.find('.//cell_definition[5]//phenotype//cycle//phase_transition_rates//rate[3]').text)
        self.float327.value = float(uep.find('.//cell_definition[5]//phenotype//cycle//phase_transition_rates//rate[4]').text)
        # ---------  death 
        self.float328.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[1]//death_rate').text)
        self.float329.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text)
        self.float330.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text)
        self.float331.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float332.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text)
        self.float333.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//calcification_rate').text)
        self.float334.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//relative_rupture_volume').text)
        self.float335.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[2]//death_rate').text)
        self.float336.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text)
        self.float337.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text)
        self.float338.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float339.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text)
        self.float340.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//calcification_rate').text)
        self.float341.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//relative_rupture_volume').text)
        # ---------  volume 
        self.float342.value = float(uep.find('.//cell_definition[5]//phenotype//volume//total').text)
        self.float343.value = float(uep.find('.//cell_definition[5]//phenotype//volume//fluid_fraction').text)
        self.float344.value = float(uep.find('.//cell_definition[5]//phenotype//volume//nuclear').text)
        self.float345.value = float(uep.find('.//cell_definition[5]//phenotype//volume//fluid_change_rate').text)
        self.float346.value = float(uep.find('.//cell_definition[5]//phenotype//volume//cytoplasmic_biomass_change_rate').text)
        self.float347.value = float(uep.find('.//cell_definition[5]//phenotype//volume//nuclear_biomass_change_rate').text)
        self.float348.value = float(uep.find('.//cell_definition[5]//phenotype//volume//calcified_fraction').text)
        self.float349.value = float(uep.find('.//cell_definition[5]//phenotype//volume//calcification_rate').text)
        self.float350.value = float(uep.find('.//cell_definition[5]//phenotype//volume//relative_rupture_volume').text)
        # ---------  mechanics 
        self.float351.value = float(uep.find('.//cell_definition[5]//phenotype//mechanics//cell_cell_adhesion_strength').text)
        self.float352.value = float(uep.find('.//cell_definition[5]//phenotype//mechanics//cell_cell_repulsion_strength').text)
        self.float353.value = float(uep.find('.//cell_definition[5]//phenotype//mechanics//relative_maximum_adhesion_distance').text)
        self.bool20.value = ('true' == (uep.find('.//cell_definition[5]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'].lower()))
        self.bool21.value = ('true' == (uep.find('.//cell_definition[5]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'].lower()))
        # ---------  motility 
        self.float356.value = float(uep.find('.//cell_definition[5]//phenotype//motility//speed').text)
        self.float357.value = float(uep.find('.//cell_definition[5]//phenotype//motility//persistence_time').text)
        self.float358.value = float(uep.find('.//cell_definition[5]//phenotype//motility//migration_bias').text)
        self.bool22.value = ('true' == (uep.find('.//cell_definition[5]//phenotype//motility//options//enabled').text.lower()))
        self.bool23.value = ('true' == (uep.find('.//cell_definition[5]//phenotype//motility//options//use_2D').text.lower()))
        self.bool24.value = ('true' == (uep.find('.//cell_definition[5]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        self.chemotaxis_substrate5.value = uep.find('.//cell_definition[5]//phenotype//motility//options//chemotaxis//substrate').text
        self.chemotaxis_direction5.value = uep.find('.//cell_definition[5]//phenotype//motility//options//chemotaxis//direction').text
        # ---------  secretion 
        self.text12.value = uep.find('.//cell_definition[5]//phenotype//secretion//substrate[1]').attrib['name']
        self.float359.value = float(uep.find('.//cell_definition[5]//phenotype//secretion//substrate[1]//secretion_target').text)
        self.text13.value = uep.find('.//cell_definition[5]//phenotype//secretion//substrate[2]').attrib['name']
        self.float360.value = float(uep.find('.//cell_definition[5]//phenotype//secretion//substrate[2]//secretion_target').text)
        self.text14.value = uep.find('.//cell_definition[5]//phenotype//secretion//substrate[3]').attrib['name']
        self.float361.value = float(uep.find('.//cell_definition[5]//phenotype//secretion//substrate[3]//secretion_target').text)
        # ---------  molecular
        # ------------------ cell_definition: DC
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        self.float405.value = float(uep.find('.//cell_definition[6]//phenotype//cycle//phase_transition_rates//rate[1]').text)
        self.float406.value = float(uep.find('.//cell_definition[6]//phenotype//cycle//phase_transition_rates//rate[2]').text)
        self.float407.value = float(uep.find('.//cell_definition[6]//phenotype//cycle//phase_transition_rates//rate[3]').text)
        self.float408.value = float(uep.find('.//cell_definition[6]//phenotype//cycle//phase_transition_rates//rate[4]').text)
        # ---------  death 
        self.float409.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[1]//death_rate').text)
        self.float410.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text)
        self.float411.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text)
        self.float412.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float413.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text)
        self.float414.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//calcification_rate').text)
        self.float415.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//relative_rupture_volume').text)
        self.float416.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[2]//death_rate').text)
        self.float417.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text)
        self.float418.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text)
        self.float419.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float420.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text)
        self.float421.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//calcification_rate').text)
        self.float422.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//relative_rupture_volume').text)
        # ---------  volume 
        self.float423.value = float(uep.find('.//cell_definition[6]//phenotype//volume//total').text)
        self.float424.value = float(uep.find('.//cell_definition[6]//phenotype//volume//fluid_fraction').text)
        self.float425.value = float(uep.find('.//cell_definition[6]//phenotype//volume//nuclear').text)
        self.float426.value = float(uep.find('.//cell_definition[6]//phenotype//volume//fluid_change_rate').text)
        self.float427.value = float(uep.find('.//cell_definition[6]//phenotype//volume//cytoplasmic_biomass_change_rate').text)
        self.float428.value = float(uep.find('.//cell_definition[6]//phenotype//volume//nuclear_biomass_change_rate').text)
        self.float429.value = float(uep.find('.//cell_definition[6]//phenotype//volume//calcified_fraction').text)
        self.float430.value = float(uep.find('.//cell_definition[6]//phenotype//volume//calcification_rate').text)
        self.float431.value = float(uep.find('.//cell_definition[6]//phenotype//volume//relative_rupture_volume').text)
        # ---------  mechanics 
        self.float432.value = float(uep.find('.//cell_definition[6]//phenotype//mechanics//cell_cell_adhesion_strength').text)
        self.float433.value = float(uep.find('.//cell_definition[6]//phenotype//mechanics//cell_cell_repulsion_strength').text)
        self.float434.value = float(uep.find('.//cell_definition[6]//phenotype//mechanics//relative_maximum_adhesion_distance').text)
        self.bool25.value = ('true' == (uep.find('.//cell_definition[6]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'].lower()))
        self.bool26.value = ('true' == (uep.find('.//cell_definition[6]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'].lower()))
        # ---------  motility 
        self.float437.value = float(uep.find('.//cell_definition[6]//phenotype//motility//speed').text)
        self.float438.value = float(uep.find('.//cell_definition[6]//phenotype//motility//persistence_time').text)
        self.float439.value = float(uep.find('.//cell_definition[6]//phenotype//motility//migration_bias').text)
        self.bool27.value = ('true' == (uep.find('.//cell_definition[6]//phenotype//motility//options//enabled').text.lower()))
        self.bool28.value = ('true' == (uep.find('.//cell_definition[6]//phenotype//motility//options//use_2D').text.lower()))
        self.bool29.value = ('true' == (uep.find('.//cell_definition[6]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        self.chemotaxis_substrate6.value = uep.find('.//cell_definition[6]//phenotype//motility//options//chemotaxis//substrate').text
        self.chemotaxis_direction6.value = uep.find('.//cell_definition[6]//phenotype//motility//options//chemotaxis//direction').text
        # ---------  secretion 
        self.text15.value = uep.find('.//cell_definition[6]//phenotype//secretion//substrate[1]').attrib['name']
        self.float440.value = float(uep.find('.//cell_definition[6]//phenotype//secretion//substrate[1]//secretion_target').text)
        self.text16.value = uep.find('.//cell_definition[6]//phenotype//secretion//substrate[2]').attrib['name']
        self.float441.value = float(uep.find('.//cell_definition[6]//phenotype//secretion//substrate[2]//secretion_target').text)
        self.text17.value = uep.find('.//cell_definition[6]//phenotype//secretion//substrate[3]').attrib['name']
        self.float442.value = float(uep.find('.//cell_definition[6]//phenotype//secretion//substrate[3]//secretion_target').text)
        # ---------  molecular
        # ------------------ cell_definition: CD4 Tcell
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        self.float486.value = float(uep.find('.//cell_definition[7]//phenotype//cycle//phase_transition_rates//rate[1]').text)
        self.float487.value = float(uep.find('.//cell_definition[7]//phenotype//cycle//phase_transition_rates//rate[2]').text)
        self.float488.value = float(uep.find('.//cell_definition[7]//phenotype//cycle//phase_transition_rates//rate[3]').text)
        self.float489.value = float(uep.find('.//cell_definition[7]//phenotype//cycle//phase_transition_rates//rate[4]').text)
        # ---------  death 
        self.float490.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[1]//death_rate').text)
        self.float491.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text)
        self.float492.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text)
        self.float493.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float494.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text)
        self.float495.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//calcification_rate').text)
        self.float496.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//relative_rupture_volume').text)
        self.float497.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[2]//death_rate').text)
        self.float498.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text)
        self.float499.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text)
        self.float500.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float501.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text)
        self.float502.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//calcification_rate').text)
        self.float503.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//relative_rupture_volume').text)
        # ---------  volume 
        self.float504.value = float(uep.find('.//cell_definition[7]//phenotype//volume//total').text)
        self.float505.value = float(uep.find('.//cell_definition[7]//phenotype//volume//fluid_fraction').text)
        self.float506.value = float(uep.find('.//cell_definition[7]//phenotype//volume//nuclear').text)
        self.float507.value = float(uep.find('.//cell_definition[7]//phenotype//volume//fluid_change_rate').text)
        self.float508.value = float(uep.find('.//cell_definition[7]//phenotype//volume//cytoplasmic_biomass_change_rate').text)
        self.float509.value = float(uep.find('.//cell_definition[7]//phenotype//volume//nuclear_biomass_change_rate').text)
        self.float510.value = float(uep.find('.//cell_definition[7]//phenotype//volume//calcified_fraction').text)
        self.float511.value = float(uep.find('.//cell_definition[7]//phenotype//volume//calcification_rate').text)
        self.float512.value = float(uep.find('.//cell_definition[7]//phenotype//volume//relative_rupture_volume').text)
        # ---------  mechanics 
        self.float513.value = float(uep.find('.//cell_definition[7]//phenotype//mechanics//cell_cell_adhesion_strength').text)
        self.float514.value = float(uep.find('.//cell_definition[7]//phenotype//mechanics//cell_cell_repulsion_strength').text)
        self.float515.value = float(uep.find('.//cell_definition[7]//phenotype//mechanics//relative_maximum_adhesion_distance').text)
        self.bool30.value = ('true' == (uep.find('.//cell_definition[7]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'].lower()))
        self.bool31.value = ('true' == (uep.find('.//cell_definition[7]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'].lower()))
        # ---------  motility 
        self.float518.value = float(uep.find('.//cell_definition[7]//phenotype//motility//speed').text)
        self.float519.value = float(uep.find('.//cell_definition[7]//phenotype//motility//persistence_time').text)
        self.float520.value = float(uep.find('.//cell_definition[7]//phenotype//motility//migration_bias').text)
        self.bool32.value = ('true' == (uep.find('.//cell_definition[7]//phenotype//motility//options//enabled').text.lower()))
        self.bool33.value = ('true' == (uep.find('.//cell_definition[7]//phenotype//motility//options//use_2D').text.lower()))
        self.bool34.value = ('true' == (uep.find('.//cell_definition[7]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        self.chemotaxis_substrate7.value = uep.find('.//cell_definition[7]//phenotype//motility//options//chemotaxis//substrate').text
        self.chemotaxis_direction7.value = uep.find('.//cell_definition[7]//phenotype//motility//options//chemotaxis//direction').text
        # ---------  secretion 
        self.text18.value = uep.find('.//cell_definition[7]//phenotype//secretion//substrate[1]').attrib['name']
        self.float521.value = float(uep.find('.//cell_definition[7]//phenotype//secretion//substrate[1]//secretion_target').text)
        self.text19.value = uep.find('.//cell_definition[7]//phenotype//secretion//substrate[2]').attrib['name']
        self.float522.value = float(uep.find('.//cell_definition[7]//phenotype//secretion//substrate[2]//secretion_target').text)
        self.text20.value = uep.find('.//cell_definition[7]//phenotype//secretion//substrate[3]').attrib['name']
        self.float523.value = float(uep.find('.//cell_definition[7]//phenotype//secretion//substrate[3]//secretion_target').text)
        # ---------  molecular


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//cell_definitions')  # find unique entry point

        # ------------------ cell_definition: default
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[1]').text = str(self.float0.value)
        uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[2]').text = str(self.float1.value)
        uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[3]').text = str(self.float2.value)
        uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[4]').text = str(self.float3.value)
        # ---------  death 
        uep.find('.//cell_definition[1]//phenotype//death//model[1]//death_rate').text = str(self.float4.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text = str(self.float5.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text = str(self.float6.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float7.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text = str(self.float8.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//calcification_rate').text = str(self.float9.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//relative_rupture_volume').text = str(self.float10.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//death_rate').text = str(self.float11.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text = str(self.float12.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text = str(self.float13.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float14.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text = str(self.float15.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//calcification_rate').text = str(self.float16.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//relative_rupture_volume').text = str(self.float17.value)
        # ---------  volume 
        uep.find('.//cell_definition[1]//phenotype//volume//total').text = str(self.float18.value)
        uep.find('.//cell_definition[1]//phenotype//volume//fluid_fraction').text = str(self.float19.value)
        uep.find('.//cell_definition[1]//phenotype//volume//nuclear').text = str(self.float20.value)
        uep.find('.//cell_definition[1]//phenotype//volume//fluid_change_rate').text = str(self.float21.value)
        uep.find('.//cell_definition[1]//phenotype//volume//cytoplasmic_biomass_change_rate').text = str(self.float22.value)
        uep.find('.//cell_definition[1]//phenotype//volume//nuclear_biomass_change_rate').text = str(self.float23.value)
        uep.find('.//cell_definition[1]//phenotype//volume//calcified_fraction').text = str(self.float24.value)
        uep.find('.//cell_definition[1]//phenotype//volume//calcification_rate').text = str(self.float25.value)
        uep.find('.//cell_definition[1]//phenotype//volume//relative_rupture_volume').text = str(self.float26.value)
        # ---------  mechanics 
        uep.find('.//cell_definition[1]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float27.value)
        uep.find('.//cell_definition[1]//phenotype//mechanics//cell_cell_repulsion_strength').text = str(self.float28.value)
        uep.find('.//cell_definition[1]//phenotype//mechanics//relative_maximum_adhesion_distance').text = str(self.float29.value)
        uep.find('.//cell_definition[1]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'] = str(self.bool0.value)
        uep.find('.//cell_definition[1]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'] = str(self.bool1.value)
        # ---------  motility 
        uep.find('.//cell_definition[1]//phenotype//motility//speed').text = str(self.float32.value)
        uep.find('.//cell_definition[1]//phenotype//motility//persistence_time').text = str(self.float33.value)
        uep.find('.//cell_definition[1]//phenotype//motility//migration_bias').text = str(self.float34.value)
        uep.find('.//cell_definition[1]//phenotype//motility//options//enabled').text = str(self.bool2.value)
        uep.find('.//cell_definition[1]//phenotype//motility//options//use_2D').text = str(self.bool3.value)
        uep.find('.//cell_definition[1]//phenotype//motility//options//chemotaxis//enabled').text = str(self.bool4.value)
        uep.find('.//cell_definition[1]//phenotype//motility//options//chemotaxis//substrate').text = str(self.chemotaxis_substrate1.value)
        uep.find('.//cell_definition[1]//phenotype//motility//options//chemotaxis//direction').text = str(self.chemotaxis_direction1.value)
        # ---------  secretion 
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[1]').attrib['name'] = str(self.text0.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[1]//secretion_target').text = str(self.float35.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]').attrib['name'] = str(self.text1.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]//secretion_target').text = str(self.float36.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[3]').attrib['name'] = str(self.text2.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[3]//secretion_target').text = str(self.float37.value)
        # ---------  molecular
        # ------------------ cell_definition: immune
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        uep.find('.//cell_definition[2]//phenotype//cycle//phase_transition_rates//rate[1]').text = str(self.float81.value)
        uep.find('.//cell_definition[2]//phenotype//cycle//phase_transition_rates//rate[2]').text = str(self.float82.value)
        uep.find('.//cell_definition[2]//phenotype//cycle//phase_transition_rates//rate[3]').text = str(self.float83.value)
        uep.find('.//cell_definition[2]//phenotype//cycle//phase_transition_rates//rate[4]').text = str(self.float84.value)
        # ---------  death 
        uep.find('.//cell_definition[2]//phenotype//death//model[1]//death_rate').text = str(self.float85.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text = str(self.float86.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text = str(self.float87.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float88.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text = str(self.float89.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//calcification_rate').text = str(self.float90.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//relative_rupture_volume').text = str(self.float91.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[2]//death_rate').text = str(self.float92.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text = str(self.float93.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text = str(self.float94.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float95.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text = str(self.float96.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//calcification_rate').text = str(self.float97.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//relative_rupture_volume').text = str(self.float98.value)
        # ---------  volume 
        uep.find('.//cell_definition[2]//phenotype//volume//total').text = str(self.float99.value)
        uep.find('.//cell_definition[2]//phenotype//volume//fluid_fraction').text = str(self.float100.value)
        uep.find('.//cell_definition[2]//phenotype//volume//nuclear').text = str(self.float101.value)
        uep.find('.//cell_definition[2]//phenotype//volume//fluid_change_rate').text = str(self.float102.value)
        uep.find('.//cell_definition[2]//phenotype//volume//cytoplasmic_biomass_change_rate').text = str(self.float103.value)
        uep.find('.//cell_definition[2]//phenotype//volume//nuclear_biomass_change_rate').text = str(self.float104.value)
        uep.find('.//cell_definition[2]//phenotype//volume//calcified_fraction').text = str(self.float105.value)
        uep.find('.//cell_definition[2]//phenotype//volume//calcification_rate').text = str(self.float106.value)
        uep.find('.//cell_definition[2]//phenotype//volume//relative_rupture_volume').text = str(self.float107.value)
        # ---------  mechanics 
        uep.find('.//cell_definition[2]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float108.value)
        uep.find('.//cell_definition[2]//phenotype//mechanics//cell_cell_repulsion_strength').text = str(self.float109.value)
        uep.find('.//cell_definition[2]//phenotype//mechanics//relative_maximum_adhesion_distance').text = str(self.float110.value)
        uep.find('.//cell_definition[2]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'] = str(self.bool5.value)
        uep.find('.//cell_definition[2]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'] = str(self.bool6.value)
        # ---------  motility 
        uep.find('.//cell_definition[2]//phenotype//motility//speed').text = str(self.float113.value)
        uep.find('.//cell_definition[2]//phenotype//motility//persistence_time').text = str(self.float114.value)
        uep.find('.//cell_definition[2]//phenotype//motility//migration_bias').text = str(self.float115.value)
        uep.find('.//cell_definition[2]//phenotype//motility//options//enabled').text = str(self.bool7.value)
        uep.find('.//cell_definition[2]//phenotype//motility//options//use_2D').text = str(self.bool8.value)
        uep.find('.//cell_definition[2]//phenotype//motility//options//chemotaxis//enabled').text = str(self.bool9.value)
        uep.find('.//cell_definition[2]//phenotype//motility//options//chemotaxis//substrate').text = str(self.chemotaxis_substrate2.value)
        uep.find('.//cell_definition[2]//phenotype//motility//options//chemotaxis//direction').text = str(self.chemotaxis_direction2.value)
        # ---------  secretion 
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[1]').attrib['name'] = str(self.text3.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[1]//secretion_target').text = str(self.float116.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[2]').attrib['name'] = str(self.text4.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[2]//secretion_target').text = str(self.float117.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[3]').attrib['name'] = str(self.text5.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[3]//secretion_target').text = str(self.float118.value)
        # ---------  molecular
        # ------------------ cell_definition: tumor cell
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        uep.find('.//cell_definition[3]//phenotype//cycle//phase_transition_rates//rate[1]').text = str(self.float162.value)
        uep.find('.//cell_definition[3]//phenotype//cycle//phase_transition_rates//rate[2]').text = str(self.float163.value)
        uep.find('.//cell_definition[3]//phenotype//cycle//phase_transition_rates//rate[3]').text = str(self.float164.value)
        uep.find('.//cell_definition[3]//phenotype//cycle//phase_transition_rates//rate[4]').text = str(self.float165.value)
        # ---------  death 
        uep.find('.//cell_definition[3]//phenotype//death//model[1]//death_rate').text = str(self.float166.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text = str(self.float167.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text = str(self.float168.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float169.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text = str(self.float170.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//calcification_rate').text = str(self.float171.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//relative_rupture_volume').text = str(self.float172.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[2]//death_rate').text = str(self.float173.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text = str(self.float174.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text = str(self.float175.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float176.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text = str(self.float177.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//calcification_rate').text = str(self.float178.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//relative_rupture_volume').text = str(self.float179.value)
        # ---------  volume 
        uep.find('.//cell_definition[3]//phenotype//volume//total').text = str(self.float180.value)
        uep.find('.//cell_definition[3]//phenotype//volume//fluid_fraction').text = str(self.float181.value)
        uep.find('.//cell_definition[3]//phenotype//volume//nuclear').text = str(self.float182.value)
        uep.find('.//cell_definition[3]//phenotype//volume//fluid_change_rate').text = str(self.float183.value)
        uep.find('.//cell_definition[3]//phenotype//volume//cytoplasmic_biomass_change_rate').text = str(self.float184.value)
        uep.find('.//cell_definition[3]//phenotype//volume//nuclear_biomass_change_rate').text = str(self.float185.value)
        uep.find('.//cell_definition[3]//phenotype//volume//calcified_fraction').text = str(self.float186.value)
        uep.find('.//cell_definition[3]//phenotype//volume//calcification_rate').text = str(self.float187.value)
        uep.find('.//cell_definition[3]//phenotype//volume//relative_rupture_volume').text = str(self.float188.value)
        # ---------  mechanics 
        uep.find('.//cell_definition[3]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float189.value)
        uep.find('.//cell_definition[3]//phenotype//mechanics//cell_cell_repulsion_strength').text = str(self.float190.value)
        uep.find('.//cell_definition[3]//phenotype//mechanics//relative_maximum_adhesion_distance').text = str(self.float191.value)
        uep.find('.//cell_definition[3]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'] = str(self.bool10.value)
        uep.find('.//cell_definition[3]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'] = str(self.bool11.value)
        # ---------  motility 
        uep.find('.//cell_definition[3]//phenotype//motility//speed').text = str(self.float194.value)
        uep.find('.//cell_definition[3]//phenotype//motility//persistence_time').text = str(self.float195.value)
        uep.find('.//cell_definition[3]//phenotype//motility//migration_bias').text = str(self.float196.value)
        uep.find('.//cell_definition[3]//phenotype//motility//options//enabled').text = str(self.bool12.value)
        uep.find('.//cell_definition[3]//phenotype//motility//options//use_2D').text = str(self.bool13.value)
        uep.find('.//cell_definition[3]//phenotype//motility//options//chemotaxis//enabled').text = str(self.bool14.value)
        uep.find('.//cell_definition[3]//phenotype//motility//options//chemotaxis//substrate').text = str(self.chemotaxis_substrate3.value)
        uep.find('.//cell_definition[3]//phenotype//motility//options//chemotaxis//direction').text = str(self.chemotaxis_direction3.value)
        # ---------  secretion 
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[1]').attrib['name'] = str(self.text6.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[1]//secretion_target').text = str(self.float197.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[2]').attrib['name'] = str(self.text7.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[2]//secretion_target').text = str(self.float198.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[3]').attrib['name'] = str(self.text8.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[3]//secretion_target').text = str(self.float199.value)
        # ---------  molecular
        # ------------------ cell_definition: CD8 Tcell
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        uep.find('.//cell_definition[4]//phenotype//cycle//phase_transition_rates//rate[1]').text = str(self.float243.value)
        uep.find('.//cell_definition[4]//phenotype//cycle//phase_transition_rates//rate[2]').text = str(self.float244.value)
        uep.find('.//cell_definition[4]//phenotype//cycle//phase_transition_rates//rate[3]').text = str(self.float245.value)
        uep.find('.//cell_definition[4]//phenotype//cycle//phase_transition_rates//rate[4]').text = str(self.float246.value)
        # ---------  death 
        uep.find('.//cell_definition[4]//phenotype//death//model[1]//death_rate').text = str(self.float247.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text = str(self.float248.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text = str(self.float249.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float250.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text = str(self.float251.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//calcification_rate').text = str(self.float252.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//relative_rupture_volume').text = str(self.float253.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[2]//death_rate').text = str(self.float254.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text = str(self.float255.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text = str(self.float256.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float257.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text = str(self.float258.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//calcification_rate').text = str(self.float259.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//relative_rupture_volume').text = str(self.float260.value)
        # ---------  volume 
        uep.find('.//cell_definition[4]//phenotype//volume//total').text = str(self.float261.value)
        uep.find('.//cell_definition[4]//phenotype//volume//fluid_fraction').text = str(self.float262.value)
        uep.find('.//cell_definition[4]//phenotype//volume//nuclear').text = str(self.float263.value)
        uep.find('.//cell_definition[4]//phenotype//volume//fluid_change_rate').text = str(self.float264.value)
        uep.find('.//cell_definition[4]//phenotype//volume//cytoplasmic_biomass_change_rate').text = str(self.float265.value)
        uep.find('.//cell_definition[4]//phenotype//volume//nuclear_biomass_change_rate').text = str(self.float266.value)
        uep.find('.//cell_definition[4]//phenotype//volume//calcified_fraction').text = str(self.float267.value)
        uep.find('.//cell_definition[4]//phenotype//volume//calcification_rate').text = str(self.float268.value)
        uep.find('.//cell_definition[4]//phenotype//volume//relative_rupture_volume').text = str(self.float269.value)
        # ---------  mechanics 
        uep.find('.//cell_definition[4]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float270.value)
        uep.find('.//cell_definition[4]//phenotype//mechanics//cell_cell_repulsion_strength').text = str(self.float271.value)
        uep.find('.//cell_definition[4]//phenotype//mechanics//relative_maximum_adhesion_distance').text = str(self.float272.value)
        uep.find('.//cell_definition[4]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'] = str(self.bool15.value)
        uep.find('.//cell_definition[4]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'] = str(self.bool16.value)
        # ---------  motility 
        uep.find('.//cell_definition[4]//phenotype//motility//speed').text = str(self.float275.value)
        uep.find('.//cell_definition[4]//phenotype//motility//persistence_time').text = str(self.float276.value)
        uep.find('.//cell_definition[4]//phenotype//motility//migration_bias').text = str(self.float277.value)
        uep.find('.//cell_definition[4]//phenotype//motility//options//enabled').text = str(self.bool17.value)
        uep.find('.//cell_definition[4]//phenotype//motility//options//use_2D').text = str(self.bool18.value)
        uep.find('.//cell_definition[4]//phenotype//motility//options//chemotaxis//enabled').text = str(self.bool19.value)
        uep.find('.//cell_definition[4]//phenotype//motility//options//chemotaxis//substrate').text = str(self.chemotaxis_substrate4.value)
        uep.find('.//cell_definition[4]//phenotype//motility//options//chemotaxis//direction').text = str(self.chemotaxis_direction4.value)
        # ---------  secretion 
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[1]').attrib['name'] = str(self.text9.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[1]//secretion_target').text = str(self.float278.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[2]').attrib['name'] = str(self.text10.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[2]//secretion_target').text = str(self.float279.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[3]').attrib['name'] = str(self.text11.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[3]//secretion_target').text = str(self.float280.value)
        # ---------  molecular
        # ------------------ cell_definition: macrophage
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        uep.find('.//cell_definition[5]//phenotype//cycle//phase_transition_rates//rate[1]').text = str(self.float324.value)
        uep.find('.//cell_definition[5]//phenotype//cycle//phase_transition_rates//rate[2]').text = str(self.float325.value)
        uep.find('.//cell_definition[5]//phenotype//cycle//phase_transition_rates//rate[3]').text = str(self.float326.value)
        uep.find('.//cell_definition[5]//phenotype//cycle//phase_transition_rates//rate[4]').text = str(self.float327.value)
        # ---------  death 
        uep.find('.//cell_definition[5]//phenotype//death//model[1]//death_rate').text = str(self.float328.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text = str(self.float329.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text = str(self.float330.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float331.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text = str(self.float332.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//calcification_rate').text = str(self.float333.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//relative_rupture_volume').text = str(self.float334.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[2]//death_rate').text = str(self.float335.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text = str(self.float336.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text = str(self.float337.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float338.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text = str(self.float339.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//calcification_rate').text = str(self.float340.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//relative_rupture_volume').text = str(self.float341.value)
        # ---------  volume 
        uep.find('.//cell_definition[5]//phenotype//volume//total').text = str(self.float342.value)
        uep.find('.//cell_definition[5]//phenotype//volume//fluid_fraction').text = str(self.float343.value)
        uep.find('.//cell_definition[5]//phenotype//volume//nuclear').text = str(self.float344.value)
        uep.find('.//cell_definition[5]//phenotype//volume//fluid_change_rate').text = str(self.float345.value)
        uep.find('.//cell_definition[5]//phenotype//volume//cytoplasmic_biomass_change_rate').text = str(self.float346.value)
        uep.find('.//cell_definition[5]//phenotype//volume//nuclear_biomass_change_rate').text = str(self.float347.value)
        uep.find('.//cell_definition[5]//phenotype//volume//calcified_fraction').text = str(self.float348.value)
        uep.find('.//cell_definition[5]//phenotype//volume//calcification_rate').text = str(self.float349.value)
        uep.find('.//cell_definition[5]//phenotype//volume//relative_rupture_volume').text = str(self.float350.value)
        # ---------  mechanics 
        uep.find('.//cell_definition[5]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float351.value)
        uep.find('.//cell_definition[5]//phenotype//mechanics//cell_cell_repulsion_strength').text = str(self.float352.value)
        uep.find('.//cell_definition[5]//phenotype//mechanics//relative_maximum_adhesion_distance').text = str(self.float353.value)
        uep.find('.//cell_definition[5]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'] = str(self.bool20.value)
        uep.find('.//cell_definition[5]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'] = str(self.bool21.value)
        # ---------  motility 
        uep.find('.//cell_definition[5]//phenotype//motility//speed').text = str(self.float356.value)
        uep.find('.//cell_definition[5]//phenotype//motility//persistence_time').text = str(self.float357.value)
        uep.find('.//cell_definition[5]//phenotype//motility//migration_bias').text = str(self.float358.value)
        uep.find('.//cell_definition[5]//phenotype//motility//options//enabled').text = str(self.bool22.value)
        uep.find('.//cell_definition[5]//phenotype//motility//options//use_2D').text = str(self.bool23.value)
        uep.find('.//cell_definition[5]//phenotype//motility//options//chemotaxis//enabled').text = str(self.bool24.value)
        uep.find('.//cell_definition[5]//phenotype//motility//options//chemotaxis//substrate').text = str(self.chemotaxis_substrate5.value)
        uep.find('.//cell_definition[5]//phenotype//motility//options//chemotaxis//direction').text = str(self.chemotaxis_direction5.value)
        # ---------  secretion 
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[1]').attrib['name'] = str(self.text12.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[1]//secretion_target').text = str(self.float359.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[2]').attrib['name'] = str(self.text13.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[2]//secretion_target').text = str(self.float360.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[3]').attrib['name'] = str(self.text14.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[3]//secretion_target').text = str(self.float361.value)
        # ---------  molecular
        # ------------------ cell_definition: DC
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        uep.find('.//cell_definition[6]//phenotype//cycle//phase_transition_rates//rate[1]').text = str(self.float405.value)
        uep.find('.//cell_definition[6]//phenotype//cycle//phase_transition_rates//rate[2]').text = str(self.float406.value)
        uep.find('.//cell_definition[6]//phenotype//cycle//phase_transition_rates//rate[3]').text = str(self.float407.value)
        uep.find('.//cell_definition[6]//phenotype//cycle//phase_transition_rates//rate[4]').text = str(self.float408.value)
        # ---------  death 
        uep.find('.//cell_definition[6]//phenotype//death//model[1]//death_rate').text = str(self.float409.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text = str(self.float410.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text = str(self.float411.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float412.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text = str(self.float413.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//calcification_rate').text = str(self.float414.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//relative_rupture_volume').text = str(self.float415.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[2]//death_rate').text = str(self.float416.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text = str(self.float417.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text = str(self.float418.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float419.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text = str(self.float420.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//calcification_rate').text = str(self.float421.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//relative_rupture_volume').text = str(self.float422.value)
        # ---------  volume 
        uep.find('.//cell_definition[6]//phenotype//volume//total').text = str(self.float423.value)
        uep.find('.//cell_definition[6]//phenotype//volume//fluid_fraction').text = str(self.float424.value)
        uep.find('.//cell_definition[6]//phenotype//volume//nuclear').text = str(self.float425.value)
        uep.find('.//cell_definition[6]//phenotype//volume//fluid_change_rate').text = str(self.float426.value)
        uep.find('.//cell_definition[6]//phenotype//volume//cytoplasmic_biomass_change_rate').text = str(self.float427.value)
        uep.find('.//cell_definition[6]//phenotype//volume//nuclear_biomass_change_rate').text = str(self.float428.value)
        uep.find('.//cell_definition[6]//phenotype//volume//calcified_fraction').text = str(self.float429.value)
        uep.find('.//cell_definition[6]//phenotype//volume//calcification_rate').text = str(self.float430.value)
        uep.find('.//cell_definition[6]//phenotype//volume//relative_rupture_volume').text = str(self.float431.value)
        # ---------  mechanics 
        uep.find('.//cell_definition[6]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float432.value)
        uep.find('.//cell_definition[6]//phenotype//mechanics//cell_cell_repulsion_strength').text = str(self.float433.value)
        uep.find('.//cell_definition[6]//phenotype//mechanics//relative_maximum_adhesion_distance').text = str(self.float434.value)
        uep.find('.//cell_definition[6]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'] = str(self.bool25.value)
        uep.find('.//cell_definition[6]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'] = str(self.bool26.value)
        # ---------  motility 
        uep.find('.//cell_definition[6]//phenotype//motility//speed').text = str(self.float437.value)
        uep.find('.//cell_definition[6]//phenotype//motility//persistence_time').text = str(self.float438.value)
        uep.find('.//cell_definition[6]//phenotype//motility//migration_bias').text = str(self.float439.value)
        uep.find('.//cell_definition[6]//phenotype//motility//options//enabled').text = str(self.bool27.value)
        uep.find('.//cell_definition[6]//phenotype//motility//options//use_2D').text = str(self.bool28.value)
        uep.find('.//cell_definition[6]//phenotype//motility//options//chemotaxis//enabled').text = str(self.bool29.value)
        uep.find('.//cell_definition[6]//phenotype//motility//options//chemotaxis//substrate').text = str(self.chemotaxis_substrate6.value)
        uep.find('.//cell_definition[6]//phenotype//motility//options//chemotaxis//direction').text = str(self.chemotaxis_direction6.value)
        # ---------  secretion 
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[1]').attrib['name'] = str(self.text15.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[1]//secretion_target').text = str(self.float440.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[2]').attrib['name'] = str(self.text16.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[2]//secretion_target').text = str(self.float441.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[3]').attrib['name'] = str(self.text17.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[3]//secretion_target').text = str(self.float442.value)
        # ---------  molecular
        # ------------------ cell_definition: CD4 Tcell
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        uep.find('.//cell_definition[7]//phenotype//cycle//phase_transition_rates//rate[1]').text = str(self.float486.value)
        uep.find('.//cell_definition[7]//phenotype//cycle//phase_transition_rates//rate[2]').text = str(self.float487.value)
        uep.find('.//cell_definition[7]//phenotype//cycle//phase_transition_rates//rate[3]').text = str(self.float488.value)
        uep.find('.//cell_definition[7]//phenotype//cycle//phase_transition_rates//rate[4]').text = str(self.float489.value)
        # ---------  death 
        uep.find('.//cell_definition[7]//phenotype//death//model[1]//death_rate').text = str(self.float490.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text = str(self.float491.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text = str(self.float492.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float493.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text = str(self.float494.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//calcification_rate').text = str(self.float495.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//relative_rupture_volume').text = str(self.float496.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[2]//death_rate').text = str(self.float497.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text = str(self.float498.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text = str(self.float499.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float500.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text = str(self.float501.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//calcification_rate').text = str(self.float502.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//relative_rupture_volume').text = str(self.float503.value)
        # ---------  volume 
        uep.find('.//cell_definition[7]//phenotype//volume//total').text = str(self.float504.value)
        uep.find('.//cell_definition[7]//phenotype//volume//fluid_fraction').text = str(self.float505.value)
        uep.find('.//cell_definition[7]//phenotype//volume//nuclear').text = str(self.float506.value)
        uep.find('.//cell_definition[7]//phenotype//volume//fluid_change_rate').text = str(self.float507.value)
        uep.find('.//cell_definition[7]//phenotype//volume//cytoplasmic_biomass_change_rate').text = str(self.float508.value)
        uep.find('.//cell_definition[7]//phenotype//volume//nuclear_biomass_change_rate').text = str(self.float509.value)
        uep.find('.//cell_definition[7]//phenotype//volume//calcified_fraction').text = str(self.float510.value)
        uep.find('.//cell_definition[7]//phenotype//volume//calcification_rate').text = str(self.float511.value)
        uep.find('.//cell_definition[7]//phenotype//volume//relative_rupture_volume').text = str(self.float512.value)
        # ---------  mechanics 
        uep.find('.//cell_definition[7]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float513.value)
        uep.find('.//cell_definition[7]//phenotype//mechanics//cell_cell_repulsion_strength').text = str(self.float514.value)
        uep.find('.//cell_definition[7]//phenotype//mechanics//relative_maximum_adhesion_distance').text = str(self.float515.value)
        uep.find('.//cell_definition[7]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'] = str(self.bool30.value)
        uep.find('.//cell_definition[7]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'] = str(self.bool31.value)
        # ---------  motility 
        uep.find('.//cell_definition[7]//phenotype//motility//speed').text = str(self.float518.value)
        uep.find('.//cell_definition[7]//phenotype//motility//persistence_time').text = str(self.float519.value)
        uep.find('.//cell_definition[7]//phenotype//motility//migration_bias').text = str(self.float520.value)
        uep.find('.//cell_definition[7]//phenotype//motility//options//enabled').text = str(self.bool32.value)
        uep.find('.//cell_definition[7]//phenotype//motility//options//use_2D').text = str(self.bool33.value)
        uep.find('.//cell_definition[7]//phenotype//motility//options//chemotaxis//enabled').text = str(self.bool34.value)
        uep.find('.//cell_definition[7]//phenotype//motility//options//chemotaxis//substrate').text = str(self.chemotaxis_substrate7.value)
        uep.find('.//cell_definition[7]//phenotype//motility//options//chemotaxis//direction').text = str(self.chemotaxis_direction7.value)
        # ---------  secretion 
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[1]').attrib['name'] = str(self.text18.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[1]//secretion_target').text = str(self.float521.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[2]').attrib['name'] = str(self.text19.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[2]//secretion_target').text = str(self.float522.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[3]').attrib['name'] = str(self.text20.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[3]//secretion_target').text = str(self.float523.value)
        # ---------  molecular
