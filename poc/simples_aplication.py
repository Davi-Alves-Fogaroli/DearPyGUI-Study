# This is simple aplication, i using this code to search some ways to get the best solution and implamentation of 
# the real implamentation i gona do for the engeniar team, here a put almost all logical, don go put the calculon forms
# because thats is propety/"secret" of company

import dearpygui.dearpygui as dpg
 
"""Study '@contextmanager' """

dpg.create_context()

# demo.show_demo()
dpg.create_viewport(title="Test de viabilidade", width=1208, height=800)



with dpg.window(label="Menu de Definição", menubar= False, height=200, width=500):
    with dpg.tab_bar(label="Tab bar", tag="tab_bar"):
        
        with dpg.tab(label="Geometria do projeto", tag="tab_1"):
            pass
          
        with dpg.tab(label="Dados do projeto"):
            name = dpg.add_input_text(label="Name")
            burntime = dpg.add_input_float(label="Burn Time")
            thrust = dpg.add_input_float(label="Thrust")
            totalMass = dpg.add_input_float(label="Total Mass")
            propellantMass = dpg.add_input_float(label="Propellant Mass")
            
            import storege_values as storage
            dpg.add_button(label="Salvar", callback=storage.define_pre_ar, user_data=[name, burntime, thrust, totalMass, propellantMass])
        

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
