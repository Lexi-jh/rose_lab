from nicegui import events, ui

class path_gui:
    def __init__(self):
        self.graph_src='https://1drv.ms/i/c/c260df72ec4fef22/EfQARmtZoJ9CjMdDGs6lS5sBFDwg-GVxXPM_MnoTbhGtsA?e=xzQ8t4'
        self.interactive_graph = ui.interactive_image(self.graph_src, on_mouse=self.graph_click, events = ['click'])
        ui.run()

    def graph_click(self, e: events.MouseEventArguments):
        self.interactive_graph.content += f'<circle cx="{e.image_x}" cy={e.image_y}" r="15" fill="none stroke="SkyBlue" stroke-width = "4" />'
    
x = path_gui()