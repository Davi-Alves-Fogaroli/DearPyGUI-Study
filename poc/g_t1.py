import dearpygui.dearpygui as dpg
import g_t2 as storege

dpg.create_context()

# Create a viewport
dpg.create_viewport(title="Test de viabilidade", width=1208, height=800)

# Pre_ar class definition
class Pre_ar:
    def __init__(self, burntime, thrust, totalMass, propellantMass):
        self.burntime = burntime
        self.thrust = thrust
        self.totalMass = totalMass
        self.propellantMass = propellantMass

# First window for input
with dpg.window(label="Define Pre_ar", height=200, width=500):
    name = dpg.add_input_text(label="Name")
    burntime = dpg.add_input_float(label="Burn Time")
    thrust = dpg.add_input_float(label="Thrust")
    totalMass = dpg.add_input_float(label="Total Mass")
    propellantMass = dpg.add_input_float(label="Propellant Mass")
    dpg.add_button(label="Save", callback=lambda: storege.define_pre_ar(name, burntime, thrust, totalMass, propellantMass))

# Global variable for the listbox
global PRE_AR_LIST_G
with dpg.window(label="Lista dos pré ar cadastrados", height=200, width=300, pos=[500, 0]):
    PRE_AR_LIST_G = dpg.add_listbox(items=storege.trocador_dic["Name"], label="Pré ar cadastrados")

# Setup Dear PyGui
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()