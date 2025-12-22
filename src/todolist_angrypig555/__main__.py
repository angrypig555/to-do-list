try:import sys,tkinter;from .main import application
except ImportError:print("Error: Tkinter is not installed on this system.\nTo fix this:\n  • On Linux: sudo apt install python3-tk\n  • On Windows/macOS: reinstall Python from python.org (Tkinter is included)");sys.exit(1)
if __name__ == "__main__":application().run()