import tkinter as tk
import psycopg2
import messagebox

def clear_window(root):
    for widget in root.winfo_children():
        widget.destroy()

def look_at_data_options():
    clear_window(root)
    look_at_data_text = tk.Label(root, text="What data do you want to look at?")
    look_at_data_text.pack()

    yarn_button = tk.Button(root, text="Yarn", command=yarn_options)
    yarn_button.pack()

    safety_eyes_button = tk.Button(root, text="Safety Eyes", command=safety_eyes_options)
    safety_eyes_button.pack()

    stuffing_button = tk.Button(root, text="Stuffing", command=stuffing_options)
    stuffing_button.pack()

    products_button = tk.Button(root, text="Products", command=products_options)
    products_button.pack()

def yarn_options():
    clear_window(root)
    yarn_text = tk.Label(root, text="What data from Yarn do you want to see?")
    yarn_text.pack()

    yarn_brands_button = tk.Button(root, text="Brands", command=yarn_brands)
    yarn_brands_button.pack()

    yarn_colors_button = tk.Button(root, text="Colors", command=yarn_colors)
    yarn_colors_button.pack()

    fiber_types_button = tk.Button(root, text="Fiber Types", command=fiber_types)
    fiber_types_button.pack()

    fiber_weights_button = tk.Button(root, text="Fiber Weights", command=fiber_weights)
    fiber_weights_button.pack()

    yarn_by_prices_button = tk.Button(root, text="Yarn by Prices",
                                               command=yarn_by_prices)
    yarn_by_prices_button.pack()

    yarn_by_yardage_button = tk.Button(root, text="Yarn by Yardage/Skein",
                                                 command=yarn_by_yardage)
    yarn_by_yardage_button.pack()

    yarn_by_grams_button = tk.Button(root, text="Yarn by Grams/Skein",
                                                command=yarn_by_grams)
    yarn_by_grams_button.pack()

    yarn_by_num_in_stock_button = tk.Button(root, text="Yarn by Number in Stock",
                                              command=yarn_by_num_in_stock)
    yarn_by_num_in_stock_button.pack()

def yarn_brands():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT brand FROM Yarn ORDER BY brand")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Define headers
    headers = ["Brand"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"))
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        brand_label = tk.Label(frame, text=row[0])
        brand_label.grid(row=idx, column=0, padx=5, pady=5)

def yarn_colors():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT color FROM Yarn ORDER BY color")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Define headers
    headers = ["Color"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"))
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value)
            data_label.grid(row=idx, column=i, padx=5, pady=5)

def yarn_by_prices():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT brand, fibertype, fiberweight, color, yardageperskein, gramsperskein, numberofskeinsowned, "
                "price FROM Yarn ORDER BY price DESC, brand;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Define headers
    headers = ["Brand", "Fiber Type", "Fiber Weight", "Color", "Yardage/Skein", "Grams/Skein",
               "Number of Skeins in Stock", "Price"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"))
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value)
            data_label.grid(row=idx, column=i, padx=5, pady=5)

def fiber_types():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT fibertype FROM Yarn ORDER BY fibertype")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Define headers
    headers = ["Fiber Type"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"))
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        fiber_type_label = tk.Label(frame, text=row[0])
        fiber_type_label.grid(row=idx, column=0, padx=5, pady=5, sticky="w")

def fiber_weights():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT fiberweight FROM Yarn ORDER BY fiberweight")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Define headers
    headers = ["Fiber Weight"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"))
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        brand_label = tk.Label(frame, text=row[0])
        brand_label.grid(row=idx, column=0, padx=5, pady=5)

def yarn_by_yardage():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT brand, fibertype, fiberweight, color, gramsperskein, numberofskeinsowned, "
                "price, yardageperskein FROM Yarn ORDER BY yardageperskein DESC, brand;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Define headers
    headers = ["Brand", "Fiber Type", "Fiber Weight", "Color", "Grams/Skein", "Number of Skeins in Stock", "Price",
               "Yardage/Skein"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"))
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value)
            data_label.grid(row=idx, column=i, padx=5, pady=5)

def yarn_by_grams():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT brand, fibertype, fiberweight, color, yardageperskein, numberofskeinsowned, "
                "price, gramsperskein FROM Yarn ORDER BY gramsperskein DESC, brand;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Define headers
    headers = ["Brand", "Fiber Type", "Fiber Weight", "Color", "Yardage/Skein", "Number of Skeins in Stock", "Price",
               "Grams/Skein"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"))
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value)
            data_label.grid(row=idx, column=i, padx=5, pady=5)

def yarn_by_num_in_stock():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT brand, fibertype, fiberweight, color, yardageperskein, gramsperskein, "
                "price, numberofskeinsowned FROM Yarn ORDER BY numberofskeinsowned DESC, brand;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Define headers
    headers = ["Brand", "Fiber Type", "Fiber Weight", "Color", "Yardage/Skein", "Grams/Skein", "Price",
               "Number of Skeins in Stock"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"))
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value)
            data_label.grid(row=idx, column=i, padx=5, pady=5)

def safety_eyes_options():
    clear_window(root)
    yarn_text = tk.Label(root, text="What data from Safety Eyes do you want to see?")
    yarn_text.pack()

    size_in_mm_button = tk.Button(root, text="Size in millimeters", command=size_in_mm)
    size_in_mm_button.pack()

    eye_colors_button = tk.Button(root, text="Colors", command=eye_colors)
    eye_colors_button.pack()

    shapes_button = tk.Button(root, text="Shapes", command=shapes)
    shapes_button.pack()

    eyes_by_price_button = tk.Button(root, text="Eyes by Price", command=eyes_by_price)
    eyes_by_price_button.pack()

    eyes_by_num_in_stock_button = tk.Button(root, text="Eyes by Number in Stock",
                                                     command=eyes_by_num_in_stock)
    eyes_by_num_in_stock_button.pack()

def size_in_mm():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT sizeinmm FROM safetyeyes ORDER BY sizeinmm")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Define headers
    headers = ["Size in mm"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"))
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        brand_label = tk.Label(frame, text=row[0])
        brand_label.grid(row=idx, column=0, padx=5, pady=5)

def eye_colors():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT color FROM safetyeyes ORDER BY color")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Define headers
    headers = ["Color"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"))
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        brand_label = tk.Label(frame, text=row[0])
        brand_label.grid(row=idx, column=0, padx=5, pady=5)

def shapes():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT shape FROM safetyeyes ORDER BY shape")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Define headers
    headers = ["Shape"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"))
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        brand_label = tk.Label(frame, text=row[0])
        brand_label.grid(row=idx, column=0, padx=5, pady=5)

def eyes_by_price():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT sizeinmm, color, shape, numberofeyesowned, price FROM safetyeyes "
                "ORDER BY price DESC, sizeinmm")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Define headers
    headers = ["Size in mm", "Color", "Shape", "Number Eyes in Stock", "Price"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"))
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value)
            data_label.grid(row=idx, column=i, padx=5, pady=5)

def eyes_by_num_in_stock():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT sizeinmm, color, shape, price, numberofeyesowned FROM safetyeyes "
                "ORDER BY numberofeyesowned DESC, sizeinmm DESC")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Define headers
    headers = ["Size in mm", "Color", "Shape", "Price", "Number of Eyes in Stock"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"))
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value)
            data_label.grid(row=idx, column=i, padx=5, pady=5)

def stuffing_options():
    clear_window(root)
    yarn_text = tk.Label(root, text="What data from Stuffing do you want to see?")
    yarn_text.pack()

    stuffing_brands_button = tk.Button(root, text="Brands", command=stuffing_brands)
    stuffing_brands_button.pack()

    types_button = tk.Button(root, text="Types", command=types)
    types_button.pack()

    price_per_5_pounds_button = tk.Button(root, text="Stuffing by Price per 5 lbs",
                                          command=stuffing_by_price)
    price_per_5_pounds_button.pack()

def stuffing_brands():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT brand FROM stuffing")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Define headers
    headers = ["Brand"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"))
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value)
            data_label.grid(row=idx, column=i, padx=5, pady=5)

def types():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT type FROM stuffing")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Define headers
    headers = ["Type"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"))
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value)
            data_label.grid(row=idx, column=i, padx=5, pady=5)

def stuffing_by_price():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT brand, type, priceperfivelbs FROM stuffing ORDER BY priceperfivelbs DESC, brand")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Define headers
    headers = ["Brand", "Type", "Price per 5 lbs"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"))
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value)
            data_label.grid(row=idx, column=i, padx=5, pady=5)

def products_options():
    clear_window(root)
    yarn_text = tk.Label(root, text="What data from Products do you want to see?")
    yarn_text.pack()

    product_names_button = tk.Button(root, text="Names of Products", command=product_names)
    product_names_button.pack()

    product_time_to_make_button = tk.Button(root, text="Products by Time to Make", command=product_time_to_make)
    product_time_to_make_button.pack()

    product_cost_to_make_button = tk.Button(root, text="Products by Total Cost to Make", command=product_cost_to_make)
    product_cost_to_make_button.pack()

    product_by_price_button = tk.Button(root, text="Products by Sale Price", command=product_by_price)
    product_by_price_button.pack()

    product_by_num_in_stock_button = tk.Button(root, text="Products by Number in Stock",
                                               command=product_by_num_in_stock)
    product_by_num_in_stock_button.pack()

def product_names():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT name FROM finishedproducts ORDER BY name;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Define headers
    headers = ["Name"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"))
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value)
            data_label.grid(row=idx, column=i, padx=5, pady=5)

def product_time_to_make():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT name, totalcosttomake, saleprice, numberinstock, timetomake FROM finishedproducts "
                "ORDER BY timetomake;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Define headers
    headers = ["Name", "Total Cost to Make", "Sale Price", "Number in Stock", "Time to Make"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"))
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value)
            data_label.grid(row=idx, column=i, padx=5, pady=5)

def product_cost_to_make():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT name, timetomake, saleprice, numberinstock, totalcosttomake FROM finishedproducts "
                "ORDER BY totalcosttomake;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Define headers
    headers = ["Name", "Time to Make", "Sale Price", "Number in Stock", "Total Cost to Make"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"))
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value)
            data_label.grid(row=idx, column=i, padx=5, pady=5)

def product_by_price():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT name, timetomake, totalcosttomake, numberinstock, saleprice FROM finishedproducts "
                "ORDER BY saleprice;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Define headers
    headers = ["Name", "Time to Make", "Total Cost to Make", "Number in Stock", "Sale Price"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"))
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value)
            data_label.grid(row=idx, column=i, padx=5, pady=5)

def product_by_num_in_stock():
    clear_window(root)
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joshjazz18",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT name, timetomake, totalcosttomake, saleprice, numberinstock FROM finishedproducts "
                "ORDER BY numberinstock;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Create a canvas for scrolling
    canvas = tk.Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to contain the labels
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Define headers
    headers = ["Name", "Time to Make", "Total Cost to Make", "Sale Price", "Number in Stock"]

    # Display headers
    for i, header in enumerate(headers):
        header_label = tk.Label(frame, text=header, font=("Arial", 12, "bold"))
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display data rows
    for idx, row in enumerate(rows, start=1):
        for i, value in enumerate(row):
            data_label = tk.Label(frame, text=value)
            data_label.grid(row=idx, column=i, padx=5, pady=5)

def add_data_options():
    clear_window(root)
    add_data_text = tk.Label(root, text="What data do you want to add?")
    add_data_text.pack()

    new_finished_product_button = tk.Button(root, text="New finished product", command=new_finished_product_name)
    new_finished_product_button.pack()

    new_yarn_button = tk.Button(root, text="New yarn", command=new_yarn_brand)
    new_yarn_button.pack()

    new_safety_eyes_button = tk.Button(root, text="New safety eyes", command=new_eyes_size)
    new_safety_eyes_button.pack()

    new_stuffing_button = tk.Button(root, text="New stuffing", command=new_stuffing_brand)
    new_stuffing_button.pack()

    new_customer_button = tk.Button(root, text="New customer", command=new_customer_name)
    new_customer_button.pack()

def new_finished_product_name():
    clear_window(root)
    new_product_name_text = tk.Label(root, text="What is the name of your new product?")
    new_product_name_text.pack()

    global entry_new_finished_product_name
    entry_new_finished_product_name = tk.Entry(root, width=30)
    entry_new_finished_product_name.pack(pady=10)

    next_button = tk.Button(root, text="Next", command=new_finished_product_time)
    next_button.pack(pady=10)

def new_finished_product_time():
    global new_finished_product_name_input
    new_finished_product_name_input = entry_new_finished_product_name.get()
    clear_window(root)
    new_product_time_text = tk.Label(root, text="How much time does it take to make your new product?")
    new_product_time_text.pack()

    global entry_new_finished_product_time
    entry_new_finished_product_time = tk.Entry(root, width=30)
    entry_new_finished_product_time.pack(pady=10)

    next_button = tk.Button(root, text="Next", command=new_finished_product_cost)
    next_button.pack(pady=10)

def new_finished_product_cost():
    global new_finished_product_time_input
    new_finished_product_time_input = entry_new_finished_product_time.get()
    clear_window(root)
    new_product_time_text = tk.Label(root, text="How much does it cost to make your new product?")
    new_product_time_text.pack()

    global entry_new_finished_product_cost
    entry_new_finished_product_cost = tk.Entry(root, width=30)
    entry_new_finished_product_cost.pack(pady=10)

    next_button = tk.Button(root, text="Next", command=new_finished_product_saleprice)
    next_button.pack(pady=10)

def new_finished_product_saleprice():
    global new_finished_product_cost_input
    new_finished_product_cost_input = entry_new_finished_product_cost.get()
    clear_window(root)
    new_product_time_text = tk.Label(root, text="How much are you going to sell your new product for?")
    new_product_time_text.pack()

    global entry_new_finished_product_saleprice
    entry_new_finished_product_saleprice = tk.Entry(root, width=30)
    entry_new_finished_product_saleprice.pack(pady=10)

    next_button = tk.Button(root, text="Next", command=new_finished_product_in_stock)
    next_button.pack(pady=10)

def new_finished_product_in_stock():
    global new_finished_product_saleprice_input
    new_finished_product_saleprice_input = entry_new_finished_product_saleprice.get()
    clear_window(root)
    new_product_time_text = tk.Label(root, text="How many of this new product do you currently have in stock?")
    new_product_time_text.pack()

    global entry_new_finished_product_in_stock
    entry_new_finished_product_in_stock = tk.Entry(root, width=30)
    entry_new_finished_product_in_stock.pack(pady=10)

    next_button = tk.Button(root, text="Next", command=add_new_finished_product)
    next_button.pack(pady=10)

def add_new_finished_product():
    global new_finished_product_in_stock_input
    new_finished_product_in_stock_input = entry_new_finished_product_in_stock.get()
    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO finishedproducts (name, timetomake, totalcosttomake, saleprice, numberinstock)
            VALUES (%s, INTERVAL %s, %s, %s, %s);
            """,
            (
                new_finished_product_name_input,
                new_finished_product_time_input,
                new_finished_product_cost_input,
                new_finished_product_saleprice_input,
                new_finished_product_in_stock_input
            )
        )
        conn.commit()
        messagebox.showinfo("Success", "New product has been successfully added!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()

def new_yarn_brand():
    clear_window(root)
    new_product_name_text = tk.Label(root, text="What is the brand of your new yarn?")
    new_product_name_text.pack()

    global entry_new_yarn_brand
    entry_new_yarn_brand = tk.Entry(root, width=30)
    entry_new_yarn_brand.pack(pady=10)

    next_button = tk.Button(root, text="Next", command=new_yarn_price)
    next_button.pack(pady=10)

def new_yarn_price():
    global new_yarn_brand_input
    new_yarn_brand_input = entry_new_yarn_brand.get()
    clear_window(root)
    new_product_time_text = tk.Label(root, text="What is the price of your new yarn?")
    new_product_time_text.pack()

    global entry_new_yarn_price
    entry_new_yarn_price = tk.Entry(root, width=30)
    entry_new_yarn_price.pack(pady=10)

    next_button = tk.Button(root, text="Next", command=new_yarn_fiber_type)
    next_button.pack(pady=10)

def new_yarn_fiber_type():
    global new_yarn_price_input
    new_yarn_price_input = entry_new_yarn_price.get()
    clear_window(root)
    new_product_time_text = tk.Label(root, text="What is the fiber type of your new yarn?")
    new_product_time_text.pack()

    global entry_new_yarn_fiber_type
    entry_new_yarn_fiber_type = tk.Entry(root, width=30)
    entry_new_yarn_fiber_type.pack(pady=10)

    next_button = tk.Button(root, text="Next", command=new_yarn_fiber_weight)
    next_button.pack(pady=10)

def new_yarn_fiber_weight():
    global new_yarn_fiber_type_input
    new_yarn_fiber_type_input = entry_new_yarn_fiber_type.get()
    clear_window(root)
    new_product_time_text = tk.Label(root, text="What is the fiber weight of your new yarn?")
    new_product_time_text.pack()

    global entry_new_yarn_fiber_weight
    entry_new_yarn_fiber_weight = tk.Entry(root, width=30)
    entry_new_yarn_fiber_weight.pack(pady=10)

    next_button = tk.Button(root, text="Next", command=new_yarn_color)
    next_button.pack(pady=10)

def new_yarn_color():
    global new_yarn_fiber_weight_input
    new_yarn_fiber_weight_input = entry_new_yarn_fiber_weight.get()
    clear_window(root)
    new_product_time_text = tk.Label(root, text="What is the color of your new yarn?")
    new_product_time_text.pack()

    global entry_new_yarn_color
    entry_new_yarn_color = tk.Entry(root, width=30)
    entry_new_yarn_color.pack(pady=10)

    next_button = tk.Button(root, text="Next", command=new_yarn_yardage)
    next_button.pack(pady=10)

def new_yarn_yardage():
    global new_yarn_color_input
    new_yarn_color_input = entry_new_yarn_color.get()
    clear_window(root)
    new_product_time_text = tk.Label(root, text="What is the yardage per skein of your new yarn?")
    new_product_time_text.pack()

    global entry_new_yarn_yardage
    entry_new_yarn_yardage = tk.Entry(root, width=30)
    entry_new_yarn_yardage.pack(pady=10)

    next_button = tk.Button(root, text="Next", command=new_yarn_grams)
    next_button.pack(pady=10)

def new_yarn_grams():
    global new_yarn_yardage_input
    new_yarn_yardage_input = entry_new_yarn_yardage.get()
    clear_window(root)
    new_product_time_text = tk.Label(root, text="What is the grams per skein of your new yarn?")
    new_product_time_text.pack()

    global entry_new_yarn_grams
    entry_new_yarn_grams = tk.Entry(root, width=30)
    entry_new_yarn_grams.pack(pady=10)

    next_button = tk.Button(root, text="Next", command=new_yarn_in_stock)
    next_button.pack(pady=10)

def new_yarn_in_stock():
    global new_yarn_grams_input
    new_yarn_grams_input = entry_new_yarn_grams.get()
    clear_window(root)
    new_product_time_text = tk.Label(root, text="How many skeins of the new yarn are currently in stock?")
    new_product_time_text.pack()

    global entry_new_yarn_in_stock
    entry_new_yarn_in_stock = tk.Entry(root, width=30)
    entry_new_yarn_in_stock.pack(pady=10)

    next_button = tk.Button(root, text="Next", command=add_new_yarn)
    next_button.pack(pady=10)

def add_new_yarn():
    global new_yarn_in_stock_input
    new_yarn_in_stock_input = entry_new_yarn_in_stock.get()
    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO yarn 
            (Brand, Price, FiberType, FiberWeight, Color, YardagePerSkein, GramsPerSkein, NumberOfSkeinsOwned)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            """,
            (
                new_yarn_brand_input,
                new_yarn_price_input,
                new_yarn_fiber_type_input,
                new_yarn_fiber_weight_input,
                new_yarn_color_input,
                new_yarn_yardage_input,
                new_yarn_grams_input,
                new_yarn_in_stock_input,
            )
        )
        conn.commit()
        messagebox.showinfo("Success", "Yarn has been successfully added!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()

def new_eyes_size():
    clear_window(root)
    new_product_name_text = tk.Label(root, text="What is the size in millimeters of your new safety eyes?")
    new_product_name_text.pack()

    global entry_new_eyes_size
    entry_new_eyes_size = tk.Entry(root, width=30)
    entry_new_eyes_size.pack(pady=10)

    next_button = tk.Button(root, text="Next", command=new_eyes_color)
    next_button.pack(pady=10)

def new_eyes_color():
    global new_eyes_size_input
    new_eyes_size_input = entry_new_eyes_size.get()
    clear_window(root)
    new_product_time_text = tk.Label(root, text="What is the color of your new safety eyes?")
    new_product_time_text.pack()

    global entry_new_eyes_color
    entry_new_eyes_color = tk.Entry(root, width=30)
    entry_new_eyes_color.pack(pady=10)

    next_button = tk.Button(root, text="Next", command=new_eyes_shape)
    next_button.pack(pady=10)

def new_eyes_shape():
    global new_eyes_color_input
    new_eyes_color_input = entry_new_eyes_color.get()
    clear_window(root)
    new_product_time_text = tk.Label(root, text="What is the shape of your new safety eyes?")
    new_product_time_text.pack()

    global entry_new_eyes_shape
    entry_new_eyes_shape = tk.Entry(root, width=30)
    entry_new_eyes_shape.pack(pady=10)

    next_button = tk.Button(root, text="Next", command=new_eyes_price)
    next_button.pack(pady=10)

def new_eyes_price():
    global new_eyes_shape_input
    new_eyes_shape_input = entry_new_eyes_shape.get()
    clear_window(root)
    new_product_time_text = tk.Label(root, text="What is the price of your new safety eyes?")
    new_product_time_text.pack()

    global entry_new_eyes_price
    entry_new_eyes_price = tk.Entry(root, width=30)
    entry_new_eyes_price.pack(pady=10)

    next_button = tk.Button(root, text="Next", command=new_eyes_in_stock)
    next_button.pack(pady=10)

def new_eyes_in_stock():
    global new_eyes_price_input
    new_eyes_price_input = entry_new_eyes_price.get()
    clear_window(root)
    new_product_time_text = tk.Label(root, text="How many of these new safety eyes are currently in stock?")
    new_product_time_text.pack()

    global entry_new_eyes_in_stock
    entry_new_eyes_in_stock = tk.Entry(root, width=30)
    entry_new_eyes_in_stock.pack(pady=10)

    next_button = tk.Button(root, text="Next", command=add_new_eyes)
    next_button.pack(pady=10)

def add_new_eyes():
    global new_eyes_in_stock_input
    new_eyes_in_stock_input = entry_new_eyes_in_stock.get()
    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO safetyeyes (Price, SizeinMM, Color, Shape, NumberOfEyesOwned)
            VALUES (%s, %s, %s, %s, %s);
            """,
            (
                new_eyes_price_input,
                new_eyes_size_input,
                new_eyes_color_input,
                new_eyes_shape_input,
                new_eyes_in_stock_input
            )
        )
        conn.commit()
        messagebox.showinfo("Success", "Safety eyes have been successfully added!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()

def new_stuffing_brand():
    clear_window(root)
    new_product_name_text = tk.Label(root, text="What is the brand of your new stuffing?")
    new_product_name_text.pack()

    global entry_new_stuffing_brand
    entry_new_stuffing_brand = tk.Entry(root, width=30)
    entry_new_stuffing_brand.pack(pady=10)

    next_button = tk.Button(root, text="Next", command=new_stuffing_type)
    next_button.pack(pady=10)

def new_stuffing_type():
    global new_stuffing_brand_input
    new_stuffing_brand_input = entry_new_stuffing_brand.get()
    clear_window(root)
    new_product_time_text = tk.Label(root, text="What is the type of your new stuffing?")
    new_product_time_text.pack()

    global entry_new_stuffing_type
    entry_new_stuffing_type = tk.Entry(root, width=30)
    entry_new_stuffing_type.pack(pady=10)

    next_button = tk.Button(root, text="Next", command=new_stuffing_price)
    next_button.pack(pady=10)

def new_stuffing_price():
    global new_stuffing_type_input
    new_stuffing_type_input = entry_new_stuffing_type.get()
    clear_window(root)
    new_product_time_text = tk.Label(root, text="What is the price per 5 lbs of your new stuffing?")
    new_product_time_text.pack()

    global entry_new_stuffing_price
    entry_new_stuffing_price = tk.Entry(root, width=30)
    entry_new_stuffing_price.pack(pady=10)

    next_button = tk.Button(root, text="Next", command=add_new_stuffing)
    next_button.pack(pady=10)

def add_new_stuffing():
    global new_stuffing_price_input
    new_stuffing_price_input = entry_new_stuffing_price.get()
    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO stuffing (Brand, PricePerFivelbs, Type)
            VALUES (%s, %s, %s);
            """,
            (
                new_stuffing_brand_input,
                new_stuffing_price_input,
                new_stuffing_type_input
            )
        )
        conn.commit()
        messagebox.showinfo("Success", "Stuffing has been successfully added!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()

def new_customer_name():
    clear_window(root)
    new_product_name_text = tk.Label(root, text="What is the first and last name of your new customer?")
    new_product_name_text.pack()

    global entry_new_customer_name
    entry_new_customer_name = tk.Entry(root, width=30)
    entry_new_customer_name.pack(pady=10)

    next_button = tk.Button(root, text="Next", command=new_customer_phone)
    next_button.pack(pady=10)

def new_customer_phone():
    global new_customer_name_input
    new_customer_name_input = entry_new_customer_name.get()
    clear_window(root)
    new_product_time_text = tk.Label(root, text="What is the phone number of your new customer? "
                                                "(Leave blank and click next if unknown)")
    new_product_time_text.pack()

    global entry_new_customer_phone
    entry_new_customer_phone = tk.Entry(root, width=30)
    entry_new_customer_phone.pack(pady=10)

    next_button = tk.Button(root, text="Next", command=new_customer_email)
    next_button.pack(pady=10)
def new_customer_email():
    global new_customer_phone_input
    new_customer_phone_input = entry_new_customer_phone.get()
    clear_window(root)
    new_product_time_text = tk.Label(root, text="What is the email of your new customer? "
                                                "(Leave blank and click next if unknown)")
    new_product_time_text.pack()

    global entry_new_customer_email
    entry_new_customer_email= tk.Entry(root, width=30)
    entry_new_customer_email.pack(pady=10)

    next_button = tk.Button(root, text="Next", command=add_new_customer)
    next_button.pack(pady=10)

def add_new_customer():
    global new_customer_email_input
    new_customer_email_input = entry_new_customer_email.get()
    clear_window(root)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Joshjazz18",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO customers (Name, PhoneNumber, EmailAddress)
            VALUES (%s, %s, %s);
            """,
            (
                new_customer_name_input,
                new_customer_phone_input,
                new_customer_email_input
            )
        )
        conn.commit()
        messagebox.showinfo("Success", "Customer has been successfully added!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()

# Create main window
root = tk.Tk()
root.title("Jazmine's Yarn Database")

intro_text = tk.Label(root, text="What do you want to do?")
intro_text.pack()

look_at_data_button = tk.Button(root, text="Look at data", command=look_at_data_options)
look_at_data_button.pack()

add_data_button = tk.Button(root, text="Add data", command=add_data_options)
add_data_button.pack()

# Start the GUI event loop
root.mainloop()