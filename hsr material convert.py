import tkinter as tk
from tkinter import ttk

# Thank you to Cursor for writing the entire code!
# Created by: Cursor AI
# Idea from: Icebro Ice
# A simple material conversion calculator for Honkai: Star Rail
# rights reserved to official Honkai: Star Rail Hoyoverse
def create_conversion_window():
    window = tk.Tk()
    window.title("Material Conversion Calculator")
    window.geometry("1600x800")  # Doubled initial size
    
    # Theme variables and colors
    theme_mode = tk.StringVar(value="dark")  # Default to dark mode
    
    themes = {
        "light": {
            "bg": "#ffffff",
            "frame_bg": "#f0f0f0", 
            "text": "black",
            "entry_bg": "white",
            "entry_fg": "black",
            "tab_bg": "#e0e0e0",
            "tab_selected": "#f0f0f0",
            "button_colors": {
                "green": {"bg": "#32CD32", "fg": "black", "text": "Green", "activebackground": "#2eb82e"},
                "blue": {"bg": "#87CEEB", "fg": "black", "text": "Blue", "activebackground": "#75bcd6"},
                "purple": {"bg": "#9370DB", "fg": "black", "text": "Purple", "activebackground": "#8560c5"},
                "jade": {"bg": "#00A86B", "fg": "black", "text": "Jade", "activebackground": "#008B5C"},
                "pass": {"bg": "#FFC300", "fg": "black", "text": "Pass", "activebackground": "#E6B000"}
            }
        },
        "dark": {
            "bg": "#1a1a1a",
            "frame_bg": "#1a1a1a",
            "text": "white", 
            "entry_bg": "black",  # Black entry boxes in dark mode
            "entry_fg": "white",  # White text in dark mode
            "tab_bg": "#2d2d2d",
            "tab_selected": "#3d3d3d",
            "button_colors": {
                "green": {"bg": "#1a5c1a", "fg": "white", "text": "Green", "activebackground": "#236b23"},
                "blue": {"bg": "#1a4b6b", "fg": "white", "text": "Blue", "activebackground": "#235b7b"},
                "purple": {"bg": "#4a1a6b", "fg": "white", "text": "Purple", "activebackground": "#5b237b"},
                "jade": {"bg": "#006644", "fg": "white", "text": "Jade", "activebackground": "#005533"},
                "pass": {"bg": "#997300", "fg": "white", "text": "Pass", "activebackground": "#806000"}
            }
        }
    }

    def update_theme(*args):
        current_theme = themes[theme_mode.get()]
        
        # Update window and frame backgrounds
        window.configure(bg=current_theme["bg"])
        conversion_frame.configure(style='Current.TFrame')
        full_list_frame.configure(style='Current.TFrame')
        
        # Update styles
        style.configure('Current.TFrame', background=current_theme["frame_bg"])
        style.configure('Large.TLabel', background=current_theme["frame_bg"], foreground=current_theme["text"])
        style.configure('TNotebook', background=current_theme["bg"])
        style.configure('TNotebook.Tab', background=current_theme["tab_bg"], foreground=current_theme["text"])
        style.map('TNotebook.Tab', background=[('selected', current_theme["tab_selected"])])
        
        # Update entry fields
        for entry in [amount_entry, purple_entry, blue_entry, green_entry, jade_entry, pass_entry]:
            entry.configure(foreground=current_theme["entry_fg"], background=current_theme["entry_bg"])
            
        # Update color buttons
        for color in ["green", "blue", "purple", "jade", "pass"]:
            button_colors = current_theme["button_colors"][color]
            if color in from_buttons:
                from_buttons[color].configure(**button_colors)
            if color in to_buttons:
                to_buttons[color].configure(**button_colors)

    # Configure grid weights to allow scaling
    window.grid_columnconfigure(0, weight=1)
    window.grid_rowconfigure(0, weight=1)

    # Create styles
    style = ttk.Style()
    style.configure('Large.TLabel', font=('Helvetica', 12))
    style.configure('Large.TButton', font=('Helvetica', 12))
    style.configure('Current.TFrame')

    # Create notebook for multiple pages
    notebook = ttk.Notebook(window)
    notebook.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Create frames for each page
    conversion_frame = ttk.Frame(notebook, padding="20", style='Current.TFrame')
    full_list_frame = ttk.Frame(notebook, padding="20", style='Current.TFrame')

    # Add frames to notebook
    notebook.add(conversion_frame, text="Conversion")
    notebook.add(full_list_frame, text="Full List")
    
    # Add theme toggle button
    def toggle_theme():
        new_theme = "light" if theme_mode.get() == "dark" else "dark"
        theme_mode.set(new_theme)
        
    theme_btn = ttk.Button(window, text="Toggle Theme", command=toggle_theme)
    theme_btn.grid(row=1, column=0, pady=10)
    
    # Configure frame grid weights
    conversion_frame.grid_columnconfigure(1, weight=1)
    conversion_frame.grid_columnconfigure(2, weight=1)
    conversion_frame.grid_columnconfigure(4, weight=1)
    
    ttk.Label(conversion_frame, text="Amount:", style='Large.TLabel').grid(row=0, column=0, padx=10, pady=20)
    amount_entry = tk.Entry(conversion_frame, width=20, font=('Helvetica', 12))  # Changed to tk.Entry
    amount_entry.grid(row=0, column=1, padx=10, pady=20, sticky=(tk.W, tk.E))

    # Create button frames
    from_frame = ttk.Frame(conversion_frame, style='Current.TFrame')
    from_frame.grid(row=0, column=2, padx=10, pady=20)
    
    ttk.Label(conversion_frame, text="to", style='Large.TLabel').grid(row=0, column=3, padx=10, pady=20)
    
    to_frame = ttk.Frame(conversion_frame, style='Current.TFrame')
    to_frame.grid(row=0, column=4, padx=10, pady=20)

    # Variables to track selected buttons
    from_selected = tk.StringVar(value="jade")  # Default to jade
    to_selected = tk.StringVar(value="pass")    # Default to pass

    # Store button references
    from_buttons = {}
    to_buttons = {}

    def create_color_button(parent, color, var, other_var, is_from, button_dict):
        def on_click():
            if var.get() == color:
                return
            var.set(color)

        btn = tk.Button(parent, width=10, height=2)
        
        def update_state(*args):
            btn.configure(
                relief="sunken" if var.get() == color else "raised",
                borderwidth=5 if var.get() == color else 2
            )

        var.trace('w', update_state)
        other_var.trace('w', update_state)
        
        btn.configure(command=on_click)
        button_dict[color] = btn
        return btn

    # Create color buttons for both sides
    colors = ["green", "blue", "purple", "jade", "pass"]
    for i, color in enumerate(colors):
        from_btn = create_color_button(from_frame, color, from_selected, to_selected, True, from_buttons)
        from_btn.grid(row=0, column=i, padx=2)
        
        to_btn = create_color_button(to_frame, color, to_selected, from_selected, False, to_buttons)
        to_btn.grid(row=0, column=i, padx=2)
        
        # Set initial button states
        from_btn.configure(relief="sunken", borderwidth=5) if color == "jade" else None
        to_btn.configure(relief="sunken", borderwidth=5) if color == "pass" else None

    # Result display for conversion page
    result_var = tk.StringVar()
    result_label = ttk.Label(conversion_frame, textvariable=result_var, style='Large.TLabel', wraplength=700)
    result_label.grid(row=1, column=0, columnspan=5, pady=20)

    # Full List page content
    for i in range(8):
        full_list_frame.grid_columnconfigure(i, weight=1)

    # Input section for full list
    ttk.Label(full_list_frame, text="Input:", style='Large.TLabel').grid(row=0, column=0, columnspan=8, padx=10, pady=20)
    
    # Purple input
    ttk.Label(full_list_frame, text="Purple:", style='Large.TLabel').grid(row=1, column=0, padx=5, pady=5)
    purple_entry = tk.Entry(full_list_frame, width=10, font=('Helvetica', 12))  # Changed to tk.Entry
    purple_entry.grid(row=1, column=1, padx=5, pady=5)
    
    # Blue input
    ttk.Label(full_list_frame, text="Blue:", style='Large.TLabel').grid(row=1, column=2, padx=5, pady=5)
    blue_entry = tk.Entry(full_list_frame, width=10, font=('Helvetica', 12))  # Changed to tk.Entry
    blue_entry.grid(row=1, column=3, padx=5, pady=5)
    
    # Green input
    ttk.Label(full_list_frame, text="Green:", style='Large.TLabel').grid(row=1, column=4, padx=5, pady=5)
    green_entry = tk.Entry(full_list_frame, width=10, font=('Helvetica', 12))  # Changed to tk.Entry
    green_entry.grid(row=1, column=5, padx=5, pady=5)
    
    # Jade input
    ttk.Label(full_list_frame, text="Jades:", style='Large.TLabel').grid(row=1, column=6, padx=5, pady=5)
    jade_entry = tk.Entry(full_list_frame, width=10, font=('Helvetica', 12))  # Changed to tk.Entry
    jade_entry.grid(row=1, column=7, padx=5, pady=5)
    
    # Pass input
    ttk.Label(full_list_frame, text="Passes:", style='Large.TLabel').grid(row=2, column=0, padx=5, pady=5)
    pass_entry = tk.Entry(full_list_frame, width=10, font=('Helvetica', 12))  # Changed to tk.Entry
    pass_entry.grid(row=2, column=1, padx=5, pady=5)

    # Result display for full list
    full_list_result_var = tk.StringVar()
    full_list_result_var.set("Converted to: 0 Purple 0 Blue 0 Green 0 Jade 0 Pass")
    full_list_result_label = ttk.Label(full_list_frame, textvariable=full_list_result_var, style='Large.TLabel', wraplength=700)
    full_list_result_label.grid(row=4, column=0, columnspan=8, pady=20)

    def convert():
        try:
            missing_selection = not from_selected.get() or not to_selected.get()
            
            if missing_selection:
                result_var.set("Please select both conversion units") 
                return
                
            amount = int(float(amount_entry.get()))
            from_unit_val = from_selected.get()
            to_unit_val = to_selected.get()
            
            to_green = {
                "green": 1,
                "blue": 3,
                "purple": 9,
                "jade": 1,
                "pass": 160
            }
            
            green_amount = amount * to_green[from_unit_val]
            
            result_text = f"{amount} {from_unit_val} = "
            remaining = int(green_amount)
            
            units = ["purple", "blue", "green", "jade", "pass"]
            conversions = {"purple": 9, "blue": 3, "green": 1, "jade": 1, "pass": 160}
            
            target_index = units.index(to_unit_val)
            for unit in units[target_index:]:
                unit_count = remaining // conversions[unit]
                result_text += f"{int(unit_count)} {unit} " if unit_count > 0 else ""
                remaining = remaining % conversions[unit]
            
            result_var.set(result_text.strip())
            
        except ValueError:
            result_var.set("Please enter a valid number")

    def convert_full_list():
        try:
            purple = int(purple_entry.get()) if purple_entry.get() else 0
            blue = int(blue_entry.get()) if blue_entry.get() else 0
            green = int(green_entry.get()) if green_entry.get() else 0
            jade = int(jade_entry.get()) if jade_entry.get() else 0
            passes = int(pass_entry.get()) if pass_entry.get() else 0
            
            total_green = (purple * 9) + (blue * 3) + green
            
            result_purple = total_green // 9
            remaining = total_green % 9
            
            result_blue = remaining // 3
            remaining = remaining % 3
            
            result_green = remaining
            
            result_jade = jade
            
            result_pass = passes
            
            result_text = f"Converted to: {result_purple} Purple {result_blue} Blue {result_green} Green {result_jade} Jades {result_pass} Passes"
                
            full_list_result_var.set(result_text.strip())
            
        except ValueError:
            full_list_result_var.set("Please enter valid numbers")

    # Convert buttons
    convert_btn = ttk.Button(conversion_frame, text="Convert", command=convert, style='Large.TButton')
    convert_btn.grid(row=2, column=0, columnspan=5, pady=20, ipadx=20, ipady=10)

    full_list_convert_btn = ttk.Button(full_list_frame, text="Convert", command=convert_full_list, style='Large.TButton')
    full_list_convert_btn.grid(row=3, column=0, columnspan=8, pady=20, ipadx=20, ipady=10)

    # Bind Enter key to convert functions based on active tab
    def handle_return(event):
        current_tab = notebook.select()
        tab_index = notebook.index(current_tab)
        convert() if tab_index == 0 else convert_full_list()

    window.bind('<Return>', handle_return)
    
    # Bind 't' key to toggle theme
    window.bind('t', lambda event: toggle_theme())
    
    # Set initial theme
    theme_mode.trace('w', update_theme)
    update_theme()

    window.mainloop()

if __name__ == "__main__":
    create_conversion_window()
