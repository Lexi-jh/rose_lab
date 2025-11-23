from nicegui import binding, events, ui

class path_gui:
    def __init__(self):
        # state variables
        canvas_dim = 1000
        # for line graph
        line_space = canvas_dim/9
        line_width = 10
        start_pos = 0
        self.points = []
        # constrain area var
        self.draw_mode = False
        self.boundaries = False
        # path gen mode
        self.path_mode = 'Trajectory Planner'


        with ui.row():
            self.canvas_graph = ui.interactive_image(size=(canvas_dim,canvas_dim), on_mouse=self.canvas_click, events=['click']).classes('w-64 bg-blue-50')
            with ui.column():
                self.constrain_button = ui.toggle(['Static', 'Draw'], value = 'Static', on_change= self.draw_mode_click)
                with ui.row():
                    mode_text = ui.markdown('Mode:')
                    self.mode_toggle = ui.select(['Trajectory Planner', 'Follower'], value='Trajectory Planner', on_change= self.path_mode_click)
                # with ui.column().bind_visibility_from(self.mode_toggle, 'value'):
                #     self.boundaries = ui.button('Constrain Area', on_click=self.constrain_click())
                    



        # make graph lines
        for i in range(10):
            # x lines
            self.canvas_graph.content += f'''<line x1="{start_pos}" y1="{0}" x2="{start_pos}" y2="{canvas_dim}" stroke="black" width="{line_width}"/>'''
            # y lines
            self.canvas_graph.content += f'''<line x1="{0}" y1="{start_pos}" x2="{canvas_dim}" y2="{start_pos}" stroke="black" width="{line_width}"/>'''
            start_pos += line_space



        ui.run()

    def canvas_click(self, e: events.MouseEventArguments):
        if self.draw_mode:
            click_x, click_y = e.image_x, e.image_y
            self.canvas_graph.content += f'<circle cx="{click_x}" cy="{click_y}" r="15" fill="none" stroke="SkyBlue" stroke-width = "4" />'
            self.points.append((click_x, click_y))

    def draw_mode_click(self, e: events.ClickEventArguments):
        if self.constrain_button.value == 'Draw':
            self.draw_mode = True
        elif self.constrain_button.value == 'Static':
            self.draw_mode = False

    def path_mode_click(self, e:events.ClickEventArguments):
        self.path_mode = self.mode_toggle.value

    # def constrain_click(self, e:events.ClickEventArguments):
    #     print(1)
        


        


    
x = path_gui()