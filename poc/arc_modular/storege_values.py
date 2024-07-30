from dearpygui import dearpygui as dpg

trocador_dic = {
    "Name": [],
    "Pre_ar": []
    }


class Pre_ar:
    def __init__(self, burntime, thrust, totalMass, propellantMass):
        self.burntime = burntime
        self.thrust = thrust
        self.totalMass = totalMass
        self.propellantMass = propellantMass

with dpg.window(label="Janela de armazenamento", width=300, height=200, pos=[800, 0], show=False):
    list = dpg.add_listbox(label="Pré ar cadastrados", items=trocador_dic["Name"])


def define_pre_ar(sender, data, user_data): # user_data (list, int[id])
    def comentarios_implesmentações_futuras():
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
    
    print(100*"-",f"\nTrocador, Pre_ar: {trocador_dic["Pre_ar"]}\n")#see what storege
    dpg.configure_item(list, items=trocador_dic["Name"])

# dpg.setup_dearpygui()

