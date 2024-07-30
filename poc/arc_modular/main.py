# This is simple aplication, i using this code to search some ways to get the best solution and implamentation of 
# the real implamentation i gona do for the engeniar team, here a put almost all logical, don go put the calculon forms
# because thats is propety/"secret" of company

import dearpygui.dearpygui as dpg
 
"""Study '@contextmanager' """

dpg.create_context()

# demo.show_demo()
dpg.create_viewport(title="Test de viabilidade", width=1208, height=800)



with dpg.window(label="Calculo pre-ar", menubar= False, height=200, width=500):
    with dpg.tab_bar(label="Tab bar", tag="tab_bar"):
        
        with dpg.tab(label="Trocador inline - Gás fora / Ar dentro", tag="tab_1"):
            name = dpg.add_input_text(label="Nome do componente")

            # ---------TROCADOR INLINE - GÁS FORA/AR DENTRO---------
            diametro_externo = dpg.add_input_float(label="Diâmetro Externo", width=200)
            espessura = dpg.add_input_float(label="Espessura", width=200)

            # import inline_calculo as ic
            # diametro_interno = ic.display()
            # dpg.add_text(f"Diametro interno ={diametro_interno}")

            import inline_calculo as ic
            dpg.add_button(label="Calcular espessura", callback=ic.inline_input, 
                           user_data=[name, diametro_externo, espessura])
      
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
 # ---------FLUIDOS---------
            # vazao_ar = dpg.add_input_float(label="Vazão ar", width=200)
            # temperatura_entrada_ar = dpg.add_input_float(label="Temperatura entrada ar", width=200)
            
            # vazao_gases = dpg.add_input_text(label="Vazão gases", width=200)
            # temperatura_entrada_gases = dpg.add_input_float(label="Temperatura entrada ar", width=200)

            # diametro_interno = diametro_externo -2 * espessura
            # diametro_interno = de - 2 * e

# comprimento = dpg.add_input_float(label="Comprimento", width=200)
            # tubos_transversais = dpg.add_input_float(label="Tubos Transversais", width=200)
            # tubos_longitudinais = dpg.add_input_float(label="Tubos Longitudinais", width=200)
            # # quantidade total tubos = tubos_longitudinais * tubos_transversais
            # # quantidade total tubos = tl *tt

            # passo_transversal_st = dpg.add_input_float(label="Passo Transversal - St", width=200)
            # passo_longitudinal_Sl = dpg.add_input_float(label="Passo Longitudinal - Sl", width=200)
            # # relacao = passo_transversal_st / passo_longitudinal_Sl
            # # relacao = ptst / plsl

            # passes_de_gas = dpg.add_input_float(label="Passes de Gás", width=200)
            # passes_de_ar = dpg.add_input_float(label="Passes de Ar", width=200)

            # """PROVALVELMENTE SERA REALOCADO PARA OUTRA PARTE DO CODIGO FUTURAMENTE"""
            # # fator_foligem = dpg.add_drag_int(label="Fator de Foligem", width=200)
            # """TEM QUE SER UM MENU DE SELEÇÃO E AFETA A O CALCULO QUE SERA FEITO FUTURAMENTE"""
            # # tipo_de_fluxo = dpg.add_input_text(label="tipo_de_fluxo", width=200)

            # """"""
            # # superficie de troca = PI()*E13/1000*E16/1000*(E18*E17) 
            # # 