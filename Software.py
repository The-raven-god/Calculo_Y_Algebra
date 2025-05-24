import tkinter as tk
from tkinter import ttk, messagebox
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Polygon

class IntegralTransformerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Transformación de Integrales Dobles con Jacobiano")
        self.root.geometry("1000x800")
        
        # Símbolos matemáticos
        self.x, self.y = sp.symbols('x y')
        self.r, self.theta = sp.symbols('r theta')
        self.u, self.v = sp.symbols('u v')
        
        # Variables para almacenar expresiones
        self.funcion = tk.StringVar()
        self.x_lim_inf = tk.StringVar()
        self.x_lim_sup = tk.StringVar()
        self.y_lim_inf = tk.StringVar()
        self.y_lim_sup = tk.StringVar()
        self.u_expr = tk.StringVar(value="r*cos(theta)")
        self.v_expr = tk.StringVar(value="r*sin(theta)")
        
        # Configurar estilo
        self.setup_style()
        
        # Crear interfaz
        self.create_widgets()
        
        # Insertar ejemplos
        self.insert_examples()
    
    def setup_style(self):
        style = ttk.Style()
        style.theme_use('default')
        style.configure('TFrame', background='#f7f9fb')
        style.configure('TLabel', background='#f7f9fb', foreground='#2c3e50', font=('Arial', 10))
        style.configure('Header.TLabel', font=('Arial', 12, 'bold'), foreground='#2c3e50')
        style.configure('TButton', font=('Arial', 10), padding=6, background='#2980b9', foreground='white')
        style.map('TButton', background=[('active', '#1c5980')], foreground=[('disabled', 'gray')])
        
    def create_widgets(self):
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        input_frame = ttk.Frame(main_frame)
        input_frame.grid(row=0, column=0, sticky=tk.NSEW, padx=5, pady=5)
        
        result_frame = ttk.Frame(main_frame)
        result_frame.grid(row=0, column=1, sticky=tk.NSEW, padx=5, pady=5)
        
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=2)
        main_frame.rowconfigure(0, weight=1)
        
        self.create_input_widgets(input_frame)
        self.create_result_widgets(result_frame)
        
    def create_input_widgets(self, parent):
        ttk.Label(parent, text="ENTRADA DE DATOS", style='Header.TLabel').grid(row=0, column=0, columnspan=2, pady=5)
        
        ttk.Label(parent, text="Función f(x,y):").grid(row=1, column=0, sticky=tk.W)
        ttk.Entry(parent, textvariable=self.funcion, width=40).grid(row=1, column=1, sticky=tk.EW, pady=2)
        
        ttk.Label(parent, text="Límites de x:").grid(row=2, column=0, sticky=tk.W)
        ttk.Label(parent, text="Desde:").grid(row=3, column=0, sticky=tk.W)
        ttk.Entry(parent, textvariable=self.x_lim_inf, width=15).grid(row=3, column=1, sticky=tk.W, pady=2)
        ttk.Label(parent, text="Hasta:").grid(row=4, column=0, sticky=tk.W)
        ttk.Entry(parent, textvariable=self.x_lim_sup, width=15).grid(row=4, column=1, sticky=tk.W, pady=2)
        
        ttk.Label(parent, text="Límites de y:").grid(row=5, column=0, sticky=tk.W)
        ttk.Label(parent, text="Desde:").grid(row=6, column=0, sticky=tk.W)
        ttk.Entry(parent, textvariable=self.y_lim_inf, width=15).grid(row=6, column=1, sticky=tk.W, pady=2)
        ttk.Label(parent, text="Hasta:").grid(row=7, column=0, sticky=tk.W)
        ttk.Entry(parent, textvariable=self.y_lim_sup, width=15).grid(row=7, column=1, sticky=tk.W, pady=2)
        
        ttk.Label(parent, text="Cambio de variable (x e y en términos de nuevas variables):", 
                 style='Header.TLabel').grid(row=8, column=0, columnspan=2, pady=(10,2))
        ttk.Label(parent, text="x =").grid(row=9, column=0, sticky=tk.W)
        ttk.Entry(parent, textvariable=self.u_expr, width=20).grid(row=9, column=1, sticky=tk.W, pady=2)
        ttk.Label(parent, text="y =").grid(row=10, column=0, sticky=tk.W)
        ttk.Entry(parent, textvariable=self.v_expr, width=20).grid(row=10, column=1, sticky=tk.W, pady=2)
        
        btn_frame = ttk.Frame(parent)
        btn_frame.grid(row=11, column=0, columnspan=2, pady=10)
        ttk.Button(btn_frame, text="Calcular", command=self.calculate).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Limpiar", command=self.clear).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Ayuda", command=self.show_help).pack(side=tk.LEFT, padx=5)
        
    def create_result_widgets(self, parent):
        self.notebook = ttk.Notebook(parent)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        result_tab = ttk.Frame(self.notebook)
        self.notebook.add(result_tab, text="Resultados")
        self.result_text = tk.Text(result_tab, wrap=tk.WORD, font=('Courier New', 10))
        self.result_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        scrollbar = ttk.Scrollbar(result_tab, orient=tk.VERTICAL, command=self.result_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text['yscrollcommand'] = scrollbar.set
        
        graph_tab = ttk.Frame(self.notebook)
        self.notebook.add(graph_tab, text="Gráficos")
        self.figure = plt.Figure(figsize=(6, 5), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=graph_tab)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def insert_examples(self):
        self.funcion.set("x**2 + y**2")
        self.x_lim_inf.set("0")
        self.x_lim_sup.set("1")
        self.y_lim_inf.set("0")
        self.y_lim_sup.set("sqrt(1-x**2)")
        self.u_expr.set("r*cos(theta)")
        self.v_expr.set("r*sin(theta)")
    
    def clear(self):
        self.funcion.set("")
        self.x_lim_inf.set("")
        self.x_lim_sup.set("")
        self.y_lim_inf.set("")
        self.y_lim_sup.set("")
        self.u_expr.set("r*cos(theta)")
        self.v_expr.set("r*sin(theta)")
        self.result_text.delete(1.0, tk.END)
        self.ax.clear()
        self.canvas.draw()
        self.insert_examples()
        
    def show_help(self):
        help_text = """AYUDA: CÓMO USAR ESTA APLICACIÓN

1. Función f(x,y): Ingrese la función a integrar usando x e y como variables.
   Ejemplos: 
   - x**2 + y**2
   - sqrt(x**2 + y**2)

2. Límites de integración:
   - Para x: Ingrese los valores mínimo y máximo
   - Para y: Pueden ser constantes o funciones de x (ej: sqrt(1-x**2))

3. Cambio de variable:
   - Defina cómo se expresan x e y en términos de las nuevas variables
   - Ejemplo para coordenadas polares:
     x = r*cos(theta)
     y = r*sin(theta)
"""
        messagebox.showinfo("Ayuda", help_text)
    
    def calculate(self):
        try:
            self.result_text.delete(1.0, tk.END)
            self.ax.clear()
            
            f_expr = self.process_expression(self.funcion.get())
            x_min = self.process_expression(self.x_lim_inf.get())
            x_max = self.process_expression(self.x_lim_sup.get())
            y_min = self.process_expression(self.y_lim_inf.get())
            y_max = self.process_expression(self.y_lim_sup.get())
            u_expr = self.process_expression(self.u_expr.get())
            v_expr = self.process_expression(self.v_expr.get())
            
            self.show_original_integral(f_expr, x_min, x_max, y_min, y_max)
            self.calculate_transformation(f_expr, u_expr, v_expr)
            self.plot_region(x_min, x_max, y_min, y_max)
            
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")
            self.result_text.insert(tk.END, f"\nERROR: {str(e)}")
    
    def process_expression(self, expr):
        if not expr:
            raise ValueError("Expresión vacía")
        expr = expr.replace('^', '**').replace('sen', 'sin').replace('π', 'pi')
        return sp.sympify(expr)
    
    def show_original_integral(self, f_expr, x_min, x_max, y_min, y_max):
        self.result_text.insert(tk.END, "INTEGRAL ORIGINAL:\n")
        self.result_text.insert(tk.END, f"∬ f(x,y) dx dy = ∬ ({sp.pretty(f_expr)}) dx dy\n\n")
        self.result_text.insert(tk.END, "LÍMITES DE INTEGRACIÓN:\n")
        self.result_text.insert(tk.END, f"x ∈ [{sp.pretty(x_min)}, {sp.pretty(x_max)}]\n")
        self.result_text.insert(tk.END, f"y ∈ [{sp.pretty(y_min)}, {sp.pretty(y_max)}]\n\n")
        self.result_text.insert(tk.END, "REGION DE INTEGRACIÓN ORIGINAL (en coordenadas cartesianas):\n")
    
    def calculate_transformation(self, f_expr, u_expr, v_expr):
        
        # Determinar tipo de transformación
        is_linear = any(var in str(u_expr) or var in str(v_expr) for var in ['u', 'v'])
        
        if is_linear:
            dx_du = sp.diff(u_expr, self.u)
            dx_dv = sp.diff(u_expr, self.v)
            dy_du = sp.diff(v_expr, self.u)
            dy_dv = sp.diff(v_expr, self.v)
            jacobian = dx_du * dy_dv - dx_dv * dy_du
            vars_str = "u y v"
        else:
            dx_dr = sp.diff(u_expr, self.r)
            dx_dtheta = sp.diff(u_expr, self.theta)
            dy_dr = sp.diff(v_expr, self.r)
            dy_dtheta = sp.diff(v_expr, self.theta)
            jacobian = dx_dr * dy_dtheta - dx_dtheta * dy_dr
            vars_str = "r y θ"
        
        new_integrand = f_expr.subs({self.x: u_expr, self.y: v_expr}) * sp.Abs(jacobian)
        
        resultado = f"""
    ════════════ TRANSFORMACIÓN APLICADA ════════════
    x = {sp.pretty(u_expr)}
    y = {sp.pretty(v_expr)}

    ════════════ CÁLCULO DEL JACOBIANO ══════════════
    ∂x/∂{'u' if is_linear else 'r'}     = {sp.pretty(dx_du if is_linear else dx_dr)}
    ∂x/∂{'v' if is_linear else 'θ'}     = {sp.pretty(dx_dv if is_linear else dx_dtheta)}
    ∂y/∂{'u' if is_linear else 'r'}     = {sp.pretty(dy_du if is_linear else dy_dr)}
    ∂y/∂{'v' if is_linear else 'θ'}     = {sp.pretty(dy_dv if is_linear else dy_dtheta)}

    Jacobiano = ∂x/∂{'u' if is_linear else 'r'}·∂y/∂{'v' if is_linear else 'θ'} - ∂x/∂{'v' if is_linear else 'θ'}·∂y/∂{'u' if is_linear else 'r'}
            = {sp.pretty(jacobian)}

    ════════════ NUEVO INTEGRANDO ═══════════════════
    f({vars_str.split()[0]},{vars_str.split()[1]}) · |Jacobiano| =
    {sp.pretty(new_integrand)}
    """
        self.result_text.insert(tk.END, resultado)
    
    def plot_region(self, x_min, x_max, y_min, y_max):
        try:
            x_min_val = float(x_min.evalf())
            x_max_val = float(x_max.evalf())
            x_vals = np.linspace(x_min_val, x_max_val, 100)
            
            y_low = []
            y_up = []
            
            for xi in x_vals:
                try:
                    yl = float(y_min.subs(self.x, xi).evalf())
                    y_low.append(yl)
                except:
                    yl = float(y_min.evalf())
                    y_low = [yl] * len(x_vals)
                    break
            
            for xi in x_vals:
                try:
                    yu = float(y_max.subs(self.x, xi).evalf())
                    y_up.append(yu)
                except:
                    yu = float(y_max.evalf())
                    y_up = [yu] * len(x_vals)
                    break
            
            polygon_pts = list(zip(x_vals, y_low)) + list(zip(reversed(x_vals), reversed(y_up)))
            polygon = Polygon(polygon_pts, closed=True, alpha=0.3, color='blue')
            
            self.ax.add_patch(polygon)
            self.ax.plot(x_vals, y_low, 'b-', label=f'y_min = {sp.pretty(y_min)}')
            self.ax.plot(x_vals, y_up, 'r-', label=f'y_max = {sp.pretty(y_max)}')
            self.ax.plot([x_min_val, x_min_val], [y_low[0], y_up[0]], 'g--')
            self.ax.plot([x_max_val, x_max_val], [y_low[-1], y_up[-1]], 'g--')
            
            self.ax.set_xlabel('x')
            self.ax.set_ylabel('y')
            self.ax.set_title('Región de Integración Original')
            self.ax.legend()
            self.ax.grid(True)
            
            y_min_val = min(min(y_low), min(y_up))
            y_max_val = max(max(y_low), max(y_up))
            self.ax.set_xlim(x_min_val - 0.1*(x_max_val-x_min_val), 
                            x_max_val + 0.1*(x_max_val-x_min_val))
            self.ax.set_ylim(y_min_val - 0.1*(y_max_val-y_min_val), 
                            y_max_val + 0.1*(y_max_val-y_min_val))
            
            self.canvas.draw()
            
        except Exception as e:
            self.ax.clear()
            self.ax.text(0.5, 0.5, 'No se pudo graficar la región\nVerifique los límites', 
                         ha='center', va='center', color='red')
            self.ax.set_title('Error en visualización')
            self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = IntegralTransformerApp(root)
    root.mainloop()