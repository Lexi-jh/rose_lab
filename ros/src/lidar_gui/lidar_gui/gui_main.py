import tkinter as tk 

xpoint = 500
ROWS, COLS = 10, 10
SIZE = 40  # spacing between grid lines

class TrajGui:
    def __init__(self):
        #state variables
        self.points = []
        self.drawing = False

        ################# make background
        self.root = tk.Tk()
        self.root.title("Interactive Grid")
        self.root.configure(bg="white")
        #make the window size reasonable
        self.root.geometry("1000x700")

        ################### make grid
        self.canvas = tk.Canvas(self.root, width=COLS*SIZE, height=ROWS*SIZE, bg="white")
        # canvas.place(x=-80, y=0, anchor="sw")
        # draw grid lines
        for i in range(ROWS):
            self.canvas.create_line(0, i*SIZE, COLS*SIZE, i*SIZE, fill="lightgray")
        for j in range(COLS):
            self.canvas.create_line(j*SIZE, 0, j*SIZE, ROWS*SIZE, fill="lightgray")

        # bind mouse clicks
        self.canvas.bind("<Button-1>", self.on_click)
        #place grid canvas where i want it, centered vertically
        self.canvas.place(x=20, y=20, anchor="nw")

        ##################### make constrain area button
        self.area_button = tk.Button(self.root, text="CONSTRAIN AREA", command = self.constrain_area, bg="lightblue")
        self.area_button.place(x=xpoint, y=20, anchor="nw")

        #################### make starting, ending point entries
        starty = 70
        width_entry = 5
        endy = 110
        #start point label
        start_label = tk.Label(self.root, text="Start Point -> ", bg="white")
        start_label.place(x = xpoint, y = starty, anchor="nw")
        # x label
        xs_label = tk.Label(self.root, text="X: ", bg="white")
        xs_label.place(x = xpoint+90, y = starty, anchor="nw")
        #start x entry box
        self.start_entryx = tk.Entry(self.root, width=width_entry)
        self.start_entryx.place(x = xpoint+110, y = starty, anchor="nw" )
        self.start_entryx.insert(0, 1) #initial val
        #start y label
        ys_label = tk.Label(self.root, text="Y: ", bg="white")
        ys_label.place(x = xpoint+110+width_entry+30, y = starty, anchor="nw")
        #start y entry box
        self.start_entryy = tk.Entry(self.root, width=width_entry)
        self.start_entryy.place(x = xpoint+110+width_entry+30+20, y = starty, anchor="nw" )
        self.start_entryy.insert(0, 1) #initial val

        #end point label
        end_label = tk.Label(self.root, text="End Point -> ", bg="white")
        end_label.place(x = xpoint, y = endy, anchor="nw")
        # X label
        xe_label = tk.Label(self.root, text="X: ", bg="white")
        xe_label.place(x = xpoint+90, y = endy, anchor="nw")
        # end x box
        self.end_entryx = tk.Entry(self.root, width=width_entry)
        self.end_entryx.place(x = xpoint+110, y = endy, anchor="nw" )
        self.end_entryx.insert(0, 9)
        #end y label
        ye_label = tk.Label(self.root, text="Y: ", bg="white")
        ye_label.place(x = xpoint+110+width_entry+30, y = endy, anchor="nw")
        #end y entry box
        self.end_entryy = tk.Entry(self.root, width=width_entry)
        self.end_entryy.place(x = xpoint+110+width_entry+30+20, y = endy, anchor="nw" )
        self.end_entryy.insert(0, 9)

        ########################## Drop down menu to choose trajectory type
        #holds selectde trajectory
        self.traj_selected = tk.StringVar(value="Raster") #defaults to rastor
        #dropdown
        self.dropdown = tk.OptionMenu(self.root, self.traj_selected, "Raster", "S-curve", "Corner Spiral", "Swirly Spiral")
        self.dropdown.place(x = xpoint, y = 155, anchor="nw")

        ########################## Drop down menu to choose trajectory mode
        #holds selected mode
        self.mode_selected = tk.StringVar(value="Trajectory") 
        #dropdown
        self.dropdown = tk.OptionMenu(self.root, self.mode_selected, "Trajectory", "GOTO")
        self.dropdown.place(x = xpoint+110, y = 155, anchor="nw")

        ######################## smoothness slider
        #label
        smooth_label = tk.Label(self.root, text="Smoothness (number of points)", bg="white")
        smooth_label.place(x = xpoint, y = 195, anchor="nw")
        #slider
        self.slider = tk.Scale(self.root, from_=0, to=100, orient="horizontal", length=170, command=self.change_number_text)
        self.slider.place(x=xpoint, y = 220, anchor="nw")
        self.slider.set(50) #initial valus is 50
        # number of points text that will auto update
        self.num_points = tk.Label(self.root, text="Number of points: ", bg="white")
        self.num_points.place(x=xpoint, y = 260, anchor="nw")

        ########################## width number input
        #label
        width_label = tk.Label(self.root, text="Distance between passes in meters:", bg="white")
        width_label.place(x = xpoint, y = 285, anchor="nw")
        #actual box
        self.width_box = tk.Spinbox(self.root, from_=0, to=10, increment=.1)
        self.width_box.place(x=xpoint, y = 310, anchor="nw")
        self.width_box.delete(0, "end")
        self.width_box.insert(0, 1)

        ############################# generate path button
        self.generate_button = tk.Button(self.root, text="GENERATE PATH", command = self.generate_path, bg="lightblue")
        self.generate_button.place(x=xpoint, y=350, anchor="nw")

        ############################ upload path button
        self.upload_button = tk.Button(self.root, text="UPLOAD PATH", command = self.upload_path, bg="lightblue")
        self.upload_button.place(x=xpoint, y=385, anchor="nw")


    def constrain_area(self):
        self.drawing = not self.drawing
        print("constrain area button clicked, nice job dipshit")

    def on_click(self, event):
        if not self.drawing:
            return
        # snap click to nearest grid intersection
        row = round(event.y / SIZE)
        col = round(event.x / SIZE)
        x, y = col * SIZE, row * SIZE

        if self.points:
            if (x, y) in self.points:
                if (x, y) == self.points[0]: #if point equals first point, boundary created
                    print("boundary created")
                    x_prev, y_prev = self.points[-1]
                    self.canvas.create_line(x_prev, y_prev, x, y, fill="blue", width=2, tags="drawn")
                    self.points.append((x,y)) #bc fields2cover expects a ring
                    self.drawing = False
                    return
                else: #if any other point made, boundary creation error, clear all
                    print("invalid boundary created")
                    self.points = []
                    self.canvas.delete("drawn")
                    return
            else: #if not already in self.points, continue as normal
                #draw new point
                self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="green", tags="drawn")
                #create line with previous point
                x_prev, y_prev = self.points[-1]
                self.canvas.create_line(x_prev, y_prev, x, y, fill="blue", width=2, tags="drawn")
                self.points.append((x, y))
        else: #create first point
            #create point
            self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="green", tags="drawn")
            self.points.append((x, y))
                


    def change_number_text(self,val): #will change number of points text under slider
        if int(val) > 50:
            self.num_points.config(text=f"Number of points: {val}")

    def generate_path(self): #display path
        print("generate path button clicked")

    def upload_path(self):
        print("upload button pressed")
 
gui = TrajGui()
gui.root.mainloop()
