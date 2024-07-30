# This is simple aplication, i using this code to search some ways to get the best solution and implamentation of 
# the real implamentation i gona do for the engeniar team, here a put almost all logical, don go put the calculon forms
# because thats is propety/"secret" of company

import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

"""Study '@contextmanager' """

dpg.create_context()

demo.show_demo()
dpg.create_viewport(title="Test de viabilidade", width=1208, height=800)


trocador_dic = {
    "Fluidos" : {
        "Vazão" : {
            "Gases": None, #porque esses valores são calculados ao inves de inseridos diretamente ?
            "Ar": None, #porque esses valores são calculados ao inves de inseridos diretamente ?
        },
        "Temperatura Entrada": {
            "Gases": None,
            "Ar": None,
        },
    },
    "Name": [],
    "Pre_ar": []
    }


class Pre_ar:
    def __init__(self, burntime, thrust, totalMass, propellantMass):
        self.burntime = burntime
        self.thrust = thrust
        self.totalMass = totalMass
        self.propellantMass = propellantMass


def define_pre_ar(sender, data, user_data):
    #see what return
    count = 0
    print(user_data, "\n")
    for i in user_data:
        print(f"User_dada idenx: {count}, value: ",dpg.get_value(user_data[count])) #float problem "0.20000000298023224"
        count += 1

    trocador_dic["Name"].append(dpg.get_value(user_data[0]))
    trocador_dic["Pre_ar"].append(Pre_ar(
        dpg.get_value(user_data[1]),
        dpg.get_value(user_data[2]),
        dpg.get_value(user_data[3]),
        dpg.get_value(user_data[4]),
        ))
    #see what storege
    print(f"\nTrocador, Pre_ar: {trocador_dic["Pre_ar"]}\n")
    dpg.configure_item(pre_ar, items=trocador_dic["Name"])
    # dpg.configure_item(pre_ar, items=trocador_dic["Pre_ar"])


with dpg.window(label="Define Pre_ar", height=200, width=500):

    name = dpg.add_input_text(label="Name")
    burntime = dpg.add_input_float(label="Burn Time")
    thrust = dpg.add_input_float(label="Thrust")
    totalMass = dpg.add_input_float(label="Total Mass")
    propellantMass = dpg.add_input_float(label="Propellant Mass")
    dpg.add_button(label="Save", callback=define_pre_ar, user_data=[name, burntime, thrust, totalMass, propellantMass])


with dpg.window(label="Lista dos pré ar cadastrados", height=200, width=300, pos=[500, 0]):
    pre_ar = dpg.add_listbox(items=trocador_dic["Name"], label="Pré ar cadastrados")
    

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
