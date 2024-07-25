from dearpygui import dearpygui as dpg

trocador_dic = {
    "Fluidos" : {
        "Vazão" : {
            "Gases": None, #na planilha excel: porque esses valores são calculados ao inves de inseridos diretamente ?
            "Ar": None, #na planilha excel: porque esses valores são calculados ao inves de inseridos diretamente ?
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

with dpg.window(label="Janela de armazenamento", height=200, width=300, pos=[500, 0], show=False):
    PRE_AR_LIST_G = dpg.add_listbox(items=trocador_dic["Name"], label="Pré ar cadastrados")


def define_pre_ar(sender, data, user_data): # user_data (list, int[id])
    def prints():
    # count = 0
    # """-----implementar verificação de nome nullo e repetido 'user_data[0]'-----"""
    # print(type(user_data[0]), "\n")#see what return
    # for i in user_data:
    #     print(f"User_dada idenx: {count}, value: ",dpg.get_value(user_data[count])) #float problem "0.20000000298023224"
    #     count += 1
        pass
    trocador_dic["Name"].append(dpg.get_value(user_data[0]))
    trocador_dic["Pre_ar"].append(Pre_ar(
        dpg.get_value(user_data[1]),
        dpg.get_value(user_data[2]),
        dpg.get_value(user_data[3]),
        dpg.get_value(user_data[4]),
        ))
    
    print(f"\nTrocador, Pre_ar: {trocador_dic["Pre_ar"]}\n")#see what storege
    dpg.configure_item(PRE_AR_LIST_G, items=trocador_dic["Name"])

# dpg.setup_dearpygui()

