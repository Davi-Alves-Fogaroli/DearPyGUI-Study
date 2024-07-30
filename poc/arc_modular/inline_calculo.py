import dearpygui.dearpygui as dpg

# -----------------------------------------------------------------------------------------------------------
#  ESCOLHER FORMATO DE ARMAZENAMENTO PARA QUE A FUNÇÃO DPG.CONFIGURE_ITEM(ITENS=) CONSIGA ACESSAR OS DADOS
#  E DEIXAR FACIL DE ACESSAR NA HORA DE ESCOLHER A ORDEM DO CALCULO
# -----------------------------------------------------------------------------------------------------------
trocador_inline_dict = [
        {"name": []},
        {"diametro_externo" : []},
        {"espessura" : []},
        {"diametro_interno" : []},
    ]

# class inline: 
#     def __init__(self, diametro_externo, espessura):
#         self.diametro_externo = diametro_externo
#         self.espessura = espessura

with dpg.window(label="listboc", width=300, height=200, pos=[500, 0], show=False):
   list_pre_ar = dpg.add_listbox(label="Resultados", items=trocador_inline_dict, width=300)

def inline_input(sender, data, user_data):
    trocador_inline_dict[0]["name"].append(dpg.get_value(user_data[0]))
    trocador_inline_dict[1]["diametro_externo"].append(dpg.get_value(user_data[1]))
    trocador_inline_dict[2]["espessura"].append(dpg.get_value(user_data[2]))
    
    diametro_interno_retornado = inline_calculo(user_data)
    trocador_inline_dict[3]["diametro_interno"].append(diametro_interno_retornado)
    dpg.configure_item(list_pre_ar, items=trocador_inline_dict)

    

def inline_calculo(user_data):
    def comentarios_implesmentações_futuras():
    # count = 0
    # """-----implementar verificação de nome nullo e repetido 'user_data[0]'-----"""
    # print(type(user_data[0]), "\n")#see what return
    # for i in user_data:
    #     print(f"User_dada idenx: {count}, value: ",dpg.get_value(user_data[count])) #float problem "0.20000000298023224"
    #     count += 1
        pass

    # acesse data using user_data[index] because if you acesse using key, value you get list type not a float type, and code will break
    de = dpg.get_value(user_data[1])
    esp = dpg.get_value(user_data[2])
    diamtro_interno = (de - 2) * (esp)

    return diamtro_interno
    
# def display():
#     diametro_interno = trocador_inline_dict[3]["diametro_interno"]
#     dpg.configure_item(list_pre_ar, items=trocador_inline_dict)
#     a = dpg.add_text(f"Diametro interno = {diametro_interno}")
#     return a    
