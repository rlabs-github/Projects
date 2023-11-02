'''
This is the main file of the website. It will handle the user interface and control the flow of the program.
'''
import tkinter as tk
from news_feed import NewsFeed
from software_solutions import SoftwareSolutions
class WebsiteApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tech News and Software Solutions")
        self.news_feed = NewsFeed()
        self.software_solutions = SoftwareSolutions()
        self.create_widgets()
    def create_widgets(self):
        # Create and configure the GUI widgets
        # News Feed section
        self.news_label = tk.Label(self.master, text="Tech News", font=("Arial", 16, "bold"))
        self.news_label.pack()
        self.news_text = tk.Text(self.master, height=10, width=50)
        self.news_text.pack()
        self.refresh_button = tk.Button(self.master, text="Refresh News", command=self.refresh_news)
        self.refresh_button.pack()
        # Software Solutions section
        self.solutions_label = tk.Label(self.master, text="Software Solutions", font=("Arial", 16, "bold"))
        self.solutions_label.pack()
        self.solutions_text = tk.Text(self.master, height=10, width=50)
        self.solutions_text.pack()
        self.load_solutions_button = tk.Button(self.master, text="Load Solutions", command=self.load_solutions)
        self.load_solutions_button.pack()
    def refresh_news(self):
        # Retrieve and display the latest news
        news = self.news_feed.get_news()
        self.news_text.delete(1.0, tk.END)
        self.news_text.insert(tk.END, news)
    def load_solutions(self):
        # Retrieve and display the software solutions
        solutions = self.software_solutions.get_solutions()
        self.solutions_text.delete(1.0, tk.END)
        self.solutions_text.insert(tk.END, solutions)
root = tk.Tk()
app = WebsiteApp(root)
root.mainloop()