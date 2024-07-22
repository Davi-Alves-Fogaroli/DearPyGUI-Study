import dearpygui.dearpygui as dpg

dpg.create_context()
def registro_de_cliques(sender, app_data, user_data):
    v=0 
    with dpg.window(label=f"{sender}"):       
        dpg.set_value("button", 1)
        valor = user_data
        v = v+1
        print(f"valor: {valor}, tipo {type(valor)}")
        dpg.add_text(f"sender: {sender} \napp_data: {app_data} \nuser_data: {v}\n") 

with dpg.window():
    dpg.add_button(label="Clica em min", user_data="1", tag="button")
    
    with dpg.item_handler_registry(tag="clicavel") as my_handler:
        dpg.add_item_clicked_handler(callback=registro_de_cliques)
    
    dpg.bind_item_handler_registry("button", "clicavel")
    

dpg.create_viewport(title="Teste de criação de conteiners com parentes, context managers", width=200, height=100)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()